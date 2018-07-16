import urllib.request
import urllib.error
import urllib.parse
import time
import string
import random
import csv
import ssl
import os
from threading import Thread
from lib.LogSender.CSVLogTraffic import *
from db import *
from db.cm_session import cm_session
from lib.ConfigHelper import ConfigHelper

ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)


class LogSender(object):
    MAPPING_TABLE = {
        'EntityName': 'SLF_ProductGUID',
        'Product': 'SLF_ProductID',
        'LogType': '',
        'Filename': '',
        'LogCount': ''
    }

    MSG_MAP = {'1733': 'TbWebSecurityLog', '1743': 'TbLogBehaviorMonitor', '1729': 'TbPersonalFirewallLog',
               '1756': 'TbNetworkContentInspectionEngine_Log', '1752': 'TbApplicationControlEvent',
               '1766': 'TbFileHashDetectionLog', '1769': 'TbLogIntrusionPrevention', '1771': 'TbLogIntegrityMonitor',
               '1703': 'TbAVVirusLog', '1705': 'TbSecurityLog', '1707': 'TbWebSecurityLog',
               '1750': 'TbLogDataLossPrevention', '1723': 'TbLogGeneral', '1739': 'TbLogGeneral',
               '1717': 'TbSecurityViolations', '1747': 'TbCVWLog', '1727': 'TbSpywareLog',
               '1748': 'TbLogThreatMitigation', '1701': 'Tbstatuslogjournal', '1777': 'TbSandboxDetectionlog'}

    CgiDelegateURI = '/ControlManager/ClientCGI/cgiDelegate.dll'
    SERVER_URL = '%s%s:%s' + CgiDelegateURI

    PRODUCT_ID_MAP = {'SMLN': '2', 'SMEX': '3', 'OSCE': '15', 'SPNT': '18', 'IMSSNT': '34', 'IWSA': '43', 'IMSA': '44',
                      'IWSVA': '46', 'IMSVA': '47', 'NVW': '69', 'ISVW': '95', 'TDA': '120', 'DDI36': '154',
                      'DDI37': '154', 'DDEI': '156', 'TMSM': '31001', 'TMMS': '31005', 'IDF': '31006', 'TMDS': '31004',
                      'TMEE': '31002', 'HES': '31101', 'WFBS_SVC': '31102', 'IWSAAS': '31103', 'DDES': '31009',
                      'DDAN': '31008'}

    def reset(self):
        self._column_list = []
        self._data_list = []
        self._traffic_list = []
        print('Reset CM server: %s' % self._server_url)

    def __init__(self):
        self._cm_setting = ConfigHelper().get_data_from_config('CM')
        self._db_setting = ConfigHelper().get_data_from_config('DB')
        self._column_list = self._data_list = self._traffic_list = list()
        self._registered_products = []
        self._server_ip = self._cm_setting['ip']
        self._server_port = self._cm_setting['port']
        self._server_protocol = self._cm_setting['protocol']
        self._server_url = self.SERVER_URL % (self._server_protocol, self._server_ip, str(self._server_port))
        self._db_server = self._db_setting['address']
        self._db_name = self._db_setting['dbname']
        self._db_user = self._db_setting['account']
        self._db_password = self._db_setting['password']
        self._log_tmp_path = None
        self._reg_tmp_path = None
        self._unreg_tmp_path = None
        self.reset()

    def set_tmp_path(self, log_path=None, reg_path=None, unreg_path=None):
        self._log_tmp_path = log_path
        self._reg_tmp_path = reg_path
        self._unreg_tmp_path = unreg_path

    def _get_entity_info(self, entity_name, product_name):
        product_id = None
        if product_name:
            product_id = self.PRODUCT_ID_MAP.get(product_name)
        entity = TbTreeNode.get_server_info(entity_name, product_id)
        if not entity:
            msg = 'Fail on get entity guid'
            raise Exception(msg)
        return entity

    @staticmethod
    def _get_parent_info(parent_name, product_name):
        return TbTreeNode.get_parent_tree_node(parent_name, product_name)

    @staticmethod
    def _get_product_info(product_name):
        return TbTreeNode.find_by_displayname(product_name)

    @staticmethod
    def _check_tb_registered(guid, max_retry=15):
        for i in range(max_retry):
            entity = TbEntityInfo.find_by_entityid(guid)
            if entity is not None:
                return True
            time.sleep(2)
        return False

    @staticmethod
    def _check_server_registered(guid, max_retry=3):
        for i in range(max_retry):
            server = TbServerList.find_by_serverid(guid)
            if server is not None:
                return True
            time.sleep(1)
        return False

    @staticmethod
    def _check_guid_is_existed(guid, max_retry=3, is_existed=True):
        for i in range(max_retry):
            server = TbServerList.find_by_serverid(guid)
            if server is not None:
                return True
            time.sleep(1)
        return False if not is_existed else True

    @staticmethod
    def _generate_random_uid():
        dash_range = [12, 8, 4, 4, 4]
        uid_scope = string.hexdigits.lower()
        uid = ''
        for i in dash_range:
            if len(uid) > 0:
                uid += '-'
            uid += ''.join(random.SystemRandom().choice(uid_scope) for _ in range(i))

        return uid

    @staticmethod
    def _get_guid_list(pre_guid, count):
        ret = []
        pre_guid_lst = pre_guid.split('-')
        for i in range(1, count+1):
            tmp_guid = '%08d' % i
            if len(pre_guid_lst) == 3:
                guid_lst = pre_guid_lst + [tmp_guid[:4], tmp_guid[4:]]
                guid = '-'.join(guid_lst)
                ret.append(guid)
        return ret

    @staticmethod
    def _urlopen(server_url, body_str, timeout=60):
        rep = None
        try:
            rep = urllib.request.urlopen(server_url, body_str, timeout=timeout, context=ctx)
        except:
            pass
        return rep

    @staticmethod
    def _get_int_count_output(table_name):
        return eval("%s.count()" % table_name)

    def create_log_traffic(self, entity_name, log_type, tmp_file, log_count, product_name=None, time_deviation=''):
        entity = self._get_entity_info(entity_name, product_name)

        obj_traffic = CSVLogTraffic(entity['ProductGuid'], log_type, tmp_file,
                                    log_count, log_tmp_root=self._log_tmp_path)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductID', entity['ProductType'])
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', entity['EntityID'])
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ClientGUID', entity['EntityID'])
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', entity_name)
        if time_deviation == '':
            time_deviation = '0'
        obj_traffic.funcSetPredefinedLogTemplate('SLF_LogGenerationTime', '<Gen_Time><HOUR_%s>' % time_deviation)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_LogGenLocalDateTime', '<Gen_Time><HOUR_%s>' % time_deviation)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_LogGenUTCDatetime', '<Gen_UTCTime><HOUR_%s>' % time_deviation)

        return obj_traffic

    def prepare_log_data_list(self):
        print('Log data list: {0}'.format(self._data_list))
        if len(self._data_list) <= 0:
            return 'There are no log data existed.'
        entity_name_idx = self._column_list.index('EntityName')
        product_idx = self._column_list.index('Product')
        log_type_idx = self._column_list.index('LogType')
        filename_idx = self._column_list.index('Filename')
        log_count_idx = self._column_list.index('LogCount')
        time_deviation_idx = -1
        if 'TimeDeviation' in self._column_list:
            time_deviation_idx = self._column_list.index('TimeDeviation')

        for data_row_list in self._data_list:
            if len(data_row_list) != len(self._column_list):
                return 'The data row length is not equal with column: %d/ %d' % (len(data_row_list),
                                                                                 len(self._column_list))
            if len(data_row_list) < 5:
                return 'The data row length less than 5'
            if time_deviation_idx > 0:
                obj_traffic = self.create_log_traffic(data_row_list[entity_name_idx], data_row_list[log_type_idx],
                                                  data_row_list[filename_idx], data_row_list[log_count_idx],
                                                  data_row_list[product_idx],data_row_list[time_deviation_idx])
            else:
                obj_traffic = self.create_log_traffic(data_row_list[entity_name_idx], data_row_list[log_type_idx],
                                                      data_row_list[filename_idx], data_row_list[log_count_idx],
                                                      data_row_list[product_idx])
            if isinstance(obj_traffic, str):
                return obj_traffic
            for i in range(0, len(data_row_list)):
                if i in (entity_name_idx, product_idx, log_type_idx, filename_idx, log_count_idx):
                    continue
                column_name = self._column_list[i]
                column_value = data_row_list[i]
                obj_traffic.funcSetPredefinedLogTemplate(column_name, column_value)
            self._traffic_list.append(obj_traffic)
        return 0

    def _load_csv_file(self, csv_file):
        """
            :return: str for error return, 0 for normal return
        """
        self.reset()
        with open(csv_file, 'r') as f:
            content_list = list(csv.reader(f))
        content_list = [_f for _f in content_list if _f]
        if len(content_list) <= 1:
            return 'Fail on read data from csv file: %s' % csv_file
        self._column_list = content_list[0]
        self._data_list = content_list[1:]
        return 0

    def load_csv_data(self, csv_file):
        """
            :return: str for error return, 0 for normal return
        """
        self._load_csv_file(csv_file)
        return self.prepare_log_data_list()

    def send_log(self, csv_log_file):
        ret = self._load_csv_file(csv_log_file)
        if ret != 0:
            return ret
        ret = self.prepare_log_data_list()
        if ret != 0:
            return ret
        return self.send_traffic_list()

    def send_log_by_log_list(self, log_list):
        self.reset()
        self._column_list = log_list[0]
        self._data_list = log_list[1:]
        ret = self.prepare_log_data_list()
        if ret != 0:
            return ret
        return self.send_traffic_list()

    def send_traffic_list(self):
        check_log_dict = {}
        for traffic_obj in self._traffic_list:
            blob_header = traffic_obj.funcGetHeader()
            blob_header = blob_header.encode()
            blob_list = traffic_obj.funcGetBlobList()
            cur_log_type = traffic_obj.funcGetTemplateValue('SLF_MsgType')
            target_table = self.MSG_MAP.get(cur_log_type)
            send_log_count = traffic_obj.funcGetTotalAmount()

            if target_table is not None:
                original_count = self._get_int_count_output(target_table)
            print('Connect to: %s' % self._server_url)
            for blob_obj in blob_list:
                blob_msg = b''.join(blob_obj)
                print('blob length: %d / %d' % (len(blob_header), len(blob_msg)))
                resp = self._send_log_with_retry(blob_header, blob_msg)
                if resp.getcode() != 200:
                    raise Exception('Send blob might failed, get http error: {0}'.format(resp.getcode(), resp.read()))
            if target_table is not None:
                if check_log_dict.get(target_table) is None:
                    print('Sending log to target table %s: %d+%d' % (target_table, original_count, send_log_count))
                    check_log_dict[target_table] = [original_count, send_log_count]
                else:
                    print('Sending log to target table %s: %d+%d' % (target_table, original_count, send_log_count))
                    check_log_dict[target_table][1] += send_log_count
        for target_table, v in check_log_dict.items():
            expected_count = v[0] + v[1]
            if expected_count > 300000:
                interval = 10
            else:
                interval = 3
            for i in range(100):
                cur_table_count = self._get_int_count_output(target_table)
                if cur_table_count >= expected_count:
                    break
                print('waiting log into table: %s, %d : %d+%d' % (target_table, cur_table_count, v[0], v[1]))
                time.sleep(interval)
                print('Wait for some time to avoid the http error')
        self._traffic_list = []
        return 0

    def _send_log_with_retry(self, blob_header, blob_msg):
        retry_count = 5
        resp = None
        for retries in range(retry_count):
            try:
                resp = self._urlopen(self._server_url, blob_header+blob_msg, timeout=120)
            except:
                pass
            if resp:
                return resp
        return False

    # server_type: 1: WSI, 2: SAAS
    def _add_server_by_traffic(self, obj_traffic, server_type):
        if server_type != 1:
            return 'Not support SAAS server add yet'
        server_url = obj_traffic.funcGetTemplateValue('SLF_ConfigURL')
        host = server_url.split('/')[2]
        guid = obj_traffic.funcGetTemplateValue('SLF_ProductGUID')

        params = [guid, server_url, obj_traffic.funcGetTemplateValue('SLF_DisplayName')] + \
                 [obj_traffic.funcGetTemplateValue('SLF_ProductID')] + \
                 [obj_traffic.funcGetTemplateValue('SLF_ProductVersion'), server_type] + \
                 [obj_traffic.funcGetTemplateValue('SLF_ProtocolName'), host] + \
                 [obj_traffic.funcGetTemplateValue('SLF_Port'), 'test', 'test'] + \
                 [obj_traffic.funcGetTemplateValue('SLF_Status'), 1, 1, 0, '', '', '']

        param_dict = {}
        for i in range(0, len(params)):
            key = 'p%s' % str(i+1)
            param_dict.update({key: params[i]})

        cm_session.execute('sp_Policy_AddServer :p1,:p2,:p3,:p4,:p5,:p6,:p7,:p8,:p9,' +
                           ':p10,:p11,:p12,:p13,:p14,:p15,:p16,:p17', param_dict)
        if not self._check_server_registered(guid):
            raise Exception('Server %s is not in tb_ServerList' % guid)
        return 0

    def _send_register_request(self, obj_traffic=None, with_status=False):
        if obj_traffic is None:
            for traffic_obj in self._traffic_list:
                ret = self._send_register_request(traffic_obj, with_status)
                if ret != 0:
                    return ret
            return 0
        self.send_traffic_blob(obj_traffic)
        guid = obj_traffic.funcGetUid()

        if not self._check_tb_registered(guid):
            return 'Register %s fail' % guid
        if obj_traffic.getEntityType() != 1:
            if with_status:
                # complete status log here or
                name = obj_traffic.funcGetTemplateValue('SLF_DisplayName')
                status_traffic = self.create_log_traffic(name, 'Status', 'status_15_OSCE+DLP', 1)
                status_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', guid)
                for idx_column in range(len(self._column_list)):
                    status_traffic.funcSetPredefinedLogTemplate(self._column_list[idx_column],obj_traffic.funcGetTemplateValue(self._column_list[idx_column]))
                self.send_traffic_blob(status_traffic)
            return 0
        # check entity exist in tb_ServerList or not
        if self._check_server_registered(guid):
            return 0
        if TbEntityInfo.is_wsi_server(guid):
            return self._add_server_by_traffic(obj_traffic, 1)
        if TbEntityInfo.is_saas_server(guid):
            return self._add_server_by_traffic(obj_traffic, 2)
        return 'Why product %s is not in tb_ServerList?! ' % guid

    def _get_register_product_traffic(self, product_type, guid=None, display_name=None):
        if guid is None:
            guid = self._generate_random_uid()
        obj_traffic = CSVRegTraffic(guid, product_type, product_tmp_root=self._reg_tmp_path)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', guid)
        if display_name is not None:
            obj_traffic.funcSetPredefinedLogTemplate('SLF_DisplayName', display_name)
            obj_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', display_name)
        product_type = product_type
        product_name = display_name
        product_guid = guid
        self._registered_products.append((product_type, product_name, product_guid))
        return obj_traffic

    def _get_register_domain_traffic(self, product_type, product_name, guid=None, display_name=None):
        if guid is None:
            guid = self._generate_random_uid()
        tree_node = self._get_product_info(product_name)
        if not tree_node:
            return 'Fail to get entity info: %s for domain register' % product_name
        obj_traffic = CSVRegDomainTraffic(guid, product_type, tree_node.Guid, product_tmp_root=self._reg_tmp_path)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', guid)
        if display_name is not None:
            obj_traffic.funcSetPredefinedLogTemplate('SLF_DisplayName', display_name)
            obj_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', display_name)
        return obj_traffic

    def _get_register_client_traffic(self, product_type, product_name, parent_name, guid=None, display_name=None):
        if guid is None:
            guid = self._generate_random_uid()
        tree_node = self._get_parent_info(parent_name, product_name)

        if not tree_node:
            return 'Fail to get entity info: %s for client register' % product_name
        obj_traffic = CSVRegClientTraffic(guid, product_type, tree_node.Guid, product_tmp_root=self._reg_tmp_path)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', guid)
        if display_name is not None:
            obj_traffic.funcSetPredefinedLogTemplate('SLF_DisplayName', display_name)
            obj_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', display_name)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_DomainName', parent_name)
        return obj_traffic

    # type [0: product, 1: domain, 2: client]
    def prepare_register_data_list(self, register_type):
        print('Register Data list: {0}'.format(self._data_list))
        if len(self._data_list) <= 0:
            return 'There are no log data existed.'
        product_idx = self._column_list.index('Product')
        entity_name_idx = self._column_list.index('Entity Name')
        try:
            guid_idx = self._column_list.index('GUID')
        except:
            guid_idx = -1
        if register_type == 0:
            parent_product = ''
            parent_tree_name = self._column_list.index('Entity Tree Path')
        elif register_type == 1:
            parent_product = self._column_list.index('Parent_Product_Entity')
            parent_tree_name = parent_product
        elif register_type == 2:
            parent_product = self._column_list.index('Parent_Product_Entity')
            parent_tree_name = self._column_list.index('Parent_Domain')
        else:
            return 'Un-support type'

        tmp_csv_name_mapping = {
            'Entity Tree Path': 'SLF_FolderPath',
            'Hostname': 'SLF_ComputerName',
            'MAC_Addr': 'SLF_MACAddressList',
            'IP_Addr': 'SLF_IPAddressList',
            'OSName': 'SLF_OSName',
            'OSVersion': 'SLF_OSVersion',
            'OS_SevicePack': 'SLF_OSServicePackVersion',
            'GUID': 'SLF_ProductGUID'
        }

        for data_row_list in self._data_list:
            if len(data_row_list) < 4:
                continue
            obj_traffic = 'Un-support type'
            if guid_idx < 0:
                guid = None
            else:
                guid = data_row_list[guid_idx]
            if register_type == 0:
                obj_traffic = self._get_register_product_traffic(data_row_list[product_idx], guid,
                                                                 data_row_list[entity_name_idx])
                obj_traffic.funcSetPredefinedLogTemplate('SLF_FolderPath',
                                                         data_row_list[parent_tree_name])
            elif register_type == 1:
                obj_traffic = self._get_register_domain_traffic(data_row_list[product_idx],
                                                                data_row_list[parent_product],
                                                                guid, data_row_list[entity_name_idx])
            elif register_type == 2:
                obj_traffic = self._get_register_client_traffic(data_row_list[product_idx],
                                                                data_row_list[parent_product],
                                                                data_row_list[parent_tree_name],
                                                                guid, data_row_list[entity_name_idx])
            if isinstance(obj_traffic, str):
                return obj_traffic
            for i in range(0, len(data_row_list)):
                if i in (entity_name_idx, product_idx, parent_product, parent_tree_name, entity_name_idx, guid_idx):
                    continue
                real_key = tmp_csv_name_mapping.get(self._column_list[i])
                if real_key is None:
                    real_key = self._column_list[i]
                if len(data_row_list[i]) > 0:
                    obj_traffic.funcSetPredefinedLogTemplate(real_key, data_row_list[i])
            self._traffic_list.append(obj_traffic)
        return 0

    def register_product_with_csv_file(self, file_path, reg_type, with_status=True):
        if not os.path.isfile(file_path):
            return 0
        print('Register product: '+file_path)
        ret = self._load_csv_file(file_path)
        if ret != 0:
            return ret
        ret = self.prepare_register_data_list(reg_type)
        if ret != 0:
            return ret
        if reg_type == 2:
            ret = self._send_register_request(with_status=with_status)
        else:
            ret = self._send_register_request()
        return ret

    def register_with_csv_file(self, set_name, set_root, with_status=True):
        product_csv_file = os.path.join(set_root, set_name+'_Product_register.csv')
        domain_csv_file = os.path.join(set_root, set_name+'_Domain_register.csv')
        client_csv_file = os.path.join(set_root, set_name+'_Client_register.csv')
        self._registered_products = []
        if not (os.path.isfile(product_csv_file) or os.path.isfile(domain_csv_file) or os.path.isfile(client_csv_file)):
            return 'Nothing to register!!'
        list_reg_file = (product_csv_file, domain_csv_file, client_csv_file)
        for reg_file in list_reg_file:
            ret = self.register_product_with_csv_file(reg_file, list_reg_file.index(reg_file), with_status)
            if ret != 0:
                return ret
        return 0

    def unregister_with_csv_file(self, set_name, set_root):
        product_csv_file = os.path.join(set_root, set_name+'_Product_register.csv')
        if not os.path.isfile(product_csv_file):
            return 'Nothing to unregister!!'
        ret = self._load_csv_file(product_csv_file)
        if ret != 0:
            return ret
        idx_guid = self._column_list.index('GUID')
        for product in self._data_list:
            self.unregister_product(product[idx_guid])
            if self._check_guid_is_existed(product[idx_guid]):
                ret = 'Unregister failed: %s' % product[idx_guid]
        return ret

    def register_product(self, product_type, guid=None, display_name=None):
        self._registered_products = []
        obj_traffic = self._get_register_product_traffic(product_type, guid, display_name)
        ret = self._send_register_request(obj_traffic)
        if ret != 0:
            return ret
        return ret

    def register_domain(self, product_type, product_name, guid=None, display_name=None):
        obj_traffic = self._get_register_domain_traffic(product_type, product_name, guid, display_name)
        return self._send_register_request(obj_traffic)

    def register_client(self, product_type, product_name, parent_name, guid=None, display_name=None, with_status=False):
        obj_traffic = self._get_register_client_traffic(product_type, product_name, parent_name, guid, display_name)
        return self._send_register_request(obj_traffic, with_status)

    def batch_register_client_by_csv(self, csv_file):
        self._load_csv_file(csv_file)
        idx_type = self._column_list.index('Product')
        idx_parent = self._column_list.index('Parent_Product_Entity')
        idx_domain = self._column_list.index('Parent_Domain')
        idx_pre_name = self._column_list.index('Entity Name')
        idx_pre_guid = self._column_list.index('GUID')
        idx_count = self._column_list.index('Count')
        for data_line in self._data_list:
            ret = self.batch_register_client(data_line[idx_type], data_line[idx_parent], data_line[idx_domain],
                                             data_line[idx_pre_guid], data_line[idx_pre_name], data_line[idx_count])
            print('Batch register result: {0}'.format(ret))
        return 0

    def batch_register_client(self, product_type, product_name, parent_name, pre_guid, pre_display_name, count):
        # send client register
        pending_clients = []
        tmp_clients = []
        entity_info = self._get_product_info(product_name)
        client_traffic = self._get_register_client_traffic(product_type, product_name, parent_name,
                                                           entity_info[1], product_name)
        product_id = client_traffic.funcGetTemplateValue('SLF_ProductID')
        guid_lst = self._get_guid_list(pre_guid, int(count))
        index = 0
        for guid in guid_lst:
            index += 1
            client_guid = guid
            client_name = pre_display_name+'_'+str(index)
            client_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', client_guid)
            client_traffic.funcSetPredefinedLogTemplate('SLF_DisplayName', client_name)
            client_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', client_name)
            blob_msg = client_traffic.funcGetBlobMessage()
            tmp_clients.append(blob_msg)
            if len(tmp_clients) >= 1:
                pending_clients.append(tmp_clients)
                tmp_clients = []

        if len(tmp_clients) > 0:
            pending_clients.append(tmp_clients)
            tmp_clients = []
        for_index = 0
        for client_blob in pending_clients:
            for_index += 1
            header_str = client_traffic.funcGetHeader()
            body_str = ''.join(client_blob)
            if 1:
                rep = self._urlopen(self._server_url, header_str+body_str, timeout=60)
                resp_data_list = rep.read().split('\r\n')
                print('Return of batch register: {0}'.format(resp_data_list))
            else:
                t = Thread(target=t_send_blob, args=(self._server_url, header_str+body_str,))
                t.start()

        # send client status log
        pending_status = []
        tmp_status = []
        for_index = 0
        status_traffic = CSVLogTraffic(entity_info[1], 'Status', 'status_15-FULL', 1, log_tmp_root=self._log_tmp_path)
        index = 0
        for guid in guid_lst:
            index += 1
            client_guid = guid
            client_name = pre_display_name+'_'+str(index)
            status_traffic.funcSetPredefinedLogTemplate('SLF_ProductID', product_id)
            status_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', client_guid)
            status_traffic.funcSetPredefinedLogTemplate('SLF_ClientGUID', client_guid)
            status_traffic.funcSetPredefinedLogTemplate('SLF_ComputerName', client_name)
            blob_msg = status_traffic.funcGetBlobMessage()
            tmp_status.append(blob_msg)
            if len(tmp_status) > 500:
                pending_status.append(tmp_status)
                tmp_status = []
        if len(tmp_status) > 0:
            pending_status.append(tmp_status)
        for status_obj in pending_status:
            for_index += 1
            header_str = status_traffic.funcGetHeader()
            body_str = ''.join(status_obj)
            rep = self._urlopen(self._server_url, header_str+body_str, timeout=60)
            print('Ret: {1} of sending status: {0}'.format(rep.read(), for_index))

        return 0

    def unregister_product(self, guid):
        obj_traffic = CSVUnRegTraffic(guid, product_tmp_root=self._unreg_tmp_path)
        obj_traffic.funcSetPredefinedLogTemplate('SLF_ProductGUID', guid)

        self.send_traffic_blob(obj_traffic)
        if self._check_guid_is_existed(guid, is_existed=False):
            return 0

        return 'Check unregister failed'

    def upload_profile(self, product_type, product_name=None, guid=None, profile_file=None):
        if guid is None:
            if product_name is None:
                return 'No product name and guid assigned'
            product_info = self._get_product_info(product_name)
            guid = product_info[1]
        obj_traffic = CSVRegTraffic(guid, product_type, product_tmp_root=self._reg_tmp_path)
        header_str = obj_traffic.funcGetProfileHeader()
        body_str = obj_traffic.funcGetProfileBlobMessage(profile_file=profile_file)
        resp = self._urlopen(self._server_url, header_str+body_str, timeout=60)
        list_resp = resp.read().splitlines()
        if 'content: ' not in list_resp:
            print('Upload profile might failed, {0}: name: {1}, guid: {2}'.format(
                product_type, product_name, guid))
        else:
            print('Upload profile response: {0}\ncontent: {1}'.format(resp.getcode(), resp.read()))
        return 0

    def upload_profile_by_file(self, csv_file):
        self._load_csv_file(csv_file)
        if len(self._data_list) <= 0:
            return 'There are no log data existed.'
        name_idx = self._column_list.index('EntityName')
        product_idx = self._column_list.index('Product')
        profile_idx = self._column_list.index('Profile')
        for list_profile in self._data_list:
            if not all(list_profile):
                print('Data not enough: {0}'.format(list_profile))
                continue
            print('Prepare to upload profile: {0} / {1}'.format(list_profile[product_idx], list_profile[name_idx]))
            profile_file = list_profile[profile_idx]
            if not os.path.exists(profile_file):
                root_path = os.path.dirname(csv_file)
                profile_file = os.path.join(root_path, profile_file)
            if not os.path.exists(profile_file):
                print('Profile is not existed: {0}'.format(list_profile[profile_idx]))
                continue
            ret = self.upload_profile(list_profile[product_idx], list_profile[name_idx], profile_file=profile_file)
            print('Upload Profile {0}: {1}'.format(list_profile, ret))
        return 0

    def upload_registered_product_profile(self):
        if len(self._registered_products) == 0:
            return 'No registered products'
        dict_uploads = {}
        for (product_type, name, guid) in self._registered_products:
            dict_uploads[product_type] = (name, guid)
        for k, v in dict_uploads.items():
            ret = self.upload_profile(k, v[0], v[1])
            if ret != 0:
                return ret
        return 0

    def send_traffic_blob(self, traffic_obj):
        header_str = traffic_obj.funcGetHeader()
        header_str = header_str.encode()
        body_str = traffic_obj.funcGetBlobMessage()
        rep = self._urlopen(self._server_url, header_str+body_str, timeout=60)

        return rep


def t_send_blob(server_url, body_str):
    rep = _urlopen(server_url, body_str, timeout=60)
    resp_data_list = rep.read().split('\r\n')
    print('Send blob result: {0}'.format(resp_data_list))


def _urlopen(server_url, body_str, timeout):
    rep = None
    try:
        rep = urllib.request.urlopen(server_url, body_str, timeout=timeout, context=ctx)
    except:
        pass
    return rep


if __name__ == '__main__':
    log_sender = LogSender()
    # log_sender.send_log(r'C:\Users\tmcm\Downloads\log_TOOL\Testing_Data\MDR\Initialize\status.csv')
    # print(log_sender.register_with_csv_file('Init', r'C:\Users\tmcm\Downloads\log_TOOL\Testing_Data\MDR\Initialize'))

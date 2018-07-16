import re
import inspect
import datetime
from lib.LogSender import MCPStreamWrapper, ValueGenerator


# Define Global Type Value
(tSTRING, tWSTRING, tBYTE, tINT16, tUINT16, tINT32, tUINT32, tGROUP_START, tGROUP_END) = list(range(1, 8)) + [100, 101]
(tGROUP_START_TAG, tGROUP_ITEM_START_TAG, tGROUP_ITEM_END_TAG, tGROUP_END_TAG) = list(range(1, 5))
X_STRING = 1
X_WSTRING = 2
X_BYTE = 3
X_INT16 = 4
X_UINT16 = 5
X_INT32 = 6
X_UINT32 = 7
X_INT64 = 8
X_UINT64 = 9
X_GROUP_START = 100
X_GROUP_END = 101


class LogGenerator(object):
    """
    The Log / Reg Blob Generator
    """
    _mcp_item_cache = dict()

    def __init__(self, str_template_path):
        self._strTemplatePath = str_template_path
        self._listTemplate = []
        self._funcLoadTemplate()
        self._isrepeatable = True

    def _funcLoadTemplate(self):
        """
        Load Template into the dictTemplate
        """
        obj_compiler = re.compile(r"(?P<id>\d+)[,](?P<type>\d+)[,](?P<symbolic>(\w+)?)[,](?P<value>.*)$")

        for strLine in open(self._strTemplatePath, 'r'):
            # Skip Empty Line or Comment
            if strLine == '':
                continue
            if strLine.startswith("#"):
                continue

            # Start Match
            obj_matched = obj_compiler.match(strLine)
            if obj_matched is None:
                continue
            else:
                self._listTemplate.append({"id": int(obj_matched.group('id')),
                                           "type": int(obj_matched.group('type')),
                                           "symbol": obj_matched.group('symbolic'),
                                           "value": self._funcCreateValueGen(obj_matched.group('value'))})

    def funcSetRedefinedTemplate(self, str_field_name, obj_content):
        """
        Set the pre-defined Content to overwrite Template
        """

        # Find the Target Field on Template
        for dictField in self._listTemplate:
            if dictField["symbol"].lower() == str_field_name.lower():
                if isinstance(obj_content, list):
                    dictField["value"] = ValueGenerator.ListGen(obj_content)
                else:
                    new_value = self._funcCreateValueGen(obj_content)
                    if new_value is not None:
                        dictField["value"] = new_value

    def funcGetTemplateValue(self, str_field_name):
        """
        Get the Template value
        """

        # Find the Target Field on Template
        for dictField in self._listTemplate:
            if dictField["symbol"] == str_field_name:
                return dictField["value"]

    def _funcAddMCPItem(self, obj_mcp_message, str_type, str_field_id, str_value):
        mcp_item_key = hash((str_type, str_field_id, str_value))
        mcp_item = self._mcp_item_cache.get(mcp_item_key)
        if mcp_item is not None:
            pass
        elif str_type == tBYTE:
            mcp_item = MCPStreamWrapper.MCPItemByte(str_field_id, str_value, True)
        elif str_type == tINT16:
            mcp_item = MCPStreamWrapper.MCPItemINT16(str_field_id, str_value, True)
        elif str_type == tUINT16:
            mcp_item = MCPStreamWrapper.MCPItemUINT16(str_field_id, str_value, True)
        elif str_type == tINT32:
            mcp_item = MCPStreamWrapper.MCPItemINT32(str_field_id, str_value, True)
        elif str_type == tUINT32:
            mcp_item = MCPStreamWrapper.MCPItemUINT32(str_field_id, str_value, True)
        elif str_type == tSTRING:
            mcp_item = MCPStreamWrapper.MCPItemString(str_field_id, str_value, True)
        elif str_type == tWSTRING:
            if not str_value:
                str_value = ""
            mcp_item = MCPStreamWrapper.MCPItemWString(str_field_id, str_value, True)
        elif str_type == tGROUP_START:
            mcp_item = MCPStreamWrapper.MCPItemGroupTag(str_field_id, True, True)
        elif str_type == tGROUP_END:
            mcp_item = MCPStreamWrapper.MCPItemGroupTag(str_field_id, False, True)
        else:
            raise Exception("No Matched Content %s " % str_type)
        self._mcp_item_cache[mcp_item_key] = mcp_item
        obj_mcp_message.Add(mcp_item)

    def funcIsRepeatable(self):
        return self._isrepeatable

    def funcGetOneBlob(self, is_network_order=True):
        """
        Generate One Blob content
        """
        obj_mcp_blob = MCPStreamWrapper.MCPMessage(is_network_order)
        for dict_one_field in self._listTemplate:
            if inspect.isroutine(dict_one_field["value"]):
                self._funcAddMCPItem(obj_mcp_blob, dict_one_field["type"], dict_one_field["id"],
                                     dict_one_field["value"]())
            elif isinstance(dict_one_field["value"], ValueGenerator.Generator):
                self._funcAddMCPItem(obj_mcp_blob, dict_one_field["type"], dict_one_field["id"],
                                     dict_one_field["value"].GetNext())
            else:
                self._funcAddMCPItem(obj_mcp_blob, dict_one_field["type"], dict_one_field["id"],
                                     dict_one_field["value"])

        return obj_mcp_blob.Pack()

    def _get_date_string(self, key):
        time_format = '%Y-%m-%d %H:%M:%S'
        is_utc = True if '<Gen_UTCTime>' in key else False
        key_list = [_f for _f in key.split('>') if _f]
        cur_time = datetime.datetime.utcnow() if is_utc else datetime.datetime.now()
        if len(key_list) > 1:
            for time_offset_value in key_list[1:]:
                time_offset_str = time_offset_value.replace('<', '')
                time_offset_list = time_offset_str.split('_')
                time_offset_int = int(time_offset_list[1])
                if time_offset_list[0] == 'DAY':
                    time_offset = datetime.timedelta(days=time_offset_int)
                elif time_offset_list[0] == 'HOUR':
                    time_offset = datetime.timedelta(hours=time_offset_int)
                else:
                    time_offset = datetime.timedelta()
                cur_time = cur_time + time_offset
        return cur_time.strftime(time_format)

    def _funcCreateValueGen(self, str_value):
        """
        Create the Corresponding Data Generator
        """
        obj_return = str_value
        if not isinstance(str_value, str):
            return obj_return

        tmp_value = str_value.strip('"')
        if tmp_value.startswith("%%"):
            self._is_repeatable = False
            str_token_key = tmp_value.split("%%")[1]
            if str_token_key == "Random_UUID":
                obj_return = ValueGenerator.funcCreateRandomTUID()
            elif str_token_key == "Array_Content":
                obj_return = ValueGenerator.ListGen(tmp_value.split("%%")[-1].split(","))
            elif str_token_key.startswith("Random_String"):
                int_string_length = int(str_token_key.split("_")[-1])
                obj_return = ValueGenerator.funcCreateRandomString(int_string_length)
            elif str_token_key.startswith("SEQ_Time_Today"):
                obj_return = ValueGenerator.SeqGen(datetime.date.today().strftime("%Y-%m-%d") + " %s",
                                                   ValueGenerator.SeqGen.G_TIME)
            elif str_token_key.startswith("Auto_Increment"):
                tmp_list = str_token_key.split('-')
                start_idx = 0 if len(tmp_list) == 1 else int(tmp_list[1])
                obj_return = ValueGenerator.SeqGen('%d', ValueGenerator.SeqGen.G_INT)
                obj_return.objBase = start_idx
        elif tmp_value.startswith('<Gen_Time>') or tmp_value.startswith('<Gen_UTCTime>'):
            self._is_repeatable = False
            obj_return = self._get_date_string(tmp_value)
        elif tmp_value == '<DEFAULT>':
            obj_return = None
        elif tmp_value.startswith('<NEST>'):
            return None

        return obj_return


if __name__ == "__main__":
    pass
    # import os
    # template_root = os.path.dirname(os.path.realpath(__file__))
    # strTemplatePath = os.path.join(G_TemplateRoot, "REG", "LogonAccount.ini")
    # objLogGenerator = LogGenerator(strTemplatePath)
    # print(objLogGenerator.funcGetOneBlob())

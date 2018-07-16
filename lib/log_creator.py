from db.factory_boy import *
from db import *


def create_SO_log(**kwargs):
    return TbLogBlacklistInfoJournalFactory(**kwargs)


def create_virus_log(**kwargs):
    return TbAvviruslogFactory(**kwargs)


def create_NCIE_log(**kwargs):
    return TbNetworkContentInspectionEngineLogFactory(**kwargs)


def create_websecurity_log(**kwargs):
    return TbWebSecurityLogFactory(**kwargs)


def create_file_hash_detection_log(**kwargs):
    return TbFileHashDetectionLogFactory(**kwargs)


def create_TMUFE_log(**kwargs):
    kwargs['MsgType'] = 1739
    create_log_general_set(**kwargs)


def create_CAV_log(**kwargs):
    kwargs['MsgType'] = 1723
    create_log_general_set(**kwargs)


def get_args_for_table(args, model):
    columns = [column.key for column in model.__table__.columns]
    return {k: v for (k, v) in args.items() if k in columns}


def create_log_general_set(**kwargs):
    blacklist = None
    log_general_args = get_args_for_table(kwargs, TbLogGeneral)
    log_ip_args = get_args_for_table(kwargs, TbLogIP)
    log_mail_args = get_args_for_table(kwargs, TbLogMail)
    log_file_args = get_args_for_table(kwargs, TbLogFile)
    if 'blacklist' in kwargs:
        blacklist = kwargs['blacklist']

    log_general = TbLogGeneralFactory(**log_general_args)

    if 'SHA1' in kwargs:
        TbLogFileFactory(log_general=log_general, **log_file_args)
    else:
        TbLogIPFactory(log_general=log_general, blacklist=blacklist, **log_ip_args)
        TbLogMailFactory(log_general=log_general, **log_mail_args)


def create_assess_impact_set(user, match_so, match_client):
    ddes_task = TbDDESTaskFactory(user=user)
    if isinstance(match_so, TbLogBlacklistInfoJournal):
        match_so = TbBlacklistInfo.find_by_slf_data(match_so.SLF_Data)
    return TbDDESScanResultFactory(client=match_client, match_so=match_so, task=ddes_task)

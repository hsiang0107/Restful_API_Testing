from db import *
from db.cm_session import cm_session


def execute_store_procedure(sp):
    cm_session.execute(sp)
    cm_session.commit()


def clear_blacklist_logs():
    TbLogBlacklistInfoJournal.truncate()
    TbBlacklistInfo.truncate()
    TbBlacklistExtraInfo.truncate()
    TbBlacklistRestJournal.truncate()
    TbBlacklistRESTRegisterProductList.truncate()


def clear_web_security_logs():
    TbWebSecurityLog.truncate()
    TbTotalWebSecurityCount.truncate()
    TbWebSecurityLogCategory.truncate()


def clear_personal_firewall_logs():
    TbPersonalFirewallLog.truncate()


def clear_tda_logs():
    TbLogGeneral.truncate()
    TbLogIP.truncate()
    TbLogMitigation.truncate()
    TbLogMail.truncate()
    TbLogFile.truncate()
    TbSuspiciousLogH.truncate()
    TbSuspiciousLogI.truncate()
    TbSuspiciousLogL.truncate()
    TbSuspiciousLogM.truncate()
    TbSuspiciousLogIPList.truncate()
    TbLogGeneralAffectedHost.truncate()
    TbSuspiciousLogSummaryToday1.truncate()
    TbSuspiciousLogSummaryToday2.truncate()
    TbSuspiciousLogSummaryHistory.truncate()
    TbSuspiciousLogSummaryPreSum.truncate()


def clear_ncie_logs():
    TbNetworkContentInspectionEngineLog.truncate()


def clear_cnc_logs():
    TbCnCDetection.truncate()
    TbCnCDetectionByMachine.truncate()
    TbMessageDetectionByUser.truncate()


def clear_file_hash_detection_logs():
    TbFileHashDetectionLog.truncate()
    TbFileHashDetectionByMachine.truncate()
    TbFileHashDetectionByUser.truncate()


def clear_virus_logs():
    TbAVVirusLog.truncate()
    TbTotalVirusCount.truncate()
    Tbvirusspywaresummary.truncate()
    TbDCSsummary.truncate()
    TbVirusOutbreakAccumulate.truncate()


def clear_spyware_logs():
    TbSpywareLog.truncate()
    TbSpywareDetail.truncate()


def clear_device_access_control_logs():
    TbDeviceAccessControlLog.truncate()


def clear_security_logs():
    TbSecurityLog.truncate()
    TbSecurityLogViolateBlackInfo.truncate()


def clear_behavior_monitor_logs():
    TbLogBehaviorMonitor.truncate()
    TbLogBehaviorMonitorDetail.truncate()


def clear_intrusion_prevention_logs():
    TbLogIntrusionPrevention.truncate()


def clear_correlation_logs():
    TbLogCorrelation.truncate()


def clear_application_control_event_logs():
    TbApplicationControlEvent.truncate()


def clear_security_compliance_logs():
    TbSecurityCompliance.truncate()


def clear_dlp_logs():
    TbLogDataLossPrevention.truncate()
    TbLogDataLossPreventionTemplate.truncate()
    TbLogDataLossPreventionAction.truncate()


def clear_data_discovery_logs():
    TbLogDataDiscoveryJournal.truncate()
    TbLogDataDiscoveryTemplate.truncate()
    TbLogDataDiscoveryFileAction.truncate()
    TbLogDataDiscoveryDeviceJournal.truncate()
    TbLogDataDiscoveryFileJournal.truncate()


def clear_integrity_monitor_logs():
    TbLogIntegrityMonitor.truncate()


def clear_threat_mitigation_logs():
    TbLogThreatMitigation.truncate()
    TbLogThreatMitigationHistory.truncate()


def clear_role_base_auditing_logs():
    TbProductRoleBaseAuditLog.truncate()


def clear_event_logs():
    TbAVEventLog.truncate()


def clear_security_violation_logs():
    TbSecurityViolations.truncate()


def clear_network_virus_logs():
    TbPacketsVirusLog.truncate()


def clear_security_statistic_logs():
    TbSecurityStatistics.truncate()


def clear_ddes_assess_impact_logs():
    TbDDESTask.truncate()
    TbDDESScanResult.truncate()


def reset_watermark():
    Tbjournalcheckpoint.reset_all_bigwatermark()
    Tbjournalcheckpoint.reset_all_watermark()


def clear_so_logs():
    clear_blacklist_logs()
    clear_web_security_logs()
    clear_personal_firewall_logs()
    clear_tda_logs()
    clear_ncie_logs()
    clear_cnc_logs()
    clear_file_hash_detection_logs()
    clear_ddes_assess_impact_logs()
    reset_watermark()


def clear_log_query_logs():
    clear_virus_logs()
    clear_spyware_logs()
    clear_web_security_logs()
    clear_personal_firewall_logs()
    clear_ncie_logs()
    clear_device_access_control_logs()
    clear_behavior_monitor_logs()
    clear_file_hash_detection_logs()
    clear_security_logs()
    clear_tda_logs()
    clear_intrusion_prevention_logs()
    clear_correlation_logs()
    clear_application_control_event_logs()
    clear_security_compliance_logs()
    clear_dlp_logs()
    clear_data_discovery_logs()
    clear_integrity_monitor_logs()
    clear_threat_mitigation_logs()
    clear_blacklist_logs()
    clear_role_base_auditing_logs()
    clear_event_logs()
    clear_security_violation_logs()
    clear_network_virus_logs()
    clear_security_statistic_logs()
    reset_watermark()


def clear_inventory_logs():
    TbInventorySecurityToUserDataMD5Map.truncate()
    TbInventorySecurityToUserEndpoint.truncate()
    TbInventorySecurityToUserMachine.truncate()
    TbInventorySecurityToUserUser.truncate()
    TbInventorySecurityToUserSummaryEndpoint.truncate()
    TbInventorySecurityToUserSummaryMachine.truncate()
    TbInventorySecurityToUserSummaryUser.truncate()
    TbInventorySecurityToUserPreSumEndpoint.truncate()
    TbInventorySecurityToUserPreSumUser.truncate()
    TbInventorySecurityToUserPreSumMachine.truncate()
    TbInventoryCriticalEventSummaryUser.truncate()
    TbInventoryCriticalEventSummaryEndpoint.truncate()
    TbInventoryCriticalEventSummaryMachine.truncate()


def clear_iES_backend_logs():
    TbInventoryQuickInvScanMapping.truncate()
    TbQuickInvTask.truncate()
    TbQuickInvMatchObjectInfo.truncate()
    TbRCATask.truncate()
    TbRCAMatchObjectJournal.truncate()
    TbRCAMatchObjectJournal.truncate()


def clear_global_retroscan_task():
    TbGlobalRetroScanTask.truncate()


def clear_tb_ExternalWebServiceConsumers():
    TbExternalWebServiceConsumers.truncate()


def clear_ioc_stix_yara_table():
    TbIOCFileList.truncate()
    TbIOCsSTIXFileList.truncate()
    TbIOCsYARAFileList.truncate()
    TbIOCsUDSOMap.truncate()
    TbBlacklistSourceInfo.truncate()
    TbBlacklistInfo.truncate()

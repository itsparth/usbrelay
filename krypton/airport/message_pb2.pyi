from google.protobuf import timestamp_pb2 as _timestamp_pb2
from krypton.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmployeeSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    employeeSort_unspecified: _ClassVar[EmployeeSort]
    employeeSort_biometricsIdAsc: _ClassVar[EmployeeSort]
    employeeSort_biometricsIdDesc: _ClassVar[EmployeeSort]
    employeeSort_cisfIdAsc: _ClassVar[EmployeeSort]
    employeeSort_cisfIdDesc: _ClassVar[EmployeeSort]
    employeeSort_nameAsc: _ClassVar[EmployeeSort]
    employeeSort_nameDesc: _ClassVar[EmployeeSort]
    employeeSort_rankAsc: _ClassVar[EmployeeSort]
    employeeSort_rankDesc: _ClassVar[EmployeeSort]

class EmployeeActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    employeeActivityLogSort_unspecified: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_activityAtAsc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_activityAtDesc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_biometricsIdAsc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_biometricsIdDesc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_cisfIdAsc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_cisfIdDesc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_nameAsc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_nameDesc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_rankAsc: _ClassVar[EmployeeActivityLogSort]
    employeeActivityLogSort_rankDesc: _ClassVar[EmployeeActivityLogSort]

class DutyPostSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    dutyPostSort_unspecified: _ClassVar[DutyPostSort]
    dutyPostSort_nameAsc: _ClassVar[DutyPostSort]
    dutyPostSort_nameDesc: _ClassVar[DutyPostSort]

class DutyPostActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    dutyPostActivityLogSort_unspecified: _ClassVar[DutyPostActivityLogSort]
    dutyPostActivityLogSort_activityAtAsc: _ClassVar[DutyPostActivityLogSort]
    dutyPostActivityLogSort_activityAtDesc: _ClassVar[DutyPostActivityLogSort]
    dutyPostActivityLogSort_nameAsc: _ClassVar[DutyPostActivityLogSort]
    dutyPostActivityLogSort_nameDesc: _ClassVar[DutyPostActivityLogSort]

class WeaponSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponSort_unspecified: _ClassVar[WeaponSort]
    weaponSort_nameAsc: _ClassVar[WeaponSort]
    weaponSort_nameDesc: _ClassVar[WeaponSort]
    weaponSort_countAsc: _ClassVar[WeaponSort]
    weaponSort_countDesc: _ClassVar[WeaponSort]

class WeaponActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponActivityLogSort_unspecified: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_activityAtAsc: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_activityAtDesc: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_nameAsc: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_nameDesc: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_countAsc: _ClassVar[WeaponActivityLogSort]
    weaponActivityLogSort_countDesc: _ClassVar[WeaponActivityLogSort]

class AmmoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoSort_unspecified: _ClassVar[AmmoSort]
    ammoSort_nameAsc: _ClassVar[AmmoSort]
    ammoSort_nameDesc: _ClassVar[AmmoSort]
    ammoSort_countAsc: _ClassVar[AmmoSort]
    ammoSort_countDesc: _ClassVar[AmmoSort]

class AmmoActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoActivityLogSort_unspecified: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_activityAtAsc: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_activityAtDesc: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_nameAsc: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_nameDesc: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_countAsc: _ClassVar[AmmoActivityLogSort]
    ammoActivityLogSort_countDesc: _ClassVar[AmmoActivityLogSort]

class OtherItemsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    otherItemsSort_unspecified: _ClassVar[OtherItemsSort]
    otherItemsSort_nameAsc: _ClassVar[OtherItemsSort]
    otherItemsSort_nameDesc: _ClassVar[OtherItemsSort]
    otherItemsSort_countAsc: _ClassVar[OtherItemsSort]
    otherItemsSort_countDesc: _ClassVar[OtherItemsSort]

class OtherItemsActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    otherItemsActivityLogSort_unspecified: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_activityAtAsc: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_activityAtDesc: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_nameAsc: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_nameDesc: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_countAsc: _ClassVar[OtherItemsActivityLogSort]
    otherItemsActivityLogSort_countDesc: _ClassVar[OtherItemsActivityLogSort]

class AssignmentSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    assignmentSort_unspecified: _ClassVar[AssignmentSort]

class AssignmentActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    assignmentActivityLogSort_unspecified: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_activityAtAsc: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_activityAtDesc: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_weaponButtNoAsc: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_weaponButtNoDesc: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_ammoCountAsc: _ClassVar[AssignmentActivityLogSort]
    assignmentActivityLogSort_ammoCountDesc: _ClassVar[AssignmentActivityLogSort]

class ShiftReportItemSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    shiftReportItemSort_unspecified: _ClassVar[ShiftReportItemSort]
    shiftReportItemSort_employeeNameAsc: _ClassVar[ShiftReportItemSort]
    shiftReportItemSort_employeeNameDesc: _ClassVar[ShiftReportItemSort]

class ScheduleSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    scheduleSort_unspecified: _ClassVar[ScheduleSort]
    scheduleSort_startTimeAsc: _ClassVar[ScheduleSort]
    scheduleSort_startTimeDesc: _ClassVar[ScheduleSort]
    scheduleSort_endTimeAsc: _ClassVar[ScheduleSort]
    scheduleSort_endTimeDesc: _ClassVar[ScheduleSort]

class ScheduleActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    scheduleActivityLogSort_unspecified: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_activityAtAsc: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_activityAtDesc: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_startTimeAsc: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_startTimeDesc: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_endTimeAsc: _ClassVar[ScheduleActivityLogSort]
    scheduleActivityLogSort_endTimeDesc: _ClassVar[ScheduleActivityLogSort]

class WeaponAmmoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponAmmoSort_unspecified: _ClassVar[WeaponAmmoSort]
    weaponAmmoSort_countAsc: _ClassVar[WeaponAmmoSort]
    weaponAmmoSort_countDesc: _ClassVar[WeaponAmmoSort]

class WeaponAmmoActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponAmmoActivityLogSort_unspecified: _ClassVar[WeaponAmmoActivityLogSort]
    weaponAmmoActivityLogSort_activityAtAsc: _ClassVar[WeaponAmmoActivityLogSort]
    weaponAmmoActivityLogSort_activityAtDesc: _ClassVar[WeaponAmmoActivityLogSort]
    weaponAmmoActivityLogSort_countAsc: _ClassVar[WeaponAmmoActivityLogSort]
    weaponAmmoActivityLogSort_countDesc: _ClassVar[WeaponAmmoActivityLogSort]

class GlobalConfigSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    globalConfigSort_unspecified: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueBeforeStartBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueBeforeStartBufferDesc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueAfterStartBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueAfterStartBufferDesc: _ClassVar[GlobalConfigSort]
    globalConfigSort_scheduleEditAfterBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_scheduleEditAfterBufferDesc: _ClassVar[GlobalConfigSort]

class GlobalConfigActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    globalConfigActivityLogSort_unspecified: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_activityAtAsc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_activityAtDesc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_weaponIssueBeforeStartBufferAsc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_weaponIssueBeforeStartBufferDesc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_weaponIssueAfterStartBufferAsc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_weaponIssueAfterStartBufferDesc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_scheduleEditAfterBufferAsc: _ClassVar[GlobalConfigActivityLogSort]
    globalConfigActivityLogSort_scheduleEditAfterBufferDesc: _ClassVar[GlobalConfigActivityLogSort]

class FlowAlertsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowAlertsSort_unspecified: _ClassVar[FlowAlertsSort]
    flowAlertsSort_weaponIssueAfterShiftStartDurationAsc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_weaponIssueAfterShiftStartDurationDesc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_clearingIssueAfterWeaponEntryDurationAsc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_clearingIssueAfterWeaponEntryDurationDesc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_ammoIssueAfterClearingEntryDurationAsc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_ammoIssueAfterClearingEntryDurationDesc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_weaponNotDepositDurationAsc: _ClassVar[FlowAlertsSort]
    flowAlertsSort_weaponNotDepositDurationDesc: _ClassVar[FlowAlertsSort]

class FlowAlertsActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowAlertsActivityLogSort_unspecified: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_activityAtAsc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_activityAtDesc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_weaponIssueAfterShiftStartDurationAsc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_weaponIssueAfterShiftStartDurationDesc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_clearingIssueAfterWeaponEntryDurationAsc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_clearingIssueAfterWeaponEntryDurationDesc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_ammoIssueAfterClearingEntryDurationAsc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_ammoIssueAfterClearingEntryDurationDesc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_weaponNotDepositDurationAsc: _ClassVar[FlowAlertsActivityLogSort]
    flowAlertsActivityLogSort_weaponNotDepositDurationDesc: _ClassVar[FlowAlertsActivityLogSort]

class CommonInfoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    commonInfoSort_unspecified: _ClassVar[CommonInfoSort]
    commonInfoSort_timeAsc: _ClassVar[CommonInfoSort]
    commonInfoSort_timeDesc: _ClassVar[CommonInfoSort]
    commonInfoSort_remarksAsc: _ClassVar[CommonInfoSort]
    commonInfoSort_remarksDesc: _ClassVar[CommonInfoSort]

class CommonInfoActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    commonInfoActivityLogSort_unspecified: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_activityAtAsc: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_activityAtDesc: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_timeAsc: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_timeDesc: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_remarksAsc: _ClassVar[CommonInfoActivityLogSort]
    commonInfoActivityLogSort_remarksDesc: _ClassVar[CommonInfoActivityLogSort]

class AmmoInfoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoInfoSort_unspecified: _ClassVar[AmmoInfoSort]
    ammoInfoSort_timeAsc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_timeDesc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_remarksAsc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_remarksDesc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_countAsc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_countDesc: _ClassVar[AmmoInfoSort]

class AmmoInfoActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoInfoActivityLogSort_unspecified: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_activityAtAsc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_activityAtDesc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_timeAsc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_timeDesc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_remarksAsc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_remarksDesc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_countAsc: _ClassVar[AmmoInfoActivityLogSort]
    ammoInfoActivityLogSort_countDesc: _ClassVar[AmmoInfoActivityLogSort]

class FlowsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowsSort_unspecified: _ClassVar[FlowsSort]

class FlowsActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowsActivityLogSort_unspecified: _ClassVar[FlowsActivityLogSort]
    flowsActivityLogSort_activityAtAsc: _ClassVar[FlowsActivityLogSort]
    flowsActivityLogSort_activityAtDesc: _ClassVar[FlowsActivityLogSort]

class Position(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Position_unspecified: _ClassVar[Position]
    Position_weapon: _ClassVar[Position]
    Position_clearing: _ClassVar[Position]
    Position_ammo: _ClassVar[Position]

class AlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertType_unspecified: _ClassVar[AlertType]
    alertType_skipWeaponIssue: _ClassVar[AlertType]
    alertType_skipClearingIssue: _ClassVar[AlertType]
    alertType_skipAmmoIssue: _ClassVar[AlertType]
    alertType_skipAmmoDeposit: _ClassVar[AlertType]
    alertType_skipClearingDeposit: _ClassVar[AlertType]
    alertType_skipWeaponDeposit: _ClassVar[AlertType]
    alertType_delayedWeaponIssue: _ClassVar[AlertType]
    alertType_delayedClearingIssue: _ClassVar[AlertType]
    alertType_delayedAmmoIssue: _ClassVar[AlertType]
    alertType_delayedAmmoDeposit: _ClassVar[AlertType]
    alertType_delayedClearingDeposit: _ClassVar[AlertType]
    alertType_delayedWeaponDeposit: _ClassVar[AlertType]

class AlertSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertSort_unspecified: _ClassVar[AlertSort]
    alertSort_timeAsc: _ClassVar[AlertSort]
    alertSort_timeDesc: _ClassVar[AlertSort]

class CheckPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    checkPoint_unspecified: _ClassVar[CheckPoint]
    checkPoint_weapon: _ClassVar[CheckPoint]
    checkPoint_ammo: _ClassVar[CheckPoint]

class UserSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    userSort_unspecified: _ClassVar[UserSort]
    userSort_authNameAsc: _ClassVar[UserSort]
    userSort_authNameDesc: _ClassVar[UserSort]
    userSort_nameAsc: _ClassVar[UserSort]
    userSort_nameDesc: _ClassVar[UserSort]

class UserActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    userActivityLogSort_unspecified: _ClassVar[UserActivityLogSort]
    userActivityLogSort_activityAtAsc: _ClassVar[UserActivityLogSort]
    userActivityLogSort_activityAtDesc: _ClassVar[UserActivityLogSort]
    userActivityLogSort_authNameAsc: _ClassVar[UserActivityLogSort]
    userActivityLogSort_authNameDesc: _ClassVar[UserActivityLogSort]
    userActivityLogSort_nameAsc: _ClassVar[UserActivityLogSort]
    userActivityLogSort_nameDesc: _ClassVar[UserActivityLogSort]

class WeaponInfoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponInfoSort_unspecified: _ClassVar[WeaponInfoSort]
    weaponInfoSort_timeAsc: _ClassVar[WeaponInfoSort]
    weaponInfoSort_timeDesc: _ClassVar[WeaponInfoSort]
    weaponInfoSort_remarksAsc: _ClassVar[WeaponInfoSort]
    weaponInfoSort_remarksDesc: _ClassVar[WeaponInfoSort]
    weaponInfoSort_issuedButtNoAsc: _ClassVar[WeaponInfoSort]
    weaponInfoSort_issuedButtNoDesc: _ClassVar[WeaponInfoSort]

class WeaponInfoActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponInfoActivityLogSort_unspecified: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_activityAtAsc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_activityAtDesc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_timeAsc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_timeDesc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_remarksAsc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_remarksDesc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_issuedButtNoAsc: _ClassVar[WeaponInfoActivityLogSort]
    weaponInfoActivityLogSort_issuedButtNoDesc: _ClassVar[WeaponInfoActivityLogSort]

class Perm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    perm_unspecified: _ClassVar[Perm]
    perm_createP: _ClassVar[Perm]
    perm_readP: _ClassVar[Perm]
    perm_updateP: _ClassVar[Perm]
    perm_deleteP: _ClassVar[Perm]
    perm_accessP: _ClassVar[Perm]

class Scopes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    scopes_unspecified: _ClassVar[Scopes]
    scopes_employee: _ClassVar[Scopes]
    scopes_dutyPost: _ClassVar[Scopes]
    scopes_weapon: _ClassVar[Scopes]
    scopes_ammo: _ClassVar[Scopes]
    scopes_otherItems: _ClassVar[Scopes]
    scopes_assignment: _ClassVar[Scopes]
    scopes_schedule: _ClassVar[Scopes]
    scopes_weaponAmmo: _ClassVar[Scopes]
    scopes_globalConfig: _ClassVar[Scopes]
    scopes_flowAlerts: _ClassVar[Scopes]
    scopes_commonInfo: _ClassVar[Scopes]
    scopes_ammoInfo: _ClassVar[Scopes]
    scopes_flows: _ClassVar[Scopes]
    scopes_alert: _ClassVar[Scopes]
    scopes_user: _ClassVar[Scopes]
    scopes_weaponInfo: _ClassVar[Scopes]
    scopes_tags: _ClassVar[Scopes]

class AccessControlSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    accessControlSort_unspecified: _ClassVar[AccessControlSort]

class AccessControlActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    accessControlActivityLogSort_unspecified: _ClassVar[AccessControlActivityLogSort]
    accessControlActivityLogSort_activityAtAsc: _ClassVar[AccessControlActivityLogSort]
    accessControlActivityLogSort_activityAtDesc: _ClassVar[AccessControlActivityLogSort]
employeeSort_unspecified: EmployeeSort
employeeSort_biometricsIdAsc: EmployeeSort
employeeSort_biometricsIdDesc: EmployeeSort
employeeSort_cisfIdAsc: EmployeeSort
employeeSort_cisfIdDesc: EmployeeSort
employeeSort_nameAsc: EmployeeSort
employeeSort_nameDesc: EmployeeSort
employeeSort_rankAsc: EmployeeSort
employeeSort_rankDesc: EmployeeSort
employeeActivityLogSort_unspecified: EmployeeActivityLogSort
employeeActivityLogSort_activityAtAsc: EmployeeActivityLogSort
employeeActivityLogSort_activityAtDesc: EmployeeActivityLogSort
employeeActivityLogSort_biometricsIdAsc: EmployeeActivityLogSort
employeeActivityLogSort_biometricsIdDesc: EmployeeActivityLogSort
employeeActivityLogSort_cisfIdAsc: EmployeeActivityLogSort
employeeActivityLogSort_cisfIdDesc: EmployeeActivityLogSort
employeeActivityLogSort_nameAsc: EmployeeActivityLogSort
employeeActivityLogSort_nameDesc: EmployeeActivityLogSort
employeeActivityLogSort_rankAsc: EmployeeActivityLogSort
employeeActivityLogSort_rankDesc: EmployeeActivityLogSort
dutyPostSort_unspecified: DutyPostSort
dutyPostSort_nameAsc: DutyPostSort
dutyPostSort_nameDesc: DutyPostSort
dutyPostActivityLogSort_unspecified: DutyPostActivityLogSort
dutyPostActivityLogSort_activityAtAsc: DutyPostActivityLogSort
dutyPostActivityLogSort_activityAtDesc: DutyPostActivityLogSort
dutyPostActivityLogSort_nameAsc: DutyPostActivityLogSort
dutyPostActivityLogSort_nameDesc: DutyPostActivityLogSort
weaponSort_unspecified: WeaponSort
weaponSort_nameAsc: WeaponSort
weaponSort_nameDesc: WeaponSort
weaponSort_countAsc: WeaponSort
weaponSort_countDesc: WeaponSort
weaponActivityLogSort_unspecified: WeaponActivityLogSort
weaponActivityLogSort_activityAtAsc: WeaponActivityLogSort
weaponActivityLogSort_activityAtDesc: WeaponActivityLogSort
weaponActivityLogSort_nameAsc: WeaponActivityLogSort
weaponActivityLogSort_nameDesc: WeaponActivityLogSort
weaponActivityLogSort_countAsc: WeaponActivityLogSort
weaponActivityLogSort_countDesc: WeaponActivityLogSort
ammoSort_unspecified: AmmoSort
ammoSort_nameAsc: AmmoSort
ammoSort_nameDesc: AmmoSort
ammoSort_countAsc: AmmoSort
ammoSort_countDesc: AmmoSort
ammoActivityLogSort_unspecified: AmmoActivityLogSort
ammoActivityLogSort_activityAtAsc: AmmoActivityLogSort
ammoActivityLogSort_activityAtDesc: AmmoActivityLogSort
ammoActivityLogSort_nameAsc: AmmoActivityLogSort
ammoActivityLogSort_nameDesc: AmmoActivityLogSort
ammoActivityLogSort_countAsc: AmmoActivityLogSort
ammoActivityLogSort_countDesc: AmmoActivityLogSort
otherItemsSort_unspecified: OtherItemsSort
otherItemsSort_nameAsc: OtherItemsSort
otherItemsSort_nameDesc: OtherItemsSort
otherItemsSort_countAsc: OtherItemsSort
otherItemsSort_countDesc: OtherItemsSort
otherItemsActivityLogSort_unspecified: OtherItemsActivityLogSort
otherItemsActivityLogSort_activityAtAsc: OtherItemsActivityLogSort
otherItemsActivityLogSort_activityAtDesc: OtherItemsActivityLogSort
otherItemsActivityLogSort_nameAsc: OtherItemsActivityLogSort
otherItemsActivityLogSort_nameDesc: OtherItemsActivityLogSort
otherItemsActivityLogSort_countAsc: OtherItemsActivityLogSort
otherItemsActivityLogSort_countDesc: OtherItemsActivityLogSort
assignmentSort_unspecified: AssignmentSort
assignmentActivityLogSort_unspecified: AssignmentActivityLogSort
assignmentActivityLogSort_activityAtAsc: AssignmentActivityLogSort
assignmentActivityLogSort_activityAtDesc: AssignmentActivityLogSort
assignmentActivityLogSort_weaponButtNoAsc: AssignmentActivityLogSort
assignmentActivityLogSort_weaponButtNoDesc: AssignmentActivityLogSort
assignmentActivityLogSort_ammoCountAsc: AssignmentActivityLogSort
assignmentActivityLogSort_ammoCountDesc: AssignmentActivityLogSort
shiftReportItemSort_unspecified: ShiftReportItemSort
shiftReportItemSort_employeeNameAsc: ShiftReportItemSort
shiftReportItemSort_employeeNameDesc: ShiftReportItemSort
scheduleSort_unspecified: ScheduleSort
scheduleSort_startTimeAsc: ScheduleSort
scheduleSort_startTimeDesc: ScheduleSort
scheduleSort_endTimeAsc: ScheduleSort
scheduleSort_endTimeDesc: ScheduleSort
scheduleActivityLogSort_unspecified: ScheduleActivityLogSort
scheduleActivityLogSort_activityAtAsc: ScheduleActivityLogSort
scheduleActivityLogSort_activityAtDesc: ScheduleActivityLogSort
scheduleActivityLogSort_startTimeAsc: ScheduleActivityLogSort
scheduleActivityLogSort_startTimeDesc: ScheduleActivityLogSort
scheduleActivityLogSort_endTimeAsc: ScheduleActivityLogSort
scheduleActivityLogSort_endTimeDesc: ScheduleActivityLogSort
weaponAmmoSort_unspecified: WeaponAmmoSort
weaponAmmoSort_countAsc: WeaponAmmoSort
weaponAmmoSort_countDesc: WeaponAmmoSort
weaponAmmoActivityLogSort_unspecified: WeaponAmmoActivityLogSort
weaponAmmoActivityLogSort_activityAtAsc: WeaponAmmoActivityLogSort
weaponAmmoActivityLogSort_activityAtDesc: WeaponAmmoActivityLogSort
weaponAmmoActivityLogSort_countAsc: WeaponAmmoActivityLogSort
weaponAmmoActivityLogSort_countDesc: WeaponAmmoActivityLogSort
globalConfigSort_unspecified: GlobalConfigSort
globalConfigSort_weaponIssueBeforeStartBufferAsc: GlobalConfigSort
globalConfigSort_weaponIssueBeforeStartBufferDesc: GlobalConfigSort
globalConfigSort_weaponIssueAfterStartBufferAsc: GlobalConfigSort
globalConfigSort_weaponIssueAfterStartBufferDesc: GlobalConfigSort
globalConfigSort_scheduleEditAfterBufferAsc: GlobalConfigSort
globalConfigSort_scheduleEditAfterBufferDesc: GlobalConfigSort
globalConfigActivityLogSort_unspecified: GlobalConfigActivityLogSort
globalConfigActivityLogSort_activityAtAsc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_activityAtDesc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_weaponIssueBeforeStartBufferAsc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_weaponIssueBeforeStartBufferDesc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_weaponIssueAfterStartBufferAsc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_weaponIssueAfterStartBufferDesc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_scheduleEditAfterBufferAsc: GlobalConfigActivityLogSort
globalConfigActivityLogSort_scheduleEditAfterBufferDesc: GlobalConfigActivityLogSort
flowAlertsSort_unspecified: FlowAlertsSort
flowAlertsSort_weaponIssueAfterShiftStartDurationAsc: FlowAlertsSort
flowAlertsSort_weaponIssueAfterShiftStartDurationDesc: FlowAlertsSort
flowAlertsSort_clearingIssueAfterWeaponEntryDurationAsc: FlowAlertsSort
flowAlertsSort_clearingIssueAfterWeaponEntryDurationDesc: FlowAlertsSort
flowAlertsSort_ammoIssueAfterClearingEntryDurationAsc: FlowAlertsSort
flowAlertsSort_ammoIssueAfterClearingEntryDurationDesc: FlowAlertsSort
flowAlertsSort_weaponNotDepositDurationAsc: FlowAlertsSort
flowAlertsSort_weaponNotDepositDurationDesc: FlowAlertsSort
flowAlertsActivityLogSort_unspecified: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_activityAtAsc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_activityAtDesc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_weaponIssueAfterShiftStartDurationAsc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_weaponIssueAfterShiftStartDurationDesc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_clearingIssueAfterWeaponEntryDurationAsc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_clearingIssueAfterWeaponEntryDurationDesc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_ammoIssueAfterClearingEntryDurationAsc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_ammoIssueAfterClearingEntryDurationDesc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_weaponNotDepositDurationAsc: FlowAlertsActivityLogSort
flowAlertsActivityLogSort_weaponNotDepositDurationDesc: FlowAlertsActivityLogSort
commonInfoSort_unspecified: CommonInfoSort
commonInfoSort_timeAsc: CommonInfoSort
commonInfoSort_timeDesc: CommonInfoSort
commonInfoSort_remarksAsc: CommonInfoSort
commonInfoSort_remarksDesc: CommonInfoSort
commonInfoActivityLogSort_unspecified: CommonInfoActivityLogSort
commonInfoActivityLogSort_activityAtAsc: CommonInfoActivityLogSort
commonInfoActivityLogSort_activityAtDesc: CommonInfoActivityLogSort
commonInfoActivityLogSort_timeAsc: CommonInfoActivityLogSort
commonInfoActivityLogSort_timeDesc: CommonInfoActivityLogSort
commonInfoActivityLogSort_remarksAsc: CommonInfoActivityLogSort
commonInfoActivityLogSort_remarksDesc: CommonInfoActivityLogSort
ammoInfoSort_unspecified: AmmoInfoSort
ammoInfoSort_timeAsc: AmmoInfoSort
ammoInfoSort_timeDesc: AmmoInfoSort
ammoInfoSort_remarksAsc: AmmoInfoSort
ammoInfoSort_remarksDesc: AmmoInfoSort
ammoInfoSort_countAsc: AmmoInfoSort
ammoInfoSort_countDesc: AmmoInfoSort
ammoInfoActivityLogSort_unspecified: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_activityAtAsc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_activityAtDesc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_timeAsc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_timeDesc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_remarksAsc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_remarksDesc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_countAsc: AmmoInfoActivityLogSort
ammoInfoActivityLogSort_countDesc: AmmoInfoActivityLogSort
flowsSort_unspecified: FlowsSort
flowsActivityLogSort_unspecified: FlowsActivityLogSort
flowsActivityLogSort_activityAtAsc: FlowsActivityLogSort
flowsActivityLogSort_activityAtDesc: FlowsActivityLogSort
Position_unspecified: Position
Position_weapon: Position
Position_clearing: Position
Position_ammo: Position
alertType_unspecified: AlertType
alertType_skipWeaponIssue: AlertType
alertType_skipClearingIssue: AlertType
alertType_skipAmmoIssue: AlertType
alertType_skipAmmoDeposit: AlertType
alertType_skipClearingDeposit: AlertType
alertType_skipWeaponDeposit: AlertType
alertType_delayedWeaponIssue: AlertType
alertType_delayedClearingIssue: AlertType
alertType_delayedAmmoIssue: AlertType
alertType_delayedAmmoDeposit: AlertType
alertType_delayedClearingDeposit: AlertType
alertType_delayedWeaponDeposit: AlertType
alertSort_unspecified: AlertSort
alertSort_timeAsc: AlertSort
alertSort_timeDesc: AlertSort
checkPoint_unspecified: CheckPoint
checkPoint_weapon: CheckPoint
checkPoint_ammo: CheckPoint
userSort_unspecified: UserSort
userSort_authNameAsc: UserSort
userSort_authNameDesc: UserSort
userSort_nameAsc: UserSort
userSort_nameDesc: UserSort
userActivityLogSort_unspecified: UserActivityLogSort
userActivityLogSort_activityAtAsc: UserActivityLogSort
userActivityLogSort_activityAtDesc: UserActivityLogSort
userActivityLogSort_authNameAsc: UserActivityLogSort
userActivityLogSort_authNameDesc: UserActivityLogSort
userActivityLogSort_nameAsc: UserActivityLogSort
userActivityLogSort_nameDesc: UserActivityLogSort
weaponInfoSort_unspecified: WeaponInfoSort
weaponInfoSort_timeAsc: WeaponInfoSort
weaponInfoSort_timeDesc: WeaponInfoSort
weaponInfoSort_remarksAsc: WeaponInfoSort
weaponInfoSort_remarksDesc: WeaponInfoSort
weaponInfoSort_issuedButtNoAsc: WeaponInfoSort
weaponInfoSort_issuedButtNoDesc: WeaponInfoSort
weaponInfoActivityLogSort_unspecified: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_activityAtAsc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_activityAtDesc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_timeAsc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_timeDesc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_remarksAsc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_remarksDesc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_issuedButtNoAsc: WeaponInfoActivityLogSort
weaponInfoActivityLogSort_issuedButtNoDesc: WeaponInfoActivityLogSort
perm_unspecified: Perm
perm_createP: Perm
perm_readP: Perm
perm_updateP: Perm
perm_deleteP: Perm
perm_accessP: Perm
scopes_unspecified: Scopes
scopes_employee: Scopes
scopes_dutyPost: Scopes
scopes_weapon: Scopes
scopes_ammo: Scopes
scopes_otherItems: Scopes
scopes_assignment: Scopes
scopes_schedule: Scopes
scopes_weaponAmmo: Scopes
scopes_globalConfig: Scopes
scopes_flowAlerts: Scopes
scopes_commonInfo: Scopes
scopes_ammoInfo: Scopes
scopes_flows: Scopes
scopes_alert: Scopes
scopes_user: Scopes
scopes_weaponInfo: Scopes
scopes_tags: Scopes
accessControlSort_unspecified: AccessControlSort
accessControlActivityLogSort_unspecified: AccessControlActivityLogSort
accessControlActivityLogSort_activityAtAsc: AccessControlActivityLogSort
accessControlActivityLogSort_activityAtDesc: AccessControlActivityLogSort

class EmployeeCreateRequest(_message.Message):
    __slots__ = ("biometricsId", "cisfId", "name", "rank", "photo")
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    biometricsId: str
    cisfId: str
    name: str
    rank: str
    photo: EmployeeCreateRequestPhoto
    def __init__(self, biometricsId: _Optional[str] = ..., cisfId: _Optional[str] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class EmployeeReadResponse(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: str
    cisfId: str
    name: str
    rank: str
    photo: EmployeeReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[str] = ..., cisfId: _Optional[str] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeReadResponsePhoto, _Mapping]] = ...) -> None: ...

class EmployeeUpdateRequest(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: str
    cisfId: str
    name: str
    rank: str
    photo: EmployeeUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[str] = ..., cisfId: _Optional[str] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

class EmployeeListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: EmployeeFilters
    search: str
    sort: EmployeeSort
    cursor: EmployeeCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[EmployeeFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[EmployeeSort, str]] = ..., cursor: _Optional[_Union[EmployeeCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class EmployeeListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Employee]
    cursor: EmployeeCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Employee, _Mapping]]] = ..., cursor: _Optional[_Union[EmployeeCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class EmployeeActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: EmployeeActivityLogFilters
    search: str
    sort: EmployeeActivityLogSort
    cursor: EmployeeActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[EmployeeActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[EmployeeActivityLogSort, str]] = ..., cursor: _Optional[_Union[EmployeeActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class EmployeeActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EmployeeActivityLog]
    cursor: EmployeeActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[EmployeeActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[EmployeeActivityLogCursor, _Mapping]] = ...) -> None: ...

class DutyPostCreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DutyPostReadResponse(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DutyPostUpdateRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DutyPostListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: DutyPostFilters
    search: str
    sort: DutyPostSort
    cursor: DutyPostCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[DutyPostFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[DutyPostSort, str]] = ..., cursor: _Optional[_Union[DutyPostCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class DutyPostListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DutyPost]
    cursor: DutyPostCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[DutyPost, _Mapping]]] = ..., cursor: _Optional[_Union[DutyPostCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class DutyPostActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: DutyPostActivityLogFilters
    search: str
    sort: DutyPostActivityLogSort
    cursor: DutyPostActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[DutyPostActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[DutyPostActivityLogSort, str]] = ..., cursor: _Optional[_Union[DutyPostActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class DutyPostActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DutyPostActivityLog]
    cursor: DutyPostActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[DutyPostActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[DutyPostActivityLogCursor, _Mapping]] = ...) -> None: ...

class WeaponCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo", "weaponAmmo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: WeaponCreateRequestPhoto
    weaponAmmo: WeaponCreateRequestWeaponAmmo
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponCreateRequestPhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponCreateRequestWeaponAmmo, _Mapping]] = ...) -> None: ...

class WeaponReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "weaponAmmo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: WeaponReadResponsePhoto
    weaponAmmo: WeaponReadResponseWeaponAmmo
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponReadResponsePhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponReadResponseWeaponAmmo, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class WeaponUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "weaponAmmo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: WeaponUpdateRequestPhoto
    weaponAmmo: WeaponUpdateRequestWeaponAmmo
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponUpdateRequestPhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponUpdateRequestWeaponAmmo, _Mapping]] = ...) -> None: ...

class WeaponListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponFilters
    search: str
    sort: WeaponSort
    cursor: WeaponCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponSort, str]] = ..., cursor: _Optional[_Union[WeaponCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Weapon]
    cursor: WeaponCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Weapon, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponActivityLogFilters
    search: str
    sort: WeaponActivityLogSort
    cursor: WeaponActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponActivityLogSort, str]] = ..., cursor: _Optional[_Union[WeaponActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WeaponActivityLog]
    cursor: WeaponActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[WeaponActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponActivityLogCursor, _Mapping]] = ...) -> None: ...

class AmmoCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: AmmoCreateRequestPhoto
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[AmmoCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class AmmoReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: AmmoReadResponsePhoto
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[AmmoReadResponsePhoto, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class AmmoUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: AmmoUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[AmmoUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

class AmmoListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AmmoFilters
    search: str
    sort: AmmoSort
    cursor: AmmoCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AmmoFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AmmoSort, str]] = ..., cursor: _Optional[_Union[AmmoCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AmmoListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Ammo]
    cursor: AmmoCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Ammo, _Mapping]]] = ..., cursor: _Optional[_Union[AmmoCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AmmoActivityLogFilters
    search: str
    sort: AmmoActivityLogSort
    cursor: AmmoActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AmmoActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AmmoActivityLogSort, str]] = ..., cursor: _Optional[_Union[AmmoActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AmmoActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AmmoActivityLog]
    cursor: AmmoActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AmmoActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[AmmoActivityLogCursor, _Mapping]] = ...) -> None: ...

class OtherItemsCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: OtherItemsCreateRequestPhoto
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[OtherItemsCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class OtherItemsReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: OtherItemsReadResponsePhoto
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[OtherItemsReadResponsePhoto, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class OtherItemsUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: OtherItemsUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[OtherItemsUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

class OtherItemsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: OtherItemsFilters
    search: str
    sort: OtherItemsSort
    cursor: OtherItemsCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[OtherItemsFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[OtherItemsSort, str]] = ..., cursor: _Optional[_Union[OtherItemsCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class OtherItemsListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OtherItems]
    cursor: OtherItemsCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[OtherItems, _Mapping]]] = ..., cursor: _Optional[_Union[OtherItemsCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class OtherItemsActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: OtherItemsActivityLogFilters
    search: str
    sort: OtherItemsActivityLogSort
    cursor: OtherItemsActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[OtherItemsActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[OtherItemsActivityLogSort, str]] = ..., cursor: _Optional[_Union[OtherItemsActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class OtherItemsActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OtherItemsActivityLog]
    cursor: OtherItemsActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[OtherItemsActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[OtherItemsActivityLogCursor, _Mapping]] = ...) -> None: ...

class AssignmentCreateRequest(_message.Message):
    __slots__ = ("employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    employee: AssignmentCreateRequestEmployee
    dutyPost: AssignmentCreateRequestDutyPost
    weapon: AssignmentCreateRequestWeapon
    weaponButtNo: str
    ammo: AssignmentCreateRequestAmmo
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[AssignmentCreateRequestOtherItems]
    def __init__(self, employee: _Optional[_Union[AssignmentCreateRequestEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[AssignmentCreateRequestDutyPost, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentCreateRequestWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[AssignmentCreateRequestAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[AssignmentCreateRequestOtherItems, _Mapping]]] = ...) -> None: ...

class AssignmentReadResponse(_message.Message):
    __slots__ = ("id", "employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentReadResponseEmployee
    dutyPost: AssignmentReadResponseDutyPost
    weapon: AssignmentReadResponseWeapon
    weaponButtNo: str
    ammo: AssignmentReadResponseAmmo
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[AssignmentReadResponseOtherItems]
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentReadResponseEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[AssignmentReadResponseDutyPost, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentReadResponseWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[AssignmentReadResponseAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[AssignmentReadResponseOtherItems, _Mapping]]] = ...) -> None: ...

class AssignmentUpdateRequest(_message.Message):
    __slots__ = ("id", "employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentUpdateRequestEmployee
    dutyPost: AssignmentUpdateRequestDutyPost
    weapon: AssignmentUpdateRequestWeapon
    weaponButtNo: str
    ammo: AssignmentUpdateRequestAmmo
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[AssignmentUpdateRequestOtherItems]
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentUpdateRequestEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[AssignmentUpdateRequestDutyPost, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentUpdateRequestWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[AssignmentUpdateRequestAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[AssignmentUpdateRequestOtherItems, _Mapping]]] = ...) -> None: ...

class AssignmentListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AssignmentFilters
    search: str
    sort: AssignmentSort
    cursor: AssignmentCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AssignmentFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AssignmentSort, str]] = ..., cursor: _Optional[_Union[AssignmentCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AssignmentListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Assignment]
    cursor: AssignmentCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Assignment, _Mapping]]] = ..., cursor: _Optional[_Union[AssignmentCursor, _Mapping]] = ...) -> None: ...

class AssignmentActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AssignmentActivityLogFilters
    search: str
    sort: AssignmentActivityLogSort
    cursor: AssignmentActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AssignmentActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AssignmentActivityLogSort, str]] = ..., cursor: _Optional[_Union[AssignmentActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AssignmentActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssignmentActivityLog]
    cursor: AssignmentActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AssignmentActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[AssignmentActivityLogCursor, _Mapping]] = ...) -> None: ...

class ScheduleAssignmentsAddRequest(_message.Message):
    __slots__ = ("id", "assignments")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    assignments: AssignmentCreateRequest
    def __init__(self, id: _Optional[str] = ..., assignments: _Optional[_Union[AssignmentCreateRequest, _Mapping]] = ...) -> None: ...

class ScheduleAssignmentsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit", "parentId")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    filters: AssignmentFilters
    search: str
    sort: AssignmentSort
    cursor: AssignmentCursor
    limit: int
    parentId: str
    def __init__(self, filters: _Optional[_Union[AssignmentFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AssignmentSort, str]] = ..., cursor: _Optional[_Union[AssignmentCursor, _Mapping]] = ..., limit: _Optional[int] = ..., parentId: _Optional[str] = ...) -> None: ...

class ScheduleAssignmentsListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Assignment]
    cursor: AssignmentCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Assignment, _Mapping]]] = ..., cursor: _Optional[_Union[AssignmentCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class ShiftReportItemListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit", "parentId")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    filters: ShiftReportItemFilters
    search: str
    sort: ShiftReportItemSort
    cursor: ShiftReportItemCursor
    limit: int
    parentId: str
    def __init__(self, filters: _Optional[_Union[ShiftReportItemFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ShiftReportItemSort, str]] = ..., cursor: _Optional[_Union[ShiftReportItemCursor, _Mapping]] = ..., limit: _Optional[int] = ..., parentId: _Optional[str] = ...) -> None: ...

class ShiftReportItemListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ShiftReportItem]
    cursor: ShiftReportItemCursor
    def __init__(self, items: _Optional[_Iterable[_Union[ShiftReportItem, _Mapping]]] = ..., cursor: _Optional[_Union[ShiftReportItemCursor, _Mapping]] = ...) -> None: ...

class ScheduleCreateRequest(_message.Message):
    __slots__ = ("startTime", "endTime", "shiftIncharge", "koteNco", "armsIssueDepositSupervisor", "armsInspectionSupervisor", "clearingSupervisor")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGE_FIELD_NUMBER: _ClassVar[int]
    KOTENCO_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    shiftIncharge: ScheduleCreateRequestShiftIncharge
    koteNco: ScheduleCreateRequestKoteNco
    armsIssueDepositSupervisor: ScheduleCreateRequestArmsIssueDepositSupervisor
    armsInspectionSupervisor: ScheduleCreateRequestArmsInspectionSupervisor
    clearingSupervisor: ScheduleCreateRequestClearingSupervisor
    def __init__(self, startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[_Union[ScheduleCreateRequestShiftIncharge, _Mapping]] = ..., koteNco: _Optional[_Union[ScheduleCreateRequestKoteNco, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[ScheduleCreateRequestArmsIssueDepositSupervisor, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[ScheduleCreateRequestArmsInspectionSupervisor, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[ScheduleCreateRequestClearingSupervisor, _Mapping]] = ...) -> None: ...

class ScheduleReadResponse(_message.Message):
    __slots__ = ("id", "startTime", "endTime", "employeesCount", "shiftIncharge", "koteNco", "armsIssueDepositSupervisor", "armsInspectionSupervisor", "clearingSupervisor", "assignments")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEESCOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGE_FIELD_NUMBER: _ClassVar[int]
    KOTENCO_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    employeesCount: int
    shiftIncharge: ScheduleReadResponseShiftIncharge
    koteNco: ScheduleReadResponseKoteNco
    armsIssueDepositSupervisor: ScheduleReadResponseArmsIssueDepositSupervisor
    armsInspectionSupervisor: ScheduleReadResponseArmsInspectionSupervisor
    clearingSupervisor: ScheduleReadResponseClearingSupervisor
    assignments: _containers.RepeatedCompositeFieldContainer[ScheduleReadResponseAssignments]
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., employeesCount: _Optional[int] = ..., shiftIncharge: _Optional[_Union[ScheduleReadResponseShiftIncharge, _Mapping]] = ..., koteNco: _Optional[_Union[ScheduleReadResponseKoteNco, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[ScheduleReadResponseArmsIssueDepositSupervisor, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[ScheduleReadResponseArmsInspectionSupervisor, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[ScheduleReadResponseClearingSupervisor, _Mapping]] = ..., assignments: _Optional[_Iterable[_Union[ScheduleReadResponseAssignments, _Mapping]]] = ...) -> None: ...

class ScheduleUpdateRequest(_message.Message):
    __slots__ = ("id", "startTime", "endTime", "shiftIncharge", "koteNco", "armsIssueDepositSupervisor", "armsInspectionSupervisor", "clearingSupervisor")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGE_FIELD_NUMBER: _ClassVar[int]
    KOTENCO_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    shiftIncharge: ScheduleUpdateRequestShiftIncharge
    koteNco: ScheduleUpdateRequestKoteNco
    armsIssueDepositSupervisor: ScheduleUpdateRequestArmsIssueDepositSupervisor
    armsInspectionSupervisor: ScheduleUpdateRequestArmsInspectionSupervisor
    clearingSupervisor: ScheduleUpdateRequestClearingSupervisor
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[_Union[ScheduleUpdateRequestShiftIncharge, _Mapping]] = ..., koteNco: _Optional[_Union[ScheduleUpdateRequestKoteNco, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[ScheduleUpdateRequestArmsIssueDepositSupervisor, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[ScheduleUpdateRequestArmsInspectionSupervisor, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[ScheduleUpdateRequestClearingSupervisor, _Mapping]] = ...) -> None: ...

class ScheduleListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: ScheduleFilters
    search: str
    sort: ScheduleSort
    cursor: ScheduleCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[ScheduleFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ScheduleSort, str]] = ..., cursor: _Optional[_Union[ScheduleCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class ScheduleListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Schedule]
    cursor: ScheduleCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Schedule, _Mapping]]] = ..., cursor: _Optional[_Union[ScheduleCursor, _Mapping]] = ...) -> None: ...

class ScheduleActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: ScheduleActivityLogFilters
    search: str
    sort: ScheduleActivityLogSort
    cursor: ScheduleActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[ScheduleActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ScheduleActivityLogSort, str]] = ..., cursor: _Optional[_Union[ScheduleActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class ScheduleActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScheduleActivityLog]
    cursor: ScheduleActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[ScheduleActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[ScheduleActivityLogCursor, _Mapping]] = ...) -> None: ...

class WeaponAmmoCreateRequest(_message.Message):
    __slots__ = ("ammo", "count")
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ammo: WeaponAmmoCreateRequestAmmo
    count: int
    def __init__(self, ammo: _Optional[_Union[WeaponAmmoCreateRequestAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponAmmoReadResponse(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponAmmoReadResponseAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponAmmoReadResponseAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponAmmoUpdateRequest(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponAmmoUpdateRequestAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponAmmoUpdateRequestAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponAmmoListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponAmmoFilters
    search: str
    sort: WeaponAmmoSort
    cursor: WeaponAmmoCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponAmmoFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponAmmoSort, str]] = ..., cursor: _Optional[_Union[WeaponAmmoCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponAmmoListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WeaponAmmo]
    cursor: WeaponAmmoCursor
    def __init__(self, items: _Optional[_Iterable[_Union[WeaponAmmo, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponAmmoCursor, _Mapping]] = ...) -> None: ...

class WeaponAmmoActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponAmmoActivityLogFilters
    search: str
    sort: WeaponAmmoActivityLogSort
    cursor: WeaponAmmoActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponAmmoActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponAmmoActivityLogSort, str]] = ..., cursor: _Optional[_Union[WeaponAmmoActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponAmmoActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WeaponAmmoActivityLog]
    cursor: WeaponAmmoActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[WeaponAmmoActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponAmmoActivityLogCursor, _Mapping]] = ...) -> None: ...

class GlobalConfigCreateRequest(_message.Message):
    __slots__ = ("weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer", "flowAlerts")
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTS_FIELD_NUMBER: _ClassVar[int]
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    flowAlerts: GlobalConfigCreateRequestFlowAlerts
    def __init__(self, weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[GlobalConfigCreateRequestFlowAlerts, _Mapping]] = ...) -> None: ...

class GlobalConfigReadResponse(_message.Message):
    __slots__ = ("id", "weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer", "flowAlerts")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    flowAlerts: GlobalConfigReadResponseFlowAlerts
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[GlobalConfigReadResponseFlowAlerts, _Mapping]] = ...) -> None: ...

class GlobalConfigUpdateRequest(_message.Message):
    __slots__ = ("id", "weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer", "flowAlerts")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    flowAlerts: GlobalConfigUpdateRequestFlowAlerts
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[GlobalConfigUpdateRequestFlowAlerts, _Mapping]] = ...) -> None: ...

class GlobalConfigListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: GlobalConfigFilters
    search: str
    sort: GlobalConfigSort
    cursor: GlobalConfigCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[GlobalConfigFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[GlobalConfigSort, str]] = ..., cursor: _Optional[_Union[GlobalConfigCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class GlobalConfigListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GlobalConfig]
    cursor: GlobalConfigCursor
    def __init__(self, items: _Optional[_Iterable[_Union[GlobalConfig, _Mapping]]] = ..., cursor: _Optional[_Union[GlobalConfigCursor, _Mapping]] = ...) -> None: ...

class GlobalConfigActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: GlobalConfigActivityLogFilters
    search: str
    sort: GlobalConfigActivityLogSort
    cursor: GlobalConfigActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[GlobalConfigActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[GlobalConfigActivityLogSort, str]] = ..., cursor: _Optional[_Union[GlobalConfigActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class GlobalConfigActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GlobalConfigActivityLog]
    cursor: GlobalConfigActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[GlobalConfigActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[GlobalConfigActivityLogCursor, _Mapping]] = ...) -> None: ...

class FlowAlertsCreateRequest(_message.Message):
    __slots__ = ("weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class FlowAlertsReadResponse(_message.Message):
    __slots__ = ("id", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class FlowAlertsUpdateRequest(_message.Message):
    __slots__ = ("id", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class FlowAlertsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FlowAlertsFilters
    search: str
    sort: FlowAlertsSort
    cursor: FlowAlertsCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FlowAlertsFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FlowAlertsSort, str]] = ..., cursor: _Optional[_Union[FlowAlertsCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FlowAlertsListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FlowAlerts]
    cursor: FlowAlertsCursor
    def __init__(self, items: _Optional[_Iterable[_Union[FlowAlerts, _Mapping]]] = ..., cursor: _Optional[_Union[FlowAlertsCursor, _Mapping]] = ...) -> None: ...

class FlowAlertsActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FlowAlertsActivityLogFilters
    search: str
    sort: FlowAlertsActivityLogSort
    cursor: FlowAlertsActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FlowAlertsActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FlowAlertsActivityLogSort, str]] = ..., cursor: _Optional[_Union[FlowAlertsActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FlowAlertsActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FlowAlertsActivityLog]
    cursor: FlowAlertsActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[FlowAlertsActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[FlowAlertsActivityLogCursor, _Mapping]] = ...) -> None: ...

class CommonInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class CommonInfoReadResponse(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: CommonInfoReadResponseAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[CommonInfoReadResponseAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class CommonInfoUpdateRequest(_message.Message):
    __slots__ = ("id", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class CommonInfoListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: CommonInfoFilters
    search: str
    sort: CommonInfoSort
    cursor: CommonInfoCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[CommonInfoFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[CommonInfoSort, str]] = ..., cursor: _Optional[_Union[CommonInfoCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class CommonInfoListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CommonInfo]
    cursor: CommonInfoCursor
    def __init__(self, items: _Optional[_Iterable[_Union[CommonInfo, _Mapping]]] = ..., cursor: _Optional[_Union[CommonInfoCursor, _Mapping]] = ...) -> None: ...

class CommonInfoActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: CommonInfoActivityLogFilters
    search: str
    sort: CommonInfoActivityLogSort
    cursor: CommonInfoActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[CommonInfoActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[CommonInfoActivityLogSort, str]] = ..., cursor: _Optional[_Union[CommonInfoActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class CommonInfoActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CommonInfoActivityLog]
    cursor: CommonInfoActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[CommonInfoActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[CommonInfoActivityLogCursor, _Mapping]] = ...) -> None: ...

class AmmoInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoInfoReadResponse(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: AmmoInfoReadResponseAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[AmmoInfoReadResponseAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoInfoUpdateRequest(_message.Message):
    __slots__ = ("id", "time", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoInfoListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AmmoInfoFilters
    search: str
    sort: AmmoInfoSort
    cursor: AmmoInfoCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AmmoInfoFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AmmoInfoSort, str]] = ..., cursor: _Optional[_Union[AmmoInfoCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AmmoInfoListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AmmoInfo]
    cursor: AmmoInfoCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AmmoInfo, _Mapping]]] = ..., cursor: _Optional[_Union[AmmoInfoCursor, _Mapping]] = ...) -> None: ...

class AmmoInfoActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AmmoInfoActivityLogFilters
    search: str
    sort: AmmoInfoActivityLogSort
    cursor: AmmoInfoActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AmmoInfoActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AmmoInfoActivityLogSort, str]] = ..., cursor: _Optional[_Union[AmmoInfoActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AmmoInfoActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AmmoInfoActivityLog]
    cursor: AmmoInfoActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AmmoInfoActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[AmmoInfoActivityLogCursor, _Mapping]] = ...) -> None: ...

class FlowsCreateRequest(_message.Message):
    __slots__ = ("assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit")
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    assignment: FlowsCreateRequestAssignment
    weaponEntry: FlowsCreateRequestWeaponEntry
    clearingEntry: FlowsCreateRequestClearingEntry
    ammoEntry: FlowsCreateRequestAmmoEntry
    ammoExit: FlowsCreateRequestAmmoExit
    clearingExit: FlowsCreateRequestClearingExit
    weaponExit: FlowsCreateRequestWeaponExit
    def __init__(self, assignment: _Optional[_Union[FlowsCreateRequestAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsCreateRequestWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsCreateRequestClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsCreateRequestAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsCreateRequestAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsCreateRequestClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsCreateRequestWeaponExit, _Mapping]] = ...) -> None: ...

class FlowsReadResponse(_message.Message):
    __slots__ = ("id", "assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit", "isActive")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    ISACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    assignment: FlowsReadResponseAssignment
    weaponEntry: FlowsReadResponseWeaponEntry
    clearingEntry: FlowsReadResponseClearingEntry
    ammoEntry: FlowsReadResponseAmmoEntry
    ammoExit: FlowsReadResponseAmmoExit
    clearingExit: FlowsReadResponseClearingExit
    weaponExit: FlowsReadResponseWeaponExit
    isActive: bool
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsReadResponseAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsReadResponseWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsReadResponseClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsReadResponseAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsReadResponseAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsReadResponseClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsReadResponseWeaponExit, _Mapping]] = ..., isActive: bool = ...) -> None: ...

class FlowsUpdateRequest(_message.Message):
    __slots__ = ("id", "assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    assignment: FlowsUpdateRequestAssignment
    weaponEntry: FlowsUpdateRequestWeaponEntry
    clearingEntry: FlowsUpdateRequestClearingEntry
    ammoEntry: FlowsUpdateRequestAmmoEntry
    ammoExit: FlowsUpdateRequestAmmoExit
    clearingExit: FlowsUpdateRequestClearingExit
    weaponExit: FlowsUpdateRequestWeaponExit
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsUpdateRequestAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsUpdateRequestWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsUpdateRequestClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsUpdateRequestAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsUpdateRequestAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsUpdateRequestClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsUpdateRequestWeaponExit, _Mapping]] = ...) -> None: ...

class FlowsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FlowsFilters
    search: str
    sort: FlowsSort
    cursor: FlowsCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FlowsFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FlowsSort, str]] = ..., cursor: _Optional[_Union[FlowsCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FlowsListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Flows]
    cursor: FlowsCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Flows, _Mapping]]] = ..., cursor: _Optional[_Union[FlowsCursor, _Mapping]] = ...) -> None: ...

class FlowsActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FlowsActivityLogFilters
    search: str
    sort: FlowsActivityLogSort
    cursor: FlowsActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FlowsActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FlowsActivityLogSort, str]] = ..., cursor: _Optional[_Union[FlowsActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FlowsActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FlowsActivityLog]
    cursor: FlowsActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[FlowsActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[FlowsActivityLogCursor, _Mapping]] = ...) -> None: ...

class FlowsOnScanRequest(_message.Message):
    __slots__ = ("biometricsId", "position")
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    biometricsId: str
    position: Position
    def __init__(self, biometricsId: _Optional[str] = ..., position: _Optional[_Union[Position, str]] = ...) -> None: ...

class FlowsOnScanResponse(_message.Message):
    __slots__ = ("position", "red", "green", "buzzer")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BUZZER_FIELD_NUMBER: _ClassVar[int]
    position: Position
    red: bool
    green: bool
    buzzer: bool
    def __init__(self, position: _Optional[_Union[Position, str]] = ..., red: bool = ..., green: bool = ..., buzzer: bool = ...) -> None: ...

class AlertCreateRequest(_message.Message):
    __slots__ = ("employee", "alertType", "time", "remarks")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    employee: AlertCreateRequestEmployee
    alertType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, employee: _Optional[_Union[AlertCreateRequestEmployee, _Mapping]] = ..., alertType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertReadResponse(_message.Message):
    __slots__ = ("id", "employee", "alertType", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AlertReadResponseEmployee
    alertType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertReadResponseEmployee, _Mapping]] = ..., alertType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AlertFilters
    search: str
    sort: AlertSort
    cursor: AlertCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AlertFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AlertSort, str]] = ..., cursor: _Optional[_Union[AlertCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AlertListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Alert]
    cursor: AlertCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Alert, _Mapping]]] = ..., cursor: _Optional[_Union[AlertCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class UserCreateRequest(_message.Message):
    __slots__ = ("authName", "password", "name", "popUpFor", "popUpDuration")
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPUPFOR_FIELD_NUMBER: _ClassVar[int]
    POPUPDURATION_FIELD_NUMBER: _ClassVar[int]
    authName: str
    password: str
    name: str
    popUpFor: _containers.RepeatedScalarFieldContainer[CheckPoint]
    popUpDuration: int
    def __init__(self, authName: _Optional[str] = ..., password: _Optional[str] = ..., name: _Optional[str] = ..., popUpFor: _Optional[_Iterable[_Union[CheckPoint, str]]] = ..., popUpDuration: _Optional[int] = ...) -> None: ...

class UserReadResponse(_message.Message):
    __slots__ = ("id", "authName", "name", "popUpFor", "popUpDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPUPFOR_FIELD_NUMBER: _ClassVar[int]
    POPUPDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    name: str
    popUpFor: _containers.RepeatedScalarFieldContainer[CheckPoint]
    popUpDuration: int
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ..., name: _Optional[str] = ..., popUpFor: _Optional[_Iterable[_Union[CheckPoint, str]]] = ..., popUpDuration: _Optional[int] = ...) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ("id", "authName", "name", "popUpFor", "popUpDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPUPFOR_FIELD_NUMBER: _ClassVar[int]
    POPUPDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    name: str
    popUpFor: _containers.RepeatedScalarFieldContainer[CheckPoint]
    popUpDuration: int
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ..., name: _Optional[str] = ..., popUpFor: _Optional[_Iterable[_Union[CheckPoint, str]]] = ..., popUpDuration: _Optional[int] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: UserFilters
    search: str
    sort: UserSort
    cursor: UserCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[UserFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[UserSort, str]] = ..., cursor: _Optional[_Union[UserCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[User]
    cursor: UserCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., cursor: _Optional[_Union[UserCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class UserActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: UserActivityLogFilters
    search: str
    sort: UserActivityLogSort
    cursor: UserActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[UserActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[UserActivityLogSort, str]] = ..., cursor: _Optional[_Union[UserActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class UserActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UserActivityLog]
    cursor: UserActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[UserActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[UserActivityLogCursor, _Mapping]] = ...) -> None: ...

class WeaponInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks", "issuedButtNo")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class WeaponInfoReadResponse(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: WeaponInfoReadResponseAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[WeaponInfoReadResponseAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class WeaponInfoUpdateRequest(_message.Message):
    __slots__ = ("id", "time", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class WeaponInfoListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponInfoFilters
    search: str
    sort: WeaponInfoSort
    cursor: WeaponInfoCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponInfoFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponInfoSort, str]] = ..., cursor: _Optional[_Union[WeaponInfoCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponInfoListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WeaponInfo]
    cursor: WeaponInfoCursor
    def __init__(self, items: _Optional[_Iterable[_Union[WeaponInfo, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponInfoCursor, _Mapping]] = ...) -> None: ...

class WeaponInfoActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: WeaponInfoActivityLogFilters
    search: str
    sort: WeaponInfoActivityLogSort
    cursor: WeaponInfoActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[WeaponInfoActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[WeaponInfoActivityLogSort, str]] = ..., cursor: _Optional[_Union[WeaponInfoActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class WeaponInfoActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WeaponInfoActivityLog]
    cursor: WeaponInfoActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[WeaponInfoActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponInfoActivityLogCursor, _Mapping]] = ...) -> None: ...

class AccessControlCreateRequest(_message.Message):
    __slots__ = ("auth", "perms", "tags", "scopes")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    auth: AccessControlCreateRequestAuth
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    tags: _containers.RepeatedCompositeFieldContainer[AccessControlCreateRequestTags]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, auth: _Optional[_Union[AccessControlCreateRequestAuth, _Mapping]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., tags: _Optional[_Iterable[_Union[AccessControlCreateRequestTags, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlReadResponse(_message.Message):
    __slots__ = ("id", "auth", "perms", "tags", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    auth: AccessControlReadResponseAuth
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    tags: _containers.RepeatedCompositeFieldContainer[AccessControlReadResponseTags]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, id: _Optional[str] = ..., auth: _Optional[_Union[AccessControlReadResponseAuth, _Mapping]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., tags: _Optional[_Iterable[_Union[AccessControlReadResponseTags, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlUpdateRequest(_message.Message):
    __slots__ = ("id", "auth", "perms", "tags", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    auth: AccessControlUpdateRequestAuth
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    tags: _containers.RepeatedCompositeFieldContainer[AccessControlUpdateRequestTags]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, id: _Optional[str] = ..., auth: _Optional[_Union[AccessControlUpdateRequestAuth, _Mapping]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., tags: _Optional[_Iterable[_Union[AccessControlUpdateRequestTags, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AccessControlFilters
    search: str
    sort: AccessControlSort
    cursor: AccessControlCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AccessControlFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AccessControlSort, str]] = ..., cursor: _Optional[_Union[AccessControlCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AccessControlListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccessControl]
    cursor: AccessControlCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[AccessControl, _Mapping]]] = ..., cursor: _Optional[_Union[AccessControlCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class AccessControlActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AccessControlActivityLogFilters
    search: str
    sort: AccessControlActivityLogSort
    cursor: AccessControlActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AccessControlActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AccessControlActivityLogSort, str]] = ..., cursor: _Optional[_Union[AccessControlActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AccessControlActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccessControlActivityLog]
    cursor: AccessControlActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AccessControlActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[AccessControlActivityLogCursor, _Mapping]] = ...) -> None: ...

class EmployeeCreateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmployeeReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class EmployeeUpdateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmployeeFilters(_message.Message):
    __slots__ = ("idIn", "biometricsIdMin", "biometricsIdMax", "cisfIdMin", "cisfIdMax", "nameMin", "nameMax", "rankMin", "rankMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMIN_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMAX_FIELD_NUMBER: _ClassVar[int]
    CISFIDMIN_FIELD_NUMBER: _ClassVar[int]
    CISFIDMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    RANKMIN_FIELD_NUMBER: _ClassVar[int]
    RANKMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    biometricsIdMin: str
    biometricsIdMax: str
    cisfIdMin: str
    cisfIdMax: str
    nameMin: str
    nameMax: str
    rankMin: str
    rankMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., biometricsIdMin: _Optional[str] = ..., biometricsIdMax: _Optional[str] = ..., cisfIdMin: _Optional[str] = ..., cisfIdMax: _Optional[str] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., rankMin: _Optional[str] = ..., rankMax: _Optional[str] = ...) -> None: ...

class EmployeeCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: EmployeeFilters
    sort: EmployeeSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[EmployeeFilters, _Mapping]] = ..., sort: _Optional[_Union[EmployeeSort, str]] = ...) -> None: ...

class Employee(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: str
    cisfId: str
    name: str
    rank: str
    photo: EmployeePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[str] = ..., cisfId: _Optional[str] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeePhoto, _Mapping]] = ...) -> None: ...

class EmployeeActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "biometricsIdMin", "biometricsIdMax", "cisfIdMin", "cisfIdMax", "nameMin", "nameMax", "rankMin", "rankMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMIN_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMAX_FIELD_NUMBER: _ClassVar[int]
    CISFIDMIN_FIELD_NUMBER: _ClassVar[int]
    CISFIDMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    RANKMIN_FIELD_NUMBER: _ClassVar[int]
    RANKMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    biometricsIdMin: str
    biometricsIdMax: str
    cisfIdMin: str
    cisfIdMax: str
    nameMin: str
    nameMax: str
    rankMin: str
    rankMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., biometricsIdMin: _Optional[str] = ..., biometricsIdMax: _Optional[str] = ..., cisfIdMin: _Optional[str] = ..., cisfIdMax: _Optional[str] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., rankMin: _Optional[str] = ..., rankMax: _Optional[str] = ...) -> None: ...

class EmployeeActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: EmployeeActivityLogFilters
    sort: EmployeeActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[EmployeeActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[EmployeeActivityLogSort, str]] = ...) -> None: ...

class EmployeeActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    biometricsId: str
    cisfId: str
    name: str
    rank: str
    photo: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., biometricsId: _Optional[str] = ..., cisfId: _Optional[str] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[str] = ...) -> None: ...

class DutyPostFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class DutyPostCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: DutyPostFilters
    sort: DutyPostSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[DutyPostFilters, _Mapping]] = ..., sort: _Optional[_Union[DutyPostSort, str]] = ...) -> None: ...

class DutyPost(_message.Message):
    __slots__ = ("id", "name", "currentDutyOfficer")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENTDUTYOFFICER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    currentDutyOfficer: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., currentDutyOfficer: _Optional[str] = ...) -> None: ...

class DutyPostActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class DutyPostActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: DutyPostActivityLogFilters
    sort: DutyPostActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[DutyPostActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[DutyPostActivityLogSort, str]] = ...) -> None: ...

class DutyPostActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponCreateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponCreateRequestWeaponAmmo(_message.Message):
    __slots__ = ("ammo", "count")
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ammo: WeaponCreateRequestWeaponAmmoAmmo
    count: int
    def __init__(self, ammo: _Optional[_Union[WeaponCreateRequestWeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponReadResponseWeaponAmmo(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponReadResponseWeaponAmmoAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponReadResponseWeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponUpdateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponUpdateRequestWeaponAmmo(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponUpdateRequestWeaponAmmoAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponUpdateRequestWeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class WeaponCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponFilters
    sort: WeaponSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponSort, str]] = ...) -> None: ...

class Weapon(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "weaponAmmo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: WeaponPhoto
    weaponAmmo: WeaponWeaponAmmo
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponPhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponWeaponAmmo, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class WeaponActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "nameMin", "nameMax", "countMin", "countMax", "weaponAmmoIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMOIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    weaponAmmoIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ..., weaponAmmoIn: _Optional[_Iterable[str]] = ...) -> None: ...

class WeaponActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponActivityLogFilters
    sort: WeaponActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponActivityLogSort, str]] = ...) -> None: ...

class WeaponActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name", "count", "photo", "weaponAmmo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    count: int
    photo: str
    weaponAmmo: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[str] = ..., weaponAmmo: _Optional[str] = ...) -> None: ...

class AmmoCreateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AmmoReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoUpdateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AmmoFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class AmmoCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AmmoFilters
    sort: AmmoSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AmmoFilters, _Mapping]] = ..., sort: _Optional[_Union[AmmoSort, str]] = ...) -> None: ...

class Ammo(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: AmmoPhoto
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[AmmoPhoto, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class AmmoActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "nameMin", "nameMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class AmmoActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AmmoActivityLogFilters
    sort: AmmoActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AmmoActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[AmmoActivityLogSort, str]] = ...) -> None: ...

class AmmoActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    count: int
    photo: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[str] = ...) -> None: ...

class OtherItemsCreateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class OtherItemsReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OtherItemsUpdateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class OtherItemsFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class OtherItemsCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: OtherItemsFilters
    sort: OtherItemsSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[OtherItemsFilters, _Mapping]] = ..., sort: _Optional[_Union[OtherItemsSort, str]] = ...) -> None: ...

class OtherItems(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "issuedCount", "remainingCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: OtherItemsPhoto
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[OtherItemsPhoto, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class OtherItemsActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "nameMin", "nameMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class OtherItemsActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: OtherItemsActivityLogFilters
    sort: OtherItemsActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[OtherItemsActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[OtherItemsActivityLogSort, str]] = ...) -> None: ...

class OtherItemsActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    count: int
    photo: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequestEmployee(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequestDutyPost(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequestWeapon(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequestAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequestOtherItems(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentReadResponseDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentReadResponseWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentReadResponseOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentUpdateRequestEmployee(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentUpdateRequestDutyPost(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentUpdateRequestWeapon(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentUpdateRequestAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentUpdateRequestOtherItems(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssignmentFilters(_message.Message):
    __slots__ = ("idIn",)
    IDIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignmentCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AssignmentFilters
    sort: AssignmentSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AssignmentFilters, _Mapping]] = ..., sort: _Optional[_Union[AssignmentSort, str]] = ...) -> None: ...

class Assignment(_message.Message):
    __slots__ = ("id", "employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentEmployee
    dutyPost: AssignmentDutyPost
    weapon: AssignmentWeapon
    weaponButtNo: str
    ammo: AssignmentAmmo
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[AssignmentOtherItems]
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[AssignmentDutyPost, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[AssignmentAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[AssignmentOtherItems, _Mapping]]] = ...) -> None: ...

class AssignmentActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "employeeIn", "dutyPostIn", "weaponIn", "weaponButtNoMin", "weaponButtNoMax", "ammoIn", "ammoCountMin", "ammoCountMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEEIN_FIELD_NUMBER: _ClassVar[int]
    DUTYPOSTIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNOMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNOMAX_FIELD_NUMBER: _ClassVar[int]
    AMMOIN_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNTMIN_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    employeeIn: _containers.RepeatedScalarFieldContainer[str]
    dutyPostIn: _containers.RepeatedScalarFieldContainer[str]
    weaponIn: _containers.RepeatedScalarFieldContainer[str]
    weaponButtNoMin: str
    weaponButtNoMax: str
    ammoIn: _containers.RepeatedScalarFieldContainer[str]
    ammoCountMin: int
    ammoCountMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., employeeIn: _Optional[_Iterable[str]] = ..., dutyPostIn: _Optional[_Iterable[str]] = ..., weaponIn: _Optional[_Iterable[str]] = ..., weaponButtNoMin: _Optional[str] = ..., weaponButtNoMax: _Optional[str] = ..., ammoIn: _Optional[_Iterable[str]] = ..., ammoCountMin: _Optional[int] = ..., ammoCountMax: _Optional[int] = ...) -> None: ...

class AssignmentActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AssignmentActivityLogFilters
    sort: AssignmentActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AssignmentActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[AssignmentActivityLogSort, str]] = ...) -> None: ...

class AssignmentActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    employee: str
    dutyPost: str
    weapon: str
    weaponButtNo: str
    ammo: str
    ammoCount: int
    otherItems: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., employee: _Optional[str] = ..., dutyPost: _Optional[str] = ..., weapon: _Optional[str] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[str] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[str]] = ...) -> None: ...

class ShiftReportItemFilters(_message.Message):
    __slots__ = ("idIn", "employeeNameMin", "employeeNameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEENAMEMIN_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEENAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    employeeNameMin: str
    employeeNameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., employeeNameMin: _Optional[str] = ..., employeeNameMax: _Optional[str] = ...) -> None: ...

class ShiftReportItemCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: ShiftReportItemFilters
    sort: ShiftReportItemSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[ShiftReportItemFilters, _Mapping]] = ..., sort: _Optional[_Union[ShiftReportItemSort, str]] = ...) -> None: ...

class ShiftReportItem(_message.Message):
    __slots__ = ("id", "employeeCisfId", "employeeRank", "employeeName", "dutyPostName", "weaponName", "flowWeaponEntryRemarks", "flowAmmoEntryCount", "flowWeaponEntryTime", "flowAmmoEntryTime", "flowWeaponExitTime", "flowAmmoExitTime")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEECISFID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEERANK_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEENAME_FIELD_NUMBER: _ClassVar[int]
    DUTYPOSTNAME_FIELD_NUMBER: _ClassVar[int]
    WEAPONNAME_FIELD_NUMBER: _ClassVar[int]
    FLOWWEAPONENTRYREMARKS_FIELD_NUMBER: _ClassVar[int]
    FLOWAMMOENTRYCOUNT_FIELD_NUMBER: _ClassVar[int]
    FLOWWEAPONENTRYTIME_FIELD_NUMBER: _ClassVar[int]
    FLOWAMMOENTRYTIME_FIELD_NUMBER: _ClassVar[int]
    FLOWWEAPONEXITTIME_FIELD_NUMBER: _ClassVar[int]
    FLOWAMMOEXITTIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    employeeCisfId: str
    employeeRank: str
    employeeName: str
    dutyPostName: str
    weaponName: str
    flowWeaponEntryRemarks: str
    flowAmmoEntryCount: int
    flowWeaponEntryTime: _timestamp_pb2.Timestamp
    flowAmmoEntryTime: _timestamp_pb2.Timestamp
    flowWeaponExitTime: _timestamp_pb2.Timestamp
    flowAmmoExitTime: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., employeeCisfId: _Optional[str] = ..., employeeRank: _Optional[str] = ..., employeeName: _Optional[str] = ..., dutyPostName: _Optional[str] = ..., weaponName: _Optional[str] = ..., flowWeaponEntryRemarks: _Optional[str] = ..., flowAmmoEntryCount: _Optional[int] = ..., flowWeaponEntryTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowAmmoEntryTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowWeaponExitTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowAmmoExitTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleCreateRequestShiftIncharge(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleCreateRequestKoteNco(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleCreateRequestArmsIssueDepositSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleCreateRequestArmsInspectionSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleCreateRequestClearingSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseShiftIncharge(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseKoteNco(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseArmsIssueDepositSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseArmsInspectionSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseClearingSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseAssignments(_message.Message):
    __slots__ = ("id", "employee", "dutyPost")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: ScheduleReadResponseAssignmentsEmployee
    dutyPost: DutyPost
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[ScheduleReadResponseAssignmentsEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[DutyPost, _Mapping]] = ...) -> None: ...

class ScheduleUpdateRequestShiftIncharge(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleUpdateRequestKoteNco(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleUpdateRequestArmsIssueDepositSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleUpdateRequestArmsInspectionSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleUpdateRequestClearingSupervisor(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ScheduleFilters(_message.Message):
    __slots__ = ("idIn", "startTimeMin", "startTimeMax", "endTimeMin", "endTimeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    startTimeMin: _timestamp_pb2.Timestamp
    startTimeMax: _timestamp_pb2.Timestamp
    endTimeMin: _timestamp_pb2.Timestamp
    endTimeMax: _timestamp_pb2.Timestamp
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., startTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., startTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: ScheduleFilters
    sort: ScheduleSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[ScheduleFilters, _Mapping]] = ..., sort: _Optional[_Union[ScheduleSort, str]] = ...) -> None: ...

class Schedule(_message.Message):
    __slots__ = ("id", "status", "startTime", "endTime", "employeesCount", "shiftIncharge", "koteNco", "armsIssueDepositSupervisor", "armsInspectionSupervisor", "clearingSupervisor")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEESCOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGE_FIELD_NUMBER: _ClassVar[int]
    KOTENCO_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: bool
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    employeesCount: int
    shiftIncharge: ScheduleShiftIncharge
    koteNco: ScheduleKoteNco
    armsIssueDepositSupervisor: ScheduleArmsIssueDepositSupervisor
    armsInspectionSupervisor: ScheduleArmsInspectionSupervisor
    clearingSupervisor: ScheduleClearingSupervisor
    def __init__(self, id: _Optional[str] = ..., status: bool = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., employeesCount: _Optional[int] = ..., shiftIncharge: _Optional[_Union[ScheduleShiftIncharge, _Mapping]] = ..., koteNco: _Optional[_Union[ScheduleKoteNco, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[ScheduleArmsIssueDepositSupervisor, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[ScheduleArmsInspectionSupervisor, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[ScheduleClearingSupervisor, _Mapping]] = ...) -> None: ...

class ScheduleActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "startTimeMin", "startTimeMax", "endTimeMin", "endTimeMax", "shiftInchargeIn", "koteNcoIn", "armsIssueDepositSupervisorIn", "armsInspectionSupervisorIn", "clearingSupervisorIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGEIN_FIELD_NUMBER: _ClassVar[int]
    KOTENCOIN_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISORIN_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISORIN_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISORIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    startTimeMin: _timestamp_pb2.Timestamp
    startTimeMax: _timestamp_pb2.Timestamp
    endTimeMin: _timestamp_pb2.Timestamp
    endTimeMax: _timestamp_pb2.Timestamp
    shiftInchargeIn: _containers.RepeatedScalarFieldContainer[str]
    koteNcoIn: _containers.RepeatedScalarFieldContainer[str]
    armsIssueDepositSupervisorIn: _containers.RepeatedScalarFieldContainer[str]
    armsInspectionSupervisorIn: _containers.RepeatedScalarFieldContainer[str]
    clearingSupervisorIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., startTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., startTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftInchargeIn: _Optional[_Iterable[str]] = ..., koteNcoIn: _Optional[_Iterable[str]] = ..., armsIssueDepositSupervisorIn: _Optional[_Iterable[str]] = ..., armsInspectionSupervisorIn: _Optional[_Iterable[str]] = ..., clearingSupervisorIn: _Optional[_Iterable[str]] = ...) -> None: ...

class ScheduleActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: ScheduleActivityLogFilters
    sort: ScheduleActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[ScheduleActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[ScheduleActivityLogSort, str]] = ...) -> None: ...

class ScheduleActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "startTime", "endTime", "shiftIncharge", "koteNco", "armsIssueDepositSupervisor", "armsInspectionSupervisor", "clearingSupervisor", "assignments")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    SHIFTINCHARGE_FIELD_NUMBER: _ClassVar[int]
    KOTENCO_FIELD_NUMBER: _ClassVar[int]
    ARMSISSUEDEPOSITSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ARMSINSPECTIONSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    CLEARINGSUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    shiftIncharge: str
    koteNco: str
    armsIssueDepositSupervisor: str
    armsInspectionSupervisor: str
    clearingSupervisor: str
    assignments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[str] = ..., koteNco: _Optional[str] = ..., armsIssueDepositSupervisor: _Optional[str] = ..., armsInspectionSupervisor: _Optional[str] = ..., clearingSupervisor: _Optional[str] = ..., assignments: _Optional[_Iterable[str]] = ...) -> None: ...

class WeaponAmmoCreateRequestAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponAmmoReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponAmmoUpdateRequestAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponAmmoFilters(_message.Message):
    __slots__ = ("idIn", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class WeaponAmmoCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponAmmoFilters
    sort: WeaponAmmoSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponAmmoFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponAmmoSort, str]] = ...) -> None: ...

class WeaponAmmo(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponAmmoAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponAmmoActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "ammoIn", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    AMMOIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    ammoIn: _containers.RepeatedScalarFieldContainer[str]
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ammoIn: _Optional[_Iterable[str]] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class WeaponAmmoActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponAmmoActivityLogFilters
    sort: WeaponAmmoActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponAmmoActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponAmmoActivityLogSort, str]] = ...) -> None: ...

class WeaponAmmoActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    ammo: str
    count: int
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ammo: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GlobalConfigCreateRequestFlowAlerts(_message.Message):
    __slots__ = ("weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class GlobalConfigReadResponseFlowAlerts(_message.Message):
    __slots__ = ("id", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class GlobalConfigUpdateRequestFlowAlerts(_message.Message):
    __slots__ = ("id", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class GlobalConfigFilters(_message.Message):
    __slots__ = ("idIn", "weaponIssueBeforeStartBufferMin", "weaponIssueBeforeStartBufferMax", "weaponIssueAfterStartBufferMin", "weaponIssueAfterStartBufferMax", "scheduleEditAfterBufferMin", "scheduleEditAfterBufferMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    weaponIssueBeforeStartBufferMin: int
    weaponIssueBeforeStartBufferMax: int
    weaponIssueAfterStartBufferMin: int
    weaponIssueAfterStartBufferMax: int
    scheduleEditAfterBufferMin: int
    scheduleEditAfterBufferMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., weaponIssueBeforeStartBufferMin: _Optional[int] = ..., weaponIssueBeforeStartBufferMax: _Optional[int] = ..., weaponIssueAfterStartBufferMin: _Optional[int] = ..., weaponIssueAfterStartBufferMax: _Optional[int] = ..., scheduleEditAfterBufferMin: _Optional[int] = ..., scheduleEditAfterBufferMax: _Optional[int] = ...) -> None: ...

class GlobalConfigCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: GlobalConfigFilters
    sort: GlobalConfigSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[GlobalConfigFilters, _Mapping]] = ..., sort: _Optional[_Union[GlobalConfigSort, str]] = ...) -> None: ...

class GlobalConfig(_message.Message):
    __slots__ = ("id", "weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ...) -> None: ...

class GlobalConfigActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "weaponIssueBeforeStartBufferMin", "weaponIssueBeforeStartBufferMax", "weaponIssueAfterStartBufferMin", "weaponIssueAfterStartBufferMax", "scheduleEditAfterBufferMin", "scheduleEditAfterBufferMax", "flowAlertsIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFERMIN_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFERMAX_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTSIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    weaponIssueBeforeStartBufferMin: int
    weaponIssueBeforeStartBufferMax: int
    weaponIssueAfterStartBufferMin: int
    weaponIssueAfterStartBufferMax: int
    scheduleEditAfterBufferMin: int
    scheduleEditAfterBufferMax: int
    flowAlertsIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., weaponIssueBeforeStartBufferMin: _Optional[int] = ..., weaponIssueBeforeStartBufferMax: _Optional[int] = ..., weaponIssueAfterStartBufferMin: _Optional[int] = ..., weaponIssueAfterStartBufferMax: _Optional[int] = ..., scheduleEditAfterBufferMin: _Optional[int] = ..., scheduleEditAfterBufferMax: _Optional[int] = ..., flowAlertsIn: _Optional[_Iterable[str]] = ...) -> None: ...

class GlobalConfigActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: GlobalConfigActivityLogFilters
    sort: GlobalConfigActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[GlobalConfigActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[GlobalConfigActivityLogSort, str]] = ...) -> None: ...

class GlobalConfigActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer", "flowAlerts")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    flowAlerts: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[str] = ...) -> None: ...

class FlowAlertsFilters(_message.Message):
    __slots__ = ("idIn", "weaponIssueAfterShiftStartDurationMin", "weaponIssueAfterShiftStartDurationMax", "clearingIssueAfterWeaponEntryDurationMin", "clearingIssueAfterWeaponEntryDurationMax", "ammoIssueAfterClearingEntryDurationMin", "ammoIssueAfterClearingEntryDurationMax", "weaponNotDepositDurationMin", "weaponNotDepositDurationMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    weaponIssueAfterShiftStartDurationMin: int
    weaponIssueAfterShiftStartDurationMax: int
    clearingIssueAfterWeaponEntryDurationMin: int
    clearingIssueAfterWeaponEntryDurationMax: int
    ammoIssueAfterClearingEntryDurationMin: int
    ammoIssueAfterClearingEntryDurationMax: int
    weaponNotDepositDurationMin: int
    weaponNotDepositDurationMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., weaponIssueAfterShiftStartDurationMin: _Optional[int] = ..., weaponIssueAfterShiftStartDurationMax: _Optional[int] = ..., clearingIssueAfterWeaponEntryDurationMin: _Optional[int] = ..., clearingIssueAfterWeaponEntryDurationMax: _Optional[int] = ..., ammoIssueAfterClearingEntryDurationMin: _Optional[int] = ..., ammoIssueAfterClearingEntryDurationMax: _Optional[int] = ..., weaponNotDepositDurationMin: _Optional[int] = ..., weaponNotDepositDurationMax: _Optional[int] = ...) -> None: ...

class FlowAlertsCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FlowAlertsFilters
    sort: FlowAlertsSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FlowAlertsFilters, _Mapping]] = ..., sort: _Optional[_Union[FlowAlertsSort, str]] = ...) -> None: ...

class FlowAlerts(_message.Message):
    __slots__ = ("id", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class FlowAlertsActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "weaponIssueAfterShiftStartDurationMin", "weaponIssueAfterShiftStartDurationMax", "clearingIssueAfterWeaponEntryDurationMin", "clearingIssueAfterWeaponEntryDurationMax", "ammoIssueAfterClearingEntryDurationMin", "ammoIssueAfterClearingEntryDurationMax", "weaponNotDepositDurationMin", "weaponNotDepositDurationMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATIONMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    weaponIssueAfterShiftStartDurationMin: int
    weaponIssueAfterShiftStartDurationMax: int
    clearingIssueAfterWeaponEntryDurationMin: int
    clearingIssueAfterWeaponEntryDurationMax: int
    ammoIssueAfterClearingEntryDurationMin: int
    ammoIssueAfterClearingEntryDurationMax: int
    weaponNotDepositDurationMin: int
    weaponNotDepositDurationMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., weaponIssueAfterShiftStartDurationMin: _Optional[int] = ..., weaponIssueAfterShiftStartDurationMax: _Optional[int] = ..., clearingIssueAfterWeaponEntryDurationMin: _Optional[int] = ..., clearingIssueAfterWeaponEntryDurationMax: _Optional[int] = ..., ammoIssueAfterClearingEntryDurationMin: _Optional[int] = ..., ammoIssueAfterClearingEntryDurationMax: _Optional[int] = ..., weaponNotDepositDurationMin: _Optional[int] = ..., weaponNotDepositDurationMax: _Optional[int] = ...) -> None: ...

class FlowAlertsActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FlowAlertsActivityLogFilters
    sort: FlowAlertsActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FlowAlertsActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[FlowAlertsActivityLogSort, str]] = ...) -> None: ...

class FlowAlertsActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "weaponIssueAfterShiftStartDuration", "clearingIssueAfterWeaponEntryDuration", "ammoIssueAfterClearingEntryDuration", "weaponNotDepositDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSHIFTSTARTDURATION_FIELD_NUMBER: _ClassVar[int]
    CLEARINGISSUEAFTERWEAPONENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    AMMOISSUEAFTERCLEARINGENTRYDURATION_FIELD_NUMBER: _ClassVar[int]
    WEAPONNOTDEPOSITDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    weaponIssueAfterShiftStartDuration: int
    clearingIssueAfterWeaponEntryDuration: int
    ammoIssueAfterClearingEntryDuration: int
    weaponNotDepositDuration: int
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., weaponIssueAfterShiftStartDuration: _Optional[int] = ..., clearingIssueAfterWeaponEntryDuration: _Optional[int] = ..., ammoIssueAfterClearingEntryDuration: _Optional[int] = ..., weaponNotDepositDuration: _Optional[int] = ...) -> None: ...

class CommonInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CommonInfoFilters(_message.Message):
    __slots__ = ("idIn", "timeMin", "timeMax", "remarksMin", "remarksMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    remarksMin: str
    remarksMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ...) -> None: ...

class CommonInfoCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: CommonInfoFilters
    sort: CommonInfoSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[CommonInfoFilters, _Mapping]] = ..., sort: _Optional[_Union[CommonInfoSort, str]] = ...) -> None: ...

class CommonInfo(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: CommonInfoAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[CommonInfoAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class CommonInfoActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "timeMin", "timeMax", "acknowledgedByIn", "remarksMin", "remarksMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBYIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    acknowledgedByIn: _containers.RepeatedScalarFieldContainer[str]
    remarksMin: str
    remarksMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedByIn: _Optional[_Iterable[str]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ...) -> None: ...

class CommonInfoActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: CommonInfoActivityLogFilters
    sort: CommonInfoActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[CommonInfoActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[CommonInfoActivityLogSort, str]] = ...) -> None: ...

class CommonInfoActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: str
    remarks: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[str] = ..., remarks: _Optional[str] = ...) -> None: ...

class AmmoInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoInfoFilters(_message.Message):
    __slots__ = ("idIn", "timeMin", "timeMax", "remarksMin", "remarksMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    remarksMin: str
    remarksMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class AmmoInfoCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AmmoInfoFilters
    sort: AmmoInfoSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AmmoInfoFilters, _Mapping]] = ..., sort: _Optional[_Union[AmmoInfoSort, str]] = ...) -> None: ...

class AmmoInfo(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: AmmoInfoAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[AmmoInfoAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoInfoActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "timeMin", "timeMax", "acknowledgedByIn", "remarksMin", "remarksMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBYIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    acknowledgedByIn: _containers.RepeatedScalarFieldContainer[str]
    remarksMin: str
    remarksMax: str
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedByIn: _Optional[_Iterable[str]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

class AmmoInfoActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AmmoInfoActivityLogFilters
    sort: AmmoInfoActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AmmoInfoActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[AmmoInfoActivityLogSort, str]] = ...) -> None: ...

class AmmoInfoActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: str
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[str] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsCreateRequestAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestWeaponEntry(_message.Message):
    __slots__ = ("time", "remarks", "issuedButtNo")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestClearingEntry(_message.Message):
    __slots__ = ("time", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestAmmoEntry(_message.Message):
    __slots__ = ("time", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsCreateRequestAmmoExit(_message.Message):
    __slots__ = ("time", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsCreateRequestClearingExit(_message.Message):
    __slots__ = ("time", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestWeaponExit(_message.Message):
    __slots__ = ("time", "remarks", "issuedButtNo")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAssignment(_message.Message):
    __slots__ = ("id", "employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: FlowsReadResponseAssignmentEmployee
    dutyPost: DutyPost
    weapon: FlowsReadResponseAssignmentWeapon
    weaponButtNo: str
    ammo: FlowsReadResponseAssignmentAmmo
    ammoCount: int
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[FlowsReadResponseAssignmentEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[DutyPost, _Mapping]] = ..., weapon: _Optional[_Union[FlowsReadResponseAssignmentWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[FlowsReadResponseAssignmentAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ...) -> None: ...

class FlowsReadResponseWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseWeaponEntryAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsReadResponseClearingEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseClearingEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseClearingEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAmmoEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseAmmoEntryAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseAmmoEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsReadResponseAmmoExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseAmmoExitAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseAmmoExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsReadResponseClearingExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseClearingExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseClearingExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsReadResponseWeaponExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseWeaponExitAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestClearingEntry(_message.Message):
    __slots__ = ("id", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAmmoEntry(_message.Message):
    __slots__ = ("id", "time", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsUpdateRequestAmmoExit(_message.Message):
    __slots__ = ("id", "time", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsUpdateRequestClearingExit(_message.Message):
    __slots__ = ("id", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestWeaponExit(_message.Message):
    __slots__ = ("id", "time", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsFilters(_message.Message):
    __slots__ = ("idIn",)
    IDIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ...) -> None: ...

class FlowsCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FlowsFilters
    sort: FlowsSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FlowsFilters, _Mapping]] = ..., sort: _Optional[_Union[FlowsSort, str]] = ...) -> None: ...

class Flows(_message.Message):
    __slots__ = ("id", "assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit", "isActive")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    ISACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    assignment: FlowsAssignment
    weaponEntry: FlowsWeaponEntry
    clearingEntry: FlowsClearingEntry
    ammoEntry: FlowsAmmoEntry
    ammoExit: FlowsAmmoExit
    clearingExit: FlowsClearingExit
    weaponExit: FlowsWeaponExit
    isActive: bool
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsWeaponExit, _Mapping]] = ..., isActive: bool = ...) -> None: ...

class FlowsActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "assignmentIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    assignmentIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignmentIn: _Optional[_Iterable[str]] = ...) -> None: ...

class FlowsActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FlowsActivityLogFilters
    sort: FlowsActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FlowsActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[FlowsActivityLogSort, str]] = ...) -> None: ...

class FlowsActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    assignment: str
    weaponEntry: str
    clearingEntry: str
    ammoEntry: str
    ammoExit: str
    clearingExit: str
    weaponExit: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignment: _Optional[str] = ..., weaponEntry: _Optional[str] = ..., clearingEntry: _Optional[str] = ..., ammoEntry: _Optional[str] = ..., ammoExit: _Optional[str] = ..., clearingExit: _Optional[str] = ..., weaponExit: _Optional[str] = ...) -> None: ...

class AlertCreateRequestEmployee(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AlertReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AlertFilters(_message.Message):
    __slots__ = ("idIn", "alertTypeIn", "timeMin", "timeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPEIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    alertTypeIn: _containers.RepeatedScalarFieldContainer[AlertType]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., alertTypeIn: _Optional[_Iterable[_Union[AlertType, str]]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AlertCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AlertFilters
    sort: AlertSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AlertFilters, _Mapping]] = ..., sort: _Optional[_Union[AlertSort, str]] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("id", "employee", "alertType", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AlertEmployee
    alertType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertEmployee, _Mapping]] = ..., alertType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class UserFilters(_message.Message):
    __slots__ = ("idIn", "authNameMin", "authNameMax", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    authNameMin: str
    authNameMax: str
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., authNameMin: _Optional[str] = ..., authNameMax: _Optional[str] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class UserCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: UserFilters
    sort: UserSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[UserFilters, _Mapping]] = ..., sort: _Optional[_Union[UserSort, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "authName", "name", "popUpFor", "popUpDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPUPFOR_FIELD_NUMBER: _ClassVar[int]
    POPUPDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    name: str
    popUpFor: _containers.RepeatedScalarFieldContainer[CheckPoint]
    popUpDuration: int
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ..., name: _Optional[str] = ..., popUpFor: _Optional[_Iterable[_Union[CheckPoint, str]]] = ..., popUpDuration: _Optional[int] = ...) -> None: ...

class UserActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "authNameMin", "authNameMax", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    authNameMin: str
    authNameMax: str
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., authNameMin: _Optional[str] = ..., authNameMax: _Optional[str] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class UserActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: UserActivityLogFilters
    sort: UserActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[UserActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[UserActivityLogSort, str]] = ...) -> None: ...

class UserActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "authName", "name", "popUpFor", "popUpDuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPUPFOR_FIELD_NUMBER: _ClassVar[int]
    POPUPDURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    authName: str
    name: str
    popUpFor: _containers.RepeatedScalarFieldContainer[CheckPoint]
    popUpDuration: int
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., authName: _Optional[str] = ..., name: _Optional[str] = ..., popUpFor: _Optional[_Iterable[_Union[CheckPoint, str]]] = ..., popUpDuration: _Optional[int] = ...) -> None: ...

class WeaponInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponInfoFilters(_message.Message):
    __slots__ = ("idIn", "timeMin", "timeMax", "remarksMin", "remarksMax", "issuedButtNoMin", "issuedButtNoMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNOMIN_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNOMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    remarksMin: str
    remarksMax: str
    issuedButtNoMin: str
    issuedButtNoMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ..., issuedButtNoMin: _Optional[str] = ..., issuedButtNoMax: _Optional[str] = ...) -> None: ...

class WeaponInfoCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponInfoFilters
    sort: WeaponInfoSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponInfoFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponInfoSort, str]] = ...) -> None: ...

class WeaponInfo(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: WeaponInfoAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[WeaponInfoAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class WeaponInfoActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "timeMin", "timeMax", "acknowledgedByIn", "remarksMin", "remarksMax", "issuedButtNoMin", "issuedButtNoMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBYIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMIN_FIELD_NUMBER: _ClassVar[int]
    REMARKSMAX_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNOMIN_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNOMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    acknowledgedByIn: _containers.RepeatedScalarFieldContainer[str]
    remarksMin: str
    remarksMax: str
    issuedButtNoMin: str
    issuedButtNoMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedByIn: _Optional[_Iterable[str]] = ..., remarksMin: _Optional[str] = ..., remarksMax: _Optional[str] = ..., issuedButtNoMin: _Optional[str] = ..., issuedButtNoMax: _Optional[str] = ...) -> None: ...

class WeaponInfoActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: WeaponInfoActivityLogFilters
    sort: WeaponInfoActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[WeaponInfoActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[WeaponInfoActivityLogSort, str]] = ...) -> None: ...

class WeaponInfoActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: str
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[str] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class AccessControlCreateRequestAuth(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AccessControlCreateRequestTags(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AccessControlReadResponseAuth(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AccessControlReadResponseTags(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AccessControlUpdateRequestAuth(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AccessControlUpdateRequestTags(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AccessControlFilters(_message.Message):
    __slots__ = ("idIn", "authIn", "permsIn", "scopesIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIN_FIELD_NUMBER: _ClassVar[int]
    PERMSIN_FIELD_NUMBER: _ClassVar[int]
    SCOPESIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    authIn: _containers.RepeatedScalarFieldContainer[str]
    permsIn: _containers.RepeatedScalarFieldContainer[Perm]
    scopesIn: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., authIn: _Optional[_Iterable[str]] = ..., permsIn: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopesIn: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AccessControlFilters
    sort: AccessControlSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AccessControlFilters, _Mapping]] = ..., sort: _Optional[_Union[AccessControlSort, str]] = ...) -> None: ...

class AccessControl(_message.Message):
    __slots__ = ("id", "auth", "perms", "tags", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    auth: AccessControlAuth
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    tags: _containers.RepeatedCompositeFieldContainer[AccessControlTags]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, id: _Optional[str] = ..., auth: _Optional[_Union[AccessControlAuth, _Mapping]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., tags: _Optional[_Iterable[_Union[AccessControlTags, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlActivityLogFilters(_message.Message):
    __slots__ = ("idIn", "actionIn", "objectIdIn", "authIdIn", "activityAtMin", "activityAtMax", "authIn", "permsIn", "scopesIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIONIN_FIELD_NUMBER: _ClassVar[int]
    OBJECTIDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHIDIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYATMAX_FIELD_NUMBER: _ClassVar[int]
    AUTHIN_FIELD_NUMBER: _ClassVar[int]
    PERMSIN_FIELD_NUMBER: _ClassVar[int]
    SCOPESIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    actionIn: _containers.RepeatedScalarFieldContainer[_message_pb2.ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    authIn: _containers.RepeatedScalarFieldContainer[str]
    permsIn: _containers.RepeatedScalarFieldContainer[Perm]
    scopesIn: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[_message_pb2.ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., authIn: _Optional[_Iterable[str]] = ..., permsIn: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopesIn: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class AccessControlActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AccessControlActivityLogFilters
    sort: AccessControlActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AccessControlActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[AccessControlActivityLogSort, str]] = ...) -> None: ...

class AccessControlActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "auth", "perms", "tags", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: _message_pb2.ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    auth: str
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    tags: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[_message_pb2.ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auth: _Optional[str] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., tags: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

class EmployeePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponCreateRequestWeaponAmmoAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponReadResponseWeaponAmmoAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponUpdateRequestWeaponAmmoAmmo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponPhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponWeaponAmmo(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponWeaponAmmoAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponWeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class AmmoPhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OtherItemsPhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleReadResponseAssignmentsEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleShiftIncharge(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleKoteNco(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleArmsIssueDepositSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleArmsInspectionSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleClearingSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponAmmoAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CommonInfoAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoInfoAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAssignmentEmployee(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: _message_pb2.FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[_message_pb2.FileObject, _Mapping]] = ...) -> None: ...

class FlowsReadResponseAssignmentWeapon(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: _message_pb2.FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[_message_pb2.FileObject, _Mapping]] = ...) -> None: ...

class FlowsReadResponseAssignmentAmmo(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: _message_pb2.FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[_message_pb2.FileObject, _Mapping]] = ...) -> None: ...

class FlowsReadResponseWeaponEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseClearingEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAmmoEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAmmoExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseClearingExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsReadResponseWeaponExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsWeaponEntryAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class FlowsClearingEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsClearingEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsClearingEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsAmmoEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsAmmoEntryAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsAmmoEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsAmmoExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsAmmoExitAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsAmmoExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsClearingExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsClearingExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsClearingExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsWeaponExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "issuedButtNo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsWeaponExitAcknowledgedBy
    remarks: str
    issuedButtNo: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class AlertEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponInfoAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AccessControlAuth(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

class AccessControlTags(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponWeaponAmmoAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsWeaponEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsClearingEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsAmmoEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsAmmoExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsClearingExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FlowsWeaponExitAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

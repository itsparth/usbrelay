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

class DutyPostSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    dutyPostSort_unspecified: _ClassVar[DutyPostSort]
    dutyPostSort_nameAsc: _ClassVar[DutyPostSort]
    dutyPostSort_nameDesc: _ClassVar[DutyPostSort]

class WeaponSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponSort_unspecified: _ClassVar[WeaponSort]
    weaponSort_nameAsc: _ClassVar[WeaponSort]
    weaponSort_nameDesc: _ClassVar[WeaponSort]
    weaponSort_countAsc: _ClassVar[WeaponSort]
    weaponSort_countDesc: _ClassVar[WeaponSort]

class AmmoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoSort_unspecified: _ClassVar[AmmoSort]
    ammoSort_nameAsc: _ClassVar[AmmoSort]
    ammoSort_nameDesc: _ClassVar[AmmoSort]
    ammoSort_countAsc: _ClassVar[AmmoSort]
    ammoSort_countDesc: _ClassVar[AmmoSort]

class OtherItemsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    otherItemsSort_unspecified: _ClassVar[OtherItemsSort]
    otherItemsSort_nameAsc: _ClassVar[OtherItemsSort]
    otherItemsSort_nameDesc: _ClassVar[OtherItemsSort]
    otherItemsSort_countAsc: _ClassVar[OtherItemsSort]
    otherItemsSort_countDesc: _ClassVar[OtherItemsSort]

class AssignmentSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    assignmentSort_unspecified: _ClassVar[AssignmentSort]

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

class GlobalConfigSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    globalConfigSort_unspecified: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueBeforeStartBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueBeforeStartBufferDesc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueAfterStartBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_weaponIssueAfterStartBufferDesc: _ClassVar[GlobalConfigSort]
    globalConfigSort_scheduleEditAfterBufferAsc: _ClassVar[GlobalConfigSort]
    globalConfigSort_scheduleEditAfterBufferDesc: _ClassVar[GlobalConfigSort]

class FlowsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowsSort_unspecified: _ClassVar[FlowsSort]

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

class AlertsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertsSort_unspecified: _ClassVar[AlertsSort]
    alertsSort_timeAsc: _ClassVar[AlertsSort]
    alertsSort_timeDesc: _ClassVar[AlertsSort]

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

class Perm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    perm_unspecified: _ClassVar[Perm]
    perm_create: _ClassVar[Perm]
    perm_read: _ClassVar[Perm]
    perm_update: _ClassVar[Perm]
    perm_delete: _ClassVar[Perm]
    perm_readActivity: _ClassVar[Perm]

class Scopes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    scopes_unspecified: _ClassVar[Scopes]
    scopes_accessControl: _ClassVar[Scopes]
    scopes_alerts: _ClassVar[Scopes]
    scopes_ammo: _ClassVar[Scopes]
    scopes_dutyPost: _ClassVar[Scopes]
    scopes_employee: _ClassVar[Scopes]
    scopes_flows: _ClassVar[Scopes]
    scopes_globalConfig: _ClassVar[Scopes]
    scopes_otherItems: _ClassVar[Scopes]
    scopes_resourceGroup: _ClassVar[Scopes]
    scopes_schedule: _ClassVar[Scopes]
    scopes_tags: _ClassVar[Scopes]
    scopes_user: _ClassVar[Scopes]
    scopes_weapon: _ClassVar[Scopes]

class AccessControlSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    accessControlSort_unspecified: _ClassVar[AccessControlSort]
    accessControlSort_nameAsc: _ClassVar[AccessControlSort]
    accessControlSort_nameDesc: _ClassVar[AccessControlSort]

class ResourceGroupSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    resourceGroupSort_unspecified: _ClassVar[ResourceGroupSort]
    resourceGroupSort_nameAsc: _ClassVar[ResourceGroupSort]
    resourceGroupSort_nameDesc: _ClassVar[ResourceGroupSort]
employeeSort_unspecified: EmployeeSort
employeeSort_biometricsIdAsc: EmployeeSort
employeeSort_biometricsIdDesc: EmployeeSort
employeeSort_cisfIdAsc: EmployeeSort
employeeSort_cisfIdDesc: EmployeeSort
employeeSort_nameAsc: EmployeeSort
employeeSort_nameDesc: EmployeeSort
employeeSort_rankAsc: EmployeeSort
employeeSort_rankDesc: EmployeeSort
dutyPostSort_unspecified: DutyPostSort
dutyPostSort_nameAsc: DutyPostSort
dutyPostSort_nameDesc: DutyPostSort
weaponSort_unspecified: WeaponSort
weaponSort_nameAsc: WeaponSort
weaponSort_nameDesc: WeaponSort
weaponSort_countAsc: WeaponSort
weaponSort_countDesc: WeaponSort
ammoSort_unspecified: AmmoSort
ammoSort_nameAsc: AmmoSort
ammoSort_nameDesc: AmmoSort
ammoSort_countAsc: AmmoSort
ammoSort_countDesc: AmmoSort
otherItemsSort_unspecified: OtherItemsSort
otherItemsSort_nameAsc: OtherItemsSort
otherItemsSort_nameDesc: OtherItemsSort
otherItemsSort_countAsc: OtherItemsSort
otherItemsSort_countDesc: OtherItemsSort
assignmentSort_unspecified: AssignmentSort
shiftReportItemSort_unspecified: ShiftReportItemSort
shiftReportItemSort_employeeNameAsc: ShiftReportItemSort
shiftReportItemSort_employeeNameDesc: ShiftReportItemSort
scheduleSort_unspecified: ScheduleSort
scheduleSort_startTimeAsc: ScheduleSort
scheduleSort_startTimeDesc: ScheduleSort
scheduleSort_endTimeAsc: ScheduleSort
scheduleSort_endTimeDesc: ScheduleSort
globalConfigSort_unspecified: GlobalConfigSort
globalConfigSort_weaponIssueBeforeStartBufferAsc: GlobalConfigSort
globalConfigSort_weaponIssueBeforeStartBufferDesc: GlobalConfigSort
globalConfigSort_weaponIssueAfterStartBufferAsc: GlobalConfigSort
globalConfigSort_weaponIssueAfterStartBufferDesc: GlobalConfigSort
globalConfigSort_scheduleEditAfterBufferAsc: GlobalConfigSort
globalConfigSort_scheduleEditAfterBufferDesc: GlobalConfigSort
flowsSort_unspecified: FlowsSort
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
alertsSort_unspecified: AlertsSort
alertsSort_timeAsc: AlertsSort
alertsSort_timeDesc: AlertsSort
checkPoint_unspecified: CheckPoint
checkPoint_weapon: CheckPoint
checkPoint_ammo: CheckPoint
userSort_unspecified: UserSort
userSort_authNameAsc: UserSort
userSort_authNameDesc: UserSort
userSort_nameAsc: UserSort
userSort_nameDesc: UserSort
perm_unspecified: Perm
perm_create: Perm
perm_read: Perm
perm_update: Perm
perm_delete: Perm
perm_readActivity: Perm
scopes_unspecified: Scopes
scopes_accessControl: Scopes
scopes_alerts: Scopes
scopes_ammo: Scopes
scopes_dutyPost: Scopes
scopes_employee: Scopes
scopes_flows: Scopes
scopes_globalConfig: Scopes
scopes_otherItems: Scopes
scopes_resourceGroup: Scopes
scopes_schedule: Scopes
scopes_tags: Scopes
scopes_user: Scopes
scopes_weapon: Scopes
accessControlSort_unspecified: AccessControlSort
accessControlSort_nameAsc: AccessControlSort
accessControlSort_nameDesc: AccessControlSort
resourceGroupSort_unspecified: ResourceGroupSort
resourceGroupSort_nameAsc: ResourceGroupSort
resourceGroupSort_nameDesc: ResourceGroupSort

class EmployeeCreateRequest(_message.Message):
    __slots__ = ("biometricsId", "cisfId", "name", "rank", "photo")
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    biometricsId: int
    cisfId: int
    name: str
    rank: str
    photo: _message_pb2.IdMessage
    def __init__(self, biometricsId: _Optional[int] = ..., cisfId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

class EmployeeReadResponse(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    cisfId: int
    name: str
    rank: str
    photo: EmployeeReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., cisfId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeReadResponsePhoto, _Mapping]] = ...) -> None: ...

class EmployeeUpdateRequest(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    cisfId: int
    name: str
    rank: str
    photo: _message_pb2.IdMessage
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., cisfId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

class EmployeeUpdateReadResponse(_message.Message):
    __slots__ = ("id", "biometricsId", "cisfId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    CISFID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    cisfId: int
    name: str
    rank: str
    photo: EmployeeUpdateReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., cisfId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeUpdateReadResponsePhoto, _Mapping]] = ...) -> None: ...

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

class DutyPostUpdateReadResponse(_message.Message):
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

class WeaponCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo", "weaponAmmo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: _message_pb2.IdMessage
    weaponAmmo: WeaponAmmoCreateRequest
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponAmmoCreateRequest, _Mapping]] = ...) -> None: ...

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
    weaponAmmo: WeaponAmmoReadResponse
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponReadResponsePhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponAmmoReadResponse, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

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
    photo: _message_pb2.IdMessage
    weaponAmmo: WeaponAmmoCreateRequest
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponAmmoCreateRequest, _Mapping]] = ...) -> None: ...

class WeaponUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo", "weaponAmmo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    WEAPONAMMO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: WeaponUpdateReadResponsePhoto
    weaponAmmo: WeaponAmmoReadResponse
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponUpdateReadResponsePhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponAmmoReadResponse, _Mapping]] = ...) -> None: ...

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

class AmmoCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: _message_pb2.IdMessage
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

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
    photo: _message_pb2.IdMessage
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

class AmmoUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: AmmoUpdateReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[AmmoUpdateReadResponsePhoto, _Mapping]] = ...) -> None: ...

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

class OtherItemsCreateRequest(_message.Message):
    __slots__ = ("name", "count", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    photo: _message_pb2.IdMessage
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

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
    photo: _message_pb2.IdMessage
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

class OtherItemsUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "count", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    photo: OtherItemsUpdateReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[OtherItemsUpdateReadResponsePhoto, _Mapping]] = ...) -> None: ...

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
    employee: _message_pb2.IdMessage
    dutyPost: _message_pb2.IdMessage
    weapon: _message_pb2.IdMessage
    weaponButtNo: str
    ammo: _message_pb2.IdMessage
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., dutyPost: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weapon: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

class AssignmentUpdateReadResponse(_message.Message):
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
    employee: AssignmentUpdateReadResponseEmployee
    dutyPost: AssignmentUpdateReadResponseDutyPost
    weapon: AssignmentUpdateReadResponseWeapon
    weaponButtNo: str
    ammo: AssignmentUpdateReadResponseAmmo
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[AssignmentUpdateReadResponseOtherItems]
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentUpdateReadResponseEmployee, _Mapping]] = ..., dutyPost: _Optional[_Union[AssignmentUpdateReadResponseDutyPost, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentUpdateReadResponseWeapon, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[AssignmentUpdateReadResponseAmmo, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[AssignmentUpdateReadResponseOtherItems, _Mapping]]] = ...) -> None: ...

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
    shiftIncharge: _message_pb2.IdMessage
    koteNco: _message_pb2.IdMessage
    armsIssueDepositSupervisor: _message_pb2.IdMessage
    armsInspectionSupervisor: _message_pb2.IdMessage
    clearingSupervisor: _message_pb2.IdMessage
    def __init__(self, startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., koteNco: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

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
    shiftIncharge: _message_pb2.IdMessage
    koteNco: _message_pb2.IdMessage
    armsIssueDepositSupervisor: _message_pb2.IdMessage
    armsInspectionSupervisor: _message_pb2.IdMessage
    clearingSupervisor: _message_pb2.IdMessage
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., koteNco: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ...) -> None: ...

class ScheduleUpdateReadResponse(_message.Message):
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
    shiftIncharge: ScheduleUpdateReadResponseShiftIncharge
    koteNco: ScheduleUpdateReadResponseKoteNco
    armsIssueDepositSupervisor: ScheduleUpdateReadResponseArmsIssueDepositSupervisor
    armsInspectionSupervisor: ScheduleUpdateReadResponseArmsInspectionSupervisor
    clearingSupervisor: ScheduleUpdateReadResponseClearingSupervisor
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shiftIncharge: _Optional[_Union[ScheduleUpdateReadResponseShiftIncharge, _Mapping]] = ..., koteNco: _Optional[_Union[ScheduleUpdateReadResponseKoteNco, _Mapping]] = ..., armsIssueDepositSupervisor: _Optional[_Union[ScheduleUpdateReadResponseArmsIssueDepositSupervisor, _Mapping]] = ..., armsInspectionSupervisor: _Optional[_Union[ScheduleUpdateReadResponseArmsInspectionSupervisor, _Mapping]] = ..., clearingSupervisor: _Optional[_Union[ScheduleUpdateReadResponseClearingSupervisor, _Mapping]] = ...) -> None: ...

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
    ammo: _message_pb2.IdMessage
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponAmmoUpdateReadResponse(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponAmmoUpdateReadResponseAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponAmmoUpdateReadResponseAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class GlobalConfigCreateRequest(_message.Message):
    __slots__ = ("weaponIssueBeforeStartBuffer", "weaponIssueAfterStartBuffer", "scheduleEditAfterBuffer", "flowAlerts")
    WEAPONISSUEBEFORESTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    WEAPONISSUEAFTERSTARTBUFFER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEEDITAFTERBUFFER_FIELD_NUMBER: _ClassVar[int]
    FLOWALERTS_FIELD_NUMBER: _ClassVar[int]
    weaponIssueBeforeStartBuffer: int
    weaponIssueAfterStartBuffer: int
    scheduleEditAfterBuffer: int
    flowAlerts: FlowAlertsCreateRequest
    def __init__(self, weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[FlowAlertsCreateRequest, _Mapping]] = ...) -> None: ...

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
    flowAlerts: FlowAlertsReadResponse
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[FlowAlertsReadResponse, _Mapping]] = ...) -> None: ...

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
    flowAlerts: FlowAlertsCreateRequest
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[FlowAlertsCreateRequest, _Mapping]] = ...) -> None: ...

class GlobalConfigUpdateReadResponse(_message.Message):
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
    flowAlerts: FlowAlertsReadResponse
    def __init__(self, id: _Optional[str] = ..., weaponIssueBeforeStartBuffer: _Optional[int] = ..., weaponIssueAfterStartBuffer: _Optional[int] = ..., scheduleEditAfterBuffer: _Optional[int] = ..., flowAlerts: _Optional[_Union[FlowAlertsReadResponse, _Mapping]] = ...) -> None: ...

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

class FlowAlertsUpdateReadResponse(_message.Message):
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

class FlowsCreateRequest(_message.Message):
    __slots__ = ("assignment", "weaponEntry", "clearingEntry", "ammoEntry", "ammoExit", "clearingExit", "weaponExit")
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPONENTRY_FIELD_NUMBER: _ClassVar[int]
    CLEARINGENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOENTRY_FIELD_NUMBER: _ClassVar[int]
    AMMOEXIT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGEXIT_FIELD_NUMBER: _ClassVar[int]
    WEAPONEXIT_FIELD_NUMBER: _ClassVar[int]
    assignment: _message_pb2.IdMessage
    weaponEntry: WeaponInfoCreateRequest
    clearingEntry: CommonInfoCreateRequest
    ammoEntry: AmmoInfoCreateRequest
    ammoExit: AmmoInfoCreateRequest
    clearingExit: CommonInfoCreateRequest
    weaponExit: WeaponInfoCreateRequest
    def __init__(self, assignment: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponEntry: _Optional[_Union[WeaponInfoCreateRequest, _Mapping]] = ..., clearingEntry: _Optional[_Union[CommonInfoCreateRequest, _Mapping]] = ..., ammoEntry: _Optional[_Union[AmmoInfoCreateRequest, _Mapping]] = ..., ammoExit: _Optional[_Union[AmmoInfoCreateRequest, _Mapping]] = ..., clearingExit: _Optional[_Union[CommonInfoCreateRequest, _Mapping]] = ..., weaponExit: _Optional[_Union[WeaponInfoCreateRequest, _Mapping]] = ...) -> None: ...

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
    weaponEntry: WeaponInfoReadResponse
    clearingEntry: CommonInfoReadResponse
    ammoEntry: AmmoInfoReadResponse
    ammoExit: AmmoInfoReadResponse
    clearingExit: CommonInfoReadResponse
    weaponExit: WeaponInfoReadResponse
    isActive: bool
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsReadResponseAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[WeaponInfoReadResponse, _Mapping]] = ..., clearingEntry: _Optional[_Union[CommonInfoReadResponse, _Mapping]] = ..., ammoEntry: _Optional[_Union[AmmoInfoReadResponse, _Mapping]] = ..., ammoExit: _Optional[_Union[AmmoInfoReadResponse, _Mapping]] = ..., clearingExit: _Optional[_Union[CommonInfoReadResponse, _Mapping]] = ..., weaponExit: _Optional[_Union[WeaponInfoReadResponse, _Mapping]] = ..., isActive: bool = ...) -> None: ...

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
    assignment: _message_pb2.IdMessage
    weaponEntry: WeaponInfoCreateRequest
    clearingEntry: CommonInfoCreateRequest
    ammoEntry: AmmoInfoCreateRequest
    ammoExit: AmmoInfoCreateRequest
    clearingExit: CommonInfoCreateRequest
    weaponExit: WeaponInfoCreateRequest
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponEntry: _Optional[_Union[WeaponInfoCreateRequest, _Mapping]] = ..., clearingEntry: _Optional[_Union[CommonInfoCreateRequest, _Mapping]] = ..., ammoEntry: _Optional[_Union[AmmoInfoCreateRequest, _Mapping]] = ..., ammoExit: _Optional[_Union[AmmoInfoCreateRequest, _Mapping]] = ..., clearingExit: _Optional[_Union[CommonInfoCreateRequest, _Mapping]] = ..., weaponExit: _Optional[_Union[WeaponInfoCreateRequest, _Mapping]] = ...) -> None: ...

class FlowsUpdateReadResponse(_message.Message):
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
    assignment: FlowsUpdateReadResponseAssignment
    weaponEntry: WeaponInfoReadResponse
    clearingEntry: CommonInfoReadResponse
    ammoEntry: AmmoInfoReadResponse
    ammoExit: AmmoInfoReadResponse
    clearingExit: CommonInfoReadResponse
    weaponExit: WeaponInfoReadResponse
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsUpdateReadResponseAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[WeaponInfoReadResponse, _Mapping]] = ..., clearingEntry: _Optional[_Union[CommonInfoReadResponse, _Mapping]] = ..., ammoEntry: _Optional[_Union[AmmoInfoReadResponse, _Mapping]] = ..., ammoExit: _Optional[_Union[AmmoInfoReadResponse, _Mapping]] = ..., clearingExit: _Optional[_Union[CommonInfoReadResponse, _Mapping]] = ..., weaponExit: _Optional[_Union[WeaponInfoReadResponse, _Mapping]] = ...) -> None: ...

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

class FlowsOnScanRequest(_message.Message):
    __slots__ = ("biometricsId", "position")
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    biometricsId: int
    position: Position
    def __init__(self, biometricsId: _Optional[int] = ..., position: _Optional[_Union[Position, str]] = ...) -> None: ...

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

class AlertsCreateRequest(_message.Message):
    __slots__ = ("employee", "alertsType", "time", "remarks")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTSTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    employee: _message_pb2.IdMessage
    alertsType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, employee: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., alertsType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertsReadResponse(_message.Message):
    __slots__ = ("id", "employee", "alertsType", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTSTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AlertsReadResponseEmployee
    alertsType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertsReadResponseEmployee, _Mapping]] = ..., alertsType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AlertsFilters
    search: str
    sort: AlertsSort
    cursor: AlertsCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AlertsFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AlertsSort, str]] = ..., cursor: _Optional[_Union[AlertsCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AlertsListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Alerts]
    cursor: AlertsCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Alerts, _Mapping]]] = ..., cursor: _Optional[_Union[AlertsCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

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

class UserUpdateReadResponse(_message.Message):
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

class AccessControlCreateRequest(_message.Message):
    __slots__ = ("name", "active", "expiry", "auths", "perms", "scopes", "resourceGroups")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    AUTHS_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEGROUPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    active: bool
    expiry: _timestamp_pb2.Timestamp
    auths: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    resourceGroups: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, name: _Optional[str] = ..., active: bool = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auths: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ..., resourceGroups: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

class AccessControlReadResponse(_message.Message):
    __slots__ = ("id", "name", "active", "expiry", "auths", "perms", "scopes", "resourceGroups")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    AUTHS_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEGROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    active: bool
    expiry: _timestamp_pb2.Timestamp
    auths: _containers.RepeatedCompositeFieldContainer[AccessControlReadResponseAuths]
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    resourceGroups: _containers.RepeatedCompositeFieldContainer[AccessControlReadResponseResourceGroups]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auths: _Optional[_Iterable[_Union[AccessControlReadResponseAuths, _Mapping]]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ..., resourceGroups: _Optional[_Iterable[_Union[AccessControlReadResponseResourceGroups, _Mapping]]] = ...) -> None: ...

class AccessControlUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "active", "expiry", "auths", "perms", "scopes", "resourceGroups")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    AUTHS_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEGROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    active: bool
    expiry: _timestamp_pb2.Timestamp
    auths: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    resourceGroups: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auths: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ..., resourceGroups: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

class AccessControlUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "active", "expiry", "auths", "perms", "scopes", "resourceGroups")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    AUTHS_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEGROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    active: bool
    expiry: _timestamp_pb2.Timestamp
    auths: _containers.RepeatedCompositeFieldContainer[AccessControlUpdateReadResponseAuths]
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    resourceGroups: _containers.RepeatedCompositeFieldContainer[AccessControlUpdateReadResponseResourceGroups]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auths: _Optional[_Iterable[_Union[AccessControlUpdateReadResponseAuths, _Mapping]]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ..., resourceGroups: _Optional[_Iterable[_Union[AccessControlUpdateReadResponseResourceGroups, _Mapping]]] = ...) -> None: ...

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

class ResourceGroupCreateRequest(_message.Message):
    __slots__ = ("name", "allEmployee", "employee", "allDutyPost", "dutyPost", "allWeapon", "weapon", "allAmmo", "ammo", "allOtherItems", "otherItems", "allSchedule", "schedule", "allGlobalConfig", "globalConfig", "allFlows", "allAlerts", "alerts", "allUser", "user", "allTags", "tags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOST_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    ALLAMMO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALLUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ALLTAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    allEmployee: bool
    employee: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allDutyPost: bool
    dutyPost: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allWeapon: bool
    weapon: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allAmmo: bool
    ammo: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allOtherItems: bool
    otherItems: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allSchedule: bool
    schedule: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allGlobalConfig: bool
    globalConfig: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allFlows: bool
    allAlerts: bool
    alerts: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allUser: bool
    user: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allTags: bool
    tags: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, name: _Optional[str] = ..., allEmployee: bool = ..., employee: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allDutyPost: bool = ..., dutyPost: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allWeapon: bool = ..., weapon: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allAmmo: bool = ..., ammo: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allOtherItems: bool = ..., otherItems: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allSchedule: bool = ..., schedule: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allGlobalConfig: bool = ..., globalConfig: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allFlows: bool = ..., allAlerts: bool = ..., alerts: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allUser: bool = ..., user: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allTags: bool = ..., tags: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

class ResourceGroupReadResponse(_message.Message):
    __slots__ = ("id", "name", "allEmployee", "employee", "allDutyPost", "dutyPost", "allWeapon", "weapon", "allAmmo", "ammo", "allOtherItems", "otherItems", "allSchedule", "schedule", "allGlobalConfig", "globalConfig", "allFlows", "allAlerts", "alerts", "allUser", "user", "allTags", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOST_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    ALLAMMO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALLUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ALLTAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    allEmployee: bool
    employee: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseEmployee]
    allDutyPost: bool
    dutyPost: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseDutyPost]
    allWeapon: bool
    weapon: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseWeapon]
    allAmmo: bool
    ammo: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseAmmo]
    allOtherItems: bool
    otherItems: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseOtherItems]
    allSchedule: bool
    schedule: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseSchedule]
    allGlobalConfig: bool
    globalConfig: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseGlobalConfig]
    allFlows: bool
    allAlerts: bool
    alerts: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseAlerts]
    allUser: bool
    user: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseUser]
    allTags: bool
    tags: _containers.RepeatedCompositeFieldContainer[ResourceGroupReadResponseTags]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., allEmployee: bool = ..., employee: _Optional[_Iterable[_Union[ResourceGroupReadResponseEmployee, _Mapping]]] = ..., allDutyPost: bool = ..., dutyPost: _Optional[_Iterable[_Union[ResourceGroupReadResponseDutyPost, _Mapping]]] = ..., allWeapon: bool = ..., weapon: _Optional[_Iterable[_Union[ResourceGroupReadResponseWeapon, _Mapping]]] = ..., allAmmo: bool = ..., ammo: _Optional[_Iterable[_Union[ResourceGroupReadResponseAmmo, _Mapping]]] = ..., allOtherItems: bool = ..., otherItems: _Optional[_Iterable[_Union[ResourceGroupReadResponseOtherItems, _Mapping]]] = ..., allSchedule: bool = ..., schedule: _Optional[_Iterable[_Union[ResourceGroupReadResponseSchedule, _Mapping]]] = ..., allGlobalConfig: bool = ..., globalConfig: _Optional[_Iterable[_Union[ResourceGroupReadResponseGlobalConfig, _Mapping]]] = ..., allFlows: bool = ..., allAlerts: bool = ..., alerts: _Optional[_Iterable[_Union[ResourceGroupReadResponseAlerts, _Mapping]]] = ..., allUser: bool = ..., user: _Optional[_Iterable[_Union[ResourceGroupReadResponseUser, _Mapping]]] = ..., allTags: bool = ..., tags: _Optional[_Iterable[_Union[ResourceGroupReadResponseTags, _Mapping]]] = ...) -> None: ...

class ResourceGroupUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "allEmployee", "employee", "allDutyPost", "dutyPost", "allWeapon", "weapon", "allAmmo", "ammo", "allOtherItems", "otherItems", "allSchedule", "schedule", "allGlobalConfig", "globalConfig", "allFlows", "allAlerts", "alerts", "allUser", "user", "allTags", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOST_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    ALLAMMO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALLUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ALLTAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    allEmployee: bool
    employee: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allDutyPost: bool
    dutyPost: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allWeapon: bool
    weapon: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allAmmo: bool
    ammo: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allOtherItems: bool
    otherItems: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allSchedule: bool
    schedule: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allGlobalConfig: bool
    globalConfig: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allFlows: bool
    allAlerts: bool
    alerts: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allUser: bool
    user: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    allTags: bool
    tags: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., allEmployee: bool = ..., employee: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allDutyPost: bool = ..., dutyPost: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allWeapon: bool = ..., weapon: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allAmmo: bool = ..., ammo: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allOtherItems: bool = ..., otherItems: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allSchedule: bool = ..., schedule: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allGlobalConfig: bool = ..., globalConfig: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allFlows: bool = ..., allAlerts: bool = ..., alerts: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allUser: bool = ..., user: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ..., allTags: bool = ..., tags: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

class ResourceGroupUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "allEmployee", "employee", "allDutyPost", "dutyPost", "allWeapon", "weapon", "allAmmo", "ammo", "allOtherItems", "otherItems", "allSchedule", "schedule", "allGlobalConfig", "globalConfig", "allFlows", "allAlerts", "alerts", "allUser", "user", "allTags", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOST_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    ALLAMMO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALLUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ALLTAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    allEmployee: bool
    employee: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseEmployee]
    allDutyPost: bool
    dutyPost: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseDutyPost]
    allWeapon: bool
    weapon: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseWeapon]
    allAmmo: bool
    ammo: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseAmmo]
    allOtherItems: bool
    otherItems: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseOtherItems]
    allSchedule: bool
    schedule: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseSchedule]
    allGlobalConfig: bool
    globalConfig: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseGlobalConfig]
    allFlows: bool
    allAlerts: bool
    alerts: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseAlerts]
    allUser: bool
    user: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseUser]
    allTags: bool
    tags: _containers.RepeatedCompositeFieldContainer[ResourceGroupUpdateReadResponseTags]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., allEmployee: bool = ..., employee: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseEmployee, _Mapping]]] = ..., allDutyPost: bool = ..., dutyPost: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseDutyPost, _Mapping]]] = ..., allWeapon: bool = ..., weapon: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseWeapon, _Mapping]]] = ..., allAmmo: bool = ..., ammo: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseAmmo, _Mapping]]] = ..., allOtherItems: bool = ..., otherItems: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseOtherItems, _Mapping]]] = ..., allSchedule: bool = ..., schedule: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseSchedule, _Mapping]]] = ..., allGlobalConfig: bool = ..., globalConfig: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseGlobalConfig, _Mapping]]] = ..., allFlows: bool = ..., allAlerts: bool = ..., alerts: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseAlerts, _Mapping]]] = ..., allUser: bool = ..., user: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseUser, _Mapping]]] = ..., allTags: bool = ..., tags: _Optional[_Iterable[_Union[ResourceGroupUpdateReadResponseTags, _Mapping]]] = ...) -> None: ...

class ResourceGroupListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: ResourceGroupFilters
    search: str
    sort: ResourceGroupSort
    cursor: ResourceGroupCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[ResourceGroupFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ResourceGroupSort, str]] = ..., cursor: _Optional[_Union[ResourceGroupCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class ResourceGroupListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ResourceGroup]
    cursor: ResourceGroupCursor
    def __init__(self, items: _Optional[_Iterable[_Union[ResourceGroup, _Mapping]]] = ..., cursor: _Optional[_Union[ResourceGroupCursor, _Mapping]] = ...) -> None: ...

class EmployeeReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class EmployeeUpdateReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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
    biometricsIdMin: int
    biometricsIdMax: int
    cisfIdMin: int
    cisfIdMax: int
    nameMin: str
    nameMax: str
    rankMin: str
    rankMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., biometricsIdMin: _Optional[int] = ..., biometricsIdMax: _Optional[int] = ..., cisfIdMin: _Optional[int] = ..., cisfIdMax: _Optional[int] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., rankMin: _Optional[str] = ..., rankMax: _Optional[str] = ...) -> None: ...

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
    biometricsId: int
    cisfId: int
    name: str
    rank: str
    photo: EmployeePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., cisfId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeePhoto, _Mapping]] = ...) -> None: ...

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

class WeaponAmmoCreateRequest(_message.Message):
    __slots__ = ("ammo", "count")
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ammo: _message_pb2.IdMessage
    count: int
    def __init__(self, ammo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class WeaponReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponUpdateReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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
    weaponAmmo: WeaponAmmo
    issuedCount: int
    remainingCount: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., photo: _Optional[_Union[WeaponPhoto, _Mapping]] = ..., weaponAmmo: _Optional[_Union[WeaponAmmo, _Mapping]] = ..., issuedCount: _Optional[int] = ..., remainingCount: _Optional[int] = ...) -> None: ...

class AmmoReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoUpdateReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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

class OtherItemsReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OtherItemsUpdateReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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

class AssignmentUpdateReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentUpdateReadResponseDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentUpdateReadResponseWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentUpdateReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentUpdateReadResponseOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AssignmentCreateRequest(_message.Message):
    __slots__ = ("employee", "dutyPost", "weapon", "weaponButtNo", "ammo", "ammoCount", "otherItems")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPONBUTTNO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    employee: _message_pb2.IdMessage
    dutyPost: _message_pb2.IdMessage
    weapon: _message_pb2.IdMessage
    weaponButtNo: str
    ammo: _message_pb2.IdMessage
    ammoCount: int
    otherItems: _containers.RepeatedCompositeFieldContainer[_message_pb2.IdMessage]
    def __init__(self, employee: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., dutyPost: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weapon: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., weaponButtNo: _Optional[str] = ..., ammo: _Optional[_Union[_message_pb2.IdMessage, _Mapping]] = ..., ammoCount: _Optional[int] = ..., otherItems: _Optional[_Iterable[_Union[_message_pb2.IdMessage, _Mapping]]] = ...) -> None: ...

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
    employeeCisfId: int
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
    def __init__(self, id: _Optional[str] = ..., employeeCisfId: _Optional[int] = ..., employeeRank: _Optional[str] = ..., employeeName: _Optional[str] = ..., dutyPostName: _Optional[str] = ..., weaponName: _Optional[str] = ..., flowWeaponEntryRemarks: _Optional[str] = ..., flowAmmoEntryCount: _Optional[int] = ..., flowWeaponEntryTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowAmmoEntryTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowWeaponExitTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flowAmmoExitTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class ScheduleUpdateReadResponseShiftIncharge(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleUpdateReadResponseKoteNco(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleUpdateReadResponseArmsIssueDepositSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleUpdateReadResponseArmsInspectionSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ScheduleUpdateReadResponseClearingSupervisor(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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

class WeaponAmmoReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponAmmoUpdateReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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

class WeaponInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks", "issuedButtNo")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    ISSUEDBUTTNO_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    issuedButtNo: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., issuedButtNo: _Optional[str] = ...) -> None: ...

class CommonInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AmmoInfoCreateRequest(_message.Message):
    __slots__ = ("time", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

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

class FlowsUpdateReadResponseAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

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
    weaponEntry: WeaponInfo
    clearingEntry: CommonInfo
    ammoEntry: AmmoInfo
    ammoExit: AmmoInfo
    clearingExit: CommonInfo
    weaponExit: WeaponInfo
    isActive: bool
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[WeaponInfo, _Mapping]] = ..., clearingEntry: _Optional[_Union[CommonInfo, _Mapping]] = ..., ammoEntry: _Optional[_Union[AmmoInfo, _Mapping]] = ..., ammoExit: _Optional[_Union[AmmoInfo, _Mapping]] = ..., clearingExit: _Optional[_Union[CommonInfo, _Mapping]] = ..., weaponExit: _Optional[_Union[WeaponInfo, _Mapping]] = ..., isActive: bool = ...) -> None: ...

class AlertsReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AlertsFilters(_message.Message):
    __slots__ = ("idIn", "alertsTypeIn", "timeMin", "timeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ALERTSTYPEIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    alertsTypeIn: _containers.RepeatedScalarFieldContainer[AlertType]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., alertsTypeIn: _Optional[_Iterable[_Union[AlertType, str]]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AlertsCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AlertsFilters
    sort: AlertsSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AlertsFilters, _Mapping]] = ..., sort: _Optional[_Union[AlertsSort, str]] = ...) -> None: ...

class Alerts(_message.Message):
    __slots__ = ("id", "employee", "alertsType", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTSTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AlertsEmployee
    alertsType: AlertType
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertsEmployee, _Mapping]] = ..., alertsType: _Optional[_Union[AlertType, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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

class AccessControlReadResponseAuths(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

class AccessControlReadResponseResourceGroups(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AccessControlUpdateReadResponseAuths(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

class AccessControlUpdateReadResponseResourceGroups(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AccessControlFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax", "activeEq", "authsIn", "permsIn", "scopesIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    ACTIVEEQ_FIELD_NUMBER: _ClassVar[int]
    AUTHSIN_FIELD_NUMBER: _ClassVar[int]
    PERMSIN_FIELD_NUMBER: _ClassVar[int]
    SCOPESIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    activeEq: bool
    authsIn: _containers.RepeatedScalarFieldContainer[str]
    permsIn: _containers.RepeatedScalarFieldContainer[Perm]
    scopesIn: _containers.RepeatedScalarFieldContainer[Scopes]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., activeEq: bool = ..., authsIn: _Optional[_Iterable[str]] = ..., permsIn: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopesIn: _Optional[_Iterable[_Union[Scopes, str]]] = ...) -> None: ...

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
    __slots__ = ("id", "name", "active", "expiry", "auths", "perms", "scopes", "resourceGroups")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    AUTHS_FIELD_NUMBER: _ClassVar[int]
    PERMS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEGROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    active: bool
    expiry: _timestamp_pb2.Timestamp
    auths: _containers.RepeatedCompositeFieldContainer[AccessControlAuths]
    perms: _containers.RepeatedScalarFieldContainer[Perm]
    scopes: _containers.RepeatedScalarFieldContainer[Scopes]
    resourceGroups: _containers.RepeatedCompositeFieldContainer[AccessControlResourceGroups]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auths: _Optional[_Iterable[_Union[AccessControlAuths, _Mapping]]] = ..., perms: _Optional[_Iterable[_Union[Perm, str]]] = ..., scopes: _Optional[_Iterable[_Union[Scopes, str]]] = ..., resourceGroups: _Optional[_Iterable[_Union[AccessControlResourceGroups, _Mapping]]] = ...) -> None: ...

class ResourceGroupReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseSchedule(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseGlobalConfig(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseAlerts(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseUser(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupReadResponseTags(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseSchedule(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseGlobalConfig(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseAlerts(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseUser(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupUpdateReadResponseTags(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax", "allEmployeeEq", "allDutyPostEq", "allWeaponEq", "allAmmoEq", "allOtherItemsEq", "allScheduleEq", "allGlobalConfigEq", "allFlowsEq", "allAlertsEq", "allUserEq", "allTagsEq")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEEEQ_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOSTEQ_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPONEQ_FIELD_NUMBER: _ClassVar[int]
    ALLAMMOEQ_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMSEQ_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULEEQ_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIGEQ_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWSEQ_FIELD_NUMBER: _ClassVar[int]
    ALLALERTSEQ_FIELD_NUMBER: _ClassVar[int]
    ALLUSEREQ_FIELD_NUMBER: _ClassVar[int]
    ALLTAGSEQ_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    allEmployeeEq: bool
    allDutyPostEq: bool
    allWeaponEq: bool
    allAmmoEq: bool
    allOtherItemsEq: bool
    allScheduleEq: bool
    allGlobalConfigEq: bool
    allFlowsEq: bool
    allAlertsEq: bool
    allUserEq: bool
    allTagsEq: bool
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., allEmployeeEq: bool = ..., allDutyPostEq: bool = ..., allWeaponEq: bool = ..., allAmmoEq: bool = ..., allOtherItemsEq: bool = ..., allScheduleEq: bool = ..., allGlobalConfigEq: bool = ..., allFlowsEq: bool = ..., allAlertsEq: bool = ..., allUserEq: bool = ..., allTagsEq: bool = ...) -> None: ...

class ResourceGroupCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: ResourceGroupFilters
    sort: ResourceGroupSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[ResourceGroupFilters, _Mapping]] = ..., sort: _Optional[_Union[ResourceGroupSort, str]] = ...) -> None: ...

class ResourceGroup(_message.Message):
    __slots__ = ("id", "name", "allEmployee", "employee", "allDutyPost", "dutyPost", "allWeapon", "weapon", "allAmmo", "ammo", "allOtherItems", "otherItems", "allSchedule", "schedule", "allGlobalConfig", "globalConfig", "allFlows", "allAlerts", "alerts", "allUser", "user", "allTags", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALLDUTYPOST_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    ALLWEAPON_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    ALLAMMO_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    ALLOTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    OTHERITEMS_FIELD_NUMBER: _ClassVar[int]
    ALLSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ALLGLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLFLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALLUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ALLTAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    allEmployee: bool
    employee: _containers.RepeatedCompositeFieldContainer[ResourceGroupEmployee]
    allDutyPost: bool
    dutyPost: _containers.RepeatedCompositeFieldContainer[ResourceGroupDutyPost]
    allWeapon: bool
    weapon: _containers.RepeatedCompositeFieldContainer[ResourceGroupWeapon]
    allAmmo: bool
    ammo: _containers.RepeatedCompositeFieldContainer[ResourceGroupAmmo]
    allOtherItems: bool
    otherItems: _containers.RepeatedCompositeFieldContainer[ResourceGroupOtherItems]
    allSchedule: bool
    schedule: _containers.RepeatedCompositeFieldContainer[ResourceGroupSchedule]
    allGlobalConfig: bool
    globalConfig: _containers.RepeatedCompositeFieldContainer[ResourceGroupGlobalConfig]
    allFlows: bool
    allAlerts: bool
    alerts: _containers.RepeatedCompositeFieldContainer[ResourceGroupAlerts]
    allUser: bool
    user: _containers.RepeatedCompositeFieldContainer[ResourceGroupUser]
    allTags: bool
    tags: _containers.RepeatedCompositeFieldContainer[ResourceGroupTags]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., allEmployee: bool = ..., employee: _Optional[_Iterable[_Union[ResourceGroupEmployee, _Mapping]]] = ..., allDutyPost: bool = ..., dutyPost: _Optional[_Iterable[_Union[ResourceGroupDutyPost, _Mapping]]] = ..., allWeapon: bool = ..., weapon: _Optional[_Iterable[_Union[ResourceGroupWeapon, _Mapping]]] = ..., allAmmo: bool = ..., ammo: _Optional[_Iterable[_Union[ResourceGroupAmmo, _Mapping]]] = ..., allOtherItems: bool = ..., otherItems: _Optional[_Iterable[_Union[ResourceGroupOtherItems, _Mapping]]] = ..., allSchedule: bool = ..., schedule: _Optional[_Iterable[_Union[ResourceGroupSchedule, _Mapping]]] = ..., allGlobalConfig: bool = ..., globalConfig: _Optional[_Iterable[_Union[ResourceGroupGlobalConfig, _Mapping]]] = ..., allFlows: bool = ..., allAlerts: bool = ..., alerts: _Optional[_Iterable[_Union[ResourceGroupAlerts, _Mapping]]] = ..., allUser: bool = ..., user: _Optional[_Iterable[_Union[ResourceGroupUser, _Mapping]]] = ..., allTags: bool = ..., tags: _Optional[_Iterable[_Union[ResourceGroupTags, _Mapping]]] = ...) -> None: ...

class EmployeePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponPhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponAmmo(_message.Message):
    __slots__ = ("id", "ammo", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ammo: WeaponAmmoAmmo
    count: int
    def __init__(self, id: _Optional[str] = ..., ammo: _Optional[_Union[WeaponAmmoAmmo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

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

class WeaponInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CommonInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoInfoReadResponseAcknowledgedBy(_message.Message):
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

class AlertsEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AccessControlAuths(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

class AccessControlResourceGroups(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupEmployee(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupDutyPost(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupWeapon(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupAmmo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupOtherItems(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupSchedule(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupGlobalConfig(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupAlerts(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGroupUser(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ResourceGroupTags(_message.Message):
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

class WeaponInfoAcknowledgedBy(_message.Message):
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

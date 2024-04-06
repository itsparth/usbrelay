from google.protobuf import timestamp_pb2 as _timestamp_pb2
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
    employeeSort_nameAsc: _ClassVar[EmployeeSort]
    employeeSort_nameDesc: _ClassVar[EmployeeSort]
    employeeSort_rankAsc: _ClassVar[EmployeeSort]
    employeeSort_rankDesc: _ClassVar[EmployeeSort]

class WeaponSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    weaponSort_unspecified: _ClassVar[WeaponSort]
    weaponSort_nameAsc: _ClassVar[WeaponSort]
    weaponSort_nameDesc: _ClassVar[WeaponSort]

class AmmoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoSort_unspecified: _ClassVar[AmmoSort]
    ammoSort_nameAsc: _ClassVar[AmmoSort]
    ammoSort_nameDesc: _ClassVar[AmmoSort]

class AssignmentSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    assignmentSort_unspecified: _ClassVar[AssignmentSort]
    assignmentSort_dutyPostAsc: _ClassVar[AssignmentSort]
    assignmentSort_dutyPostDesc: _ClassVar[AssignmentSort]
    assignmentSort_ammoCountAsc: _ClassVar[AssignmentSort]
    assignmentSort_ammoCountDesc: _ClassVar[AssignmentSort]

class ScheduleSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    scheduleSort_unspecified: _ClassVar[ScheduleSort]
    scheduleSort_startTimeAsc: _ClassVar[ScheduleSort]
    scheduleSort_startTimeDesc: _ClassVar[ScheduleSort]
    scheduleSort_endTimeAsc: _ClassVar[ScheduleSort]
    scheduleSort_endTimeDesc: _ClassVar[ScheduleSort]

class CommonInfoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    commonInfoSort_unspecified: _ClassVar[CommonInfoSort]
    commonInfoSort_timeAsc: _ClassVar[CommonInfoSort]
    commonInfoSort_timeDesc: _ClassVar[CommonInfoSort]

class AmmoInfoSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ammoInfoSort_unspecified: _ClassVar[AmmoInfoSort]
    ammoInfoSort_timeAsc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_timeDesc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_countAsc: _ClassVar[AmmoInfoSort]
    ammoInfoSort_countDesc: _ClassVar[AmmoInfoSort]

class FlowsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    flowsSort_unspecified: _ClassVar[FlowsSort]

class Position(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Position_unspecified: _ClassVar[Position]
    Position_weapon: _ClassVar[Position]
    Position_clearing: _ClassVar[Position]
    Position_ammo: _ClassVar[Position]

class AlertSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertSort_unspecified: _ClassVar[AlertSort]
    alertSort_alertTypeAsc: _ClassVar[AlertSort]
    alertSort_alertTypeDesc: _ClassVar[AlertSort]
    alertSort_timeAsc: _ClassVar[AlertSort]
    alertSort_timeDesc: _ClassVar[AlertSort]

class FileObjectSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    fileObjectSort_unspecified: _ClassVar[FileObjectSort]
    fileObjectSort_nameAsc: _ClassVar[FileObjectSort]
    fileObjectSort_nameDesc: _ClassVar[FileObjectSort]
employeeSort_unspecified: EmployeeSort
employeeSort_biometricsIdAsc: EmployeeSort
employeeSort_biometricsIdDesc: EmployeeSort
employeeSort_nameAsc: EmployeeSort
employeeSort_nameDesc: EmployeeSort
employeeSort_rankAsc: EmployeeSort
employeeSort_rankDesc: EmployeeSort
weaponSort_unspecified: WeaponSort
weaponSort_nameAsc: WeaponSort
weaponSort_nameDesc: WeaponSort
ammoSort_unspecified: AmmoSort
ammoSort_nameAsc: AmmoSort
ammoSort_nameDesc: AmmoSort
assignmentSort_unspecified: AssignmentSort
assignmentSort_dutyPostAsc: AssignmentSort
assignmentSort_dutyPostDesc: AssignmentSort
assignmentSort_ammoCountAsc: AssignmentSort
assignmentSort_ammoCountDesc: AssignmentSort
scheduleSort_unspecified: ScheduleSort
scheduleSort_startTimeAsc: ScheduleSort
scheduleSort_startTimeDesc: ScheduleSort
scheduleSort_endTimeAsc: ScheduleSort
scheduleSort_endTimeDesc: ScheduleSort
commonInfoSort_unspecified: CommonInfoSort
commonInfoSort_timeAsc: CommonInfoSort
commonInfoSort_timeDesc: CommonInfoSort
ammoInfoSort_unspecified: AmmoInfoSort
ammoInfoSort_timeAsc: AmmoInfoSort
ammoInfoSort_timeDesc: AmmoInfoSort
ammoInfoSort_countAsc: AmmoInfoSort
ammoInfoSort_countDesc: AmmoInfoSort
flowsSort_unspecified: FlowsSort
Position_unspecified: Position
Position_weapon: Position
Position_clearing: Position
Position_ammo: Position
alertSort_unspecified: AlertSort
alertSort_alertTypeAsc: AlertSort
alertSort_alertTypeDesc: AlertSort
alertSort_timeAsc: AlertSort
alertSort_timeDesc: AlertSort
fileObjectSort_unspecified: FileObjectSort
fileObjectSort_nameAsc: FileObjectSort
fileObjectSort_nameDesc: FileObjectSort

class EmployeeCreateRequest(_message.Message):
    __slots__ = ("biometricsId", "name", "rank", "photo")
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    biometricsId: int
    name: str
    rank: str
    photo: EmployeeCreateRequestPhoto
    def __init__(self, biometricsId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class IdMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmployeeReadResponse(_message.Message):
    __slots__ = ("id", "biometricsId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    name: str
    rank: str
    photo: EmployeeReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeReadResponsePhoto, _Mapping]] = ...) -> None: ...

class EmployeeUpdateRequest(_message.Message):
    __slots__ = ("id", "biometricsId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    name: str
    rank: str
    photo: EmployeeUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeeUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

class OkMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Employee]
    cursor: EmployeeCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Employee, _Mapping]]] = ..., cursor: _Optional[_Union[EmployeeCursor, _Mapping]] = ...) -> None: ...

class WeaponCreateRequest(_message.Message):
    __slots__ = ("name", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    photo: WeaponCreateRequestPhoto
    def __init__(self, name: _Optional[str] = ..., photo: _Optional[_Union[WeaponCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class WeaponReadResponse(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: WeaponReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[WeaponReadResponsePhoto, _Mapping]] = ...) -> None: ...

class WeaponUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: WeaponUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[WeaponUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Weapon]
    cursor: WeaponCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Weapon, _Mapping]]] = ..., cursor: _Optional[_Union[WeaponCursor, _Mapping]] = ...) -> None: ...

class AmmoCreateRequest(_message.Message):
    __slots__ = ("name", "photo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    name: str
    photo: AmmoCreateRequestPhoto
    def __init__(self, name: _Optional[str] = ..., photo: _Optional[_Union[AmmoCreateRequestPhoto, _Mapping]] = ...) -> None: ...

class AmmoReadResponse(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: AmmoReadResponsePhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[AmmoReadResponsePhoto, _Mapping]] = ...) -> None: ...

class AmmoUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: AmmoUpdateRequestPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[AmmoUpdateRequestPhoto, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Ammo]
    cursor: AmmoCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Ammo, _Mapping]]] = ..., cursor: _Optional[_Union[AmmoCursor, _Mapping]] = ...) -> None: ...

class AssignmentCreateRequest(_message.Message):
    __slots__ = ("employee", "weapon", "ammo", "dutyPost", "ammoCount")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    employee: AssignmentCreateRequestEmployee
    weapon: AssignmentCreateRequestWeapon
    ammo: AssignmentCreateRequestAmmo
    dutyPost: str
    ammoCount: int
    def __init__(self, employee: _Optional[_Union[AssignmentCreateRequestEmployee, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentCreateRequestWeapon, _Mapping]] = ..., ammo: _Optional[_Union[AssignmentCreateRequestAmmo, _Mapping]] = ..., dutyPost: _Optional[str] = ..., ammoCount: _Optional[int] = ...) -> None: ...

class AssignmentReadResponse(_message.Message):
    __slots__ = ("id", "employee", "weapon", "ammo", "dutyPost", "ammoCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentReadResponseEmployee
    weapon: AssignmentReadResponseWeapon
    ammo: AssignmentReadResponseAmmo
    dutyPost: str
    ammoCount: int
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentReadResponseEmployee, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentReadResponseWeapon, _Mapping]] = ..., ammo: _Optional[_Union[AssignmentReadResponseAmmo, _Mapping]] = ..., dutyPost: _Optional[str] = ..., ammoCount: _Optional[int] = ...) -> None: ...

class AssignmentUpdateRequest(_message.Message):
    __slots__ = ("id", "employee", "weapon", "ammo", "dutyPost", "ammoCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentUpdateRequestEmployee
    weapon: AssignmentUpdateRequestWeapon
    ammo: AssignmentUpdateRequestAmmo
    dutyPost: str
    ammoCount: int
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentUpdateRequestEmployee, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentUpdateRequestWeapon, _Mapping]] = ..., ammo: _Optional[_Union[AssignmentUpdateRequestAmmo, _Mapping]] = ..., dutyPost: _Optional[str] = ..., ammoCount: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Assignment]
    cursor: AssignmentCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Assignment, _Mapping]]] = ..., cursor: _Optional[_Union[AssignmentCursor, _Mapping]] = ...) -> None: ...

class ScheduleCreateRequest(_message.Message):
    __slots__ = ("startTime", "endTime")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    def __init__(self, startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleReadResponse(_message.Message):
    __slots__ = ("id", "startTime", "endTime", "assignments")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    assignments: _containers.RepeatedCompositeFieldContainer[ScheduleReadResponseAssignments]
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignments: _Optional[_Iterable[_Union[ScheduleReadResponseAssignments, _Mapping]]] = ...) -> None: ...

class ScheduleUpdateRequest(_message.Message):
    __slots__ = ("id", "startTime", "endTime")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class CommonInfoCreateRequest(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: CommonInfoCreateRequestAcknowledgedBy
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[CommonInfoCreateRequestAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: CommonInfoUpdateRequestAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[CommonInfoUpdateRequestAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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

class AmmoInfoCreateRequest(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: AmmoInfoCreateRequestAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[AmmoInfoCreateRequestAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: AmmoInfoUpdateRequestAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[AmmoInfoUpdateRequestAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

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
    assignment: FlowsReadResponseAssignment
    weaponEntry: FlowsReadResponseWeaponEntry
    clearingEntry: FlowsReadResponseClearingEntry
    ammoEntry: FlowsReadResponseAmmoEntry
    ammoExit: FlowsReadResponseAmmoExit
    clearingExit: FlowsReadResponseClearingExit
    weaponExit: FlowsReadResponseWeaponExit
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsReadResponseAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsReadResponseWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsReadResponseClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsReadResponseAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsReadResponseAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsReadResponseClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsReadResponseWeaponExit, _Mapping]] = ...) -> None: ...

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

class AlertCreateRequest(_message.Message):
    __slots__ = ("employee", "alertType", "time", "remarks")
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    employee: AlertCreateRequestEmployee
    alertType: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, employee: _Optional[_Union[AlertCreateRequestEmployee, _Mapping]] = ..., alertType: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertReadResponse(_message.Message):
    __slots__ = ("id", "employee", "alertType", "time", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AlertReadResponseEmployee
    alertType: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertReadResponseEmployee, _Mapping]] = ..., alertType: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Alert]
    cursor: AlertCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Alert, _Mapping]]] = ..., cursor: _Optional[_Union[AlertCursor, _Mapping]] = ...) -> None: ...

class SignInRequest(_message.Message):
    __slots__ = ("authName", "password")
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    authName: str
    password: str
    def __init__(self, authName: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SignInResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class FileObjectCreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FileObjectReadResponse(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FileObjectUpdateRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FileObjectListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FileObjectFilters
    search: str
    sort: FileObjectSort
    cursor: FileObjectCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FileObjectFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FileObjectSort, str]] = ..., cursor: _Optional[_Union[FileObjectCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FileObjectListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FileObject]
    cursor: FileObjectCursor
    def __init__(self, items: _Optional[_Iterable[_Union[FileObject, _Mapping]]] = ..., cursor: _Optional[_Union[FileObjectCursor, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("idIn", "biometricsIdMin", "biometricsIdMax", "nameMin", "nameMax", "rankMin", "rankMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMIN_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSIDMAX_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    RANKMIN_FIELD_NUMBER: _ClassVar[int]
    RANKMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    biometricsIdMin: int
    biometricsIdMax: int
    nameMin: str
    nameMax: str
    rankMin: str
    rankMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., biometricsIdMin: _Optional[int] = ..., biometricsIdMax: _Optional[int] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ..., rankMin: _Optional[str] = ..., rankMax: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "biometricsId", "name", "rank", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICSID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    biometricsId: int
    name: str
    rank: str
    photo: EmployeePhoto
    def __init__(self, id: _Optional[str] = ..., biometricsId: _Optional[int] = ..., name: _Optional[str] = ..., rank: _Optional[str] = ..., photo: _Optional[_Union[EmployeePhoto, _Mapping]] = ...) -> None: ...

class WeaponCreateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponReadResponsePhoto(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WeaponUpdateRequestPhoto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WeaponFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: WeaponPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[WeaponPhoto, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("idIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: AmmoPhoto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[AmmoPhoto, _Mapping]] = ...) -> None: ...

class AssignmentCreateRequestEmployee(_message.Message):
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

class AssignmentReadResponseEmployee(_message.Message):
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

class AssignmentUpdateRequestEmployee(_message.Message):
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

class AssignmentFilters(_message.Message):
    __slots__ = ("idIn", "employeeIn", "weaponIn", "ammoIn", "dutyPostMin", "dutyPostMax", "ammoCountMin", "ammoCountMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEEIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONIN_FIELD_NUMBER: _ClassVar[int]
    AMMOIN_FIELD_NUMBER: _ClassVar[int]
    DUTYPOSTMIN_FIELD_NUMBER: _ClassVar[int]
    DUTYPOSTMAX_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNTMIN_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    employeeIn: _containers.RepeatedScalarFieldContainer[str]
    weaponIn: _containers.RepeatedScalarFieldContainer[str]
    ammoIn: _containers.RepeatedScalarFieldContainer[str]
    dutyPostMin: str
    dutyPostMax: str
    ammoCountMin: int
    ammoCountMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., employeeIn: _Optional[_Iterable[str]] = ..., weaponIn: _Optional[_Iterable[str]] = ..., ammoIn: _Optional[_Iterable[str]] = ..., dutyPostMin: _Optional[str] = ..., dutyPostMax: _Optional[str] = ..., ammoCountMin: _Optional[int] = ..., ammoCountMax: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("id", "employee", "weapon", "ammo", "dutyPost", "ammoCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: AssignmentEmployee
    weapon: AssignmentWeapon
    ammo: AssignmentAmmo
    dutyPost: str
    ammoCount: int
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AssignmentEmployee, _Mapping]] = ..., weapon: _Optional[_Union[AssignmentWeapon, _Mapping]] = ..., ammo: _Optional[_Union[AssignmentAmmo, _Mapping]] = ..., dutyPost: _Optional[str] = ..., ammoCount: _Optional[int] = ...) -> None: ...

class ScheduleReadResponseAssignments(_message.Message):
    __slots__ = ("id", "employee", "dutyPost")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: ScheduleReadResponseAssignmentsEmployee
    dutyPost: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[ScheduleReadResponseAssignmentsEmployee, _Mapping]] = ..., dutyPost: _Optional[str] = ...) -> None: ...

class ScheduleFilters(_message.Message):
    __slots__ = ("idIn", "startTimeMin", "startTimeMax", "endTimeMin", "endTimeMax", "assignmentsIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    STARTTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMIN_FIELD_NUMBER: _ClassVar[int]
    ENDTIMEMAX_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTSIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    startTimeMin: _timestamp_pb2.Timestamp
    startTimeMax: _timestamp_pb2.Timestamp
    endTimeMin: _timestamp_pb2.Timestamp
    endTimeMax: _timestamp_pb2.Timestamp
    assignmentsIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., startTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., startTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignmentsIn: _Optional[_Iterable[str]] = ...) -> None: ...

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
    __slots__ = ("id", "startTime", "endTime")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    startTime: _timestamp_pb2.Timestamp
    endTime: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., startTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommonInfoCreateRequestAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CommonInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CommonInfoUpdateRequestAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CommonInfoFilters(_message.Message):
    __slots__ = ("idIn", "timeMin", "timeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class AmmoInfoCreateRequestAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AmmoInfoReadResponseAcknowledgedBy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AmmoInfoUpdateRequestAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AmmoInfoFilters(_message.Message):
    __slots__ = ("idIn", "timeMin", "timeMax", "countMin", "countMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    COUNTMIN_FIELD_NUMBER: _ClassVar[int]
    COUNTMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    countMin: int
    countMax: int
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., countMin: _Optional[int] = ..., countMax: _Optional[int] = ...) -> None: ...

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

class FlowsCreateRequestAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestWeaponEntry(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestWeaponEntryAcknowledgedBy
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestClearingEntry(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestClearingEntryAcknowledgedBy
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestClearingEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestAmmoEntry(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestAmmoEntryAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestAmmoEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsCreateRequestAmmoExit(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks", "count")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestAmmoExitAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestAmmoExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsCreateRequestClearingExit(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestClearingExitAcknowledgedBy
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestClearingExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestWeaponExit(_message.Message):
    __slots__ = ("time", "acknowledgedBy", "remarks")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsCreateRequestWeaponExitAcknowledgedBy
    remarks: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsCreateRequestWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAssignment(_message.Message):
    __slots__ = ("id", "employee", "weapon", "ammo", "dutyPost", "ammoCount")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    AMMO_FIELD_NUMBER: _ClassVar[int]
    DUTYPOST_FIELD_NUMBER: _ClassVar[int]
    AMMOCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    employee: FlowsReadResponseAssignmentEmployee
    weapon: FlowsReadResponseAssignmentWeapon
    ammo: FlowsReadResponseAssignmentAmmo
    dutyPost: str
    ammoCount: int
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[FlowsReadResponseAssignmentEmployee, _Mapping]] = ..., weapon: _Optional[_Union[FlowsReadResponseAssignmentWeapon, _Mapping]] = ..., ammo: _Optional[_Union[FlowsReadResponseAssignmentAmmo, _Mapping]] = ..., dutyPost: _Optional[str] = ..., ammoCount: _Optional[int] = ...) -> None: ...

class FlowsReadResponseWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseWeaponEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsReadResponseWeaponExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsReadResponseWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestWeaponEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestClearingEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestClearingEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestClearingEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAmmoEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestAmmoEntryAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestAmmoEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsUpdateRequestAmmoExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestAmmoExitAcknowledgedBy
    remarks: str
    count: int
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestAmmoExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class FlowsUpdateRequestClearingExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestClearingExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestClearingExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestWeaponExit(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsUpdateRequestWeaponExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsUpdateRequestWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FlowsFilters(_message.Message):
    __slots__ = ("idIn", "assignmentIn")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTIN_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    assignmentIn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., assignmentIn: _Optional[_Iterable[str]] = ...) -> None: ...

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
    assignment: FlowsAssignment
    weaponEntry: FlowsWeaponEntry
    clearingEntry: FlowsClearingEntry
    ammoEntry: FlowsAmmoEntry
    ammoExit: FlowsAmmoExit
    clearingExit: FlowsClearingExit
    weaponExit: FlowsWeaponExit
    def __init__(self, id: _Optional[str] = ..., assignment: _Optional[_Union[FlowsAssignment, _Mapping]] = ..., weaponEntry: _Optional[_Union[FlowsWeaponEntry, _Mapping]] = ..., clearingEntry: _Optional[_Union[FlowsClearingEntry, _Mapping]] = ..., ammoEntry: _Optional[_Union[FlowsAmmoEntry, _Mapping]] = ..., ammoExit: _Optional[_Union[FlowsAmmoExit, _Mapping]] = ..., clearingExit: _Optional[_Union[FlowsClearingExit, _Mapping]] = ..., weaponExit: _Optional[_Union[FlowsWeaponExit, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("idIn", "employeeIn", "alertTypeMin", "alertTypeMax", "timeMin", "timeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEEIN_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPEMIN_FIELD_NUMBER: _ClassVar[int]
    ALERTTYPEMAX_FIELD_NUMBER: _ClassVar[int]
    TIMEMIN_FIELD_NUMBER: _ClassVar[int]
    TIMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    employeeIn: _containers.RepeatedScalarFieldContainer[str]
    alertTypeMin: str
    alertTypeMax: str
    timeMin: _timestamp_pb2.Timestamp
    timeMax: _timestamp_pb2.Timestamp
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., employeeIn: _Optional[_Iterable[str]] = ..., alertTypeMin: _Optional[str] = ..., alertTypeMax: _Optional[str] = ..., timeMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    alertType: str
    time: _timestamp_pb2.Timestamp
    remarks: str
    def __init__(self, id: _Optional[str] = ..., employee: _Optional[_Union[AlertEmployee, _Mapping]] = ..., alertType: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class FileObjectFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class FileObjectCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FileObjectFilters
    sort: FileObjectSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FileObjectFilters, _Mapping]] = ..., sort: _Optional[_Union[FileObjectSort, str]] = ...) -> None: ...

class FileObject(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

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

class AmmoPhoto(_message.Message):
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

class ScheduleReadResponseAssignmentsEmployee(_message.Message):
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

class FlowsCreateRequestWeaponEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestClearingEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestAmmoEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestAmmoExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestClearingExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsCreateRequestWeaponExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsReadResponseAssignmentEmployee(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[FileObject, _Mapping]] = ...) -> None: ...

class FlowsReadResponseAssignmentWeapon(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[FileObject, _Mapping]] = ...) -> None: ...

class FlowsReadResponseAssignmentAmmo(_message.Message):
    __slots__ = ("id", "name", "photo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    photo: FileObject
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[FileObject, _Mapping]] = ...) -> None: ...

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

class FlowsUpdateRequestWeaponEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestClearingEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAmmoEntryAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestAmmoExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestClearingExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsUpdateRequestWeaponExitAcknowledgedBy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsAssignment(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FlowsWeaponEntry(_message.Message):
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsWeaponEntryAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsWeaponEntryAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "time", "acknowledgedBy", "remarks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEDBY_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    acknowledgedBy: FlowsWeaponExitAcknowledgedBy
    remarks: str
    def __init__(self, id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledgedBy: _Optional[_Union[FlowsWeaponExitAcknowledgedBy, _Mapping]] = ..., remarks: _Optional[str] = ...) -> None: ...

class AlertEmployee(_message.Message):
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

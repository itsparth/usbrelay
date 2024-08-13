from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertRuleTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertRuleTrigger_unspecified: _ClassVar[AlertRuleTrigger]
    alertRuleTrigger_onConditionChange: _ClassVar[AlertRuleTrigger]
    alertRuleTrigger_onConditionMatch: _ClassVar[AlertRuleTrigger]

class TicketSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ticketSeverity_unspecified: _ClassVar[TicketSeverity]
    ticketSeverity_sev1: _ClassVar[TicketSeverity]
    ticketSeverity_sev2: _ClassVar[TicketSeverity]
    ticketSeverity_sev3: _ClassVar[TicketSeverity]
    ticketSeverity_sev4: _ClassVar[TicketSeverity]
    ticketSeverity_sev5: _ClassVar[TicketSeverity]

class TicketStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ticketStatus_unspecified: _ClassVar[TicketStatus]
    ticketStatus_open: _ClassVar[TicketStatus]
    ticketStatus_acknowledged: _ClassVar[TicketStatus]
    ticketStatus_mitigated: _ClassVar[TicketStatus]
    ticketStatus_closed: _ClassVar[TicketStatus]

class AlertNotification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    alertNotification_unspecified: _ClassVar[AlertNotification]
    alertNotification_push: _ClassVar[AlertNotification]
    alertNotification_email: _ClassVar[AlertNotification]
    alertNotification_sms: _ClassVar[AlertNotification]
    alertNotification_whatsapp: _ClassVar[AlertNotification]

class AuthSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    authSort_unspecified: _ClassVar[AuthSort]
    authSort_authNameAsc: _ClassVar[AuthSort]
    authSort_authNameDesc: _ClassVar[AuthSort]

class AuthSessionSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    authSessionSort_unspecified: _ClassVar[AuthSessionSort]
    authSessionSort_tokenHashAsc: _ClassVar[AuthSessionSort]
    authSessionSort_tokenHashDesc: _ClassVar[AuthSessionSort]

class FileObjectSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    fileObjectSort_unspecified: _ClassVar[FileObjectSort]
    fileObjectSort_nameAsc: _ClassVar[FileObjectSort]
    fileObjectSort_nameDesc: _ClassVar[FileObjectSort]

class PointSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    pointSort_unspecified: _ClassVar[PointSort]
    pointSort_lattitudeAsc: _ClassVar[PointSort]
    pointSort_lattitudeDesc: _ClassVar[PointSort]
    pointSort_longitudeAsc: _ClassVar[PointSort]
    pointSort_longitudeDesc: _ClassVar[PointSort]

class TagsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    tagsSort_unspecified: _ClassVar[TagsSort]
    tagsSort_nameAsc: _ClassVar[TagsSort]
    tagsSort_nameDesc: _ClassVar[TagsSort]
alertRuleTrigger_unspecified: AlertRuleTrigger
alertRuleTrigger_onConditionChange: AlertRuleTrigger
alertRuleTrigger_onConditionMatch: AlertRuleTrigger
ticketSeverity_unspecified: TicketSeverity
ticketSeverity_sev1: TicketSeverity
ticketSeverity_sev2: TicketSeverity
ticketSeverity_sev3: TicketSeverity
ticketSeverity_sev4: TicketSeverity
ticketSeverity_sev5: TicketSeverity
ticketStatus_unspecified: TicketStatus
ticketStatus_open: TicketStatus
ticketStatus_acknowledged: TicketStatus
ticketStatus_mitigated: TicketStatus
ticketStatus_closed: TicketStatus
alertNotification_unspecified: AlertNotification
alertNotification_push: AlertNotification
alertNotification_email: AlertNotification
alertNotification_sms: AlertNotification
alertNotification_whatsapp: AlertNotification
authSort_unspecified: AuthSort
authSort_authNameAsc: AuthSort
authSort_authNameDesc: AuthSort
authSessionSort_unspecified: AuthSessionSort
authSessionSort_tokenHashAsc: AuthSessionSort
authSessionSort_tokenHashDesc: AuthSessionSort
fileObjectSort_unspecified: FileObjectSort
fileObjectSort_nameAsc: FileObjectSort
fileObjectSort_nameDesc: FileObjectSort
pointSort_unspecified: PointSort
pointSort_lattitudeAsc: PointSort
pointSort_lattitudeDesc: PointSort
pointSort_longitudeAsc: PointSort
pointSort_longitudeDesc: PointSort
tagsSort_unspecified: TagsSort
tagsSort_nameAsc: TagsSort
tagsSort_nameDesc: TagsSort

class AuthListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AuthFilters
    search: str
    sort: AuthSort
    cursor: AuthCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AuthFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AuthSort, str]] = ..., cursor: _Optional[_Union[AuthCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AuthListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Auth]
    cursor: AuthCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Auth, _Mapping]]] = ..., cursor: _Optional[_Union[AuthCursor, _Mapping]] = ...) -> None: ...

class SignInRequest(_message.Message):
    __slots__ = ("authName", "password")
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    authName: str
    password: str
    def __init__(self, authName: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SignInResponse(_message.Message):
    __slots__ = ("authId", "token")
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    authId: str
    token: str
    def __init__(self, authId: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class OkMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChangePasswordRequest(_message.Message):
    __slots__ = ("oldPassword", "newPassword")
    OLDPASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEWPASSWORD_FIELD_NUMBER: _ClassVar[int]
    oldPassword: str
    newPassword: str
    def __init__(self, oldPassword: _Optional[str] = ..., newPassword: _Optional[str] = ...) -> None: ...

class AuthSessionListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: AuthSessionFilters
    search: str
    sort: AuthSessionSort
    cursor: AuthSessionCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[AuthSessionFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[AuthSessionSort, str]] = ..., cursor: _Optional[_Union[AuthSessionCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class AuthSessionListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuthSession]
    cursor: AuthSessionCursor
    def __init__(self, items: _Optional[_Iterable[_Union[AuthSession, _Mapping]]] = ..., cursor: _Optional[_Union[AuthSessionCursor, _Mapping]] = ...) -> None: ...

class FileObjectCreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class IdMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

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

class FileObjectUpdateReadResponse(_message.Message):
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

class PointReadResponse(_message.Message):
    __slots__ = ("id", "lattitude", "longitude")
    ID_FIELD_NUMBER: _ClassVar[int]
    LATTITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    lattitude: float
    longitude: float
    def __init__(self, id: _Optional[str] = ..., lattitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class PointUpdateRequest(_message.Message):
    __slots__ = ("id", "lattitude", "longitude")
    ID_FIELD_NUMBER: _ClassVar[int]
    LATTITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    lattitude: float
    longitude: float
    def __init__(self, id: _Optional[str] = ..., lattitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class PointUpdateReadResponse(_message.Message):
    __slots__ = ("id", "lattitude", "longitude")
    ID_FIELD_NUMBER: _ClassVar[int]
    LATTITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    lattitude: float
    longitude: float
    def __init__(self, id: _Optional[str] = ..., lattitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class PointListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: PointFilters
    search: str
    sort: PointSort
    cursor: PointCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[PointFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[PointSort, str]] = ..., cursor: _Optional[_Union[PointCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class PointListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Point]
    cursor: PointCursor
    def __init__(self, items: _Optional[_Iterable[_Union[Point, _Mapping]]] = ..., cursor: _Optional[_Union[PointCursor, _Mapping]] = ...) -> None: ...

class TagsCreateRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class TagsReadResponse(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class TagsUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class TagsUpdateReadResponse(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class TagsListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: TagsFilters
    search: str
    sort: TagsSort
    cursor: TagsCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[TagsFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[TagsSort, str]] = ..., cursor: _Optional[_Union[TagsCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class TagsListResponse(_message.Message):
    __slots__ = ("items", "cursor", "count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Tags]
    cursor: TagsCursor
    count: int
    def __init__(self, items: _Optional[_Iterable[_Union[Tags, _Mapping]]] = ..., cursor: _Optional[_Union[TagsCursor, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class IntAlertCondition(_message.Message):
    __slots__ = ("lessThan", "greaterThan", "equals")
    LESSTHAN_FIELD_NUMBER: _ClassVar[int]
    GREATERTHAN_FIELD_NUMBER: _ClassVar[int]
    EQUALS_FIELD_NUMBER: _ClassVar[int]
    lessThan: int
    greaterThan: int
    equals: int
    def __init__(self, lessThan: _Optional[int] = ..., greaterThan: _Optional[int] = ..., equals: _Optional[int] = ...) -> None: ...

class DoubleAlertCondition(_message.Message):
    __slots__ = ("lessThan", "greaterThan", "equals")
    LESSTHAN_FIELD_NUMBER: _ClassVar[int]
    GREATERTHAN_FIELD_NUMBER: _ClassVar[int]
    EQUALS_FIELD_NUMBER: _ClassVar[int]
    lessThan: float
    greaterThan: float
    equals: float
    def __init__(self, lessThan: _Optional[float] = ..., greaterThan: _Optional[float] = ..., equals: _Optional[float] = ...) -> None: ...

class AuthFilters(_message.Message):
    __slots__ = ("idIn", "authNameMin", "authNameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    authNameMin: str
    authNameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., authNameMin: _Optional[str] = ..., authNameMax: _Optional[str] = ...) -> None: ...

class AuthCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AuthFilters
    sort: AuthSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AuthFilters, _Mapping]] = ..., sort: _Optional[_Union[AuthSort, str]] = ...) -> None: ...

class Auth(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

class AuthSessionFilters(_message.Message):
    __slots__ = ("idIn", "tokenHashMin", "tokenHashMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    TOKENHASHMIN_FIELD_NUMBER: _ClassVar[int]
    TOKENHASHMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    tokenHashMin: str
    tokenHashMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., tokenHashMin: _Optional[str] = ..., tokenHashMax: _Optional[str] = ...) -> None: ...

class AuthSessionCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: AuthSessionFilters
    sort: AuthSessionSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[AuthSessionFilters, _Mapping]] = ..., sort: _Optional[_Union[AuthSessionSort, str]] = ...) -> None: ...

class AuthSession(_message.Message):
    __slots__ = ("id", "auth", "tokenHash")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    TOKENHASH_FIELD_NUMBER: _ClassVar[int]
    id: str
    auth: AuthSessionAuth
    tokenHash: str
    def __init__(self, id: _Optional[str] = ..., auth: _Optional[_Union[AuthSessionAuth, _Mapping]] = ..., tokenHash: _Optional[str] = ...) -> None: ...

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

class PointFilters(_message.Message):
    __slots__ = ("idIn", "lattitudeMin", "lattitudeMax", "longitudeMin", "longitudeMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    LATTITUDEMIN_FIELD_NUMBER: _ClassVar[int]
    LATTITUDEMAX_FIELD_NUMBER: _ClassVar[int]
    LONGITUDEMIN_FIELD_NUMBER: _ClassVar[int]
    LONGITUDEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    lattitudeMin: float
    lattitudeMax: float
    longitudeMin: float
    longitudeMax: float
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., lattitudeMin: _Optional[float] = ..., lattitudeMax: _Optional[float] = ..., longitudeMin: _Optional[float] = ..., longitudeMax: _Optional[float] = ...) -> None: ...

class PointCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: PointFilters
    sort: PointSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[PointFilters, _Mapping]] = ..., sort: _Optional[_Union[PointSort, str]] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("id", "lattitude", "longitude")
    ID_FIELD_NUMBER: _ClassVar[int]
    LATTITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    lattitude: float
    longitude: float
    def __init__(self, id: _Optional[str] = ..., lattitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class TagsFilters(_message.Message):
    __slots__ = ("idIn", "idNotIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    IDNOTIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    idNotIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., idNotIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class TagsCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: TagsFilters
    sort: TagsSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[TagsFilters, _Mapping]] = ..., sort: _Optional[_Union[TagsSort, str]] = ...) -> None: ...

class Tags(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class AuthSessionAuth(_message.Message):
    __slots__ = ("id", "authName")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    authName: str
    def __init__(self, id: _Optional[str] = ..., authName: _Optional[str] = ...) -> None: ...

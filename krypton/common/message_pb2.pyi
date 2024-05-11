from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class FileObjectActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    fileObjectActivityLogSort_unspecified: _ClassVar[FileObjectActivityLogSort]
    fileObjectActivityLogSort_activityAtAsc: _ClassVar[FileObjectActivityLogSort]
    fileObjectActivityLogSort_activityAtDesc: _ClassVar[FileObjectActivityLogSort]
    fileObjectActivityLogSort_nameAsc: _ClassVar[FileObjectActivityLogSort]
    fileObjectActivityLogSort_nameDesc: _ClassVar[FileObjectActivityLogSort]

class TagsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    tagsSort_unspecified: _ClassVar[TagsSort]
    tagsSort_nameAsc: _ClassVar[TagsSort]
    tagsSort_nameDesc: _ClassVar[TagsSort]

class TagsActivityLogSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    tagsActivityLogSort_unspecified: _ClassVar[TagsActivityLogSort]
    tagsActivityLogSort_activityAtAsc: _ClassVar[TagsActivityLogSort]
    tagsActivityLogSort_activityAtDesc: _ClassVar[TagsActivityLogSort]
    tagsActivityLogSort_nameAsc: _ClassVar[TagsActivityLogSort]
    tagsActivityLogSort_nameDesc: _ClassVar[TagsActivityLogSort]

class ActivityLogAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    activityLogAction_unspecified: _ClassVar[ActivityLogAction]
    activityLogAction_insertA: _ClassVar[ActivityLogAction]
    activityLogAction_updateA: _ClassVar[ActivityLogAction]
    activityLogAction_deleteA: _ClassVar[ActivityLogAction]
authSort_unspecified: AuthSort
authSort_authNameAsc: AuthSort
authSort_authNameDesc: AuthSort
authSessionSort_unspecified: AuthSessionSort
authSessionSort_tokenHashAsc: AuthSessionSort
authSessionSort_tokenHashDesc: AuthSessionSort
fileObjectSort_unspecified: FileObjectSort
fileObjectSort_nameAsc: FileObjectSort
fileObjectSort_nameDesc: FileObjectSort
fileObjectActivityLogSort_unspecified: FileObjectActivityLogSort
fileObjectActivityLogSort_activityAtAsc: FileObjectActivityLogSort
fileObjectActivityLogSort_activityAtDesc: FileObjectActivityLogSort
fileObjectActivityLogSort_nameAsc: FileObjectActivityLogSort
fileObjectActivityLogSort_nameDesc: FileObjectActivityLogSort
tagsSort_unspecified: TagsSort
tagsSort_nameAsc: TagsSort
tagsSort_nameDesc: TagsSort
tagsActivityLogSort_unspecified: TagsActivityLogSort
tagsActivityLogSort_activityAtAsc: TagsActivityLogSort
tagsActivityLogSort_activityAtDesc: TagsActivityLogSort
tagsActivityLogSort_nameAsc: TagsActivityLogSort
tagsActivityLogSort_nameDesc: TagsActivityLogSort
activityLogAction_unspecified: ActivityLogAction
activityLogAction_insertA: ActivityLogAction
activityLogAction_updateA: ActivityLogAction
activityLogAction_deleteA: ActivityLogAction

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

class FileObjectActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: FileObjectActivityLogFilters
    search: str
    sort: FileObjectActivityLogSort
    cursor: FileObjectActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[FileObjectActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[FileObjectActivityLogSort, str]] = ..., cursor: _Optional[_Union[FileObjectActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FileObjectActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FileObjectActivityLog]
    cursor: FileObjectActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[FileObjectActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[FileObjectActivityLogCursor, _Mapping]] = ...) -> None: ...

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

class TagsActivityLogListRequest(_message.Message):
    __slots__ = ("filters", "search", "sort", "cursor", "limit")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filters: TagsActivityLogFilters
    search: str
    sort: TagsActivityLogSort
    cursor: TagsActivityLogCursor
    limit: int
    def __init__(self, filters: _Optional[_Union[TagsActivityLogFilters, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[TagsActivityLogSort, str]] = ..., cursor: _Optional[_Union[TagsActivityLogCursor, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class TagsActivityLogListResponse(_message.Message):
    __slots__ = ("items", "cursor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TagsActivityLog]
    cursor: TagsActivityLogCursor
    def __init__(self, items: _Optional[_Iterable[_Union[TagsActivityLog, _Mapping]]] = ..., cursor: _Optional[_Union[TagsActivityLogCursor, _Mapping]] = ...) -> None: ...

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

class FileObjectActivityLogFilters(_message.Message):
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
    actionIn: _containers.RepeatedScalarFieldContainer[ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class FileObjectActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: FileObjectActivityLogFilters
    sort: FileObjectActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[FileObjectActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[FileObjectActivityLogSort, str]] = ...) -> None: ...

class FileObjectActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class TagsFilters(_message.Message):
    __slots__ = ("idIn", "nameMin", "nameMax")
    IDIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMIN_FIELD_NUMBER: _ClassVar[int]
    NAMEMAX_FIELD_NUMBER: _ClassVar[int]
    idIn: _containers.RepeatedScalarFieldContainer[str]
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

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

class TagsActivityLogFilters(_message.Message):
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
    actionIn: _containers.RepeatedScalarFieldContainer[ActivityLogAction]
    objectIdIn: _containers.RepeatedScalarFieldContainer[str]
    authIdIn: _containers.RepeatedScalarFieldContainer[str]
    activityAtMin: _timestamp_pb2.Timestamp
    activityAtMax: _timestamp_pb2.Timestamp
    nameMin: str
    nameMax: str
    def __init__(self, idIn: _Optional[_Iterable[str]] = ..., actionIn: _Optional[_Iterable[_Union[ActivityLogAction, str]]] = ..., objectIdIn: _Optional[_Iterable[str]] = ..., authIdIn: _Optional[_Iterable[str]] = ..., activityAtMin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activityAtMax: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nameMin: _Optional[str] = ..., nameMax: _Optional[str] = ...) -> None: ...

class TagsActivityLogCursor(_message.Message):
    __slots__ = ("id", "filters", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    filters: TagsActivityLogFilters
    sort: TagsActivityLogSort
    def __init__(self, id: _Optional[str] = ..., filters: _Optional[_Union[TagsActivityLogFilters, _Mapping]] = ..., sort: _Optional[_Union[TagsActivityLogSort, str]] = ...) -> None: ...

class TagsActivityLog(_message.Message):
    __slots__ = ("id", "action", "objectId", "authId", "activityAt", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: ActivityLogAction
    objectId: str
    authId: str
    activityAt: _timestamp_pb2.Timestamp
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[ActivityLogAction, str]] = ..., objectId: _Optional[str] = ..., authId: _Optional[str] = ..., activityAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class AuthSessionAuth(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

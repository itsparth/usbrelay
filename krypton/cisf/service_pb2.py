# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krypton/cisf/service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from krypton.cisf import message_pb2 as krypton_dot_cisf_dot_message__pb2
from google.api import http_pb2 as google_dot_api_dot_http__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from krypton.common import message_pb2 as krypton_dot_common_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1akrypton/cisf/service.proto\x1a\x1akrypton/cisf/message.proto\x1a\x15google/api/http.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ckrypton/common/message.proto2\x84\x04\n\x0f\x45mployeeService\x12Q\n\x0e\x65mployeeCreate\x12\x16.EmployeeCreateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/employeeCreate\x12L\n\x0c\x65mployeeRead\x12\n.IdMessage\x1a\x15.EmployeeReadResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/employeeRead\x12Q\n\x0e\x65mployeeUpdate\x12\x16.EmployeeUpdateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/employeeUpdate\x12^\n\x12\x65mployeeUpdateRead\x12\n.IdMessage\x1a\x1b.EmployeeUpdateReadResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/employeeUpdateRead\x12\x45\n\x0e\x65mployeeDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/employeeDelete\x12V\n\x0c\x65mployeeList\x12\x14.EmployeeListRequest\x1a\x15.EmployeeListResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/employeeList2\x84\x04\n\x0f\x44utyPostService\x12Q\n\x0e\x64utyPostCreate\x12\x16.DutyPostCreateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/dutyPostCreate\x12L\n\x0c\x64utyPostRead\x12\n.IdMessage\x1a\x15.DutyPostReadResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/dutyPostRead\x12Q\n\x0e\x64utyPostUpdate\x12\x16.DutyPostUpdateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/dutyPostUpdate\x12^\n\x12\x64utyPostUpdateRead\x12\n.IdMessage\x1a\x1b.DutyPostUpdateReadResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/dutyPostUpdateRead\x12\x45\n\x0e\x64utyPostDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/dutyPostDelete\x12V\n\x0c\x64utyPostList\x12\x14.DutyPostListRequest\x1a\x15.DutyPostListResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/dutyPostList2\xde\x03\n\rWeaponService\x12K\n\x0cweaponCreate\x12\x14.WeaponCreateRequest\x1a\n.IdMessage\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/weaponCreate\x12\x46\n\nweaponRead\x12\n.IdMessage\x1a\x13.WeaponReadResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/weaponRead\x12K\n\x0cweaponUpdate\x12\x14.WeaponUpdateRequest\x1a\n.IdMessage\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/weaponUpdate\x12X\n\x10weaponUpdateRead\x12\n.IdMessage\x1a\x19.WeaponUpdateReadResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/weaponUpdateRead\x12\x41\n\x0cweaponDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/weaponDelete\x12N\n\nweaponList\x12\x12.WeaponListRequest\x1a\x13.WeaponListResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/weaponList2\xb8\x03\n\x0b\x41mmoService\x12\x45\n\nammoCreate\x12\x12.AmmoCreateRequest\x1a\n.IdMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/ammoCreate\x12@\n\x08\x61mmoRead\x12\n.IdMessage\x1a\x11.AmmoReadResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/api/ammoRead\x12\x45\n\nammoUpdate\x12\x12.AmmoUpdateRequest\x1a\n.IdMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/ammoUpdate\x12R\n\x0e\x61mmoUpdateRead\x12\n.IdMessage\x1a\x17.AmmoUpdateReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/ammoUpdateRead\x12=\n\nammoDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/ammoDelete\x12\x46\n\x08\x61mmoList\x12\x10.AmmoListRequest\x1a\x11.AmmoListResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/api/ammoList2\xaa\x04\n\x11OtherItemsService\x12W\n\x10otherItemsCreate\x12\x18.OtherItemsCreateRequest\x1a\n.IdMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/otherItemsCreate\x12R\n\x0eotherItemsRead\x12\n.IdMessage\x1a\x17.OtherItemsReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/otherItemsRead\x12W\n\x10otherItemsUpdate\x12\x18.OtherItemsUpdateRequest\x1a\n.IdMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/otherItemsUpdate\x12\x64\n\x14otherItemsUpdateRead\x12\n.IdMessage\x1a\x1d.OtherItemsUpdateReadResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/api/otherItemsUpdateRead\x12I\n\x10otherItemsDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/otherItemsDelete\x12^\n\x0eotherItemsList\x12\x16.OtherItemsListRequest\x1a\x17.OtherItemsListResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/otherItemsList2\xf1\x02\n\x11\x41ssignmentService\x12R\n\x0e\x61ssignmentRead\x12\n.IdMessage\x1a\x17.AssignmentReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/assignmentRead\x12W\n\x10\x61ssignmentUpdate\x12\x18.AssignmentUpdateRequest\x1a\n.IdMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/assignmentUpdate\x12\x64\n\x14\x61ssignmentUpdateRead\x12\n.IdMessage\x1a\x1d.AssignmentUpdateReadResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/api/assignmentUpdateRead\x12I\n\x10\x61ssignmentDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/assignmentDelete2\xd8\x06\n\x0fScheduleService\x12i\n\x16scheduleAssignmentsAdd\x12\x1e.ScheduleAssignmentsAddRequest\x1a\n.IdMessage\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/api/scheduleAssignmentsAdd\x12\x82\x01\n\x17scheduleAssignmentsList\x12\x1f.ScheduleAssignmentsListRequest\x1a .ScheduleAssignmentsListResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/api/scheduleAssignmentsList\x12\x62\n\x0bshiftReport\x12\x1b.ShiftReportItemListRequest\x1a\x1c.ShiftReportItemListResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/shiftReport\x12Q\n\x0escheduleCreate\x12\x16.ScheduleCreateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/scheduleCreate\x12L\n\x0cscheduleRead\x12\n.IdMessage\x1a\x15.ScheduleReadResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/scheduleRead\x12Q\n\x0escheduleUpdate\x12\x16.ScheduleUpdateRequest\x1a\n.IdMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/scheduleUpdate\x12^\n\x12scheduleUpdateRead\x12\n.IdMessage\x1a\x1b.ScheduleUpdateReadResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/scheduleUpdateRead\x12\x45\n\x0escheduleDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/scheduleDelete\x12V\n\x0cscheduleList\x12\x14.ScheduleListRequest\x1a\x15.ScheduleListResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/scheduleList2\xf1\x02\n\x11WeaponAmmoService\x12R\n\x0eweaponAmmoRead\x12\n.IdMessage\x1a\x17.WeaponAmmoReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/weaponAmmoRead\x12W\n\x10weaponAmmoUpdate\x12\x18.WeaponAmmoUpdateRequest\x1a\n.IdMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/weaponAmmoUpdate\x12\x64\n\x14weaponAmmoUpdateRead\x12\n.IdMessage\x1a\x1d.WeaponAmmoUpdateReadResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/api/weaponAmmoUpdateRead\x12I\n\x10weaponAmmoDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/weaponAmmoDelete2\xd0\x04\n\x13GlobalConfigService\x12]\n\x12globalConfigCreate\x12\x1a.GlobalConfigCreateRequest\x1a\n.IdMessage\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/globalConfigCreate\x12X\n\x10globalConfigRead\x12\n.IdMessage\x1a\x19.GlobalConfigReadResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/globalConfigRead\x12]\n\x12globalConfigUpdate\x12\x1a.GlobalConfigUpdateRequest\x1a\n.IdMessage\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/globalConfigUpdate\x12j\n\x16globalConfigUpdateRead\x12\n.IdMessage\x1a\x1f.GlobalConfigUpdateReadResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/api/globalConfigUpdateRead\x12M\n\x12globalConfigDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/api/globalConfigDelete\x12\x66\n\x10globalConfigList\x12\x18.GlobalConfigListRequest\x1a\x19.GlobalConfigListResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/globalConfigList2\xf1\x02\n\x11\x46lowAlertsService\x12R\n\x0e\x66lowAlertsRead\x12\n.IdMessage\x1a\x17.FlowAlertsReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/flowAlertsRead\x12W\n\x10\x66lowAlertsUpdate\x12\x18.FlowAlertsUpdateRequest\x1a\n.IdMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/flowAlertsUpdate\x12\x64\n\x14\x66lowAlertsUpdateRead\x12\n.IdMessage\x1a\x1d.FlowAlertsUpdateReadResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/api/flowAlertsUpdateRead\x12I\n\x10\x66lowAlertsDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/api/flowAlertsDelete2\xea\x04\n\x0c\x46lowsService\x12H\n\x0b\x66lowsCreate\x12\x13.FlowsCreateRequest\x1a\n.IdMessage\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/flowsCreate\x12\x43\n\tflowsRead\x12\n.IdMessage\x1a\x12.FlowsReadResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/api/flowsRead\x12H\n\x0b\x66lowsUpdate\x12\x13.FlowsUpdateRequest\x1a\n.IdMessage\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/flowsUpdate\x12U\n\x0f\x66lowsUpdateRead\x12\n.IdMessage\x1a\x18.FlowsUpdateReadResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/api/flowsUpdateRead\x12?\n\x0b\x66lowsDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/flowsDelete\x12J\n\tflowsList\x12\x11.FlowsListRequest\x1a\x12.FlowsListResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/api/flowsList\x12R\n\x0b\x66lowsOnScan\x12\x13.FlowsOnScanRequest\x1a\x14.FlowsOnScanResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/flowsOnScan\x12I\n\x0b\x66lowsListen\x12\n.OkMessage\x1a\x12.FlowsReadResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/api/flowsListen0\x01\x32\xf4\x01\n\rAlertsService\x12K\n\x0c\x61lertsCreate\x12\x14.AlertsCreateRequest\x1a\n.IdMessage\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/api/alertsCreate\x12\x46\n\nalertsRead\x12\n.IdMessage\x1a\x13.AlertsReadResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/alertsRead\x12N\n\nalertsList\x12\x12.AlertsListRequest\x1a\x13.AlertsListResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/alertsList2\x89\x04\n\x0bUserService\x12\x45\n\nuserCreate\x12\x12.UserCreateRequest\x1a\n.IdMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/userCreate\x12@\n\x08userRead\x12\n.IdMessage\x1a\x11.UserReadResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/api/userRead\x12\x45\n\nuserUpdate\x12\x12.UserUpdateRequest\x1a\n.IdMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/userUpdate\x12R\n\x0euserUpdateRead\x12\n.IdMessage\x1a\x17.UserUpdateReadResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/api/userUpdateRead\x12=\n\nuserDelete\x12\n.IdMessage\x1a\n.OkMessage\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0f/api/userDelete\x12\x46\n\x08userList\x12\x10.UserListRequest\x1a\x11.UserListResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/api/userList\x12O\n\x0fuserCreateSuper\x12\x12.UserCreateRequest\x1a\n.IdMessage\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/api/userCreateSuper2\xe3\x04\n\x14\x41\x63\x63\x65ssControlService\x12`\n\x13\x61\x63\x63\x65ssControlCreate\x12\x1b.AccessControlCreateRequest\x1a\n.IdMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/accessControlCreate\x12[\n\x11\x61\x63\x63\x65ssControlRead\x12\n.IdMessage\x1a\x1a.AccessControlReadResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/api/accessControlRead\x12`\n\x13\x61\x63\x63\x65ssControlUpdate\x12\x1b.AccessControlUpdateRequest\x1a\n.IdMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/accessControlUpdate\x12m\n\x17\x61\x63\x63\x65ssControlUpdateRead\x12\n.IdMessage\x1a .AccessControlUpdateReadResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/api/accessControlUpdateRead\x12O\n\x13\x61\x63\x63\x65ssControlDelete\x12\n.IdMessage\x1a\n.OkMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/accessControlDelete\x12j\n\x11\x61\x63\x63\x65ssControlList\x12\x19.AccessControlListRequest\x1a\x1a.AccessControlListResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/api/accessControlList2\xe3\x04\n\x14ResourceGroupService\x12`\n\x13resourceGroupCreate\x12\x1b.ResourceGroupCreateRequest\x1a\n.IdMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/resourceGroupCreate\x12[\n\x11resourceGroupRead\x12\n.IdMessage\x1a\x1a.ResourceGroupReadResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/api/resourceGroupRead\x12`\n\x13resourceGroupUpdate\x12\x1b.ResourceGroupUpdateRequest\x1a\n.IdMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/resourceGroupUpdate\x12m\n\x17resourceGroupUpdateRead\x12\n.IdMessage\x1a .ResourceGroupUpdateReadResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/api/resourceGroupUpdateRead\x12O\n\x13resourceGroupDelete\x12\n.IdMessage\x1a\n.OkMessage\" \x82\xd3\xe4\x93\x02\x1a\"\x18/api/resourceGroupDelete\x12j\n\x11resourceGroupList\x12\x19.ResourceGroupListRequest\x1a\x1a.ResourceGroupListResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/api/resourceGroupListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krypton.cisf.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeCreate']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeCreate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/employeeCreate'
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeRead']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeRead']._serialized_options = b'\202\323\344\223\002\023\"\021/api/employeeRead'
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeUpdate']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeUpdate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/employeeUpdate'
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeUpdateRead']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeUpdateRead']._serialized_options = b'\202\323\344\223\002\031\"\027/api/employeeUpdateRead'
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeDelete']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeDelete']._serialized_options = b'\202\323\344\223\002\025\"\023/api/employeeDelete'
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeList']._options = None
  _globals['_EMPLOYEESERVICE'].methods_by_name['employeeList']._serialized_options = b'\202\323\344\223\002\023\"\021/api/employeeList'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostCreate']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostCreate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/dutyPostCreate'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostRead']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostRead']._serialized_options = b'\202\323\344\223\002\023\"\021/api/dutyPostRead'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostUpdate']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostUpdate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/dutyPostUpdate'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostUpdateRead']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostUpdateRead']._serialized_options = b'\202\323\344\223\002\031\"\027/api/dutyPostUpdateRead'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostDelete']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostDelete']._serialized_options = b'\202\323\344\223\002\025\"\023/api/dutyPostDelete'
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostList']._options = None
  _globals['_DUTYPOSTSERVICE'].methods_by_name['dutyPostList']._serialized_options = b'\202\323\344\223\002\023\"\021/api/dutyPostList'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponCreate']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponCreate']._serialized_options = b'\202\323\344\223\002\023\"\021/api/weaponCreate'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponRead']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponRead']._serialized_options = b'\202\323\344\223\002\021\"\017/api/weaponRead'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponUpdate']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponUpdate']._serialized_options = b'\202\323\344\223\002\023\"\021/api/weaponUpdate'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponUpdateRead']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponUpdateRead']._serialized_options = b'\202\323\344\223\002\027\"\025/api/weaponUpdateRead'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponDelete']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponDelete']._serialized_options = b'\202\323\344\223\002\023\"\021/api/weaponDelete'
  _globals['_WEAPONSERVICE'].methods_by_name['weaponList']._options = None
  _globals['_WEAPONSERVICE'].methods_by_name['weaponList']._serialized_options = b'\202\323\344\223\002\021\"\017/api/weaponList'
  _globals['_AMMOSERVICE'].methods_by_name['ammoCreate']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoCreate']._serialized_options = b'\202\323\344\223\002\021\"\017/api/ammoCreate'
  _globals['_AMMOSERVICE'].methods_by_name['ammoRead']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoRead']._serialized_options = b'\202\323\344\223\002\017\"\r/api/ammoRead'
  _globals['_AMMOSERVICE'].methods_by_name['ammoUpdate']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoUpdate']._serialized_options = b'\202\323\344\223\002\021\"\017/api/ammoUpdate'
  _globals['_AMMOSERVICE'].methods_by_name['ammoUpdateRead']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoUpdateRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/ammoUpdateRead'
  _globals['_AMMOSERVICE'].methods_by_name['ammoDelete']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoDelete']._serialized_options = b'\202\323\344\223\002\021\"\017/api/ammoDelete'
  _globals['_AMMOSERVICE'].methods_by_name['ammoList']._options = None
  _globals['_AMMOSERVICE'].methods_by_name['ammoList']._serialized_options = b'\202\323\344\223\002\017\"\r/api/ammoList'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsCreate']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsCreate']._serialized_options = b'\202\323\344\223\002\027\"\025/api/otherItemsCreate'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsRead']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/otherItemsRead'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsUpdate']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsUpdate']._serialized_options = b'\202\323\344\223\002\027\"\025/api/otherItemsUpdate'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsUpdateRead']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsUpdateRead']._serialized_options = b'\202\323\344\223\002\033\"\031/api/otherItemsUpdateRead'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsDelete']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsDelete']._serialized_options = b'\202\323\344\223\002\027\"\025/api/otherItemsDelete'
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsList']._options = None
  _globals['_OTHERITEMSSERVICE'].methods_by_name['otherItemsList']._serialized_options = b'\202\323\344\223\002\025\"\023/api/otherItemsList'
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentRead']._options = None
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/assignmentRead'
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentUpdate']._options = None
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentUpdate']._serialized_options = b'\202\323\344\223\002\027\"\025/api/assignmentUpdate'
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentUpdateRead']._options = None
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentUpdateRead']._serialized_options = b'\202\323\344\223\002\033\"\031/api/assignmentUpdateRead'
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentDelete']._options = None
  _globals['_ASSIGNMENTSERVICE'].methods_by_name['assignmentDelete']._serialized_options = b'\202\323\344\223\002\027\"\025/api/assignmentDelete'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleAssignmentsAdd']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleAssignmentsAdd']._serialized_options = b'\202\323\344\223\002\035\"\033/api/scheduleAssignmentsAdd'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleAssignmentsList']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleAssignmentsList']._serialized_options = b'\202\323\344\223\002\036\"\034/api/scheduleAssignmentsList'
  _globals['_SCHEDULESERVICE'].methods_by_name['shiftReport']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['shiftReport']._serialized_options = b'\202\323\344\223\002\022\"\020/api/shiftReport'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleCreate']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleCreate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/scheduleCreate'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleRead']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleRead']._serialized_options = b'\202\323\344\223\002\023\"\021/api/scheduleRead'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleUpdate']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleUpdate']._serialized_options = b'\202\323\344\223\002\025\"\023/api/scheduleUpdate'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleUpdateRead']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleUpdateRead']._serialized_options = b'\202\323\344\223\002\031\"\027/api/scheduleUpdateRead'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleDelete']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleDelete']._serialized_options = b'\202\323\344\223\002\025\"\023/api/scheduleDelete'
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleList']._options = None
  _globals['_SCHEDULESERVICE'].methods_by_name['scheduleList']._serialized_options = b'\202\323\344\223\002\023\"\021/api/scheduleList'
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoRead']._options = None
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/weaponAmmoRead'
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoUpdate']._options = None
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoUpdate']._serialized_options = b'\202\323\344\223\002\027\"\025/api/weaponAmmoUpdate'
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoUpdateRead']._options = None
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoUpdateRead']._serialized_options = b'\202\323\344\223\002\033\"\031/api/weaponAmmoUpdateRead'
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoDelete']._options = None
  _globals['_WEAPONAMMOSERVICE'].methods_by_name['weaponAmmoDelete']._serialized_options = b'\202\323\344\223\002\027\"\025/api/weaponAmmoDelete'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigCreate']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigCreate']._serialized_options = b'\202\323\344\223\002\031\"\027/api/globalConfigCreate'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigRead']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigRead']._serialized_options = b'\202\323\344\223\002\027\"\025/api/globalConfigRead'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigUpdate']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigUpdate']._serialized_options = b'\202\323\344\223\002\031\"\027/api/globalConfigUpdate'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigUpdateRead']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigUpdateRead']._serialized_options = b'\202\323\344\223\002\035\"\033/api/globalConfigUpdateRead'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigDelete']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigDelete']._serialized_options = b'\202\323\344\223\002\031\"\027/api/globalConfigDelete'
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigList']._options = None
  _globals['_GLOBALCONFIGSERVICE'].methods_by_name['globalConfigList']._serialized_options = b'\202\323\344\223\002\027\"\025/api/globalConfigList'
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsRead']._options = None
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/flowAlertsRead'
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsUpdate']._options = None
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsUpdate']._serialized_options = b'\202\323\344\223\002\027\"\025/api/flowAlertsUpdate'
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsUpdateRead']._options = None
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsUpdateRead']._serialized_options = b'\202\323\344\223\002\033\"\031/api/flowAlertsUpdateRead'
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsDelete']._options = None
  _globals['_FLOWALERTSSERVICE'].methods_by_name['flowAlertsDelete']._serialized_options = b'\202\323\344\223\002\027\"\025/api/flowAlertsDelete'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsCreate']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsCreate']._serialized_options = b'\202\323\344\223\002\022\"\020/api/flowsCreate'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsRead']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsRead']._serialized_options = b'\202\323\344\223\002\020\"\016/api/flowsRead'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsUpdate']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsUpdate']._serialized_options = b'\202\323\344\223\002\022\"\020/api/flowsUpdate'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsUpdateRead']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsUpdateRead']._serialized_options = b'\202\323\344\223\002\026\"\024/api/flowsUpdateRead'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsDelete']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsDelete']._serialized_options = b'\202\323\344\223\002\022\"\020/api/flowsDelete'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsList']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsList']._serialized_options = b'\202\323\344\223\002\020\"\016/api/flowsList'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsOnScan']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsOnScan']._serialized_options = b'\202\323\344\223\002\022\"\020/api/flowsOnScan'
  _globals['_FLOWSSERVICE'].methods_by_name['flowsListen']._options = None
  _globals['_FLOWSSERVICE'].methods_by_name['flowsListen']._serialized_options = b'\202\323\344\223\002\022\"\020/api/flowsListen'
  _globals['_ALERTSSERVICE'].methods_by_name['alertsCreate']._options = None
  _globals['_ALERTSSERVICE'].methods_by_name['alertsCreate']._serialized_options = b'\202\323\344\223\002\023\"\021/api/alertsCreate'
  _globals['_ALERTSSERVICE'].methods_by_name['alertsRead']._options = None
  _globals['_ALERTSSERVICE'].methods_by_name['alertsRead']._serialized_options = b'\202\323\344\223\002\021\"\017/api/alertsRead'
  _globals['_ALERTSSERVICE'].methods_by_name['alertsList']._options = None
  _globals['_ALERTSSERVICE'].methods_by_name['alertsList']._serialized_options = b'\202\323\344\223\002\021\"\017/api/alertsList'
  _globals['_USERSERVICE'].methods_by_name['userCreate']._options = None
  _globals['_USERSERVICE'].methods_by_name['userCreate']._serialized_options = b'\202\323\344\223\002\021\"\017/api/userCreate'
  _globals['_USERSERVICE'].methods_by_name['userRead']._options = None
  _globals['_USERSERVICE'].methods_by_name['userRead']._serialized_options = b'\202\323\344\223\002\017\"\r/api/userRead'
  _globals['_USERSERVICE'].methods_by_name['userUpdate']._options = None
  _globals['_USERSERVICE'].methods_by_name['userUpdate']._serialized_options = b'\202\323\344\223\002\021\"\017/api/userUpdate'
  _globals['_USERSERVICE'].methods_by_name['userUpdateRead']._options = None
  _globals['_USERSERVICE'].methods_by_name['userUpdateRead']._serialized_options = b'\202\323\344\223\002\025\"\023/api/userUpdateRead'
  _globals['_USERSERVICE'].methods_by_name['userDelete']._options = None
  _globals['_USERSERVICE'].methods_by_name['userDelete']._serialized_options = b'\202\323\344\223\002\021\"\017/api/userDelete'
  _globals['_USERSERVICE'].methods_by_name['userList']._options = None
  _globals['_USERSERVICE'].methods_by_name['userList']._serialized_options = b'\202\323\344\223\002\017\"\r/api/userList'
  _globals['_USERSERVICE'].methods_by_name['userCreateSuper']._options = None
  _globals['_USERSERVICE'].methods_by_name['userCreateSuper']._serialized_options = b'\202\323\344\223\002\026\"\024/api/userCreateSuper'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlCreate']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlCreate']._serialized_options = b'\202\323\344\223\002\032\"\030/api/accessControlCreate'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlRead']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlRead']._serialized_options = b'\202\323\344\223\002\030\"\026/api/accessControlRead'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlUpdate']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlUpdate']._serialized_options = b'\202\323\344\223\002\032\"\030/api/accessControlUpdate'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlUpdateRead']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlUpdateRead']._serialized_options = b'\202\323\344\223\002\036\"\034/api/accessControlUpdateRead'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlDelete']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlDelete']._serialized_options = b'\202\323\344\223\002\032\"\030/api/accessControlDelete'
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlList']._options = None
  _globals['_ACCESSCONTROLSERVICE'].methods_by_name['accessControlList']._serialized_options = b'\202\323\344\223\002\030\"\026/api/accessControlList'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupCreate']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupCreate']._serialized_options = b'\202\323\344\223\002\032\"\030/api/resourceGroupCreate'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupRead']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupRead']._serialized_options = b'\202\323\344\223\002\030\"\026/api/resourceGroupRead'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupUpdate']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupUpdate']._serialized_options = b'\202\323\344\223\002\032\"\030/api/resourceGroupUpdate'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupUpdateRead']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupUpdateRead']._serialized_options = b'\202\323\344\223\002\036\"\034/api/resourceGroupUpdateRead'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupDelete']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupDelete']._serialized_options = b'\202\323\344\223\002\032\"\030/api/resourceGroupDelete'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupList']._options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['resourceGroupList']._serialized_options = b'\202\323\344\223\002\030\"\026/api/resourceGroupList'
  _globals['_EMPLOYEESERVICE']._serialized_start=142
  _globals['_EMPLOYEESERVICE']._serialized_end=658
  _globals['_DUTYPOSTSERVICE']._serialized_start=661
  _globals['_DUTYPOSTSERVICE']._serialized_end=1177
  _globals['_WEAPONSERVICE']._serialized_start=1180
  _globals['_WEAPONSERVICE']._serialized_end=1658
  _globals['_AMMOSERVICE']._serialized_start=1661
  _globals['_AMMOSERVICE']._serialized_end=2101
  _globals['_OTHERITEMSSERVICE']._serialized_start=2104
  _globals['_OTHERITEMSSERVICE']._serialized_end=2658
  _globals['_ASSIGNMENTSERVICE']._serialized_start=2661
  _globals['_ASSIGNMENTSERVICE']._serialized_end=3030
  _globals['_SCHEDULESERVICE']._serialized_start=3033
  _globals['_SCHEDULESERVICE']._serialized_end=3889
  _globals['_WEAPONAMMOSERVICE']._serialized_start=3892
  _globals['_WEAPONAMMOSERVICE']._serialized_end=4261
  _globals['_GLOBALCONFIGSERVICE']._serialized_start=4264
  _globals['_GLOBALCONFIGSERVICE']._serialized_end=4856
  _globals['_FLOWALERTSSERVICE']._serialized_start=4859
  _globals['_FLOWALERTSSERVICE']._serialized_end=5228
  _globals['_FLOWSSERVICE']._serialized_start=5231
  _globals['_FLOWSSERVICE']._serialized_end=5849
  _globals['_ALERTSSERVICE']._serialized_start=5852
  _globals['_ALERTSSERVICE']._serialized_end=6096
  _globals['_USERSERVICE']._serialized_start=6099
  _globals['_USERSERVICE']._serialized_end=6620
  _globals['_ACCESSCONTROLSERVICE']._serialized_start=6623
  _globals['_ACCESSCONTROLSERVICE']._serialized_end=7234
  _globals['_RESOURCEGROUPSERVICE']._serialized_start=7237
  _globals['_RESOURCEGROUPSERVICE']._serialized_end=7848
# @@protoc_insertion_point(module_scope)

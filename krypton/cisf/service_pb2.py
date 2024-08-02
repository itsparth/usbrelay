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
from krypton.common import message_pb2 as krypton_dot_common_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1akrypton/cisf/service.proto\x1a\x1akrypton/cisf/message.proto\x1a\x1ckrypton/common/message.proto2\xd6\x02\n\x0f\x45mployeeService\x12\x34\n\x0e\x65mployeeCreate\x12\x16.EmployeeCreateRequest\x1a\n.IdMessage\x12\x31\n\x0c\x65mployeeRead\x12\n.IdMessage\x1a\x15.EmployeeReadResponse\x12\x34\n\x0e\x65mployeeUpdate\x12\x16.EmployeeUpdateRequest\x1a\n.IdMessage\x12=\n\x12\x65mployeeUpdateRead\x12\n.IdMessage\x1a\x1b.EmployeeUpdateReadResponse\x12(\n\x0e\x65mployeeDelete\x12\n.IdMessage\x1a\n.OkMessage\x12;\n\x0c\x65mployeeList\x12\x14.EmployeeListRequest\x1a\x15.EmployeeListResponse2\xd6\x02\n\x0f\x44utyPostService\x12\x34\n\x0e\x64utyPostCreate\x12\x16.DutyPostCreateRequest\x1a\n.IdMessage\x12\x31\n\x0c\x64utyPostRead\x12\n.IdMessage\x1a\x15.DutyPostReadResponse\x12\x34\n\x0e\x64utyPostUpdate\x12\x16.DutyPostUpdateRequest\x1a\n.IdMessage\x12=\n\x12\x64utyPostUpdateRead\x12\n.IdMessage\x1a\x1b.DutyPostUpdateReadResponse\x12(\n\x0e\x64utyPostDelete\x12\n.IdMessage\x1a\n.OkMessage\x12;\n\x0c\x64utyPostList\x12\x14.DutyPostListRequest\x1a\x15.DutyPostListResponse2\xbc\x02\n\rWeaponService\x12\x30\n\x0cweaponCreate\x12\x14.WeaponCreateRequest\x1a\n.IdMessage\x12-\n\nweaponRead\x12\n.IdMessage\x1a\x13.WeaponReadResponse\x12\x30\n\x0cweaponUpdate\x12\x14.WeaponUpdateRequest\x1a\n.IdMessage\x12\x39\n\x10weaponUpdateRead\x12\n.IdMessage\x1a\x19.WeaponUpdateReadResponse\x12&\n\x0cweaponDelete\x12\n.IdMessage\x1a\n.OkMessage\x12\x35\n\nweaponList\x12\x12.WeaponListRequest\x1a\x13.WeaponListResponse2\xa2\x02\n\x0b\x41mmoService\x12,\n\nammoCreate\x12\x12.AmmoCreateRequest\x1a\n.IdMessage\x12)\n\x08\x61mmoRead\x12\n.IdMessage\x1a\x11.AmmoReadResponse\x12,\n\nammoUpdate\x12\x12.AmmoUpdateRequest\x1a\n.IdMessage\x12\x35\n\x0e\x61mmoUpdateRead\x12\n.IdMessage\x1a\x17.AmmoUpdateReadResponse\x12$\n\nammoDelete\x12\n.IdMessage\x1a\n.OkMessage\x12/\n\x08\x61mmoList\x12\x10.AmmoListRequest\x1a\x11.AmmoListResponse2\xf0\x02\n\x11OtherItemsService\x12\x38\n\x10otherItemsCreate\x12\x18.OtherItemsCreateRequest\x1a\n.IdMessage\x12\x35\n\x0eotherItemsRead\x12\n.IdMessage\x1a\x17.OtherItemsReadResponse\x12\x38\n\x10otherItemsUpdate\x12\x18.OtherItemsUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14otherItemsUpdateRead\x12\n.IdMessage\x1a\x1d.OtherItemsUpdateReadResponse\x12*\n\x10otherItemsDelete\x12\n.IdMessage\x1a\n.OkMessage\x12\x41\n\x0eotherItemsList\x12\x16.OtherItemsListRequest\x1a\x17.OtherItemsListResponse2\xbc\x01\n\x11\x41ssignmentService\x12\x38\n\x10\x61ssignmentUpdate\x12\x18.AssignmentUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14\x61ssignmentUpdateRead\x12\n.IdMessage\x1a\x1d.AssignmentUpdateReadResponse\x12*\n\x10\x61ssignmentDelete\x12\n.IdMessage\x1a\n.OkMessage2\xc4\x04\n\x0fScheduleService\x12\x44\n\x16scheduleAssignmentsAdd\x12\x1e.ScheduleAssignmentsAddRequest\x1a\n.IdMessage\x12\\\n\x17scheduleAssignmentsList\x12\x1f.ScheduleAssignmentsListRequest\x1a .ScheduleAssignmentsListResponse\x12H\n\x0bshiftReport\x12\x1b.ShiftReportItemListRequest\x1a\x1c.ShiftReportItemListResponse\x12\x34\n\x0escheduleCreate\x12\x16.ScheduleCreateRequest\x1a\n.IdMessage\x12\x31\n\x0cscheduleRead\x12\n.IdMessage\x1a\x15.ScheduleReadResponse\x12\x34\n\x0escheduleUpdate\x12\x16.ScheduleUpdateRequest\x1a\n.IdMessage\x12=\n\x12scheduleUpdateRead\x12\n.IdMessage\x1a\x1b.ScheduleUpdateReadResponse\x12(\n\x0escheduleDelete\x12\n.IdMessage\x1a\n.OkMessage\x12;\n\x0cscheduleList\x12\x14.ScheduleListRequest\x1a\x15.ScheduleListResponse2\xbc\x01\n\x11WeaponAmmoService\x12\x38\n\x10weaponAmmoUpdate\x12\x18.WeaponAmmoUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14weaponAmmoUpdateRead\x12\n.IdMessage\x1a\x1d.WeaponAmmoUpdateReadResponse\x12*\n\x10weaponAmmoDelete\x12\n.IdMessage\x1a\n.OkMessage2\x8a\x03\n\x13GlobalConfigService\x12<\n\x12globalConfigCreate\x12\x1a.GlobalConfigCreateRequest\x1a\n.IdMessage\x12\x39\n\x10globalConfigRead\x12\n.IdMessage\x1a\x19.GlobalConfigReadResponse\x12<\n\x12globalConfigUpdate\x12\x1a.GlobalConfigUpdateRequest\x1a\n.IdMessage\x12\x45\n\x16globalConfigUpdateRead\x12\n.IdMessage\x1a\x1f.GlobalConfigUpdateReadResponse\x12,\n\x12globalConfigDelete\x12\n.IdMessage\x1a\n.OkMessage\x12G\n\x10globalConfigList\x12\x18.GlobalConfigListRequest\x1a\x19.GlobalConfigListResponse2\xbc\x01\n\x11\x46lowAlertsService\x12\x38\n\x10\x66lowAlertsUpdate\x12\x18.FlowAlertsUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14\x66lowAlertsUpdateRead\x12\n.IdMessage\x1a\x1d.FlowAlertsUpdateReadResponse\x12*\n\x10\x66lowAlertsDelete\x12\n.IdMessage\x1a\n.OkMessage2\xbc\x01\n\x11\x43ommonInfoService\x12\x38\n\x10\x63ommonInfoUpdate\x12\x18.CommonInfoUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14\x63ommonInfoUpdateRead\x12\n.IdMessage\x1a\x1d.CommonInfoUpdateReadResponse\x12*\n\x10\x63ommonInfoDelete\x12\n.IdMessage\x1a\n.OkMessage2\xb0\x01\n\x0f\x41mmoInfoService\x12\x34\n\x0e\x61mmoInfoUpdate\x12\x16.AmmoInfoUpdateRequest\x1a\n.IdMessage\x12=\n\x12\x61mmoInfoUpdateRead\x12\n.IdMessage\x1a\x1b.AmmoInfoUpdateReadResponse\x12(\n\x0e\x61mmoInfoDelete\x12\n.IdMessage\x1a\n.OkMessage2\x9a\x03\n\x0c\x46lowsService\x12.\n\x0b\x66lowsCreate\x12\x13.FlowsCreateRequest\x1a\n.IdMessage\x12+\n\tflowsRead\x12\n.IdMessage\x1a\x12.FlowsReadResponse\x12.\n\x0b\x66lowsUpdate\x12\x13.FlowsUpdateRequest\x1a\n.IdMessage\x12\x37\n\x0f\x66lowsUpdateRead\x12\n.IdMessage\x1a\x18.FlowsUpdateReadResponse\x12%\n\x0b\x66lowsDelete\x12\n.IdMessage\x1a\n.OkMessage\x12\x32\n\tflowsList\x12\x11.FlowsListRequest\x1a\x12.FlowsListResponse\x12\x38\n\x0b\x66lowsOnScan\x12\x13.FlowsOnScanRequest\x1a\x14.FlowsOnScanResponse\x12/\n\x0b\x66lowsListen\x12\n.OkMessage\x1a\x12.FlowsReadResponse0\x01\x32\xa7\x01\n\rAlertsService\x12\x30\n\x0c\x61lertsCreate\x12\x14.AlertsCreateRequest\x1a\n.IdMessage\x12-\n\nalertsRead\x12\n.IdMessage\x1a\x13.AlertsReadResponse\x12\x35\n\nalertsList\x12\x12.AlertsListRequest\x1a\x13.AlertsListResponse2\xd5\x02\n\x0bUserService\x12,\n\nuserCreate\x12\x12.UserCreateRequest\x1a\n.IdMessage\x12)\n\x08userRead\x12\n.IdMessage\x1a\x11.UserReadResponse\x12,\n\nuserUpdate\x12\x12.UserUpdateRequest\x1a\n.IdMessage\x12\x35\n\x0euserUpdateRead\x12\n.IdMessage\x1a\x17.UserUpdateReadResponse\x12$\n\nuserDelete\x12\n.IdMessage\x1a\n.OkMessage\x12/\n\x08userList\x12\x10.UserListRequest\x1a\x11.UserListResponse\x12\x31\n\x0fuserCreateSuper\x12\x12.UserCreateRequest\x1a\n.IdMessage2\xbc\x01\n\x11WeaponInfoService\x12\x38\n\x10weaponInfoUpdate\x12\x18.WeaponInfoUpdateRequest\x1a\n.IdMessage\x12\x41\n\x14weaponInfoUpdateRead\x12\n.IdMessage\x1a\x1d.WeaponInfoUpdateReadResponse\x12*\n\x10weaponInfoDelete\x12\n.IdMessage\x1a\n.OkMessage2\x97\x03\n\x14\x41\x63\x63\x65ssControlService\x12>\n\x13\x61\x63\x63\x65ssControlCreate\x12\x1b.AccessControlCreateRequest\x1a\n.IdMessage\x12;\n\x11\x61\x63\x63\x65ssControlRead\x12\n.IdMessage\x1a\x1a.AccessControlReadResponse\x12>\n\x13\x61\x63\x63\x65ssControlUpdate\x12\x1b.AccessControlUpdateRequest\x1a\n.IdMessage\x12G\n\x17\x61\x63\x63\x65ssControlUpdateRead\x12\n.IdMessage\x1a .AccessControlUpdateReadResponse\x12-\n\x13\x61\x63\x63\x65ssControlDelete\x12\n.IdMessage\x1a\n.OkMessage\x12J\n\x11\x61\x63\x63\x65ssControlList\x12\x19.AccessControlListRequest\x1a\x1a.AccessControlListResponse2\x97\x03\n\x14ResourceGroupService\x12>\n\x13resourceGroupCreate\x12\x1b.ResourceGroupCreateRequest\x1a\n.IdMessage\x12;\n\x11resourceGroupRead\x12\n.IdMessage\x1a\x1a.ResourceGroupReadResponse\x12>\n\x13resourceGroupUpdate\x12\x1b.ResourceGroupUpdateRequest\x1a\n.IdMessage\x12G\n\x17resourceGroupUpdateRead\x12\n.IdMessage\x1a .ResourceGroupUpdateReadResponse\x12-\n\x13resourceGroupDelete\x12\n.IdMessage\x1a\n.OkMessage\x12J\n\x11resourceGroupList\x12\x19.ResourceGroupListRequest\x1a\x1a.ResourceGroupListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krypton.cisf.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPLOYEESERVICE']._serialized_start=89
  _globals['_EMPLOYEESERVICE']._serialized_end=431
  _globals['_DUTYPOSTSERVICE']._serialized_start=434
  _globals['_DUTYPOSTSERVICE']._serialized_end=776
  _globals['_WEAPONSERVICE']._serialized_start=779
  _globals['_WEAPONSERVICE']._serialized_end=1095
  _globals['_AMMOSERVICE']._serialized_start=1098
  _globals['_AMMOSERVICE']._serialized_end=1388
  _globals['_OTHERITEMSSERVICE']._serialized_start=1391
  _globals['_OTHERITEMSSERVICE']._serialized_end=1759
  _globals['_ASSIGNMENTSERVICE']._serialized_start=1762
  _globals['_ASSIGNMENTSERVICE']._serialized_end=1950
  _globals['_SCHEDULESERVICE']._serialized_start=1953
  _globals['_SCHEDULESERVICE']._serialized_end=2533
  _globals['_WEAPONAMMOSERVICE']._serialized_start=2536
  _globals['_WEAPONAMMOSERVICE']._serialized_end=2724
  _globals['_GLOBALCONFIGSERVICE']._serialized_start=2727
  _globals['_GLOBALCONFIGSERVICE']._serialized_end=3121
  _globals['_FLOWALERTSSERVICE']._serialized_start=3124
  _globals['_FLOWALERTSSERVICE']._serialized_end=3312
  _globals['_COMMONINFOSERVICE']._serialized_start=3315
  _globals['_COMMONINFOSERVICE']._serialized_end=3503
  _globals['_AMMOINFOSERVICE']._serialized_start=3506
  _globals['_AMMOINFOSERVICE']._serialized_end=3682
  _globals['_FLOWSSERVICE']._serialized_start=3685
  _globals['_FLOWSSERVICE']._serialized_end=4095
  _globals['_ALERTSSERVICE']._serialized_start=4098
  _globals['_ALERTSSERVICE']._serialized_end=4265
  _globals['_USERSERVICE']._serialized_start=4268
  _globals['_USERSERVICE']._serialized_end=4609
  _globals['_WEAPONINFOSERVICE']._serialized_start=4612
  _globals['_WEAPONINFOSERVICE']._serialized_end=4800
  _globals['_ACCESSCONTROLSERVICE']._serialized_start=4803
  _globals['_ACCESSCONTROLSERVICE']._serialized_end=5210
  _globals['_RESOURCEGROUPSERVICE']._serialized_start=5213
  _globals['_RESOURCEGROUPSERVICE']._serialized_end=5620
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from injective.wasmx.v1 import proposal_pb2 as injective_dot_wasmx_dot_v1_dot_proposal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1binjective/wasmx/v1/tx.proto\x12\x12injective.wasmx.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a!injective/wasmx/v1/proposal.proto\"e\n\x18MsgExecuteContractCompat\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x63ontract\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x66unds\x18\x04 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"0\n MsgExecuteContractCompatResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x8d\x01\n\x11MsgUpdateContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\t\x12\x11\n\tgas_limit\x18\x03 \x01(\x04\x12\x11\n\tgas_price\x18\x04 \x01(\x04\x12\x1b\n\radmin_address\x18\x05 \x01(\tB\x04\xc8\xde\x1f\x01:\x0b\x82\xe7\xb0*\x06sender\"\x1b\n\x19MsgUpdateContractResponse\"L\n\x13MsgActivateContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\x1d\n\x1bMsgActivateContractResponse\"N\n\x15MsgDeactivateContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\x1f\n\x1dMsgDeactivateContractResponse\"\x80\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32\x1a.injective.wasmx.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse\"\x90\x01\n\x13MsgRegisterContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\\\n\x1d\x63ontract_registration_request\x18\x02 \x01(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00:\x0b\x82\xe7\xb0*\x06sender\"\x1d\n\x1bMsgRegisterContractResponse2\xba\x05\n\x03Msg\x12t\n\x1cUpdateRegistryContractParams\x12%.injective.wasmx.v1.MsgUpdateContract\x1a-.injective.wasmx.v1.MsgUpdateContractResponse\x12t\n\x18\x41\x63tivateRegistryContract\x12\'.injective.wasmx.v1.MsgActivateContract\x1a/.injective.wasmx.v1.MsgActivateContractResponse\x12z\n\x1a\x44\x65\x61\x63tivateRegistryContract\x12).injective.wasmx.v1.MsgDeactivateContract\x1a\x31.injective.wasmx.v1.MsgDeactivateContractResponse\x12{\n\x15\x45xecuteContractCompat\x12,.injective.wasmx.v1.MsgExecuteContractCompat\x1a\x34.injective.wasmx.v1.MsgExecuteContractCompatResponse\x12`\n\x0cUpdateParams\x12#.injective.wasmx.v1.MsgUpdateParams\x1a+.injective.wasmx.v1.MsgUpdateParamsResponse\x12l\n\x10RegisterContract\x12\'.injective.wasmx.v1.MsgRegisterContract\x1a/.injective.wasmx.v1.MsgRegisterContractResponseBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _MSGEXECUTECONTRACTCOMPAT._options = None
  _MSGEXECUTECONTRACTCOMPAT._serialized_options = b'\202\347\260*\006sender'
  _MSGUPDATECONTRACT.fields_by_name['admin_address']._options = None
  _MSGUPDATECONTRACT.fields_by_name['admin_address']._serialized_options = b'\310\336\037\001'
  _MSGUPDATECONTRACT._options = None
  _MSGUPDATECONTRACT._serialized_options = b'\202\347\260*\006sender'
  _MSGACTIVATECONTRACT._options = None
  _MSGACTIVATECONTRACT._serialized_options = b'\202\347\260*\006sender'
  _MSGDEACTIVATECONTRACT._options = None
  _MSGDEACTIVATECONTRACT._serialized_options = b'\202\347\260*\006sender'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSGREGISTERCONTRACT.fields_by_name['contract_registration_request']._options = None
  _MSGREGISTERCONTRACT.fields_by_name['contract_registration_request']._serialized_options = b'\310\336\037\000'
  _MSGREGISTERCONTRACT._options = None
  _MSGREGISTERCONTRACT._serialized_options = b'\202\347\260*\006sender'
  _MSGEXECUTECONTRACTCOMPAT._serialized_start=219
  _MSGEXECUTECONTRACTCOMPAT._serialized_end=320
  _MSGEXECUTECONTRACTCOMPATRESPONSE._serialized_start=322
  _MSGEXECUTECONTRACTCOMPATRESPONSE._serialized_end=370
  _MSGUPDATECONTRACT._serialized_start=373
  _MSGUPDATECONTRACT._serialized_end=514
  _MSGUPDATECONTRACTRESPONSE._serialized_start=516
  _MSGUPDATECONTRACTRESPONSE._serialized_end=543
  _MSGACTIVATECONTRACT._serialized_start=545
  _MSGACTIVATECONTRACT._serialized_end=621
  _MSGACTIVATECONTRACTRESPONSE._serialized_start=623
  _MSGACTIVATECONTRACTRESPONSE._serialized_end=652
  _MSGDEACTIVATECONTRACT._serialized_start=654
  _MSGDEACTIVATECONTRACT._serialized_end=732
  _MSGDEACTIVATECONTRACTRESPONSE._serialized_start=734
  _MSGDEACTIVATECONTRACTRESPONSE._serialized_end=765
  _MSGUPDATEPARAMS._serialized_start=768
  _MSGUPDATEPARAMS._serialized_end=896
  _MSGUPDATEPARAMSRESPONSE._serialized_start=898
  _MSGUPDATEPARAMSRESPONSE._serialized_end=923
  _MSGREGISTERCONTRACT._serialized_start=926
  _MSGREGISTERCONTRACT._serialized_end=1070
  _MSGREGISTERCONTRACTRESPONSE._serialized_start=1072
  _MSGREGISTERCONTRACTRESPONSE._serialized_end=1101
  _MSG._serialized_start=1104
  _MSG._serialized_end=1802
# @@protoc_insertion_point(module_scope)

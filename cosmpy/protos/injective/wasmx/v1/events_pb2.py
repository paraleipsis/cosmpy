# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1finjective/wasmx/v1/events.proto\x12\x12injective.wasmx.v1\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a\x14gogoproto/gogo.proto\"S\n\x16\x45ventContractExecution\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x01(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\tBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _EVENTCONTRACTEXECUTION._serialized_start=109
  _EVENTCONTRACTEXECUTION._serialized_end=192
# @@protoc_insertion_point(module_scope)
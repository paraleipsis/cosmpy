# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/params.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/tokenfactory/v1beta1/params.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x8f\x01\n\x06Params\x12\x84\x01\n\x12\x64\x65nom_creation_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBM\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x19yaml:\"denom_creation_fee\"\xc8\xde\x1f\x00\x42TZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types'
  _PARAMS.fields_by_name['denom_creation_fee']._options = None
  _PARAMS.fields_by_name['denom_creation_fee']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\031yaml:\"denom_creation_fee\"\310\336\037\000'
  _PARAMS._serialized_start=217
  _PARAMS._serialized_end=360
# @@protoc_insertion_point(module_scope)
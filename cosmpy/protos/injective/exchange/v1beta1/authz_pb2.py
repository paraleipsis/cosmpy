# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/exchange/v1beta1/authz.proto\x12\x1ainjective.exchange.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\"Y\n\x19\x43reateSpotLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x43reateSpotMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"_\n\x1f\x42\x61tchCreateSpotLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"T\n\x14\x43\x61ncelSpotOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x42\x61tchCancelSpotOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"_\n\x1f\x43reateDerivativeLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"`\n CreateDerivativeMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"e\n%BatchCreateDerivativeLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x43\x61ncelDerivativeOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"`\n BatchCancelDerivativeOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"t\n\x16\x42\x61tchUpdateOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x14\n\x0cspot_markets\x18\x02 \x03(\t\x12\x1a\n\x12\x64\x65rivative_markets\x18\x03 \x03(\t:\x11\xca\xb4-\rAuthorizationBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.authz_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _CREATESPOTLIMITORDERAUTHZ._options = None
  _CREATESPOTLIMITORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CREATESPOTMARKETORDERAUTHZ._options = None
  _CREATESPOTMARKETORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _BATCHCREATESPOTLIMITORDERSAUTHZ._options = None
  _BATCHCREATESPOTLIMITORDERSAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CANCELSPOTORDERAUTHZ._options = None
  _CANCELSPOTORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _BATCHCANCELSPOTORDERSAUTHZ._options = None
  _BATCHCANCELSPOTORDERSAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CREATEDERIVATIVELIMITORDERAUTHZ._options = None
  _CREATEDERIVATIVELIMITORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CREATEDERIVATIVEMARKETORDERAUTHZ._options = None
  _CREATEDERIVATIVEMARKETORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _BATCHCREATEDERIVATIVELIMITORDERSAUTHZ._options = None
  _BATCHCREATEDERIVATIVELIMITORDERSAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CANCELDERIVATIVEORDERAUTHZ._options = None
  _CANCELDERIVATIVEORDERAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _BATCHCANCELDERIVATIVEORDERSAUTHZ._options = None
  _BATCHCANCELDERIVATIVEORDERSAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _BATCHUPDATEORDERSAUTHZ._options = None
  _BATCHUPDATEORDERSAUTHZ._serialized_options = b'\312\264-\rAuthorization'
  _CREATESPOTLIMITORDERAUTHZ._serialized_start=97
  _CREATESPOTLIMITORDERAUTHZ._serialized_end=186
  _CREATESPOTMARKETORDERAUTHZ._serialized_start=188
  _CREATESPOTMARKETORDERAUTHZ._serialized_end=278
  _BATCHCREATESPOTLIMITORDERSAUTHZ._serialized_start=280
  _BATCHCREATESPOTLIMITORDERSAUTHZ._serialized_end=375
  _CANCELSPOTORDERAUTHZ._serialized_start=377
  _CANCELSPOTORDERAUTHZ._serialized_end=461
  _BATCHCANCELSPOTORDERSAUTHZ._serialized_start=463
  _BATCHCANCELSPOTORDERSAUTHZ._serialized_end=553
  _CREATEDERIVATIVELIMITORDERAUTHZ._serialized_start=555
  _CREATEDERIVATIVELIMITORDERAUTHZ._serialized_end=650
  _CREATEDERIVATIVEMARKETORDERAUTHZ._serialized_start=652
  _CREATEDERIVATIVEMARKETORDERAUTHZ._serialized_end=748
  _BATCHCREATEDERIVATIVELIMITORDERSAUTHZ._serialized_start=750
  _BATCHCREATEDERIVATIVELIMITORDERSAUTHZ._serialized_end=851
  _CANCELDERIVATIVEORDERAUTHZ._serialized_start=853
  _CANCELDERIVATIVEORDERAUTHZ._serialized_end=943
  _BATCHCANCELDERIVATIVEORDERSAUTHZ._serialized_start=945
  _BATCHCANCELDERIVATIVEORDERSAUTHZ._serialized_end=1041
  _BATCHUPDATEORDERSAUTHZ._serialized_start=1043
  _BATCHUPDATEORDERSAUTHZ._serialized_end=1159
# @@protoc_insertion_point(module_scope)

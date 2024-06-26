# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.ocr.v1beta1 import ocr_pb2 as injective_dot_ocr_dot_v1beta1_dot_ocr__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.ocr.v1beta1 import genesis_pb2 as injective_dot_ocr_dot_v1beta1_dot_genesis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!injective/ocr/v1beta1/query.proto\x12\x15injective.ocr.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1finjective/ocr/v1beta1/ocr.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a#injective/ocr/v1beta1/genesis.proto\"\x14\n\x12QueryParamsRequest\"J\n\x13QueryParamsResponse\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1d.injective.ocr.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\")\n\x16QueryFeedConfigRequest\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\"\x92\x01\n\x17QueryFeedConfigResponse\x12?\n\x10\x66\x65\x65\x64_config_info\x18\x01 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfo\x12\x36\n\x0b\x66\x65\x65\x64_config\x18\x02 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfig\"-\n\x1aQueryFeedConfigInfoRequest\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\"\x9d\x01\n\x1bQueryFeedConfigInfoResponse\x12?\n\x10\x66\x65\x65\x64_config_info\x18\x01 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfo\x12=\n\x0f\x65poch_and_round\x18\x02 \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRound\"*\n\x17QueryLatestRoundRequest\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\"f\n\x18QueryLatestRoundResponse\x12\x17\n\x0flatest_round_id\x18\x01 \x01(\x04\x12\x31\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32#.injective.ocr.v1beta1.Transmission\"8\n%QueryLatestTransmissionDetailsRequest\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\"\xb1\x01\n&QueryLatestTransmissionDetailsResponse\x12\x15\n\rconfig_digest\x18\x01 \x01(\x0c\x12=\n\x0f\x65poch_and_round\x18\x02 \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRound\x12\x31\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32#.injective.ocr.v1beta1.Transmission\"-\n\x16QueryOwedAmountRequest\x12\x13\n\x0btransmitter\x18\x01 \x01(\t\"J\n\x17QueryOwedAmountResponse\x12/\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x19\n\x17QueryModuleStateRequest\"N\n\x18QueryModuleStateResponse\x12\x32\n\x05state\x18\x01 \x01(\x0b\x32#.injective.ocr.v1beta1.GenesisState2\xbb\t\n\x05Query\x12\x86\x01\n\x06Params\x12).injective.ocr.v1beta1.QueryParamsRequest\x1a*.injective.ocr.v1beta1.QueryParamsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/chainlink/ocr/v1beta1/params\x12\xa1\x01\n\nFeedConfig\x12-.injective.ocr.v1beta1.QueryFeedConfigRequest\x1a..injective.ocr.v1beta1.QueryFeedConfigResponse\"4\x82\xd3\xe4\x93\x02.\x12,/chainlink/ocr/v1beta1/feed_config/{feed_id}\x12\xb2\x01\n\x0e\x46\x65\x65\x64\x43onfigInfo\x12\x31.injective.ocr.v1beta1.QueryFeedConfigInfoRequest\x1a\x32.injective.ocr.v1beta1.QueryFeedConfigInfoResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/chainlink/ocr/v1beta1/feed_config_info/{feed_id}\x12\xa5\x01\n\x0bLatestRound\x12..injective.ocr.v1beta1.QueryLatestRoundRequest\x1a/.injective.ocr.v1beta1.QueryLatestRoundResponse\"5\x82\xd3\xe4\x93\x02/\x12-/chainlink/ocr/v1beta1/latest_round/{feed_id}\x12\xde\x01\n\x19LatestTransmissionDetails\x12<.injective.ocr.v1beta1.QueryLatestTransmissionDetailsRequest\x1a=.injective.ocr.v1beta1.QueryLatestTransmissionDetailsResponse\"D\x82\xd3\xe4\x93\x02>\x12</chainlink/ocr/v1beta1/latest_transmission_details/{feed_id}\x12\xa5\x01\n\nOwedAmount\x12-.injective.ocr.v1beta1.QueryOwedAmountRequest\x1a..injective.ocr.v1beta1.QueryOwedAmountResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/chainlink/ocr/v1beta1/owed_amount/{transmitter}\x12\x9e\x01\n\x0eOcrModuleState\x12..injective.ocr.v1beta1.QueryModuleStateRequest\x1a/.injective.ocr.v1beta1.QueryModuleStateResponse\"+\x82\xd3\xe4\x93\x02%\x12#/chainlink/ocr/v1beta1/module_stateBKZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYOWEDAMOUNTRESPONSE.fields_by_name['amount']._options = None
  _QUERYOWEDAMOUNTRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\037\022\035/chainlink/ocr/v1beta1/params'
  _QUERY.methods_by_name['FeedConfig']._options = None
  _QUERY.methods_by_name['FeedConfig']._serialized_options = b'\202\323\344\223\002.\022,/chainlink/ocr/v1beta1/feed_config/{feed_id}'
  _QUERY.methods_by_name['FeedConfigInfo']._options = None
  _QUERY.methods_by_name['FeedConfigInfo']._serialized_options = b'\202\323\344\223\0023\0221/chainlink/ocr/v1beta1/feed_config_info/{feed_id}'
  _QUERY.methods_by_name['LatestRound']._options = None
  _QUERY.methods_by_name['LatestRound']._serialized_options = b'\202\323\344\223\002/\022-/chainlink/ocr/v1beta1/latest_round/{feed_id}'
  _QUERY.methods_by_name['LatestTransmissionDetails']._options = None
  _QUERY.methods_by_name['LatestTransmissionDetails']._serialized_options = b'\202\323\344\223\002>\022</chainlink/ocr/v1beta1/latest_transmission_details/{feed_id}'
  _QUERY.methods_by_name['OwedAmount']._options = None
  _QUERY.methods_by_name['OwedAmount']._serialized_options = b'\202\323\344\223\0022\0220/chainlink/ocr/v1beta1/owed_amount/{transmitter}'
  _QUERY.methods_by_name['OcrModuleState']._options = None
  _QUERY.methods_by_name['OcrModuleState']._serialized_options = b'\202\323\344\223\002%\022#/chainlink/ocr/v1beta1/module_state'
  _QUERYPARAMSREQUEST._serialized_start=214
  _QUERYPARAMSREQUEST._serialized_end=234
  _QUERYPARAMSRESPONSE._serialized_start=236
  _QUERYPARAMSRESPONSE._serialized_end=310
  _QUERYFEEDCONFIGREQUEST._serialized_start=312
  _QUERYFEEDCONFIGREQUEST._serialized_end=353
  _QUERYFEEDCONFIGRESPONSE._serialized_start=356
  _QUERYFEEDCONFIGRESPONSE._serialized_end=502
  _QUERYFEEDCONFIGINFOREQUEST._serialized_start=504
  _QUERYFEEDCONFIGINFOREQUEST._serialized_end=549
  _QUERYFEEDCONFIGINFORESPONSE._serialized_start=552
  _QUERYFEEDCONFIGINFORESPONSE._serialized_end=709
  _QUERYLATESTROUNDREQUEST._serialized_start=711
  _QUERYLATESTROUNDREQUEST._serialized_end=753
  _QUERYLATESTROUNDRESPONSE._serialized_start=755
  _QUERYLATESTROUNDRESPONSE._serialized_end=857
  _QUERYLATESTTRANSMISSIONDETAILSREQUEST._serialized_start=859
  _QUERYLATESTTRANSMISSIONDETAILSREQUEST._serialized_end=915
  _QUERYLATESTTRANSMISSIONDETAILSRESPONSE._serialized_start=918
  _QUERYLATESTTRANSMISSIONDETAILSRESPONSE._serialized_end=1095
  _QUERYOWEDAMOUNTREQUEST._serialized_start=1097
  _QUERYOWEDAMOUNTREQUEST._serialized_end=1142
  _QUERYOWEDAMOUNTRESPONSE._serialized_start=1144
  _QUERYOWEDAMOUNTRESPONSE._serialized_end=1218
  _QUERYMODULESTATEREQUEST._serialized_start=1220
  _QUERYMODULESTATEREQUEST._serialized_end=1245
  _QUERYMODULESTATERESPONSE._serialized_start=1247
  _QUERYMODULESTATERESPONSE._serialized_end=1325
  _QUERY._serialized_start=1328
  _QUERY._serialized_end=2539
# @@protoc_insertion_point(module_scope)

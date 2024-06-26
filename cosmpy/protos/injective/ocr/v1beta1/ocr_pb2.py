# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/ocr.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1finjective/ocr/v1beta1/ocr.proto\x12\x15injective.ocr.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"W\n\x06Params\x12\x12\n\nlink_denom\x18\x01 \x01(\t\x12\x1d\n\x15payout_block_interval\x18\x02 \x01(\x04\x12\x14\n\x0cmodule_admin\x18\x03 \x01(\t:\x04\xe8\xa0\x1f\x01\"\xcc\x01\n\nFeedConfig\x12\x0f\n\x07signers\x18\x01 \x03(\t\x12\x14\n\x0ctransmitters\x18\x02 \x03(\t\x12\t\n\x01\x66\x18\x03 \x01(\r\x12\x16\n\x0eonchain_config\x18\x04 \x01(\x0c\x12\x1f\n\x17offchain_config_version\x18\x05 \x01(\x04\x12\x17\n\x0foffchain_config\x18\x06 \x01(\x0c\x12:\n\rmodule_params\x18\x07 \x01(\x0b\x32#.injective.ocr.v1beta1.ModuleParams\"~\n\x0e\x46\x65\x65\x64\x43onfigInfo\x12\x1c\n\x14latest_config_digest\x18\x01 \x01(\x0c\x12\t\n\x01\x66\x18\x02 \x01(\r\x12\t\n\x01n\x18\x03 \x01(\r\x12\x14\n\x0c\x63onfig_count\x18\x04 \x01(\x04\x12\"\n\x1alatest_config_block_number\x18\x05 \x01(\x03\"\xb0\x03\n\x0cModuleParams\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\x12\x42\n\nmin_answer\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nmax_answer\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12L\n\x14link_per_observation\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12M\n\x15link_per_transmission\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x12\n\nlink_denom\x18\x06 \x01(\t\x12\x16\n\x0eunique_reports\x18\x07 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x12\n\nfeed_admin\x18\t \x01(\t\x12\x15\n\rbilling_admin\x18\n \x01(\t\"\xaa\x01\n\x0e\x43ontractConfig\x12\x14\n\x0c\x63onfig_count\x18\x01 \x01(\x04\x12\x0f\n\x07signers\x18\x02 \x03(\t\x12\x14\n\x0ctransmitters\x18\x03 \x03(\t\x12\t\n\x01\x66\x18\x04 \x01(\r\x12\x16\n\x0eonchain_config\x18\x05 \x01(\x0c\x12\x1f\n\x17offchain_config_version\x18\x06 \x01(\x04\x12\x17\n\x0foffchain_config\x18\x07 \x01(\x0c\"\x92\x01\n\x11SetConfigProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x31\n\x06\x63onfig\x18\x03 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfig:&\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xd0\x03\n\x0e\x46\x65\x65\x64Properties\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\x12\t\n\x01\x66\x18\x02 \x01(\r\x12\x16\n\x0eonchain_config\x18\x03 \x01(\x0c\x12\x1f\n\x17offchain_config_version\x18\x04 \x01(\x04\x12\x17\n\x0foffchain_config\x18\x05 \x01(\x0c\x12\x42\n\nmin_answer\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nmax_answer\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12L\n\x14link_per_observation\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12M\n\x15link_per_transmission\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x16\n\x0eunique_reports\x18\n \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\"\xdf\x01\n\x16SetBatchConfigProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07signers\x18\x03 \x03(\t\x12\x14\n\x0ctransmitters\x18\x04 \x03(\t\x12\x12\n\nlink_denom\x18\x05 \x01(\t\x12>\n\x0f\x66\x65\x65\x64_properties\x18\x06 \x03(\x0b\x32%.injective.ocr.v1beta1.FeedProperties:&\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"*\n\x18OracleObservationsCounts\x12\x0e\n\x06\x63ounts\x18\x01 \x03(\r\"F\n\x11GasReimbursements\x12\x31\n\x0ereimbursements\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.Coin\"7\n\x05Payee\x12\x18\n\x10transmitter_addr\x18\x01 \x01(\t\x12\x14\n\x0cpayment_addr\x18\x02 \x01(\t\"\x8e\x01\n\x0cTransmission\x12>\n\x06\x61nswer\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x1e\n\x16observations_timestamp\x18\x02 \x01(\x03\x12\x1e\n\x16transmission_timestamp\x18\x03 \x01(\x03\"-\n\rEpochAndRound\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\r\n\x05round\x18\x02 \x01(\x04\"\x81\x01\n\x06Report\x12\x1e\n\x16observations_timestamp\x18\x01 \x01(\x03\x12\x11\n\tobservers\x18\x02 \x01(\x0c\x12\x44\n\x0cobservations\x18\x03 \x03(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"g\n\x0cReportToSign\x12\x15\n\rconfig_digest\x18\x01 \x01(\x0c\x12\r\n\x05\x65poch\x18\x02 \x01(\x04\x12\r\n\x05round\x18\x03 \x01(\x04\x12\x12\n\nextra_hash\x18\x04 \x01(\x0c\x12\x0e\n\x06report\x18\x05 \x01(\x0c\"p\n\x0f\x45ventOraclePaid\x12\x18\n\x10transmitter_addr\x18\x01 \x01(\t\x12\x12\n\npayee_addr\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\xd1\x01\n\x12\x45ventAnswerUpdated\x12?\n\x07\x63urrent\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12@\n\x08round_id\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x38\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"\x9f\x01\n\rEventNewRound\x12@\n\x08round_id\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x12\n\nstarted_by\x18\x02 \x01(\t\x12\x38\n\nstarted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"8\n\x10\x45ventTransmitted\x12\x15\n\rconfig_digest\x18\x01 \x01(\x0c\x12\r\n\x05\x65poch\x18\x02 \x01(\x04\"\xe8\x02\n\x14\x45ventNewTransmission\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\x12\x1b\n\x13\x61ggregator_round_id\x18\x02 \x01(\r\x12>\n\x06\x61nswer\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x13\n\x0btransmitter\x18\x04 \x01(\t\x12\x1e\n\x16observations_timestamp\x18\x05 \x01(\x03\x12\x44\n\x0cobservations\x18\x06 \x03(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x11\n\tobservers\x18\x07 \x01(\x0c\x12\x15\n\rconfig_digest\x18\x08 \x01(\x0c\x12=\n\x0f\x65poch_and_round\x18\t \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRound\"\xbc\x01\n\x0e\x45ventConfigSet\x12\x15\n\rconfig_digest\x18\x01 \x01(\x0c\x12$\n\x1cprevious_config_block_number\x18\x02 \x01(\x03\x12\x31\n\x06\x63onfig\x18\x03 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfig\x12:\n\x0b\x63onfig_info\x18\x04 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfoBKZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.ocr_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\350\240\037\001'
  _MODULEPARAMS.fields_by_name['min_answer']._options = None
  _MODULEPARAMS.fields_by_name['min_answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MODULEPARAMS.fields_by_name['max_answer']._options = None
  _MODULEPARAMS.fields_by_name['max_answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MODULEPARAMS.fields_by_name['link_per_observation']._options = None
  _MODULEPARAMS.fields_by_name['link_per_observation']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MODULEPARAMS.fields_by_name['link_per_transmission']._options = None
  _MODULEPARAMS.fields_by_name['link_per_transmission']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _SETCONFIGPROPOSAL._options = None
  _SETCONFIGPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _FEEDPROPERTIES.fields_by_name['min_answer']._options = None
  _FEEDPROPERTIES.fields_by_name['min_answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _FEEDPROPERTIES.fields_by_name['max_answer']._options = None
  _FEEDPROPERTIES.fields_by_name['max_answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _FEEDPROPERTIES.fields_by_name['link_per_observation']._options = None
  _FEEDPROPERTIES.fields_by_name['link_per_observation']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _FEEDPROPERTIES.fields_by_name['link_per_transmission']._options = None
  _FEEDPROPERTIES.fields_by_name['link_per_transmission']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _SETBATCHCONFIGPROPOSAL._options = None
  _SETBATCHCONFIGPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _TRANSMISSION.fields_by_name['answer']._options = None
  _TRANSMISSION.fields_by_name['answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _REPORT.fields_by_name['observations']._options = None
  _REPORT.fields_by_name['observations']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTORACLEPAID.fields_by_name['amount']._options = None
  _EVENTORACLEPAID.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _EVENTANSWERUPDATED.fields_by_name['current']._options = None
  _EVENTANSWERUPDATED.fields_by_name['current']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTANSWERUPDATED.fields_by_name['round_id']._options = None
  _EVENTANSWERUPDATED.fields_by_name['round_id']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTANSWERUPDATED.fields_by_name['updated_at']._options = None
  _EVENTANSWERUPDATED.fields_by_name['updated_at']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _EVENTNEWROUND.fields_by_name['round_id']._options = None
  _EVENTNEWROUND.fields_by_name['round_id']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTNEWROUND.fields_by_name['started_at']._options = None
  _EVENTNEWROUND.fields_by_name['started_at']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _EVENTNEWTRANSMISSION.fields_by_name['answer']._options = None
  _EVENTNEWTRANSMISSION.fields_by_name['answer']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTNEWTRANSMISSION.fields_by_name['observations']._options = None
  _EVENTNEWTRANSMISSION.fields_by_name['observations']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS._serialized_start=172
  _PARAMS._serialized_end=259
  _FEEDCONFIG._serialized_start=262
  _FEEDCONFIG._serialized_end=466
  _FEEDCONFIGINFO._serialized_start=468
  _FEEDCONFIGINFO._serialized_end=594
  _MODULEPARAMS._serialized_start=597
  _MODULEPARAMS._serialized_end=1029
  _CONTRACTCONFIG._serialized_start=1032
  _CONTRACTCONFIG._serialized_end=1202
  _SETCONFIGPROPOSAL._serialized_start=1205
  _SETCONFIGPROPOSAL._serialized_end=1351
  _FEEDPROPERTIES._serialized_start=1354
  _FEEDPROPERTIES._serialized_end=1818
  _SETBATCHCONFIGPROPOSAL._serialized_start=1821
  _SETBATCHCONFIGPROPOSAL._serialized_end=2044
  _ORACLEOBSERVATIONSCOUNTS._serialized_start=2046
  _ORACLEOBSERVATIONSCOUNTS._serialized_end=2088
  _GASREIMBURSEMENTS._serialized_start=2090
  _GASREIMBURSEMENTS._serialized_end=2160
  _PAYEE._serialized_start=2162
  _PAYEE._serialized_end=2217
  _TRANSMISSION._serialized_start=2220
  _TRANSMISSION._serialized_end=2362
  _EPOCHANDROUND._serialized_start=2364
  _EPOCHANDROUND._serialized_end=2409
  _REPORT._serialized_start=2412
  _REPORT._serialized_end=2541
  _REPORTTOSIGN._serialized_start=2543
  _REPORTTOSIGN._serialized_end=2646
  _EVENTORACLEPAID._serialized_start=2648
  _EVENTORACLEPAID._serialized_end=2760
  _EVENTANSWERUPDATED._serialized_start=2763
  _EVENTANSWERUPDATED._serialized_end=2972
  _EVENTNEWROUND._serialized_start=2975
  _EVENTNEWROUND._serialized_end=3134
  _EVENTTRANSMITTED._serialized_start=3136
  _EVENTTRANSMITTED._serialized_end=3192
  _EVENTNEWTRANSMISSION._serialized_start=3195
  _EVENTNEWTRANSMISSION._serialized_end=3555
  _EVENTCONFIGSET._serialized_start=3558
  _EVENTCONFIGSET._serialized_end=3746
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!injective/oracle/v1beta1/tx.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xa0\x01\n\x16MsgRelayProviderPrices\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\x0f\n\x07symbols\x18\x03 \x03(\t\x12>\n\x06prices\x18\x04 \x03(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x13\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\" \n\x1eMsgRelayProviderPricesResponse\"\x99\x01\n\x16MsgRelayPriceFeedPrice\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x02 \x03(\t\x12\r\n\x05quote\x18\x03 \x03(\t\x12=\n\x05price\x18\x04 \x03(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x13\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\" \n\x1eMsgRelayPriceFeedPriceResponse\"}\n\x11MsgRelayBandRates\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12\r\n\x05rates\x18\x03 \x03(\x04\x12\x15\n\rresolve_times\x18\x04 \x03(\x04\x12\x12\n\nrequestIDs\x18\x05 \x03(\x04:\x0c\x82\xe7\xb0*\x07relayer\"\x1b\n\x19MsgRelayBandRatesResponse\"e\n\x18MsgRelayCoinbaseMessages\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08messages\x18\x02 \x03(\x0c\x12\x12\n\nsignatures\x18\x03 \x03(\x0c:\x13\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\"\"\n MsgRelayCoinbaseMessagesResponse\"Q\n\x16MsgRequestBandIBCRates\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\x04:\x13\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\" \n\x1eMsgRequestBandIBCRatesResponse\"\x81\x01\n\x12MsgRelayPythPrices\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x46\n\x12price_attestations\x18\x02 \x03(\x0b\x32*.injective.oracle.v1beta1.PriceAttestation:\x13\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgRelayPythPricesResponse\"\x86\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x06params\x18\x02 \x01(\x0b\x32 .injective.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xf4\x06\n\x03Msg\x12\x81\x01\n\x13RelayProviderPrices\x12\x30.injective.oracle.v1beta1.MsgRelayProviderPrices\x1a\x38.injective.oracle.v1beta1.MsgRelayProviderPricesResponse\x12\x81\x01\n\x13RelayPriceFeedPrice\x12\x30.injective.oracle.v1beta1.MsgRelayPriceFeedPrice\x1a\x38.injective.oracle.v1beta1.MsgRelayPriceFeedPriceResponse\x12r\n\x0eRelayBandRates\x12+.injective.oracle.v1beta1.MsgRelayBandRates\x1a\x33.injective.oracle.v1beta1.MsgRelayBandRatesResponse\x12\x81\x01\n\x13RequestBandIBCRates\x12\x30.injective.oracle.v1beta1.MsgRequestBandIBCRates\x1a\x38.injective.oracle.v1beta1.MsgRequestBandIBCRatesResponse\x12\x87\x01\n\x15RelayCoinbaseMessages\x12\x32.injective.oracle.v1beta1.MsgRelayCoinbaseMessages\x1a:.injective.oracle.v1beta1.MsgRelayCoinbaseMessagesResponse\x12u\n\x0fRelayPythPrices\x12,.injective.oracle.v1beta1.MsgRelayPythPrices\x1a\x34.injective.oracle.v1beta1.MsgRelayPythPricesResponse\x12l\n\x0cUpdateParams\x12).injective.oracle.v1beta1.MsgUpdateParams\x1a\x31.injective.oracle.v1beta1.MsgUpdateParamsResponseBNZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types'
  _MSGRELAYPROVIDERPRICES.fields_by_name['prices']._options = None
  _MSGRELAYPROVIDERPRICES.fields_by_name['prices']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGRELAYPROVIDERPRICES._options = None
  _MSGRELAYPROVIDERPRICES._serialized_options = b'\350\240\037\000\210\240\037\000\202\347\260*\006sender'
  _MSGRELAYPRICEFEEDPRICE.fields_by_name['price']._options = None
  _MSGRELAYPRICEFEEDPRICE.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGRELAYPRICEFEEDPRICE._options = None
  _MSGRELAYPRICEFEEDPRICE._serialized_options = b'\350\240\037\000\210\240\037\000\202\347\260*\006sender'
  _MSGRELAYBANDRATES._options = None
  _MSGRELAYBANDRATES._serialized_options = b'\202\347\260*\007relayer'
  _MSGRELAYCOINBASEMESSAGES._options = None
  _MSGRELAYCOINBASEMESSAGES._serialized_options = b'\350\240\037\000\210\240\037\000\202\347\260*\006sender'
  _MSGREQUESTBANDIBCRATES._options = None
  _MSGREQUESTBANDIBCRATES._serialized_options = b'\350\240\037\000\210\240\037\000\202\347\260*\006sender'
  _MSGRELAYPYTHPRICES._options = None
  _MSGRELAYPYTHPRICES._serialized_options = b'\350\240\037\000\210\240\037\000\202\347\260*\006sender'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSGRELAYPROVIDERPRICES._serialized_start=177
  _MSGRELAYPROVIDERPRICES._serialized_end=337
  _MSGRELAYPROVIDERPRICESRESPONSE._serialized_start=339
  _MSGRELAYPROVIDERPRICESRESPONSE._serialized_end=371
  _MSGRELAYPRICEFEEDPRICE._serialized_start=374
  _MSGRELAYPRICEFEEDPRICE._serialized_end=527
  _MSGRELAYPRICEFEEDPRICERESPONSE._serialized_start=529
  _MSGRELAYPRICEFEEDPRICERESPONSE._serialized_end=561
  _MSGRELAYBANDRATES._serialized_start=563
  _MSGRELAYBANDRATES._serialized_end=688
  _MSGRELAYBANDRATESRESPONSE._serialized_start=690
  _MSGRELAYBANDRATESRESPONSE._serialized_end=717
  _MSGRELAYCOINBASEMESSAGES._serialized_start=719
  _MSGRELAYCOINBASEMESSAGES._serialized_end=820
  _MSGRELAYCOINBASEMESSAGESRESPONSE._serialized_start=822
  _MSGRELAYCOINBASEMESSAGESRESPONSE._serialized_end=856
  _MSGREQUESTBANDIBCRATES._serialized_start=858
  _MSGREQUESTBANDIBCRATES._serialized_end=939
  _MSGREQUESTBANDIBCRATESRESPONSE._serialized_start=941
  _MSGREQUESTBANDIBCRATESRESPONSE._serialized_end=973
  _MSGRELAYPYTHPRICES._serialized_start=976
  _MSGRELAYPYTHPRICES._serialized_end=1105
  _MSGRELAYPYTHPRICESRESPONSE._serialized_start=1107
  _MSGRELAYPYTHPRICESRESPONSE._serialized_end=1135
  _MSGUPDATEPARAMS._serialized_start=1138
  _MSGUPDATEPARAMS._serialized_end=1272
  _MSGUPDATEPARAMSRESPONSE._serialized_start=1274
  _MSGUPDATEPARAMSRESPONSE._serialized_end=1299
  _MSG._serialized_start=1302
  _MSG._serialized_end=2186
# @@protoc_insertion_point(module_scope)

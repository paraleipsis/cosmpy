# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/msgs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.peggy.v1 import types_pb2 as injective_dot_peggy_dot_v1_dot_types__pb2
from injective.peggy.v1 import params_pb2 as injective_dot_peggy_dot_v1_dot_params__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dinjective/peggy/v1/msgs.proto\x12\x12injective.peggy.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1einjective/peggy/v1/types.proto\x1a\x1finjective/peggy/v1/params.proto\x1a\x19google/protobuf/any.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\"X\n\x1bMsgSetOrchestratorAddresses\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x14\n\x0corchestrator\x18\x02 \x01(\t\x12\x13\n\x0b\x65th_address\x18\x03 \x01(\t\"%\n#MsgSetOrchestratorAddressesResponse\"r\n\x10MsgValsetConfirm\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x14\n\x0corchestrator\x18\x02 \x01(\t\x12\x13\n\x0b\x65th_address\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x1a\n\x18MsgValsetConfirmResponse\"\xa3\x01\n\x0cMsgSendToEth\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x65th_dest\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x33\n\nbridge_fee\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x0b\x82\xe7\xb0*\x06sender\"\x16\n\x14MsgSendToEthResponse\"I\n\x0fMsgRequestBatch\x12\x14\n\x0corchestrator\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x19\n\x17MsgRequestBatchResponse\"\x88\x01\n\x0fMsgConfirmBatch\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\x12\x12\n\neth_signer\x18\x03 \x01(\t\x12\x14\n\x0corchestrator\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x19\n\x17MsgConfirmBatchResponse\"\xfd\x01\n\x0fMsgDepositClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x03 \x01(\t\x12>\n\x06\x61mount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x17\n\x0f\x65thereum_sender\x18\x05 \x01(\t\x12\x17\n\x0f\x63osmos_receiver\x18\x06 \x01(\t\x12\x14\n\x0corchestrator\x18\x07 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x19\n\x17MsgDepositClaimResponse\"\x93\x01\n\x10MsgWithdrawClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x13\n\x0b\x62\x61tch_nonce\x18\x03 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\x14\n\x0corchestrator\x18\x05 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x1a\n\x18MsgWithdrawClaimResponse\"\xc9\x01\n\x15MsgERC20DeployedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x14\n\x0c\x63osmos_denom\x18\x03 \x01(\t\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06symbol\x18\x06 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x07 \x01(\x04\x12\x14\n\x0corchestrator\x18\x08 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x1f\n\x1dMsgERC20DeployedClaimResponse\"I\n\x12MsgCancelSendToEth\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x04\x12\x0e\n\x06sender\x18\x02 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgCancelSendToEthResponse\"v\n\x1dMsgSubmitBadSignatureEvidence\x12%\n\x07subject\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tsignature\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\'\n%MsgSubmitBadSignatureEvidenceResponse\"\x94\x02\n\x15MsgValsetUpdatedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0cvalset_nonce\x18\x02 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x03 \x01(\x04\x12\x34\n\x07members\x18\x04 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x45\n\rreward_amount\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x14\n\x0creward_token\x18\x06 \x01(\t\x12\x14\n\x0corchestrator\x18\x07 \x01(\t:\x11\x82\xe7\xb0*\x0corchestrator\"\x1f\n\x1dMsgValsetUpdatedClaimResponse\"\x80\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32\x1a.injective.peggy.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xa6\x0e\n\x03Msg\x12\x8f\x01\n\rValsetConfirm\x12$.injective.peggy.v1.MsgValsetConfirm\x1a,.injective.peggy.v1.MsgValsetConfirmResponse\"*\x82\xd3\xe4\x93\x02$\"\"/injective/peggy/v1/valset_confirm\x12\x80\x01\n\tSendToEth\x12 .injective.peggy.v1.MsgSendToEth\x1a(.injective.peggy.v1.MsgSendToEthResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1f/injective/peggy/v1/send_to_eth\x12\x8b\x01\n\x0cRequestBatch\x12#.injective.peggy.v1.MsgRequestBatch\x1a+.injective.peggy.v1.MsgRequestBatchResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/request_batch\x12\x8b\x01\n\x0c\x43onfirmBatch\x12#.injective.peggy.v1.MsgConfirmBatch\x1a+.injective.peggy.v1.MsgConfirmBatchResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/confirm_batch\x12\x8b\x01\n\x0c\x44\x65positClaim\x12#.injective.peggy.v1.MsgDepositClaim\x1a+.injective.peggy.v1.MsgDepositClaimResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/deposit_claim\x12\x8f\x01\n\rWithdrawClaim\x12$.injective.peggy.v1.MsgWithdrawClaim\x1a,.injective.peggy.v1.MsgWithdrawClaimResponse\"*\x82\xd3\xe4\x93\x02$\"\"/injective/peggy/v1/withdraw_claim\x12\xa3\x01\n\x11ValsetUpdateClaim\x12).injective.peggy.v1.MsgValsetUpdatedClaim\x1a\x31.injective.peggy.v1.MsgValsetUpdatedClaimResponse\"0\x82\xd3\xe4\x93\x02*\"(/injective/peggy/v1/valset_updated_claim\x12\xa4\x01\n\x12\x45RC20DeployedClaim\x12).injective.peggy.v1.MsgERC20DeployedClaim\x1a\x31.injective.peggy.v1.MsgERC20DeployedClaimResponse\"0\x82\xd3\xe4\x93\x02*\"(/injective/peggy/v1/erc20_deployed_claim\x12\xba\x01\n\x18SetOrchestratorAddresses\x12/.injective.peggy.v1.MsgSetOrchestratorAddresses\x1a\x37.injective.peggy.v1.MsgSetOrchestratorAddressesResponse\"4\x82\xd3\xe4\x93\x02.\",/injective/peggy/v1/set_orchestrator_address\x12\x99\x01\n\x0f\x43\x61ncelSendToEth\x12&.injective.peggy.v1.MsgCancelSendToEth\x1a..injective.peggy.v1.MsgCancelSendToEthResponse\".\x82\xd3\xe4\x93\x02(\"&/injective/peggy/v1/cancel_send_to_eth\x12\xc5\x01\n\x1aSubmitBadSignatureEvidence\x12\x31.injective.peggy.v1.MsgSubmitBadSignatureEvidence\x1a\x39.injective.peggy.v1.MsgSubmitBadSignatureEvidenceResponse\"9\x82\xd3\xe4\x93\x02\x33\"1/injective/peggy/v1/submit_bad_signature_evidence\x12`\n\x0cUpdateParams\x12#.injective.peggy.v1.MsgUpdateParams\x1a+.injective.peggy.v1.MsgUpdateParamsResponseBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.msgs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _MSGVALSETCONFIRM._options = None
  _MSGVALSETCONFIRM._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGSENDTOETH.fields_by_name['amount']._options = None
  _MSGSENDTOETH.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGSENDTOETH.fields_by_name['bridge_fee']._options = None
  _MSGSENDTOETH.fields_by_name['bridge_fee']._serialized_options = b'\310\336\037\000'
  _MSGSENDTOETH._options = None
  _MSGSENDTOETH._serialized_options = b'\202\347\260*\006sender'
  _MSGREQUESTBATCH._options = None
  _MSGREQUESTBATCH._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGCONFIRMBATCH._options = None
  _MSGCONFIRMBATCH._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGDEPOSITCLAIM.fields_by_name['amount']._options = None
  _MSGDEPOSITCLAIM.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGDEPOSITCLAIM._options = None
  _MSGDEPOSITCLAIM._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGWITHDRAWCLAIM._options = None
  _MSGWITHDRAWCLAIM._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGERC20DEPLOYEDCLAIM._options = None
  _MSGERC20DEPLOYEDCLAIM._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGCANCELSENDTOETH._options = None
  _MSGCANCELSENDTOETH._serialized_options = b'\202\347\260*\006sender'
  _MSGSUBMITBADSIGNATUREEVIDENCE._options = None
  _MSGSUBMITBADSIGNATUREEVIDENCE._serialized_options = b'\202\347\260*\006sender'
  _MSGVALSETUPDATEDCLAIM.fields_by_name['reward_amount']._options = None
  _MSGVALSETUPDATEDCLAIM.fields_by_name['reward_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGVALSETUPDATEDCLAIM._options = None
  _MSGVALSETUPDATEDCLAIM._serialized_options = b'\202\347\260*\014orchestrator'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSG.methods_by_name['ValsetConfirm']._options = None
  _MSG.methods_by_name['ValsetConfirm']._serialized_options = b'\202\323\344\223\002$\"\"/injective/peggy/v1/valset_confirm'
  _MSG.methods_by_name['SendToEth']._options = None
  _MSG.methods_by_name['SendToEth']._serialized_options = b'\202\323\344\223\002!\"\037/injective/peggy/v1/send_to_eth'
  _MSG.methods_by_name['RequestBatch']._options = None
  _MSG.methods_by_name['RequestBatch']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/request_batch'
  _MSG.methods_by_name['ConfirmBatch']._options = None
  _MSG.methods_by_name['ConfirmBatch']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/confirm_batch'
  _MSG.methods_by_name['DepositClaim']._options = None
  _MSG.methods_by_name['DepositClaim']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/deposit_claim'
  _MSG.methods_by_name['WithdrawClaim']._options = None
  _MSG.methods_by_name['WithdrawClaim']._serialized_options = b'\202\323\344\223\002$\"\"/injective/peggy/v1/withdraw_claim'
  _MSG.methods_by_name['ValsetUpdateClaim']._options = None
  _MSG.methods_by_name['ValsetUpdateClaim']._serialized_options = b'\202\323\344\223\002*\"(/injective/peggy/v1/valset_updated_claim'
  _MSG.methods_by_name['ERC20DeployedClaim']._options = None
  _MSG.methods_by_name['ERC20DeployedClaim']._serialized_options = b'\202\323\344\223\002*\"(/injective/peggy/v1/erc20_deployed_claim'
  _MSG.methods_by_name['SetOrchestratorAddresses']._options = None
  _MSG.methods_by_name['SetOrchestratorAddresses']._serialized_options = b'\202\323\344\223\002.\",/injective/peggy/v1/set_orchestrator_address'
  _MSG.methods_by_name['CancelSendToEth']._options = None
  _MSG.methods_by_name['CancelSendToEth']._serialized_options = b'\202\323\344\223\002(\"&/injective/peggy/v1/cancel_send_to_eth'
  _MSG.methods_by_name['SubmitBadSignatureEvidence']._options = None
  _MSG.methods_by_name['SubmitBadSignatureEvidence']._serialized_options = b'\202\323\344\223\0023\"1/injective/peggy/v1/submit_bad_signature_evidence'
  _MSGSETORCHESTRATORADDRESSES._serialized_start=281
  _MSGSETORCHESTRATORADDRESSES._serialized_end=369
  _MSGSETORCHESTRATORADDRESSESRESPONSE._serialized_start=371
  _MSGSETORCHESTRATORADDRESSESRESPONSE._serialized_end=408
  _MSGVALSETCONFIRM._serialized_start=410
  _MSGVALSETCONFIRM._serialized_end=524
  _MSGVALSETCONFIRMRESPONSE._serialized_start=526
  _MSGVALSETCONFIRMRESPONSE._serialized_end=552
  _MSGSENDTOETH._serialized_start=555
  _MSGSENDTOETH._serialized_end=718
  _MSGSENDTOETHRESPONSE._serialized_start=720
  _MSGSENDTOETHRESPONSE._serialized_end=742
  _MSGREQUESTBATCH._serialized_start=744
  _MSGREQUESTBATCH._serialized_end=817
  _MSGREQUESTBATCHRESPONSE._serialized_start=819
  _MSGREQUESTBATCHRESPONSE._serialized_end=844
  _MSGCONFIRMBATCH._serialized_start=847
  _MSGCONFIRMBATCH._serialized_end=983
  _MSGCONFIRMBATCHRESPONSE._serialized_start=985
  _MSGCONFIRMBATCHRESPONSE._serialized_end=1010
  _MSGDEPOSITCLAIM._serialized_start=1013
  _MSGDEPOSITCLAIM._serialized_end=1266
  _MSGDEPOSITCLAIMRESPONSE._serialized_start=1268
  _MSGDEPOSITCLAIMRESPONSE._serialized_end=1293
  _MSGWITHDRAWCLAIM._serialized_start=1296
  _MSGWITHDRAWCLAIM._serialized_end=1443
  _MSGWITHDRAWCLAIMRESPONSE._serialized_start=1445
  _MSGWITHDRAWCLAIMRESPONSE._serialized_end=1471
  _MSGERC20DEPLOYEDCLAIM._serialized_start=1474
  _MSGERC20DEPLOYEDCLAIM._serialized_end=1675
  _MSGERC20DEPLOYEDCLAIMRESPONSE._serialized_start=1677
  _MSGERC20DEPLOYEDCLAIMRESPONSE._serialized_end=1708
  _MSGCANCELSENDTOETH._serialized_start=1710
  _MSGCANCELSENDTOETH._serialized_end=1783
  _MSGCANCELSENDTOETHRESPONSE._serialized_start=1785
  _MSGCANCELSENDTOETHRESPONSE._serialized_end=1813
  _MSGSUBMITBADSIGNATUREEVIDENCE._serialized_start=1815
  _MSGSUBMITBADSIGNATUREEVIDENCE._serialized_end=1933
  _MSGSUBMITBADSIGNATUREEVIDENCERESPONSE._serialized_start=1935
  _MSGSUBMITBADSIGNATUREEVIDENCERESPONSE._serialized_end=1974
  _MSGVALSETUPDATEDCLAIM._serialized_start=1977
  _MSGVALSETUPDATEDCLAIM._serialized_end=2253
  _MSGVALSETUPDATEDCLAIMRESPONSE._serialized_start=2255
  _MSGVALSETUPDATEDCLAIMRESPONSE._serialized_end=2286
  _MSGUPDATEPARAMS._serialized_start=2289
  _MSGUPDATEPARAMS._serialized_end=2417
  _MSGUPDATEPARAMSRESPONSE._serialized_start=2419
  _MSGUPDATEPARAMSRESPONSE._serialized_end=2444
  _MSG._serialized_start=2447
  _MSG._serialized_end=4277
# @@protoc_insertion_point(module_scope)
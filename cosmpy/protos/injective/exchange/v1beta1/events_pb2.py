# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from injective.exchange.v1beta1 import exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/exchange/v1beta1/events.proto\x12\x1ainjective.exchange.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a)injective/exchange/v1beta1/exchange.proto\"\xb4\x01\n\x17\x45ventBatchSpotExecution\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0e\n\x06is_buy\x18\x02 \x01(\x08\x12@\n\rexecutionType\x18\x03 \x01(\x0e\x32).injective.exchange.v1beta1.ExecutionType\x12\x34\n\x06trades\x18\x04 \x03(\x0b\x32$.injective.exchange.v1beta1.TradeLog\"\xa8\x02\n\x1d\x45ventBatchDerivativeExecution\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0e\n\x06is_buy\x18\x02 \x01(\x08\x12\x16\n\x0eis_liquidation\x18\x03 \x01(\x08\x12J\n\x12\x63umulative_funding\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12@\n\rexecutionType\x18\x05 \x01(\x0e\x32).injective.exchange.v1beta1.ExecutionType\x12>\n\x06trades\x18\x06 \x03(\x0b\x32..injective.exchange.v1beta1.DerivativeTradeLog\"\x81\x02\n\x1d\x45ventLostFundsFromLiquidation\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\x0c\x12_\n\'lost_funds_from_available_during_payout\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12U\n\x1dlost_funds_from_order_cancels\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"t\n\x1c\x45ventBatchDerivativePosition\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x41\n\tpositions\x18\x02 \x03(\x0b\x32..injective.exchange.v1beta1.SubaccountPosition\"\x7f\n\x1b\x45ventDerivativeMarketPaused\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x14\n\x0csettle_price\x18\x02 \x01(\t\x12\x1b\n\x13total_missing_funds\x18\x03 \x01(\t\x12\x1a\n\x12missing_funds_rate\x18\x04 \x01(\t\"d\n\x1b\x45ventMarketBeyondBankruptcy\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x14\n\x0csettle_price\x18\x02 \x01(\t\x12\x1c\n\x14missing_market_funds\x18\x03 \x01(\t\"_\n\x18\x45ventAllPositionsHaircut\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x14\n\x0csettle_price\x18\x02 \x01(\t\x12\x1a\n\x12missing_funds_rate\x18\x03 \x01(\t\"g\n\x1e\x45ventBinaryOptionsMarketUpdate\x12\x45\n\x06market\x18\x01 \x01(\x0b\x32/.injective.exchange.v1beta1.BinaryOptionsMarketB\x04\xc8\xde\x1f\x00\"\xa8\x01\n\x12\x45ventNewSpotOrders\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12>\n\nbuy_orders\x18\x02 \x03(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrder\x12?\n\x0bsell_orders\x18\x03 \x03(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrder\"\xba\x01\n\x18\x45ventNewDerivativeOrders\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x44\n\nbuy_orders\x18\x02 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrder\x12\x45\n\x0bsell_orders\x18\x03 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrder\"j\n\x14\x45ventCancelSpotOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12?\n\x05order\x18\x02 \x01(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrderB\x04\xc8\xde\x1f\x00\"U\n\x15\x45ventSpotMarketUpdate\x12<\n\x06market\x18\x01 \x01(\x0b\x32&.injective.exchange.v1beta1.SpotMarketB\x04\xc8\xde\x1f\x00\"\x81\x02\n\x1a\x45ventPerpetualMarketUpdate\x12\x42\n\x06market\x18\x01 \x01(\x0b\x32,.injective.exchange.v1beta1.DerivativeMarketB\x04\xc8\xde\x1f\x00\x12T\n\x15perpetual_market_info\x18\x02 \x01(\x0b\x32/.injective.exchange.v1beta1.PerpetualMarketInfoB\x04\xc8\xde\x1f\x01\x12I\n\x07\x66unding\x18\x03 \x01(\x0b\x32\x32.injective.exchange.v1beta1.PerpetualMarketFundingB\x04\xc8\xde\x1f\x01\"\xc3\x01\n\x1e\x45ventExpiryFuturesMarketUpdate\x12\x42\n\x06market\x18\x01 \x01(\x0b\x32,.injective.exchange.v1beta1.DerivativeMarketB\x04\xc8\xde\x1f\x00\x12]\n\x1a\x65xpiry_futures_market_info\x18\x03 \x01(\x0b\x32\x33.injective.exchange.v1beta1.ExpiryFuturesMarketInfoB\x04\xc8\xde\x1f\x01\"\xa6\x02\n!EventPerpetualMarketFundingUpdate\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12I\n\x07\x66unding\x18\x02 \x01(\x0b\x32\x32.injective.exchange.v1beta1.PerpetualMarketFundingB\x04\xc8\xde\x1f\x00\x12\x19\n\x11is_hourly_funding\x18\x03 \x01(\x08\x12\x44\n\x0c\x66unding_rate\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12\x42\n\nmark_price\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\"u\n\x16\x45ventSubaccountDeposit\x12\x13\n\x0bsrc_address\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\x0c\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"v\n\x17\x45ventSubaccountWithdraw\x12\x15\n\rsubaccount_id\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64st_address\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x87\x01\n\x1e\x45ventSubaccountBalanceTransfer\x12\x19\n\x11src_subaccount_id\x18\x01 \x01(\t\x12\x19\n\x11\x64st_subaccount_id\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"]\n\x17\x45ventBatchDepositUpdate\x12\x42\n\x0f\x64\x65posit_updates\x18\x01 \x03(\x0b\x32).injective.exchange.v1beta1.DepositUpdate\"\xb5\x01\n\x1b\x44\x65rivativeMarketOrderCancel\x12M\n\x0cmarket_order\x18\x01 \x01(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrderB\x04\xc8\xde\x1f\x01\x12G\n\x0f\x63\x61ncel_quantity\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xef\x01\n\x1a\x45ventCancelDerivativeOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\risLimitCancel\x18\x02 \x01(\x08\x12K\n\x0blimit_order\x18\x03 \x01(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderB\x04\xc8\xde\x1f\x01\x12Z\n\x13market_order_cancel\x18\x04 \x01(\x0b\x32\x37.injective.exchange.v1beta1.DerivativeMarketOrderCancelB\x04\xc8\xde\x1f\x01\"]\n\x18\x45ventFeeDiscountSchedule\x12\x41\n\x08schedule\x18\x01 \x01(\x0b\x32/.injective.exchange.v1beta1.FeeDiscountSchedule\"\xbf\x01\n EventTradingRewardCampaignUpdate\x12L\n\rcampaign_info\x18\x01 \x01(\x0b\x32\x35.injective.exchange.v1beta1.TradingRewardCampaignInfo\x12M\n\x15\x63\x61mpaign_reward_pools\x18\x02 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool\"e\n\x1e\x45ventTradingRewardDistribution\x12\x43\n\x0f\x61\x63\x63ount_rewards\x18\x01 \x03(\x0b\x32*.injective.exchange.v1beta1.AccountRewards\"\x94\x01\n\"EventNewConditionalDerivativeOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12:\n\x05order\x18\x02 \x01(\x0b\x32+.injective.exchange.v1beta1.DerivativeOrder\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\x12\x11\n\tis_market\x18\x04 \x01(\x08\"\xed\x01\n%EventCancelConditionalDerivativeOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\risLimitCancel\x18\x02 \x01(\x08\x12K\n\x0blimit_order\x18\x03 \x01(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderB\x04\xc8\xde\x1f\x01\x12M\n\x0cmarket_order\x18\x04 \x01(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrderB\x04\xc8\xde\x1f\x01\"\x8c\x01\n&EventConditionalDerivativeOrderTrigger\x12\x11\n\tmarket_id\x18\x01 \x01(\x0c\x12\x16\n\x0eisLimitTrigger\x18\x02 \x01(\x08\x12\x1c\n\x14triggered_order_hash\x18\x03 \x01(\x0c\x12\x19\n\x11placed_order_hash\x18\x04 \x01(\x0c\"@\n\x0e\x45ventOrderFail\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x12\x0e\n\x06hashes\x18\x02 \x03(\x0c\x12\r\n\x05\x66lags\x18\x03 \x03(\r\"~\n+EventAtomicMarketOrderFeeMultipliersUpdated\x12O\n\x16market_fee_multipliers\x18\x01 \x03(\x0b\x32/.injective.exchange.v1beta1.MarketFeeMultiplier\"\xa2\x01\n\x14\x45ventOrderbookUpdate\x12\x41\n\x0cspot_updates\x18\x01 \x03(\x0b\x32+.injective.exchange.v1beta1.OrderbookUpdate\x12G\n\x12\x64\x65rivative_updates\x18\x02 \x03(\x0b\x32+.injective.exchange.v1beta1.OrderbookUpdate\"X\n\x0fOrderbookUpdate\x12\x0b\n\x03seq\x18\x01 \x01(\x04\x12\x38\n\torderbook\x18\x02 \x01(\x0b\x32%.injective.exchange.v1beta1.Orderbook\"\x8d\x01\n\tOrderbook\x12\x11\n\tmarket_id\x18\x01 \x01(\x0c\x12\x35\n\nbuy_levels\x18\x02 \x03(\x0b\x32!.injective.exchange.v1beta1.Level\x12\x36\n\x0bsell_levels\x18\x03 \x03(\x0b\x32!.injective.exchange.v1beta1.LevelBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _EVENTBATCHDERIVATIVEEXECUTION.fields_by_name['cumulative_funding']._options = None
  _EVENTBATCHDERIVATIVEEXECUTION.fields_by_name['cumulative_funding']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _EVENTLOSTFUNDSFROMLIQUIDATION.fields_by_name['lost_funds_from_available_during_payout']._options = None
  _EVENTLOSTFUNDSFROMLIQUIDATION.fields_by_name['lost_funds_from_available_during_payout']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTLOSTFUNDSFROMLIQUIDATION.fields_by_name['lost_funds_from_order_cancels']._options = None
  _EVENTLOSTFUNDSFROMLIQUIDATION.fields_by_name['lost_funds_from_order_cancels']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTBINARYOPTIONSMARKETUPDATE.fields_by_name['market']._options = None
  _EVENTBINARYOPTIONSMARKETUPDATE.fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _EVENTCANCELSPOTORDER.fields_by_name['order']._options = None
  _EVENTCANCELSPOTORDER.fields_by_name['order']._serialized_options = b'\310\336\037\000'
  _EVENTSPOTMARKETUPDATE.fields_by_name['market']._options = None
  _EVENTSPOTMARKETUPDATE.fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['market']._options = None
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['perpetual_market_info']._options = None
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['perpetual_market_info']._serialized_options = b'\310\336\037\001'
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['funding']._options = None
  _EVENTPERPETUALMARKETUPDATE.fields_by_name['funding']._serialized_options = b'\310\336\037\001'
  _EVENTEXPIRYFUTURESMARKETUPDATE.fields_by_name['market']._options = None
  _EVENTEXPIRYFUTURESMARKETUPDATE.fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _EVENTEXPIRYFUTURESMARKETUPDATE.fields_by_name['expiry_futures_market_info']._options = None
  _EVENTEXPIRYFUTURESMARKETUPDATE.fields_by_name['expiry_futures_market_info']._serialized_options = b'\310\336\037\001'
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['funding']._options = None
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['funding']._serialized_options = b'\310\336\037\000'
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['funding_rate']._options = None
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['funding_rate']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['mark_price']._options = None
  _EVENTPERPETUALMARKETFUNDINGUPDATE.fields_by_name['mark_price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _EVENTSUBACCOUNTDEPOSIT.fields_by_name['amount']._options = None
  _EVENTSUBACCOUNTDEPOSIT.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _EVENTSUBACCOUNTWITHDRAW.fields_by_name['amount']._options = None
  _EVENTSUBACCOUNTWITHDRAW.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _EVENTSUBACCOUNTBALANCETRANSFER.fields_by_name['amount']._options = None
  _EVENTSUBACCOUNTBALANCETRANSFER.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _DERIVATIVEMARKETORDERCANCEL.fields_by_name['market_order']._options = None
  _DERIVATIVEMARKETORDERCANCEL.fields_by_name['market_order']._serialized_options = b'\310\336\037\001'
  _DERIVATIVEMARKETORDERCANCEL.fields_by_name['cancel_quantity']._options = None
  _DERIVATIVEMARKETORDERCANCEL.fields_by_name['cancel_quantity']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTCANCELDERIVATIVEORDER.fields_by_name['limit_order']._options = None
  _EVENTCANCELDERIVATIVEORDER.fields_by_name['limit_order']._serialized_options = b'\310\336\037\001'
  _EVENTCANCELDERIVATIVEORDER.fields_by_name['market_order_cancel']._options = None
  _EVENTCANCELDERIVATIVEORDER.fields_by_name['market_order_cancel']._serialized_options = b'\310\336\037\001'
  _EVENTCANCELCONDITIONALDERIVATIVEORDER.fields_by_name['limit_order']._options = None
  _EVENTCANCELCONDITIONALDERIVATIVEORDER.fields_by_name['limit_order']._serialized_options = b'\310\336\037\001'
  _EVENTCANCELCONDITIONALDERIVATIVEORDER.fields_by_name['market_order']._options = None
  _EVENTCANCELCONDITIONALDERIVATIVEORDER.fields_by_name['market_order']._serialized_options = b'\310\336\037\001'
  _EVENTBATCHSPOTEXECUTION._serialized_start=208
  _EVENTBATCHSPOTEXECUTION._serialized_end=388
  _EVENTBATCHDERIVATIVEEXECUTION._serialized_start=391
  _EVENTBATCHDERIVATIVEEXECUTION._serialized_end=687
  _EVENTLOSTFUNDSFROMLIQUIDATION._serialized_start=690
  _EVENTLOSTFUNDSFROMLIQUIDATION._serialized_end=947
  _EVENTBATCHDERIVATIVEPOSITION._serialized_start=949
  _EVENTBATCHDERIVATIVEPOSITION._serialized_end=1065
  _EVENTDERIVATIVEMARKETPAUSED._serialized_start=1067
  _EVENTDERIVATIVEMARKETPAUSED._serialized_end=1194
  _EVENTMARKETBEYONDBANKRUPTCY._serialized_start=1196
  _EVENTMARKETBEYONDBANKRUPTCY._serialized_end=1296
  _EVENTALLPOSITIONSHAIRCUT._serialized_start=1298
  _EVENTALLPOSITIONSHAIRCUT._serialized_end=1393
  _EVENTBINARYOPTIONSMARKETUPDATE._serialized_start=1395
  _EVENTBINARYOPTIONSMARKETUPDATE._serialized_end=1498
  _EVENTNEWSPOTORDERS._serialized_start=1501
  _EVENTNEWSPOTORDERS._serialized_end=1669
  _EVENTNEWDERIVATIVEORDERS._serialized_start=1672
  _EVENTNEWDERIVATIVEORDERS._serialized_end=1858
  _EVENTCANCELSPOTORDER._serialized_start=1860
  _EVENTCANCELSPOTORDER._serialized_end=1966
  _EVENTSPOTMARKETUPDATE._serialized_start=1968
  _EVENTSPOTMARKETUPDATE._serialized_end=2053
  _EVENTPERPETUALMARKETUPDATE._serialized_start=2056
  _EVENTPERPETUALMARKETUPDATE._serialized_end=2313
  _EVENTEXPIRYFUTURESMARKETUPDATE._serialized_start=2316
  _EVENTEXPIRYFUTURESMARKETUPDATE._serialized_end=2511
  _EVENTPERPETUALMARKETFUNDINGUPDATE._serialized_start=2514
  _EVENTPERPETUALMARKETFUNDINGUPDATE._serialized_end=2808
  _EVENTSUBACCOUNTDEPOSIT._serialized_start=2810
  _EVENTSUBACCOUNTDEPOSIT._serialized_end=2927
  _EVENTSUBACCOUNTWITHDRAW._serialized_start=2929
  _EVENTSUBACCOUNTWITHDRAW._serialized_end=3047
  _EVENTSUBACCOUNTBALANCETRANSFER._serialized_start=3050
  _EVENTSUBACCOUNTBALANCETRANSFER._serialized_end=3185
  _EVENTBATCHDEPOSITUPDATE._serialized_start=3187
  _EVENTBATCHDEPOSITUPDATE._serialized_end=3280
  _DERIVATIVEMARKETORDERCANCEL._serialized_start=3283
  _DERIVATIVEMARKETORDERCANCEL._serialized_end=3464
  _EVENTCANCELDERIVATIVEORDER._serialized_start=3467
  _EVENTCANCELDERIVATIVEORDER._serialized_end=3706
  _EVENTFEEDISCOUNTSCHEDULE._serialized_start=3708
  _EVENTFEEDISCOUNTSCHEDULE._serialized_end=3801
  _EVENTTRADINGREWARDCAMPAIGNUPDATE._serialized_start=3804
  _EVENTTRADINGREWARDCAMPAIGNUPDATE._serialized_end=3995
  _EVENTTRADINGREWARDDISTRIBUTION._serialized_start=3997
  _EVENTTRADINGREWARDDISTRIBUTION._serialized_end=4098
  _EVENTNEWCONDITIONALDERIVATIVEORDER._serialized_start=4101
  _EVENTNEWCONDITIONALDERIVATIVEORDER._serialized_end=4249
  _EVENTCANCELCONDITIONALDERIVATIVEORDER._serialized_start=4252
  _EVENTCANCELCONDITIONALDERIVATIVEORDER._serialized_end=4489
  _EVENTCONDITIONALDERIVATIVEORDERTRIGGER._serialized_start=4492
  _EVENTCONDITIONALDERIVATIVEORDERTRIGGER._serialized_end=4632
  _EVENTORDERFAIL._serialized_start=4634
  _EVENTORDERFAIL._serialized_end=4698
  _EVENTATOMICMARKETORDERFEEMULTIPLIERSUPDATED._serialized_start=4700
  _EVENTATOMICMARKETORDERFEEMULTIPLIERSUPDATED._serialized_end=4826
  _EVENTORDERBOOKUPDATE._serialized_start=4829
  _EVENTORDERBOOKUPDATE._serialized_end=4991
  _ORDERBOOKUPDATE._serialized_start=4993
  _ORDERBOOKUPDATE._serialized_end=5081
  _ORDERBOOK._serialized_start=5084
  _ORDERBOOK._serialized_end=5225
# @@protoc_insertion_point(module_scope)

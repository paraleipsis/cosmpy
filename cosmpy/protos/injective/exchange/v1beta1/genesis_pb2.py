# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.exchange.v1beta1 import exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2
from injective.exchange.v1beta1 import tx_pb2 as injective_dot_exchange_dot_v1beta1_dot_tx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(injective/exchange/v1beta1/genesis.proto\x12\x1ainjective.exchange.v1beta1\x1a)injective/exchange/v1beta1/exchange.proto\x1a#injective/exchange/v1beta1/tx.proto\x1a\x14gogoproto/gogo.proto\"\x91\x15\n\x0cGenesisState\x12\x38\n\x06params\x18\x01 \x01(\x0b\x32\".injective.exchange.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12<\n\x0cspot_markets\x18\x02 \x03(\x0b\x32&.injective.exchange.v1beta1.SpotMarket\x12H\n\x12\x64\x65rivative_markets\x18\x03 \x03(\x0b\x32,.injective.exchange.v1beta1.DerivativeMarket\x12G\n\x0espot_orderbook\x18\x04 \x03(\x0b\x32).injective.exchange.v1beta1.SpotOrderBookB\x04\xc8\xde\x1f\x00\x12S\n\x14\x64\x65rivative_orderbook\x18\x05 \x03(\x0b\x32/.injective.exchange.v1beta1.DerivativeOrderBookB\x04\xc8\xde\x1f\x00\x12;\n\x08\x62\x61lances\x18\x06 \x03(\x0b\x32#.injective.exchange.v1beta1.BalanceB\x04\xc8\xde\x1f\x00\x12G\n\tpositions\x18\x07 \x03(\x0b\x32..injective.exchange.v1beta1.DerivativePositionB\x04\xc8\xde\x1f\x00\x12R\n\x17subaccount_trade_nonces\x18\x08 \x03(\x0b\x32+.injective.exchange.v1beta1.SubaccountNonceB\x04\xc8\xde\x1f\x00\x12h\n expiry_futures_market_info_state\x18\t \x03(\x0b\x32\x38.injective.exchange.v1beta1.ExpiryFuturesMarketInfoStateB\x04\xc8\xde\x1f\x00\x12T\n\x15perpetual_market_info\x18\n \x03(\x0b\x32/.injective.exchange.v1beta1.PerpetualMarketInfoB\x04\xc8\xde\x1f\x00\x12\x65\n\x1eperpetual_market_funding_state\x18\x0b \x03(\x0b\x32\x37.injective.exchange.v1beta1.PerpetualMarketFundingStateB\x04\xc8\xde\x1f\x00\x12p\n&derivative_market_settlement_scheduled\x18\x0c \x03(\x0b\x32:.injective.exchange.v1beta1.DerivativeMarketSettlementInfoB\x04\xc8\xde\x1f\x00\x12 \n\x18is_spot_exchange_enabled\x18\r \x01(\x08\x12\'\n\x1fis_derivatives_exchange_enabled\x18\x0e \x01(\x08\x12[\n\x1ctrading_reward_campaign_info\x18\x0f \x01(\x0b\x32\x35.injective.exchange.v1beta1.TradingRewardCampaignInfo\x12]\n%trading_reward_pool_campaign_schedule\x18\x10 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool\x12n\n&trading_reward_campaign_account_points\x18\x11 \x03(\x0b\x32>.injective.exchange.v1beta1.TradingRewardCampaignAccountPoints\x12N\n\x15\x66\x65\x65_discount_schedule\x18\x12 \x01(\x0b\x32/.injective.exchange.v1beta1.FeeDiscountSchedule\x12\\\n\x1d\x66\x65\x65_discount_account_tier_ttl\x18\x13 \x03(\x0b\x32\x35.injective.exchange.v1beta1.FeeDiscountAccountTierTTL\x12h\n#fee_discount_bucket_volume_accounts\x18\x14 \x03(\x0b\x32;.injective.exchange.v1beta1.FeeDiscountBucketVolumeAccounts\x12#\n\x1bis_first_fee_cycle_finished\x18\x15 \x01(\x08\x12\x65\n-pending_trading_reward_pool_campaign_schedule\x18\x16 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool\x12}\n.pending_trading_reward_campaign_account_points\x18\x17 \x03(\x0b\x32\x45.injective.exchange.v1beta1.TradingRewardCampaignAccountPendingPoints\x12!\n\x19rewards_opt_out_addresses\x18\x18 \x03(\t\x12J\n\x18historical_trade_records\x18\x19 \x03(\x0b\x32(.injective.exchange.v1beta1.TradeRecords\x12O\n\x16\x62inary_options_markets\x18\x1a \x03(\x0b\x32/.injective.exchange.v1beta1.BinaryOptionsMarket\x12:\n2binary_options_market_ids_scheduled_for_settlement\x18\x1b \x03(\t\x12\x30\n(spot_market_ids_scheduled_to_force_close\x18\x1c \x03(\t\x12G\n\x0e\x64\x65nom_decimals\x18\x1d \x03(\x0b\x32).injective.exchange.v1beta1.DenomDecimalsB\x04\xc8\xde\x1f\x00\x12\x65\n!conditional_derivative_orderbooks\x18\x1e \x03(\x0b\x32:.injective.exchange.v1beta1.ConditionalDerivativeOrderBook\x12O\n\x16market_fee_multipliers\x18\x1f \x03(\x0b\x32/.injective.exchange.v1beta1.MarketFeeMultiplier\x12J\n\x13orderbook_sequences\x18  \x03(\x0b\x32-.injective.exchange.v1beta1.OrderbookSequence\x12W\n\x12subaccount_volumes\x18! \x03(\x0b\x32;.injective.exchange.v1beta1.AggregateSubaccountVolumeRecord\x12@\n\x0emarket_volumes\x18\" \x03(\x0b\x32(.injective.exchange.v1beta1.MarketVolume\"8\n\x11OrderbookSequence\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x11\n\tmarket_id\x18\x02 \x01(\t\"n\n\x19\x46\x65\x65\x44iscountAccountTierTTL\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12@\n\x08tier_ttl\x18\x02 \x01(\x0b\x32..injective.exchange.v1beta1.FeeDiscountTierTTL\"\x84\x01\n\x1f\x46\x65\x65\x44iscountBucketVolumeAccounts\x12\x1e\n\x16\x62ucket_start_timestamp\x18\x01 \x01(\x03\x12\x41\n\x0e\x61\x63\x63ount_volume\x18\x02 \x03(\x0b\x32).injective.exchange.v1beta1.AccountVolume\"`\n\rAccountVolume\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12>\n\x06volume\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"u\n\"TradingRewardCampaignAccountPoints\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12>\n\x06points\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xa8\x01\n)TradingRewardCampaignAccountPendingPoints\x12#\n\x1breward_pool_start_timestamp\x18\x01 \x01(\x03\x12V\n\x0e\x61\x63\x63ount_points\x18\x02 \x03(\x0b\x32>.injective.exchange.v1beta1.TradingRewardCampaignAccountPoints\"{\n\rSpotOrderBook\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x11\n\tisBuySide\x18\x02 \x01(\x08\x12:\n\x06orders\x18\x03 \x03(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrder:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x87\x01\n\x13\x44\x65rivativeOrderBook\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x11\n\tisBuySide\x18\x02 \x01(\x08\x12@\n\x06orders\x18\x03 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrder:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xf3\x02\n\x1e\x43onditionalDerivativeOrderBook\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12J\n\x10limit_buy_orders\x18\x02 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrder\x12L\n\x11market_buy_orders\x18\x03 \x03(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrder\x12K\n\x11limit_sell_orders\x18\x04 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrder\x12M\n\x12market_sell_orders\x18\x05 \x03(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrder:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"p\n\x07\x42\x61lance\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\x35\n\x08\x64\x65posits\x18\x03 \x01(\x0b\x32#.injective.exchange.v1beta1.Deposit:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x80\x01\n\x12\x44\x65rivativePosition\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x36\n\x08position\x18\x03 \x01(\x0b\x32$.injective.exchange.v1beta1.Position:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x8a\x01\n\x0fSubaccountNonce\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12V\n\x16subaccount_trade_nonce\x18\x02 \x01(\x0b\x32\x30.injective.exchange.v1beta1.SubaccountTradeNonceB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"{\n\x1c\x45xpiryFuturesMarketInfoState\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12H\n\x0bmarket_info\x18\x02 \x01(\x0b\x32\x33.injective.exchange.v1beta1.ExpiryFuturesMarketInfo\"u\n\x1bPerpetualMarketFundingState\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x43\n\x07\x66unding\x18\x02 \x01(\x0b\x32\x32.injective.exchange.v1beta1.PerpetualMarketFundingBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['spot_orderbook']._options = None
  _GENESISSTATE.fields_by_name['spot_orderbook']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['derivative_orderbook']._options = None
  _GENESISSTATE.fields_by_name['derivative_orderbook']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['balances']._options = None
  _GENESISSTATE.fields_by_name['balances']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['positions']._options = None
  _GENESISSTATE.fields_by_name['positions']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['subaccount_trade_nonces']._options = None
  _GENESISSTATE.fields_by_name['subaccount_trade_nonces']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['expiry_futures_market_info_state']._options = None
  _GENESISSTATE.fields_by_name['expiry_futures_market_info_state']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['perpetual_market_info']._options = None
  _GENESISSTATE.fields_by_name['perpetual_market_info']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['perpetual_market_funding_state']._options = None
  _GENESISSTATE.fields_by_name['perpetual_market_funding_state']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['derivative_market_settlement_scheduled']._options = None
  _GENESISSTATE.fields_by_name['derivative_market_settlement_scheduled']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['denom_decimals']._options = None
  _GENESISSTATE.fields_by_name['denom_decimals']._serialized_options = b'\310\336\037\000'
  _ACCOUNTVOLUME.fields_by_name['volume']._options = None
  _ACCOUNTVOLUME.fields_by_name['volume']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _TRADINGREWARDCAMPAIGNACCOUNTPOINTS.fields_by_name['points']._options = None
  _TRADINGREWARDCAMPAIGNACCOUNTPOINTS.fields_by_name['points']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _SPOTORDERBOOK._options = None
  _SPOTORDERBOOK._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DERIVATIVEORDERBOOK._options = None
  _DERIVATIVEORDERBOOK._serialized_options = b'\350\240\037\000\210\240\037\000'
  _CONDITIONALDERIVATIVEORDERBOOK._options = None
  _CONDITIONALDERIVATIVEORDERBOOK._serialized_options = b'\350\240\037\000\210\240\037\000'
  _BALANCE._options = None
  _BALANCE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DERIVATIVEPOSITION._options = None
  _DERIVATIVEPOSITION._serialized_options = b'\350\240\037\000\210\240\037\000'
  _SUBACCOUNTNONCE.fields_by_name['subaccount_trade_nonce']._options = None
  _SUBACCOUNTNONCE.fields_by_name['subaccount_trade_nonce']._serialized_options = b'\310\336\037\000'
  _SUBACCOUNTNONCE._options = None
  _SUBACCOUNTNONCE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE._serialized_start=175
  _GENESISSTATE._serialized_end=2880
  _ORDERBOOKSEQUENCE._serialized_start=2882
  _ORDERBOOKSEQUENCE._serialized_end=2938
  _FEEDISCOUNTACCOUNTTIERTTL._serialized_start=2940
  _FEEDISCOUNTACCOUNTTIERTTL._serialized_end=3050
  _FEEDISCOUNTBUCKETVOLUMEACCOUNTS._serialized_start=3053
  _FEEDISCOUNTBUCKETVOLUMEACCOUNTS._serialized_end=3185
  _ACCOUNTVOLUME._serialized_start=3187
  _ACCOUNTVOLUME._serialized_end=3283
  _TRADINGREWARDCAMPAIGNACCOUNTPOINTS._serialized_start=3285
  _TRADINGREWARDCAMPAIGNACCOUNTPOINTS._serialized_end=3402
  _TRADINGREWARDCAMPAIGNACCOUNTPENDINGPOINTS._serialized_start=3405
  _TRADINGREWARDCAMPAIGNACCOUNTPENDINGPOINTS._serialized_end=3573
  _SPOTORDERBOOK._serialized_start=3575
  _SPOTORDERBOOK._serialized_end=3698
  _DERIVATIVEORDERBOOK._serialized_start=3701
  _DERIVATIVEORDERBOOK._serialized_end=3836
  _CONDITIONALDERIVATIVEORDERBOOK._serialized_start=3839
  _CONDITIONALDERIVATIVEORDERBOOK._serialized_end=4210
  _BALANCE._serialized_start=4212
  _BALANCE._serialized_end=4324
  _DERIVATIVEPOSITION._serialized_start=4327
  _DERIVATIVEPOSITION._serialized_end=4455
  _SUBACCOUNTNONCE._serialized_start=4458
  _SUBACCOUNTNONCE._serialized_end=4596
  _EXPIRYFUTURESMARKETINFOSTATE._serialized_start=4598
  _EXPIRYFUTURESMARKETINFOSTATE._serialized_end=4721
  _PERPETUALMARKETFUNDINGSTATE._serialized_start=4723
  _PERPETUALMARKETFUNDINGSTATE._serialized_end=4840
# @@protoc_insertion_point(module_scope)

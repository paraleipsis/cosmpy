"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.inflation.v1 import query_pb2 as evmos_dot_inflation_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Period = channel.unary_unary('/evmos.inflation.v1.Query/Period', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodResponse.FromString)
        self.EpochMintProvision = channel.unary_unary('/evmos.inflation.v1.Query/EpochMintProvision', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionResponse.FromString)
        self.SkippedEpochs = channel.unary_unary('/evmos.inflation.v1.Query/SkippedEpochs', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsResponse.FromString)
        self.CirculatingSupply = channel.unary_unary('/evmos.inflation.v1.Query/CirculatingSupply', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyResponse.FromString)
        self.InflationRate = channel.unary_unary('/evmos.inflation.v1.Query/InflationRate', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateResponse.FromString)
        self.Params = channel.unary_unary('/evmos.inflation.v1.Query/Params', request_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service.
    """

    def Period(self, request, context):
        """Period retrieves current period.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EpochMintProvision(self, request, context):
        """EpochMintProvision retrieves current minting epoch provision value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SkippedEpochs(self, request, context):
        """SkippedEpochs retrieves the total number of skipped epochs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CirculatingSupply(self, request, context):
        """CirculatingSupply retrieves the total number of tokens that are in
        circulation (i.e. excluding unvested tokens).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InflationRate(self, request, context):
        """InflationRate retrieves the inflation rate of the current period.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params retrieves the total set of minting parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Period': grpc.unary_unary_rpc_method_handler(servicer.Period, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodResponse.SerializeToString), 'EpochMintProvision': grpc.unary_unary_rpc_method_handler(servicer.EpochMintProvision, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionResponse.SerializeToString), 'SkippedEpochs': grpc.unary_unary_rpc_method_handler(servicer.SkippedEpochs, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsResponse.SerializeToString), 'CirculatingSupply': grpc.unary_unary_rpc_method_handler(servicer.CirculatingSupply, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyResponse.SerializeToString), 'InflationRate': grpc.unary_unary_rpc_method_handler(servicer.InflationRate, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.inflation.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service.
    """

    @staticmethod
    def Period(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/Period', evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QueryPeriodResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EpochMintProvision(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/EpochMintProvision', evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QueryEpochMintProvisionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SkippedEpochs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/SkippedEpochs', evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QuerySkippedEpochsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CirculatingSupply(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/CirculatingSupply', evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QueryCirculatingSupplyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InflationRate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/InflationRate', evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QueryInflationRateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.inflation.v1.Query/Params', evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, evmos_dot_inflation_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
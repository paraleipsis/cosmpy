# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.insurance.v1beta1 import query_pb2 as injective_dot_insurance_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InsuranceParams = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/InsuranceParams',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsResponse.FromString,
                )
        self.InsuranceFund = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/InsuranceFund',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundResponse.FromString,
                )
        self.InsuranceFunds = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/InsuranceFunds',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsResponse.FromString,
                )
        self.EstimatedRedemptions = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/EstimatedRedemptions',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsResponse.FromString,
                )
        self.PendingRedemptions = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/PendingRedemptions',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsResponse.FromString,
                )
        self.InsuranceModuleState = channel.unary_unary(
                '/injective.insurance.v1beta1.Query/InsuranceModuleState',
                request_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def InsuranceParams(self, request, context):
        """Retrieves insurance params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsuranceFund(self, request, context):
        """Retrieves individual insurance fund information from market id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsuranceFunds(self, request, context):
        """Retrieves all insurance funds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimatedRedemptions(self, request, context):
        """Retrives the value of insurance fund share token at current price (not
        pending redemption)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PendingRedemptions(self, request, context):
        """Retrieves pending redemptions' share token at current price
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsuranceModuleState(self, request, context):
        """Retrieves the entire insurance module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InsuranceParams': grpc.unary_unary_rpc_method_handler(
                    servicer.InsuranceParams,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsResponse.SerializeToString,
            ),
            'InsuranceFund': grpc.unary_unary_rpc_method_handler(
                    servicer.InsuranceFund,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundResponse.SerializeToString,
            ),
            'InsuranceFunds': grpc.unary_unary_rpc_method_handler(
                    servicer.InsuranceFunds,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsResponse.SerializeToString,
            ),
            'EstimatedRedemptions': grpc.unary_unary_rpc_method_handler(
                    servicer.EstimatedRedemptions,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsResponse.SerializeToString,
            ),
            'PendingRedemptions': grpc.unary_unary_rpc_method_handler(
                    servicer.PendingRedemptions,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsResponse.SerializeToString,
            ),
            'InsuranceModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.InsuranceModuleState,
                    request_deserializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.insurance.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def InsuranceParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/InsuranceParams',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsuranceFund(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/InsuranceFund',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsuranceFunds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/InsuranceFunds',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryInsuranceFundsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimatedRedemptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/EstimatedRedemptions',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryEstimatedRedemptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PendingRedemptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/PendingRedemptions',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryPendingRedemptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsuranceModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.insurance.v1beta1.Query/InsuranceModuleState',
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_insurance_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

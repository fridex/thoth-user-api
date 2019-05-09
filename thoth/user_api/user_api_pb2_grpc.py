# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from thoth.user_api import user_api_pb2 as thoth_dot_user__api_dot_user__api__pb2


class UserApiStub(object):
  """Interface exported by the server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Info = channel.unary_unary(
        '/stub.UserApi/Info',
        request_serializer=thoth_dot_user__api_dot_user__api__pb2.Empty.SerializeToString,
        response_deserializer=thoth_dot_user__api_dot_user__api__pb2.InfoResponse.FromString,
        )


class UserApiServicer(object):
  """Interface exported by the server.
  """

  def Info(self, request, context):
    """Obtains API Info.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=thoth_dot_user__api_dot_user__api__pb2.Empty.FromString,
          response_serializer=thoth_dot_user__api_dot_user__api__pb2.InfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'stub.UserApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

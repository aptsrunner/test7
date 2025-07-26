import grpc

import data_pb2_grpc
from service import DataService, serve

class ServiceFactory:
    @staticmethod
    def create_server():
        return serve()

    @staticmethod
    def create_client(address='localhost:50051'):
        channel = grpc.insecure_channel(address)
        stub = data_pb2_grpc.DataServiceStub(channel)
        return stub

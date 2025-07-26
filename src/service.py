import json
from concurrent import futures
import grpc

import data_pb2
import data_pb2_grpc

DATA_FILE = 'data/data.json'

class DataService(data_pb2_grpc.DataServiceServicer):
    def SaveData(self, request, context):
        data = request.data
        with open(DATA_FILE, 'w') as f:
            json.dump({'data': data}, f)
        return data_pb2.SaveDataResponse(success=True)

    def GetData(self, request, context):
        try:
            with open(DATA_FILE) as f:
                obj = json.load(f)
            data = obj.get('data', '')
        except FileNotFoundError:
            data = ''
        return data_pb2.GetDataResponse(data=data)


def serve(port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_DataServiceServicer_to_server(DataService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    return server

from factory import ServiceFactory
from data_pb2 import SaveDataRequest, GetDataRequest


def save(data: str):
    stub = ServiceFactory.create_client()
    response = stub.SaveData(SaveDataRequest(data=data))
    return response.success


def get():
    stub = ServiceFactory.create_client()
    response = stub.GetData(GetDataRequest())
    return response.data


if __name__ == '__main__':
    # Example usage
    if save('Hello World'):
        print('Data saved')
    print('Current data:', get())

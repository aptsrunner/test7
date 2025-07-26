import time
from factory import ServiceFactory


def main():
    server = ServiceFactory.create_server()
    print('Server started on port 50051')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()

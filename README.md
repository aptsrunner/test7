# test7 gRPC Example

This project demonstrates a simple gRPC service implemented in Python using the
factory pattern. The service performs two jobs:

1. **Save data** – receive a string and write it to `data/data.json`.
2. **Get data** – read the current value from `data/data.json` and return it.

## Requirements

- Python 3.12+
- `grpcio` and `grpcio-tools` (install via `pip install -r requirements.txt`)

## Running the server

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/server.py
```

The server listens on port `50051`.

## Example client usage

In another terminal, run:

```bash
python src/client.py
```

This script saves the string `"Hello World"` via gRPC and then fetches the
stored value.


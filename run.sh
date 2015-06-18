#!/bin/sh
echo "Starting Web Server... ($0)"
./rpc.py &

echo "Starting RPC Server... ($0)"
./server.py &

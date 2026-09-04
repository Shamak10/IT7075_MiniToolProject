#!/bin/bash
docker ps --filter name=juice-shop
echo
echo "=== curl http://localhost:3000 ==="
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:3000
echo
echo "=== ping container bridge IP (expected to fail on Docker Desktop for Mac) ==="
ping -c 2 172.17.0.2

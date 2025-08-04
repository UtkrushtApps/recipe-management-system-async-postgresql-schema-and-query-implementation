#!/bin/bash
set -e
cd /root/task
echo "[INFO] Starting Docker Compose deployment..."
docker-compose up -d
echo "[INFO] Waiting for PostgreSQL to be ready..."
PGREADY=1
for i in {1..30}; do
  docker exec recipe_pg pg_isready -U recipe_user -d recipe_db && PGREADY=0 && break
  sleep 2
done
if [ $PGREADY -ne 0 ]; then
  echo "[ERROR] PostgreSQL failed to start. Check docker logs."
  docker-compose logs db
  exit 1
fi
echo "[INFO] PostgreSQL is ready!"
echo "[INFO] Waiting for FastAPI to become available (up to 30s)..."
HAS_API=1
for i in {1..15}; do
  curl -s http://localhost:8000/docs >/dev/null && HAS_API=0 && break
  sleep 2
done
if [ $HAS_API -ne 0 ]; then
  echo "[ERROR] FastAPI application did not become available. Check logs."
  docker-compose logs fastapi
  exit 2
fi
echo "[INFO] FastAPI application is live and connected to the database."
echo "[INFO] All services started successfully."

# UMATT UI Server - Setup & Deployment Notes

---

## 🐳 Docker & Deployment Instructions

### ✅ Step 1: Clone the Repository
```bash
git https://github.com/umatt-ece/ui-server
cd ui-server
git pull origin feature/can_spi
```

### ✅ Step 2: Build the FastAPI Docker Image
```bash
docker buildx build -t fastapi-image .
```
> This builds the FastAPI app from your Dockerfile and tags it `fastapi-image`.

### ✅ Step 3: Run the Full Stack with Docker Compose
```bash
docker-compose up
```
> This will:
> - Launch the FastAPI container (on port `8000`)
> - Pull and launch Redis (on port `6379`)
> - Connect them over an internal Docker network

### ✅ Step 4: Access the App
- Open your browser: [http://localhost:8000](http://localhost:8000)
- WebSocket endpoint: `ws://localhost:8000/ws`

---

## 🛰️ CAN Bus Sync (mcu_driver)

To run the microcontroller data sync between Redis and CAN bus:
```bash
python3 -m mcu_driver.main
```
This script:
- Listens to CAN messages (via `Microcontroller` class)
- Reads/writes values from/to Redis using `ParameterStore`
- Keeps system state synchronized in real time

---

## 🔌 API Overview

### 📡 WebSocket `/ws`
Send JSON commands like:
```json
{
  "command": "set",
  "key": "SEAT_PRESENCE",
  "value": true
}
```

Supported commands:
- `set` → set single key
- `get` → get single key
- `mset` → set multiple keys
- `mget` → get multiple keys

### 🌐 REST Endpoints (from `items.py`)
- `GET /` → returns `{"Hello": "World"}`
- `GET /data` → returns all key-value pairs from `VARIABLES`
- `GET /test_bool/{key}/{value}` → sets a boolean key in Redis

---

## 🧹 Cleanup
```bash
docker-compose down                 # Stop containers

```

---

## 💡 Notes
- Redis host is `redis-container` (used in `ParameterStore`)
- Docker Compose uses a shared `redis` bridge network
- `.env` file support can be added for future environment config



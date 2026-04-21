# PyAPI

API CRUD sencilla con FastAPI, organizada con una estructura escalable.

## Ejecutar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Ejecutar con Docker Compose

```bash
docker compose up --build
```

Servicios disponibles:

- API: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Metrics: `http://localhost:8000/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (usuario: `admin`, password: `admin`)

El dashboard `PyAPI Overview` se provisiona automaticamente al iniciar Grafana.

## Estructura del proyecto

```text
.
├── app/
│   ├── api/
│   │   └── routes/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── monitoring/
│   ├── prometheus/
│   └── grafana/
│       └── provisioning/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── main.py
├── requirements.txt
└── .gitignore
```

## Endpoints

- `GET /`
- `POST /items`
- `GET /items`
- `GET /items/{item_id}`
- `PUT /items/{item_id}`
- `DELETE /items/{item_id}`

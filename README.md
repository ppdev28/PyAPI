# PyAPI

API CRUD sencilla con FastAPI, organizada con una estructura escalable.

## Ejecutar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

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

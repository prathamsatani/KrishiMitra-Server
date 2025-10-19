# KrishiMitra-Server

KrishiMitra is a Django-based backend for an agriculture assistant app that provides three main ML-powered services:

- Crop yield prediction
- Crop recommendation (which crop to grow given soil/weather/nutrients)
- Fertilizer recommendation (which fertilizer is best for a crop/soil state)

The project exposes a small REST API (Django + Django REST Framework) and includes lightweight ML engines under `mlengine/` used by the API views.

This repository contains the server-side code for the KrishiMitra project (APIs, admin, simple web pages and ML integration).

## Quick facts

- Framework: Django (project created with Django 5.x)
- API: Django REST Framework
- Language: Python 3.x
- DB (default dev): SQLite (file: `db.sqlite3`)
- ML deps: scikit-learn, xgboost, numpy, pandas

## Repository layout (important files)

- `manage.py` - Django CLI entrypoint
- `requirements.txt` - Python dependencies
- `Dockerfile`, `compose.yaml`, `README.Docker.md` - Docker configuration and tips
- `code4nature/` - Django project configuration (settings, urls, wsgi/asgi)
- `krishimitra/` - main app exposing API views and ML integration
- `mlengine/` - contains model code used by the API (`CropRecommendation`, `CropYieldPrediction`, `FertilizerRecommendation`)
- `mysite/`, `myadmin/` - small frontend/admin app templates

## Getting started (local development)

Prerequisites:

- Python 3.8+ (3.10+ recommended)
- pip
- (optional) virtualenv or venv

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Apply migrations and create a superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server

```powershell
python manage.py runserver
```

By default the app is configured with SQLite and DEBUG=False in `code4nature/settings.py`. For development you may want to set `DEBUG=True` in a local settings override or environment variable.

## Docker

The repository includes a `Dockerfile` and `compose.yaml`. To build and run with Docker Compose:

```powershell
docker compose up --build
```

The application will be available at http://localhost:8000.

See `README.Docker.md` for additional Docker tips (platforms, pushing images, etc.).

## API Endpoints

All API endpoints are mounted under `/api/` (see `code4nature/urls.py`). The `krishimitra` app exposes the following endpoints:

- POST /api/yieldpred/ - Predict crop yield
  - Required fields (JSON): username, name, season, state, area, annual_rainfall, fertilizer_usage, pesticide_usage
  - Response: predicted yield (numeric)

- POST /api/cropreco/ - Recommend a crop
  - Required fields (JSON): username, nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall
  - Response: recommended crop name (string)

- POST /api/fertreco/ - Recommend a fertilizer
  - Required fields (JSON): username, soil_color, nitrogen, phosphorus, potassium, ph, rainfall, temperature, crop
  - Response: recommended fertilizer name (string)

- POST /api/userdatainput/ - Save user data input (fields mapped in `krishimitra.serializers.UserDataInputSerializer`)

- POST /api/login/ and POST /api/signup/ - simple login/signup endpoints

Example curl (yield prediction):

```powershell
curl -X POST http://localhost:8000/api/yieldpred/ -H "Content-Type: application/json" -d '{"username":"alice","name":"Rice","season":"Kharif","state":"Karnataka","area":1.5,"annual_rainfall":1200,"fertilizer_usage":50,"pesticide_usage":2}'
```

Notes:

- The API uses serializers defined in `krishimitra/serializers.py` and stores inputs in models under `krishimitra/models.py`.
- The ML functions used by the views are in `mlengine/main.py` and the application uses `numpy`, `pandas`, `scikit-learn`, and `xgboost`.

## Configuration

- Default settings live in `code4nature/settings.py`. The project uses SQLite by default.
- For production you should:
  - Set `DEBUG=False` (already set in the repository)
  - Use a secure `SECRET_KEY` (do not commit real secret keys)
  - Configure a production database (Postgres, MySQL, etc.) and update `DATABASES` in settings or via environment variables
  - Add your domain(s) to `ALLOWED_HOSTS`

## Tests

There are small test files in the apps (e.g. `krishimitra/tests.py`, `mysite/tests.py`). To run tests:

```powershell
python manage.py test
```

## Contributing

If you'd like to contribute:

1. Fork the repository and create a feature branch
2. Add or update tests where appropriate
3. Open a PR with a clear description of changes

Notes for contributors:
- Keep data and model files out of the repository if they are large; use a separate storage or add them to a release
- Replace any committed secrets with environment variables or a secrets manager

## Troubleshooting

- If Django fails to import, ensure your virtual environment is activated and dependencies are installed.
- If you see ML model errors, verify the `mlengine/` code and ensure required model artifacts (if any) exist.

## License

This repository does not include an explicit license file. Add a `LICENSE` file if you intend to clarify reuse terms.

## Contact

If you need help, open an issue on the repository.

---

Generated README for quick onboarding and developer reference.

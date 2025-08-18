# Flask API Boilerplate

A clean and extensible Flask REST API project structure, ready for rapid development and easy scaling.

## Features
- Modular app structure
- SQLAlchemy ORM
- Marshmallow serialization
- Environment-based configuration
- Blueprint-based API routing
- Ready for testing and CI

## Project Structure
```
my_flask_api/
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── config.py           # Configuration settings
│   ├── extensions.py       # Flask extensions (DB, etc.)
│   ├── models/             # Data models
│   │   └── __init__.py
│   ├── resources/          # API resources/endpoints
│   │   ├── __init__.py
│   │   └── example.py
│   ├── schemas/            # Marshmallow schemas
│   │   └── __init__.py
│   └── utils/              # Utility functions
│       └── __init__.py
├── tests/                  # Test files
│   └── __init__.py
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables
├── .gitignore
├── run.py                  # Entry point
└── README.md
```

## Getting Started

### 1. Clone the repository
```
git clone https://github.com/jossieT/flask-api-boilerplate.git
cd flask-api-boilerplate
```

### 2. Create and activate a virtual environment (optional but recommended)
```
python -m venv venv
./venv/Scripts/activate  # On Windows
source venv/bin/activate # On Mac/Linux
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up environment variables
Edit the `.env` file as needed (default values are provided).

### 5. Run the application
```
python run.py
```
Visit [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello) to test the example endpoint.

## Testing
Add your tests in the `tests/` directory. To run tests (if using pytest):
```
pytest
```

## License
MIT

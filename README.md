# Basic FastAPI Service

A minimal FastAPI application to learn deployment and infrastructure concepts including GitHub Actions, AWS, and Terraform.

## Project Structure

```
.
├── app/
│   └── main.py          # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
└── README.md           # This file
```

## Quick Start

### Prerequisites
- Python 3.11+
- pip

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn app.main:app --reload
```

4. Visit `http://localhost:8000` in your browser

5. API documentation available at:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Docker

Build and run with Docker:

```bash
docker build -t basic-api .
docker run -p 8000:8000 basic-api
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /items/{item_id}` - Get item by ID with optional query parameter
- `POST /items` - Create a new item

## Example Requests

```bash
# Health check
curl http://localhost:8000/health

# Get item
curl http://localhost:8000/items/42

# Create item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```

## Learning Path

This project is designed as a foundation for learning:
- **GitHub Actions**: Add CI/CD workflows in `.github/workflows/`
- **AWS**: Deploy using ECS, Lambda, or AppRunner
- **Terraform**: Infrastructure as code for AWS resources

## Next Steps

- Add environment configuration
- Implement authentication
- Add database integration
- Create GitHub Actions workflows
- Deploy to AWS

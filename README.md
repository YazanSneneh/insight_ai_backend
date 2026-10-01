# InsightAI

AI-powered research assistant for structured, source-aware answers.

### description

InsightAI is a production-oriented AI research platform built with Python and FastAPI. It combines LLMs, web research, structured outputs, and modular backend architecture to transform user questions into organized, evidence-based research.


## Tech Stack

* Python
* FastAPI
* PostgreSQL
* LLM APIs
* Pydantic
* httpx
* pytest
* Docker

## Architecture

```bash
Backend/
├── app/
│   ├── main.py
│   ├── routers.py
│   ├── lifespan.py
│   └── middlewares/
├── modules/
│   ├── research/
│   └── chat/
├── docs/
├── tests/
├── infrastructure/
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── run.py
└── README.md
```

## Later

* RAG
* Embeddings
* Vector Database
* Tool Calling
* Streaming
* Background Jobs
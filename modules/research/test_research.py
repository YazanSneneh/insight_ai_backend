import pytest

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app



@pytest.fixture(scope="module")
def research_test_client():
    with TestClient(app) as research_test_client:
        yield research_test_client

@pytest.fixture(scope="module")
def response(research_test_client):
    return research_test_client.get("/api/v1/research/", params={"query": "benefits of Electric Vichles"})

def test_research_status_code(response):
    assert response.status_code == status.HTTP_200_OK

def test_research_result(response):
    data = response.json()
    assert "result" in data

def test_param_empty_research(research_test_client):
    response = research_test_client.get("/api/v1/research/", params={"query": ""})
    assert response.status_code == status.HTTP_200_OK

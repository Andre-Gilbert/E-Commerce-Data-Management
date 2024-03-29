"""Test REST API."""
import pytest
from typing import Generator
from fastapi.testclient import TestClient

from app.database.session import SessionLocal
from app.main import app
from tests.utils.auth import get_token_headers


@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope='module')
def token_headers(client: TestClient) -> dict[str, str]:  # pylint: disable=redefined-outer-name
    return get_token_headers(client)

from unittest.mock import patch, MagicMock
import os

os.environ.setdefault("DB_HOST", "test")
os.environ.setdefault("DB_USER", "test")
os.environ.setdefault("DB_PASSWORD", "test")
os.environ.setdefault("DB_NAME", "test")

from app import app


def test_users_returns_200_and_json():
    fake_cursor = MagicMock()
    fake_cursor.fetchall.return_value = [{"id": 1, "name": "Test"}]

    fake_db = MagicMock()
    fake_db.cursor.return_value = fake_cursor

    with patch("mysql.connector.connect", return_value=fake_db):
        client = app.test_client()
        response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "name": "Test"}]

import pytest
import os
from src.utils import read_json, created_object_for_json


@pytest.fixture
def sample_json(tmp_path):
    """Создает временный JSON файл"""
    json_content = '''
    [{
        "name": "Категория",
        "description": "Описание",
        "products": [
            {"name": "Товар1", "description": "Описание1", "price": 100.0},
            {"name": "Товар2", "description": "Описание2", "price": 200.0}
        ]
    }]
    '''
    file_path = tmp_path / "test.json"
    file_path.write_text(json_content, encoding="utf-8")
    return str(file_path)


def test_read_json(sample_json):
    data = read_json(sample_json)
    assert isinstance(data, list)
    assert data[0]["name"] == "Категория"


def test_created_object_for_json():
    test_data = [{
        "name": "Кат",
        "description": "Описание",
        "products": [
            {"name": "Товар", "description": "Описание", "price": 100.0}
        ]
    }]

    categories = created_object_for_json(test_data)
    assert len(categories) == 1
    assert categories[0].name == "Кат"
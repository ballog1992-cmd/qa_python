import pytest

from main import BooksCollector

# Фикстура на возврат обьекта
@pytest.fixture
def collector():
    return BooksCollector()


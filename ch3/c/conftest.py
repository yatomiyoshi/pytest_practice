from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture(scope='session')
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()

@pytest.fixture(scope='module')
def cards_db(db):
    db.delete_all()
    return db

@pytest.fixture(scope='session')
def some_cards():
    return [
        cards.Card('write book', 'Brian', 'done'),
        cards.Card('edit book', 'Katie', 'done'),
        cards.Card('write 2nd edition', 'Brian', 'todo'),
        cards.Card('edit 2nd edition', 'Katie', 'todo'),
    ]

@pytest.fixture(scope='function')
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db
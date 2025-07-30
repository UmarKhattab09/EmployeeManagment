import pytest
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from EmployeeDatabase import CRUD
from Tables.tableslist import Base, Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a temporary SQLite in-memory DB for testing
@pytest.fixture(scope="module")
def test_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    # session=Session()
    session.close()

def test_create_employee(test_session):
    # Create a CRUD instance using the test session (modify your CRUD to accept session)
    crud = CRUD(Session=test_session)

    # Create a test user
    crud.name = "Test User"
    crud.email = "test@example.com"
    crud.department_id = 1
    crud.create()

    # Query back
    employee = test_session.query(Employee).filter_by(name="Test User").first()
    assert employee is not None
    assert employee.email == "test@example.com"


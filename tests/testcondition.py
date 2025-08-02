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
    # Create a new employee
    crud = CRUD(Session=test_session)
    crud.name = "Test User"
    crud.email = "test@example.com"
    crud.department_id = 1
    crud.create()

    # Search for the employee
    crudsearch = CRUD(Session=test_session)
    result = crudsearch.search("Test User", "test@example.com")
    assert result is not None
    userrelatedstuff = result[0]
    assert any(user == "Test User" for user in userrelatedstuff)

    # Update the employee
    crudupdate = CRUD(Session=test_session)
    crudupdate.update("test@example.com", "TestUserUmar", "Testkhattab@gmail.com")

    # Verify update
    updated = test_session.query(Employee).filter_by(name="TestUserUmar").first()
    assert updated is not None
    assert updated.email == "Testkhattab@gmail.com"
    # Query back
    # employee = test_session.query(Employee).filter_by(name="Test User").first()
    # assert employee is not None
    # assert employee.email == "test@example.com"


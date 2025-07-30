# import pytest
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from EmployeeDatabase.employee import CRUD
from EmployeeDatabase.departments import DepartmentCRUD
from Tables.tableslist import Employee, Department
from Tables.tableslist import Base
import pytest
# Creating Rows

# user2 = CRUD(name="Akhtar",email="Aktharamin@gmail.com",department_id=5)
# user2.create()
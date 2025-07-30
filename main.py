
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from EmployeeDatabase.employee import CRUD
from EmployeeDatabase.departments import DepartmentCRUD
from Tables.tableslist import Employee, Department
from Tables.tableslist import Base






# test = DepartmentCRUD("ComputerScience",5)
# test.createdepartment()

User1 = CRUD("Hadi","randomemail4@gmail.com",1)
# Upload = User1.create()
# search = User1.searchbyemail("randomemail@gmailcom")
update = User1.update("randomemail3@gmail.com","Umara","khattabaumar",1)

# User2= CRUD("kh","32@","4")
# Upload2 = User2.create()
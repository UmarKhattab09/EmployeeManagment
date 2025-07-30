


from sqlalchemy import create_engine, Column, Integer, String, select, update
from sqlalchemy.orm import declarative_base, sessionmaker
from Tables.tableslist import Department

class DepartmentCRUD:
    def __init__(self,name,department_id):
        self.engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/employee_managment')
        self.name=name
        self.department_id = department_id
        self.Session = sessionmaker(bind=self.engine)
    
    def createdepartment(self):
        session = self.Session()
        if self.name is None and self.department_id is None:
            print("CAN NOT ADD USER")
        result = session.execute(
            select(Department).where(
                (Department.id==self.department_id) |
                (Department.name==self.name)
            )
        )

        user = result.scalars().first()
        if result:
            print(f"Department already exist with the name iD:{user.id} and NAME: {user.name}")
        else: 
            newdepartment = Department(name=self.name,id=self.department_id)
            session.add(newdepartment)
            session.commit()
            print(f"Department has been created {self.name}")

            # Need to create an error handling that if already the department is there, no more department of the same name and id
            
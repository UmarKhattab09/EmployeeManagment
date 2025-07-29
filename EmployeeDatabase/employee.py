
from sqlalchemy import create_engine, Column, Integer, String, select, update
from sqlalchemy.orm import declarative_base, sessionmaker
from main import Employee

# engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/employee_managment')


class CRUD:
    def __init__(self,name=None,email=None):
        self.name=name
        self.email = email

    def create(self):

        Session = sessionmaker(bind=engine)
        session = Session()
        if self.name is None or self.email is None:
            print("CAN NOT ADD USER")
        else: 
            newuser = Employee(name=self.name,email=self.email)
            session.add(newuser)
            session.commit()
            print("Session is commited")

    def searchbyemail(self,email):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.execute(select(Employee).where(Employee.email==email))
        user = result.scalars().first()  # Get the first result or None if no match
        if user:
            print(f"email already exist with the name {user.name} ")
        else:
            print(f"email doesn't exist in the database {user.email}")
    
    def update(self,name,email,newname=None,new_email=None):
        Session=sessionmaker(bind=engine)
        session=Session()
        result=session.execute(select(Employee).filter(Employee.name==name,Employee.email==email))
        user = result.scalars().first()
        if user:
            if newname:
                user.name=newname
            if new_email:
                user.email=new_email
            
            session.commit()
            print(f"User {name} updated sucessfully")
        else:
            print("user not found")



from sqlalchemy import create_engine, Column, Integer, String, select, update, or_
from sqlalchemy.orm import declarative_base, sessionmaker
from Tables.tableslist import Employee

class CRUD:
    def __init__(self,name=None,email=None,department_id=None,Session=None):
        self.engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/employee_managment')
        if Session:
            self.Session=Session  
        else:
            SessionLocal = sessionmaker(bind=self.engine)
            self.Session=SessionLocal()      

        # self.Session = sessionmaker(bind=self.engine)
        self.name=name
        self.email = email
        self.department_id = department_id

    def create(self):
        session = self.Session
        if self.name is None or self.email is None and self.department_id is None:
            print("CAN NOT ADD USER")

        result = session.execute(
            select(Employee).where((Employee.email==self.email)))
        user = result.scalars().first()
        if user:
            print(f"User already exist with the same email {user.email}")
        else: 
            newuser = Employee(name=self.name,email=self.email,department_id=self.department_id)
            session.add(newuser)
            session.commit()
            print("Session is commited")

    # def searchbyemail(self,email):
    #     # Session = sessionmaker(bind=engine)
    #     session = self.Session()
    #     result = session.execute(select(Employee).where(Employee.email==email))
    #     user = result.scalars().first()  # Get the first result or None if no match
    #     if user:
    #         print(f"email already exist with the name {user.name} ")
    #     else:
    #         print(f"email doesn't exist in the database {user.email}")

    # def searchbyuser(self,name):
    #     session = self.Session()
    #     result = session.execute(select(Employee).filter(Employee.name.like(name))).all()
    #     for users in result:
    #         print(users)

    def search(self,name=None,email=None):
        data = []
        session = self.Session
        try:
            if name and email:
                print("Search with Name and Email")
                conditions = []
            #     result=session.execute(select(Employee).where(
            #     (Employee.name.like(f"%{name}%") | (Employee.email==email) 
            # )))
                if name:
                    conditions.append(Employee.name.like(f"%{name}%"))
                if email:
                    conditions.append(Employee.name.like(f"%{email}%"))
                query = select(Employee).where(or_(*conditions))
                result = session.execute(query)
                users = result.scalars().all()
                for user in users:
                    data.append((user.id,user.name,user.email,user.department_id))
                return data
            else:
                print("FAILED")
                return []
        except Exception as e :
            print("Search error:",e)
            return []

        finally:
            session.close()

    def update(self,email,newname=None,new_email=None,department_id=None):
        # Session=sessionmaker(bind=engine)
        session=self.Session
        result=session.execute(select(Employee).filter(Employee.email==email))
        user = result.scalars().first()
        if user:
            if newname:
                user.name=newname
            if new_email:
                user.email=new_email
            if department_id:
                user.department_id=department_id
            
            session.commit()
            print(f"User with  {email} updated sucessfully")
        else:
            print("user not found")

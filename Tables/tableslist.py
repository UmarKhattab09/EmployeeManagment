






from sqlalchemy import create_engine, Column, Integer, String, select, update,ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import MetaData






Base = declarative_base()

class Employee(Base):

    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    department_id = Column(Integer,ForeignKey("departments.id"))

    department = relationship("Department",back_populates="employees")

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer,primary_key=True)
    name=Column(String(100))
    # email=Column(String(100),unique=True)
    # department_id=Column(String(40),ForeignKey("employees.id"))
    employees =relationship("Employee",back_populates="department")



# Base.metadata.create_all(engine) #Creating TABLE oNCE

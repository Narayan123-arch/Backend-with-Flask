from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from config import Config

Base=declarative_base()

class User(Base):
    __tablename__='nuser'
    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(50))
    password=Column(String)
    role=Column(String(20))

engine=create_engine(Config.DB_URL)
SessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def insert_user(name,email,password=None):
    session =SessionLocal()
    new_user=User(name=name,email=email,password=password,role="user")
    session.add(new_user)
    session.commit()
    session.close()

def get_all_users():
    session=SessionLocal()
    users=session.query(User).all()
    session.close()
    return users

def delete_user(user_id):
    session=SessionLocal()
    user=session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
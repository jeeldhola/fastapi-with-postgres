from database import Base
from sqlalchemy import Column,String,Integer,Boolean
from utils.temp_models import Common_class



# creating the model for the user



class User(Base,Common_class):
    """_summary_
    Args:
        Base (_type_): _description_
        Common_class (_type_): _description_
    """
    __tablename__ = 'users'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    pass_decrypted = Column(String)
    email = Column(String)

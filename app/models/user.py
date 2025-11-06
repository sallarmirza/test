from sqlalchemy import Column,Integer,String,ForeignKey,DATETIME,Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    message_sent=relationship('Message',back_populates='sender',foreign_keys='Message.sender_id')
    message_received=relationship('Message',back_populates='receiver',foreign_keys='Message.receiver_id')


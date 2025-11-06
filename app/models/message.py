from sqlalchemy import Column,Integer,String,ForeignKey,DATETIME,Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Message(Base):
    __tablename__='messages'
    id=Column(Integer,primary_key=True,index=True)
    sender_id=Column(Integer,ForeignKey('user.id'))
    receiver_id=Column(Integer,ForeignKey('user.id'))
    content=Column(Text)
    timestamp=Column(DATETIME,default=datetime.utcnow)
    
    sender=relationship('User',foreign_keys=[sender_id],back_populates='messages_sent')
    receiver=relationship('User',foreign_keys=[receiver_id],back_populates='message_received')
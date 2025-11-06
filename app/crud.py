from sqlalchemy.orm import Session
from models import user,message

def create_user(db:Session,username:str):
    user=user(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_message(db:Session,sender_id:int,receiver_id:int,content:str):
    msg=message(sender_id=sender_id,receiver_id=receiver_id,content=content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def get_conversation(db:Session,user1_id:int,user2_id:int):
     return db.query(message).filter(
        ((message.sender_id == user1_id) & (message.receiver_id == user2_id)) |
        ((message.sender_id == user2_id) & (message.receiver_id == user1_id))
    ).order_by(message.timestamp).all()
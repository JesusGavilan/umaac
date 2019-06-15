from sqlalchemy import Column
from sqlalchemy import String, Integer, Float, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from model import Base
from util import encoder


class User(Base):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(400), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    details = Column(JSONB, nullable=True)
    token = Column(String(255), nullable=False)
    uuid_id = Column(String(), nullable=False)

    def __repr__(self):
        return "User(name='%s, email='%s', token='%s')" % (self.username, self.email, self.token)

    @classmethod
    def get_id(cls):
        return User.user_id

    @classmethod
    def find_by_emails(cls, session, email):
        return session.query(User).filter(User.email == email).one()

    @classmethod
    def find_by_username(cls, session, username):
        return session.query(User).filter(User.username == username).one()


    FIELDS = {
        'username': str,
        'user_id': int,
        'email': str,
        'details': encoder.passby,
        'token': str
    }
    FIELDS.update(Base.FIELDS)

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    password = Column(Unicode(255))
    email = Column(Unicode(255), unique=True)
    group_id = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

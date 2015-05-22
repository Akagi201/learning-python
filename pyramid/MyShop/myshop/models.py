from datetime import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    ForeignKey, DateTime, Table, Float)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)
#
# Index('my_index', MyModel.name, unique=True, mysql_length=255)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    password = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255))

    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    group = relationship('Group', backref='users')

    def has_permission(self, permission):
        for perm in self.group.permissions:
            if perm.name == permission:
                return True
        return False

group_permission = Table('group_permission', Base.metadata,
                          Column('group_id', Integer, ForeignKey('groups.id'),
                                 primary_key=True),
                          Column('permission_id', Integer, ForeignKey('permissions.id'),
                                 primary_key=True)
                          )

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)

    permissions = relationship('Permission',
                               secondary=group_permission, backref='groups')

class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False, default=0.0)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', backref='items')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    parent = relationship('Category', remote_side=[id], backref='children')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ItemImage(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    path = Column(Unicode(255), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = relationship('Item', backref='images')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='comments')
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = relationship('Item', backref='comments')

    rank = Column(Integer, nullable=False, default=3)
    content = Column(Text)

cart_item = Table('cart_itemtype', Base.metadata,
                  Column('card_id', Integer, ForeignKey('carts.id'),
                         primary_key=True),
                  Column('item_id', Integer, ForeignKey('items.id'),
                         primary_key=True)
                  )

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)

    items = relationship('Item', secondary=cart_item)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='cart')

order_item = Table('order_item', Base.metadata,
                   Column('order_id', Integer, ForeignKey('orders.id'),
                          primary_key=True),
                   Column('item_id', Integer, ForeignKey('items.id'),
                          primary_key=True)
                   )

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')

    items = relationship('Item', secondary=order_item)
    add_time = Column(DateTime, nullable=False, default=datetime.now())

    address = Column(Unicode(255), nullable=False)
    telephone = Column(Unicode(25), nullable=False)

class Annoncement(Base):
    __tablename__ = 'annoncements'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    content = Column(Text)
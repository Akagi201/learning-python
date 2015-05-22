from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import remember, forget
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Item,
    Category,
    Annoncement,
    #MyModel,
    User)


@view_config(route_name='home', renderer='templates/index.pt')
def index_view(request):
    categories = DBSession.query(Category).filter_by(parent = None).all()
    annoncements = DBSession.query(Annoncement)

    return {'title': 'Index - MyShop',
            'categories': categories,
            'annoncements': annoncements}

@view_config(route_name='category', renderer='templates/category.pt')
def category_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    category = DBSession.query(Category).filter(Category.id == id).first()
    if not category:
        return HTTPNotFound()
    return {'category': category}

@view_config(route_name='item', renderer='templates/item.pt')
def item_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    item = DBSession.query(Item).filter(Item.id == id).first()
    if not item:
        return HTTPNotFound()

    return {'item': item}

@view_config(route_name='login', renderer='templates/login.pt')
def login_view(request):
    login = request.params.get('login', None)
    password = request.params.get('password', None)

    if not login:
        return {
            'title': 'login',
            'message': '',
            'login': login
        }

    user = DBSession.query(User).filter_by(name=login).first()
    if not user:
        return {
            'title': 'login',
            'message': 'User Not Found',
            'login': login
        }

    if user.password != password:
        return {
            'title': 'login',
            'message': 'Password does not match',
            'login': login
        }

    headers = remember(request, user.id)
    return HTTPFound(location='/', headers=headers)

@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)
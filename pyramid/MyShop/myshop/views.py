from pyramid.response import Response
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Item,
    Category,
    #MyModel,
    )


@view_config(route_name='home', renderer='string')
def index_view(request):
    categories = DBSession.query(Category).all()

    names = []
    for category in categories:
        names.append(category.name)
    return {'categories': names}

@view_config(route_name='category', renderer='string')
def category_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    category = DBSession.query(Category).filter(Category.id == id).first()
    if not category:
        return HTTPNotFound()
    return {'category': category}

@view_config(route_name='item', renderer='string')
def item_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    item = DBSession.query(Item).filter(Item.id == id).first()
    if not item:
        return HTTPNotFound()

    return item
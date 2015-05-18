from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Item,
    Category,
    #MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    categories = DBSession.query(Category).slice(0, 2).all()
    return {'one': 'one', 'project': categories}



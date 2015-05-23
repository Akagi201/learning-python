from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import remember, forget
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound

from sqlalchemy.exc import DBAPIError
import colander
import deform
from js.deform import deform as deform_static
from .models import (
    DBSession,
    Item,
    Category,
    Annoncement,
    # MyModel,
    User)


@view_config(route_name='home', renderer='templates/index.pt', layout="master")
def index_view(request):
    categories = request.db.query(Category).filter_by(parent=None).all()

    return {'title': 'Index - MyShop',
            'categories': categories,
            'category': None
            }


@view_config(route_name='category', renderer='templates/category.pt', layout='master')
def category_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    category = DBSession.query(Category).filter(Category.id == id).first()
    if not category:
        return HTTPNotFound()

    return {'category': category,
            'title': category.name + ' - Category'}


@view_config(route_name='item', renderer='templates/item.pt', layout='master')
def item_view(request):
    try:
        id = int(request.matchdict['id'])
    except:
        return HTTPNotFound()

    item = DBSession.query(Item).filter(Item.id == id).first()
    if not item:
        return HTTPNotFound()

    return {'item': item,
            'title': item.name + ' - Item',
            'category': item.category
            }


@view_config(route_name='add_item', renderer='templates/add_item.pt', permission='item')
def item_add(request):
    name = request.params.get('name', None)
    category_id = request.matchdict.get('id', None)
    description = request.params.get('description', None)
    price = request.params.get('price', None)
    category = request.db.query(Category). \
        filter_by(id=category_id).first()
    categories = DBSession.query(Category). \
        filter_by(parent=None).all()

    if 'submit' in request.params:
        item = Item()
        item.name = name
        item.price = float(price)
        item.description = description
        item.category = category
        request.db.add(item)
        return HTTPFound(location=request.route_url('category', \
                                                    id=category_id))

    return {
        'title': 'Item Add',
        'categories': categories,
        'category': category,
    }


class TypeUser(object):
    def serialize(self, node, appstruct):
        if appstruct is colander.null:
            return colander.null
        if not isinstance(appstruct, User):
            raise colander.Invalid(node, '%r is not a instance of User' % appstruct)

        return appstruct.name

    def deserialize(self, node, cstruct):
        if cstruct is colander.null:
            return colander.null
        if not isinstance(cstruct, basestring):
            raise colander.Invalid(node, '%r is not a valid username' % cstruct)
        user = DBSession.query(User).filter_by(name=cstruct).first()
        if not user:
            raise colander.Invalid(node, 'User with name %r does not exist' % cstruct)

        return user


class LoginFormSchema(colander.MappingSchema):
    login = colander.SchemaNode(TypeUser())
    password = colander.SchemaNode(colander.Str(),
                                   widget=deform.widget.PasswordWidget()
                                   )


def password_validator(form, value):
    user = value['login']
    password = value['password']

    if user.password != password:
        raise colander.Invalid(form, 'Password does not match user %s' % user.name)


@view_config(route_name='login', renderer='templates/login.pt')
def login_view(request):
    deform_static.need()

    search_path = ('myShop/templates/deform/',)
    renderer = deform.ZPTRendererFactory(search_path)
    schema = LoginFormSchema(validator=password_validator)
    form = deform.Form(schema, buttons=('submit',), renderer=renderer)

    if 'submit' in request.POST:
        try:
            appstruct = form.validate(request.POST.items())
        except deform.ValidationFailure, e:
            return {
                'title': 'login',
                'form': e.render()
            }

        user = appstruct['login']

        headers = remember(request, user.id)
        return HTTPFound(location='/', headers=headers)

    return {
        'title': 'login',
        'form': form.render()
    }


@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)

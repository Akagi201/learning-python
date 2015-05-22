from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.security import unauthenticated_userid, Allow
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    User,
    Group,
)


def groupfinder(userid, request):
    user = DBSession.query(User).filter_by(id=userid).first()
    if user:
        return ['g:' + str(user.group.id)]
    return None


class RootFactory(object):
    def __init__(self, request):
        groups = DBSession.query(Group).all()
        self.__acl__ = []
        for group in groups:
            for permission in group.permissions:
                self.__acl__.append(
                    (Allow, 'g:' + str(group.id), permission.name)
                )


def get_user(request):
    user_id = unauthenticated_userid(request)
    user = DBSession.query(User).filter_by(id=user_id).first()
    return user


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authn_policy = AuthTktAuthenticationPolicy(
        'secret', callback=groupfinder, hashalg='sha512'
    )
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, root_factory='myshop.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.set_request_property(get_user, 'user', reify=True)
    config.set_request_property(lambda request: DBSession, 'db', reify=True)

    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('category', '/category/{id}')
    config.add_route('item', '/item/{id}')
    config.add_route('search', '/search')
    config.add_route('annoncement', '/annoncement/{id}')

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')

    config.add_route('order', '/order')
    config.add_route('cart', '/cart')
    config.add_route('comment', '/comment')

    config.add_route('add_item', '/category/{id}/add')

    config.scan()
    return config.make_wsgi_app()

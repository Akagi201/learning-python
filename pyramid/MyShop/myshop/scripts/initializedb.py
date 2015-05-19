import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    #MyModel,
    User,
    Group,
    Base,
    Permission, Category, Item)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        #model = MyModel(name='one', value=1)
        #DBSession.add(model)

        perm_item_manage = Permission()
        perm_item_manage.name = 'item'
        DBSession.add(perm_item_manage)

        perm_user_manage = Permission()
        perm_user_manage.name = 'user'
        DBSession.add(perm_user_manage)

        perm_order_manage = Permission()
        perm_order_manage.name = 'order'
        DBSession.add(perm_order_manage)

        gadmin = Group()
        gadmin.name = 'Administrators'
        gadmin.permissions.append(perm_item_manage)
        gadmin.permissions.append(perm_order_manage)
        gadmin.permissions.append(perm_user_manage)
        DBSession.add(gadmin)

        admin = User()
        admin.name = 'admin'
        admin.password = 'admin'
        admin.email = 'admin@localhost'
        admin.group = gadmin
        DBSession.add(admin)

        cat_food = Category()
        cat_food.name = 'Food'
        DBSession.add(cat_food)

        cat_fruit = Category()
        cat_fruit.name = 'Fruit'
        cat_fruit.parent = cat_food
        DBSession.add(cat_fruit)

        cat_vegetable = Category()
        cat_vegetable.name = 'Vegetable'
        cat_vegetable.parent = cat_food
        DBSession.add(cat_vegetable)

        iapple = Item()
        iapple.name = 'Apple'
        iapple.description = '<h2>This is a <span style="color:red;">red</span> apple</h2>'
        iapple.price = 1.3
        iapple.category = cat_fruit
        DBSession.add(iapple)

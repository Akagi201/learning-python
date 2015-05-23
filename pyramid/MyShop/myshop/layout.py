from pyramid_layout.layout import layout_config
from .models import Annoncement, Category


@layout_config(name="master", template='myshop:templates/master.pt')
class MasterLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.annoncements = request.db.query(Annoncement)
        self.categories = request.db.query(Category).filter_by(parent=None).all()

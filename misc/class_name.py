
class BaseForm(object):
    def __init__(self):
        self.state = self.__class__.__name__
        self.class_val = self.__class__

a = BaseForm()
print(a.state)
print(dir(a.class_val))
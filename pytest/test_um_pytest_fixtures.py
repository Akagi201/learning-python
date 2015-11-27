from unnecessary_math import multiply


def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)


def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)


def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)


def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)


def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert multiply(3, 4) == 12


def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert multiply('a', 3) == 'aaa'


class TestUM:
    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

    def test_numbers_5_6(self):
        print 'test_numbers_5_6  <============================ actual test code'
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print 'test_strings_b_2  <============================ actual test code'
        assert multiply('b', 2) == 'bb'

from fabric.api import *

env.hosts = ['192.168.1.108']
env.user = 'shin'
env.password = '123456'


def hello():
    print "hello world"


def deploy():
    with cd('/home/shin/Todo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')
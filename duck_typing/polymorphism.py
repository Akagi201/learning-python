#!/usr/bin/env python

class Duck:
    def quack(self):
        print "Quaaaaaack!"

class Bird:
    def quack(self):
        print "bird imitate duck."

class Doge:
    def quack(self):
        print "doge imitate duck."

def in_the_forest(duck):
    duck.quack()

duck = Duck()
bird = Bird()
doge = Doge()
for x in [duck, bird, doge]:
    in_the_forest(x)

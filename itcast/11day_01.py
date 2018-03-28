# coding=utf-8

class A(object):
    def __init__(self):
        print('This is init method.')

    def __new__(cls):
        print('This is new method.')
        return object.__new__(cls)

A()
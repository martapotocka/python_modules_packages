from second_module import *


def function_one():
    print('I am in first_module, my name is: {}'.format(__name__))
    print("I'm function_one from fist_module")


def function_two():
    print("I'm function_two from first_module")

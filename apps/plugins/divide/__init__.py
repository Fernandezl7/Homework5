'''divide'''
from apps.commands import Command
# pylint: disable=too-few-public-methods
class DivideCommand(Command):
    '''divide'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Unable to divide by 0")
        print(f"The result of Dividing {self.a} / {self.b} = {self.a / self.b}")

def register():
    '''register'''
    return DivideCommand

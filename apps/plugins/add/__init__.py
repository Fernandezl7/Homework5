'''add'''
from apps.commands import Command
# pylint: disable=too-few-public-methods
class AddCommand(Command):
    '''add command'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"The result of adding {self.a} + {self.b} = {self.a + self.b}")

def register():
    '''register command'''
    return AddCommand

'''multiply'''
from apps.commands import Command
# pylint: disable=too-few-public-methods

class MultiplyCommand(Command):
    '''multiply command'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"The result of Multiplying {self.a} * {self.b} = {self.a * self.b}")

def register():
    '''register multiply command'''
    return MultiplyCommand

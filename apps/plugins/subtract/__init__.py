'''subtract'''
# pylint: disable=too-few-public-methods
from apps.commands import Command

class SubtractCommand(Command):
    '''subtract command'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"The result of Subtracting  {self.a} - {self.b} = {self.a - self.b}")

def register():
    '''register'''
    return SubtractCommand

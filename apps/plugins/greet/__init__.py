'''grettings'''
from apps.commands import Command
# pylint: disable=too-few-public-methods

class GreetCommand(Command):
    '''greet'''
    def execute(self):
        print("Hello, World!")
        
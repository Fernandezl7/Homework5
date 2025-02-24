'''menu'''
import sys
from apps.commands import Command
# pylint: disable=too-few-public-methods

class MenuCommand(Command):
    '''menu command'''
    def execute(self):
        print(f'Menu')
        
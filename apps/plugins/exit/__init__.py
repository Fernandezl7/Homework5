'''exit'''
import sys
from apps.commands import Command
# pylint: disable=too-few-public-methods

class ExitCommand(Command):
    '''exit command'''
    def execute(self):
        sys.exit("Exiting...")
        
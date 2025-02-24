'''menu'''
# app/plugins/menu.py
# pylint: disable=too-few-public-methods
from apps.commands import Command
from apps.commands import CommandHandler

class MenuCommand(Command):
    '''menu command'''
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        self.command_handler.list_commands()

def register():
    '''register command'''
    return MenuCommand  # Return the class, not an instance

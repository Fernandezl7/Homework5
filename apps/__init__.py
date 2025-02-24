'''apps'''
import os
import pkgutil
import importlib
import multiprocessing
from apps.commands import CommandHandler
from apps.commands import Command
#from app.plugins.menu import MenuCommand
#from dotenv import load_dotenv
# pylint: disable=line-too-long, unused-variable, too-many-statements, too-many-branches, broad-exception-caught
class App:
    '''class app'''
    def __init__(self):
        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins
    def load_plugins(self):
        '''load plugin'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        #if issubclass(item, (Command)) and item is not Command:  # Added extra condition as it was registering the command twice
                        if plugin_name == "Menu":
                            self.command_handler.register_command(plugin_name, item(self.command_handler))
                        else:
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        '''start'''
        self.load_plugins()
        print("\nOption To Perform Interative Calculation:")
        print("        ")
        self.command_handler.execute_command("Menu")

        choice = input("Choose an option : ")
        while True:
            try:
                if choice == "C":
                    choice = input("Choose an option: ").strip()
                    continue
                if choice in ("Add", "Subtract", "Multiply", "Divide"):
                    self.command_handler.execute_command(choice)
                elif choice in ("Exit", "E"):
                    self.command_handler.execute_command("Exit")
                    break
                elif choice == "Greet":
                    self.command_handler.execute_command("Greet")
                elif choice == "Menu":
                    self.command_handler.execute_command("Menu")
                else:
                    print("Invalid choice. Please select a valid option.")
            except Exception as e:
                print(f"An error occurred: {e}")

            print("\nType 'C' to Continue, 'E' to Exit")
            choice = input("")

def start_app():
    '''start app'''
    app = App()
    app.start()

if __name__ == "__main__":
    multiprocessing.Process(target=start_app).start()
class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")

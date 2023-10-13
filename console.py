#!/usr/bin/python3
import cmd
"""
A python console module that accepts and interprete command line argument
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """A class that defines the necessary functions and argument"""

    def emptyline(self):
        """A function that does nothing when a enter line is called"""
        pass

    def do_quit(self, line):
        """A function that quit the program"""
        return True

    def do_EOF(self, line):
        """ a functioin that exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""
A python console module that accepts and interprete command line argument
"""
prototype_names ={"BaseModel": BaseModel}

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

    def do_create(self, line):
        """
        A function that create the instamce of The BaseModel class
        from the command line
        """

        if not line:
            print("** class name missing **")
        elif line in prototype_names:
            for key, value in prototype_names.items():
                if key == line:
                    new_object = prototype_names[key]()
            storage.save()

            print(new_object.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        A function that show a particular instance of a class 
        if it exist
        """
        line = line.split(" ")
        if not line:
            print("** class name missing **")
        elif line[0] not in prototype_names:
            print("** class doesn't exist **")
        elif len(line) >= 1:
            try:
                if line[0] in prototype_names:
                    objects = FileStorage.all(self)
                    object_key = "{}.{}".format(line[0], line[1])
                    flag = 0
                    for key, value in objects.items():
                        if key == object_key:
                            flag = 1
                            print(value)
                    if flag == 0:
                        print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

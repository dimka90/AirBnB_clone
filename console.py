#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
"""
A python console module that accepts and interprete command line argument
"""

prototype_names = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """A class that defines the necessary functions and argument"""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """A function that quit the program"""
        return True

    def do_EOF(self, line):
        """ a functioin that exit the console"""
        return True

    def emptyline(self):
        """A function that does nothing when a enter line is called"""
        pass

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

    def do_destroy(self, line):
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
                    try:
                        objects.pop(object_key)
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, line):
        """A function that display all the instance of an object"""

        # spliting the argument passed to the command line e.g
        # line =["all", "model"]
        # line = line.split(" ")

        # print the values if the only command enterd is (all)
        parse_arg = line.split(" ")
        list_of_object = []
        dict_objects = FileStorage.all(self)
        if not line:
            print("coding is fun")
            # create an empty  list to put in the the object in
            # Load the instance of stored in the __objects dictionary by making
            # a call to the all method
            # looping through the objects and  appending each value
            # of the dictionary to the list
            for key, value in dict_objects.items():
                list_of_object.append(str(value))

            print(list_of_object)
        elif parse_arg[0] in prototype_names:
            for key, value in dict_objects.items():
                list_of_object.append(str(value))
            print(list_of_object)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        'Update the instances based on class name and id.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif len(my_arg) == 2:
            print("** attribute name missing **")
        elif len(my_arg) == 3:
            print("** value missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            flag = 0
            for key, values in my_objects.items():
                if key == my_key:
                    flag = 1
                    my_values = my_objects.get(key)
                    setattr(values, my_arg[2], my_arg[3])
                    values.save()
            if flag == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

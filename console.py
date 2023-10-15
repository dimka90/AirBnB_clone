#!/usr/bin/python3
"""
Entry point of the command intepreter
used for CRUD operations
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """The command shell processor"""

    prompt = "(hbnb) "

    """Models classes array"""
    del_classes = ['BaseModel', 'User', 'Amenity', 'City', 'Place'
                   'Review', 'State']

    """Command array"""
    l_cmd = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """Takes in the command inputs and parses them"""
        if '.' in arg and '(' in arg and ')' in arg:
            av = arg.split('.')
            cm = av[1].split('(')
            args = cm[1].split(')')
            if av[0] in HBNBCommand.del_classes and cm[0] in HBNBCommand.l_cmd:
                arg = cm[0] + ' ' + av[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """Help command describes a specific cmd"""
        print("Describes the function of a given command")

    def emptyline(self):
        """Does nothing when an empty line is encountered"""
        pass

    def do_create(self, type_model):
        """Creates an instance of a given class"""
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.del_classes:
            print("** class doesn't exist **")
        else:
            dictn = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                     'City': City, 'Place': Place, 'Review': Review,
                     'State': State}
            my_model = dictn[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """Shows the string value of an instance"""
        if not arg:
            print("** class name missing ** ")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.del_classes:
            print("** class doesn't exist")
        elif len(args) == 1:
            print("** instance id missing ** ")
        else:
            all_objects = storage.all()
            for k, v in all_objects.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance with an id passed"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.del_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for k, v in all_objects.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all the available instances"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.del_classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            list_rep_inst = []
            for k, v in all_objects.items():
                obj_name = v.__class__.__name__
                if obj_name == args[0]:
                    list_rep_inst += [v.__str__()]
                print(list_rep_inst)

    def do_update(self, arg):
        """ Updates an instance using the name and id"""
        if not arg:
            print("** class name missing **")
            return
        ar = ""
        for argv in arg.split(','):
            ar = ar + argv
        args = shlex.split(ar)

        if args[0] not in HBNBCommand.del_classes:
            print("** class doesn't exist")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for k, obj in all_objects.items():
                obj_name = obj.__class__.__name__
                obj_id = obj.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(obj, args[2], args[3])
                        storage.save()
                    return
                print("** no instance found **")

    def do_count(self, class_n):
        """Counts the instances of a class"""
        count = 0
        all_objects_avail = storage.all()
        for k, v in all_objects_avail.items():
            c_lass = k.split('.')
            if c_lass[0] == class_n:
                count = count + 1
        print(count)

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def do_EOF(self, line):
        """ End_of_file command to terminate the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

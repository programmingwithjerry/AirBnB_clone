#!/usr/bin/python3
"""
Module that defines the entry point for the command interpreter
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
import inspect
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User
import re
import sys


class CommandInterpreter(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = '(hbnb) '

    @staticmethod
    def convert_str_to_int(value):
        """
        Try to convert a string to an integer and return it if possible.
        """
        try:
            num = int(value)
            return num
        except:
            return value

    @staticmethod
    def is_class_defined(class_name):
        """Check if the class_name corresponds to a defined class."""
        try:
            result = inspect.isclass(eval(class_name))
            return result
        except:
            return False

    def do_EOF(self, line):
        """
        Handle the end-of-file marker.
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Exit the command interpreter.
        """
        return True

    def emptyline(self):
        """
        Handle an empty input line.
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel or its subclasses.
        Usage: create <ClassName>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif CommandInterpreter.is_class_defined(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                instance = eval(args[0])()
                instance.save()
                print("{}".format(instance.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Display the string representation of an instance based on the class name and id.
        Usage: show <ClassName> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif CommandInterpreter.is_class_defined(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    instances = storage.all()
                    if key in instances:
                        print(instances[key])
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <ClassName> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif CommandInterpreter.is_class_defined(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    instances = storage.all()
                    if key in instances:
                        del instances[key]
                        storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Display the string representations of all instances, optionally filtered by class name.
        Usage: all <ClassName> or all
        """
        args = line.split()
        instances = []
        if len(args) == 0:
            for k, v in storage.all().items():
                instances.append(str(v))
            print(instances)
        elif CommandInterpreter.is_class_defined(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    obj_keys = k.split('.')
                    if obj_keys[0] == args[0]:
                        instances.append(str(v))
                print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update an instance by adding or modifying attributes.
        Usage: update <ClassName> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif CommandInterpreter.is_class_defined(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    instances = storage.all()
                    if key in instances:
                        if len(args) == 2:
                            print('** attribute name missing **')
                        else:
                            line2 = line.split('"')
                            if len(line2) == 1:
                                print("** value missing **")
                            else:
                                setattr(
                                    instances[key],
                                    str(args[2]),
                                    str(line2[1])
                                )
                                storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    @staticmethod
    def handle_class_all(line, cls_name):
        """
        Handle the default <class name>.all() command.
        """
        instances = []
        for k, v in storage.all().items():
            if (k.split('.')[0] == cls_name):
                instances.append(str(v))
        if len(instances) > 0:
            print('[', end='')
            for i in range(len(instances)):
                print(instances[i], end='')
                if i < len(instances) - 1:
                    print(', ', end='')
                else:
                    print(']')
        else:
            print('[]')

    @staticmethod
    def handle_class_count(line, cls_name):
        """
        Handle the default <class name>.count() command.
        """
        count = 0
        for k, v in storage.all().items():
            if (k.split('.')[0] == cls_name):
                count += 1
        print(count)

    @staticmethod
    def handle_class_show(cls_name, id):
        """
        Handle the default <class name>.show(<id>) command.
        """
        instances = storage.all()
        key = cls_name + '.' + id
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    @staticmethod
    def handle_class_destroy(cls_name, id):
        """
        Handle the default <class name>.destroy(<id>) command.
        """
        instances = storage.all()
        key = cls_name + '.' + id
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    @staticmethod
    def handle_class_update(cls_name, id, attr, value):
        """
        Handle the default <class name>.update(<id>, <attribute name>, <attribute value>) command.
        """
        instances = storage.all()
        key = cls_name + '.' + id
        if key in instances:
            setattr(
                instances[key],
                attr,
                CommandInterpreter.convert_str_to_int(value)
            )
            storage.save()
        else:
            print("** no instance found **")

    @staticmethod
    def handle_class_update_with_dict(cls_name, id, attr_dict):
        """
        Handle the <class name>.update(<id>, <dictionary representation>) command.
        """
        instances = storage.all()
        key = cls_name + '.' + id
        if key in instances:
            for k, v in attr_dict.items():
                setattr(
                    instances[key],
                    k,
                    CommandInterpreter.convert_str_to_int(v)
                )
            storage.save()
        else:
            print("** no instance found **")

    def default(self, line):
        """
        Called when the command prefix is not recognized.
        Handles commands such as <class name>.all(), <class name>.count(), etc.
        """
        args = line.split('.')
        cls_name = ""
        if args[0] is not None:
            cls_name = args[0]
        if args[1] is not None:
            if (args[1] == 'all()'):
                CommandInterpreter.handle_class_all(line, cls_name)
            elif (args[1] == 'count()'):
                CommandInterpreter.handle_class_count(line, cls_name)
            else:
                cmds = re.split(r'\(|\"|\)', args[1])
                cmds = list(filter(lambda s: s != '', cmds))
                if cmds[0] == 'show':
                    CommandInterpreter.handle_class_show(cls_name, cmds[1])
                elif cmds[0] == 'destroy':
                    CommandInterpreter.handle_class_destroy(cls_name, cmds[1])
                elif cmds[0] == 'update':
                    cmds = re.split(r'\(|\"|\)|\{|\'|\}|: |:|, ', args[1])
                    cmds = list(filter(lambda s: s != '' and s != ' ', cmds))
                    cmds = list(filter(lambda s: s != ', ', cmds))
                    if (len(cmds) == 4):
                        CommandInterpreter.handle_class_update(
                            cls_name, cmds[1], cmds[2], cmds[3]
                        )
                    else:
                        attrs = cmds[2:]
                        attr_dict = {}
                        for i in range(0, len(attrs), 2):
                            attr_dict[attrs[i]] = attrs[i + 1]
                        CommandInterpreter.handle_class_update_with_dict(
                            cls_name, cmds[1], attr_dict
                        )


if __name__ == '__main__':
    CommandInterpreter().cmdloop()

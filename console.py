#!/usr/bin/env python3
""" Contains the entry point of the command interpreter """

import cmd
import json
import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter """
    __classes = ['BaseModel', 'User', 'State', 'City', 'Place',
                 'Amenity', 'Review']

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quit command to exit program """
        return True

    def do_EOF(self, args):
        """ Exit the console at end of file """
        raise systemExit

    def emptyline(self):
        """When an empty line + ENTER shouldn’t
        execute anything
        """
        pass

    def do_create(self, args):
        """ Creates a new instance """
        if not args:
            print('** class name missing **')
            return

        cls_name = args.split()[0]

        if cls_name not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return
        else:
            if cls_name == 'BaseModel':
                cls_instance = BaseModel()
            if cls_name == 'User':
                cls_instance = User()
            if cls_name == 'State':
                cls_instance = State()
            if cls_name == 'City':
                cls_instance = City()
            if cls_name == 'Place':
                cls_instance = Place()
            if cls_name == 'Amenity':
                cls_instance = Amenity()
            if cls_name == 'Review':
                cls_instance = Review()

            cls_instance.save()
            print(cls_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance """
        args_len = len(args.split())
        if (args_len == 0):
            print('** class name missing **')
            return
        elif (args_len == 1):
            print('** instance id missing **')
            return
        elif (args_len > 2):
            return

        obj_name = args.split()[0]
        obj_id = args.split()[1]

        if obj_name not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return

        storage.reload()
        c_dict = storage.all()
        key = '.'.join([obj_name, obj_id])

        try:
            print(c_dict[key])
            return
        except KeyError:
            print('** no instance found **')
            return

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args_len = len(args.split())

        if (args_len == 0):
            print('** class name missing **')
            return
        elif (args_len == 1):
            print('** instance id missing **')
            return
        elif (args_len > 2):
            return

        obj_name = args.split()[0]
        obj_id = args.split()[1]

        if obj_name not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return

        c_dict = storage.all()
        key = '.'.join([obj_name, obj_id])

        try:
            del c_dict[key]
            storage.save()
        except KeyError:
            print('** no instance found **')
            return

    def do_all(self, args):
        """ Print all the content in the dictionary """
        c_dict = storage.all()
        c_list = []

        if not args:
            c_list = [str(value) for value in c_dict.values()]
            print(c_list)
            return

        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return

        else:
            for value in c_dict.values():
                if (value.__class__.__name__ == args):
                    c_list.append(str(value))

            print(c_list)
            return

    def do_count(self, args):
        """ Counts the number of instances of a class """
        c_dict = storage.all()
        c_list = []

        if not args:
            c_list = [str(value) for value in c_dict.values()]
            print(c_list)
            return

        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return

        else:
            for value in c_dict.values():
                if (value.__class__.__name__ == args):
                    c_list.append(str(value))

            c_list_dict = dict(c_list)
            count_instances = len(c_list_dict.values)
            print(count_instances)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        c_dict = storage.all()
        args_len = len(args.split())

        if not args:
            print('** class name missing **')
            return

        elif (args_len == 1):
            print('** instance id missing **')
            return

        elif (args_len == 2):
            print('** attribute name missing **')
            return

        elif (args_len == 3):
            obj_name, obj_id, dict2 = args.split()
            key = '.'.join([obj_name, obj_id])

            if not dict2.startswith("{") and not dict2.endswith("}"):
                print('** value missing **')
                return

            try:
                obj = c_dict.get(key)
                if obj:
                    attr_dict = eval(dict2)
                    if isinstance(attr_dict, dict):
                        for attr_name, attr_value in attr_dict.items():
                            obj.__dict__[attr_name] = attr_value
                        obj.updated_at = datetime.now()
                        obj.save()
                        c_dict[key] = obj
            except Exception as e:
                print(e)

        if (args_len > 4):
            return

        obj_name, obj_id, attr_name, value = args.split()

        if obj_name not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return

        key = '.'.join([obj_name, obj_id])

        try:
            obj = c_dict.get(key)
            if obj:
                setattr(obj, attr_name, value)
                obj.save()
            else:
                print('** no instance found **')
                return
        except Exception as e:
            print(e)
            print('** no instance found **')
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

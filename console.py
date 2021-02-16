#!/usr/bin/python3
"""Console module"""
import cmd
import shlex
import models
import json
import ast
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB console class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits the console on EOF"""
        return True

    def do_quit(self, arg):
        """Exits the console"""
        return True

    def emptyline(self):
        """replace emptyline with nothing"""
        return False

    def do_create(self, arg):
        """Creates an instance of <class>: CREATE <class>"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            instance = classes[args[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        """Shows an instance of a class: SHOW <class> <id>"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        else:
            key = "{:s}.{:s}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances, or all instances from a class: ALL (<class>)"""
        args = shlex.split(arg)
        models.storage.reload()
        objects = []
        if len(args) < 1:
            for obj in models.storage.all().values():
                objects.append(str(obj))
            print(objects)
        elif args[0] in classes:
            objects = []
            for key in models.storage.all():
                if args[0] in key:
                    objects.append(str(models.storage.all()[key]))
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class and id: DESTROY <class> <id>"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        else:
            key = "{:s}.{:s}".format(args[0], args[1])
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance base on <class>, <id>, <attribute> & <value>:\
        UPDATE <class> <id> <attribute> \"<value>\""""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        elif len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False
        else:
            key = "{:s}.{:s}".format(args[0], args[1])
            if key in models.storage.all():
                obj = models.storage.all()[key]
                try:
                    args[3] = type(getattr(obj, args[2]))(args[3])
                except:
                    try:
                        args[3] = int(args[3])
                    except:
                        try:
                            args[3] = float(args[3])
                        except:
                            pass
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

    def count(self, arg):
        """Counts the number of instances of a class"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            count = models.storage.all().keys()
            print(len(count))
        else:
            print("** class doesn't exist **")
            return False

    def default(self, line):
        """Changes the default behavior to add <class>.func() behavior"""
        funcs = {"all": self.do_all, "count": self.count,
                 "create": self.do_create, "show": self.do_show,
                 "destroy": self.do_destroy, "update": self.do_update}

        cmd = line.split('.', 1)
        class_name = cmd[0]
        args = cmd[1].strip("()").split('(')
        if args[0] in funcs:
            func = funcs[args[0]]
            params = class_name + ' '
            if len(args) > 1:
                if args[0] == "update":
                    if (args[1][-1] == '}'):
                        # If the last char of params is a } then it's a dict
                        str_dict = args[1].split(' ', 1)[1]
                        upd_dict = ast.literal_eval(str_dict)
                        params += args[1].split(',', 1)[0] + ' '
                        print(params)
                        # print(upd_dict)
                        for k, v in upd_dict.items():
                            final_params = '{} "{}" "{}"'.format(params,
                                                                 str(k),
                                                                 str(v))
                            print("final params: " + final_params)
                            func(final_params)
                        return
                    else:
                        params += args[1].replace(',', '').replace(':', '')
                        params = params.replace('{', '').replace('}', '')
                        # print(params)
                else:
                    params += args[1].replace(',', '')
            func(params)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()

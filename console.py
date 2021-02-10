#!/usr/bin/python3
"""Console module"""
import cmd
import shlex
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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





if __name__ == "__main__":
    HBNBCommand().cmdloop()

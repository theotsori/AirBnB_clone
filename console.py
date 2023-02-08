#!/usr/bin/python3

import cmd
from pickle import OBJ
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class, saves it, and prints the id"""
        if not line:
            print("** calss name missing **")
        else:
            try:
                cls = eval(line)
                instance = cls()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                cls_name = args[0]
                try:
                    cls = eval(cls_name)
                    key = "{}.{}".format(cls_name, args[1])
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")

    def do_destory(self, line):
        """Delete an instance based on class name and id"""
        from models.base_model import BaseModel
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) == 1:
                print("** attribute name missing **")
                return
            elif len(args) == 2:
                print("** value missing **")
                return
            else:
                if args[2] in ["id", "created_at", "updated_at"]:
                    print("** these attributes cannot be updated **")
                    return
                for key, value in obj.__dict__.items():
                    if key == args[2]:
                        if isinstance(value, int):
                            setattr(obj, key, int(args[3]))
                        elif isinstance(value, float):
                            setattr(obj, key, float(args[3]))
                        else:
                            setattr(obj, key, str(args[3].strip("\"")))
                storage.save()
                print("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
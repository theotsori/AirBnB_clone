#!/usr/bin/python3

import cmd
import shlex
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def do_create(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        else:
            instance = models.classes()[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            key = args[0] + "." + args[1]
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destory(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = self.classes[args[0]].get(args[1])
            if not obj:
                print("** no instance found **")
            else:
                del self.classes[args[0]][args[1]]
                self.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
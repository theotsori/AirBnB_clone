#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    classes = ["BaseModel"]

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

    def do_destroy(self, line):
        """Delete an instance based on class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                obj_id = args[1]
                if class_name in models.classes:
                    obj = models.classes[class_name].get(obj_id)
                    if obj:
                        obj.delete()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        if args and args[0] not in self.classes:
            print("** class doesn't exist")
            return

        objects = models.storage.all()
        instances = [str(v) for k, v in objects.items()
                    if not args or args[0] in k.split(".")]

        print("[" + ", ".join(instances) + "]")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if len(args) < 4:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        if obj_id is None:
            print("** instance id missing **")
            return
        obj = models.storage.all()
        if "{}.{}".format(class_name, obj_id) not in obj:
            print("** no instance found **")
            return
        attr_name = args[2]
        if attr_name is None:
            print("** attribute name missing **")
            return
        attr_value = args[3].strip('"')
        if attr_value is None:
            print("** value missing **")
            return
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** attribute name can't be updated **")
            return
        if type(attr_value) not in [str, int, float]:
            print("** invalid attribute value **")
            return
        obj = obj["{}.{}".format(class_name, obj_id)]
        setattr(obj, attr_name, attr_value)
        obj.save()
        print(obj)
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
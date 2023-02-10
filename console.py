#!/usr/bin/python3
"""
This is the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class contains the entry point of the command interpreter
    """
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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it(to the JSON file)
        and prints the id. Ex: $create BaseModel
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args in classes:
            new_instance = classes[args]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based
        on class name and id.Ex $ show BaseModel 1234-1234-1234
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all().keys():
                    obj = storage.all()[key]
                    print(obj)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Delete an instance based on class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all().keys():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args = args.split()
        if len(args) == 0:
            for key in storage.all().keys():
                print(storage.all()[key])
        elif args[0] in classes:
            instances = storage.all(args[0])
            if instances:
                for key in instances.keys():
                    print(instances[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        instance = storage.get(class_name, obj_id)
        if instance is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, updated_at **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3].strip('"')
        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

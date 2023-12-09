#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl-D (EOF)"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel,
        State, City, Amenity, Place,
        or Review,save it, and print the id"""

        if not arg:
            print("** class name missing **")
            return

        try:
            # Dynamically create an instance of the specified class
            class_name = arg.capitalize()  # Capitalize the class name
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance of
        BaseModel, State, City, Amenity,
        Place, Review, or User based on
        the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0].capitalize()
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations
        of all instances of BaseModel, State,
        City, Amenity, Place, Review, or User"""
        try:
            class_name = arg.capitalize()
            instances = storage.all()[class_name]
            print(instances)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance of BaseModel,
        State, City, Amenity, Place, Review,
        or User based on the class name and id
        with a dictionary representation
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0].capitalize()
            instance_id = args[1]
            dictionary_repr = eval(args[2])

            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                instance = instances[key]
                for k, v in dictionary_repr.items():
                    setattr(instance, k, v)
                instance.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the number of instances
        of BaseModel, State, City, Amenity,
        Place, Review, or User"""
        try:
            class_name = arg.capitalize()
            instances = storage.all()[class_name]
            count = len(instances)
            print(count)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation
        of an instance of BaseModel, State,
        City, Amenity, Place, Review, or User
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0].capitalize()
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

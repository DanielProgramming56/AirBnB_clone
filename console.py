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
        """Create a new instance of BaseModel, State, City, Amenity, Place, or Review,save it, and print the id"""

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

    def do_show(self, arg):
        """Prints the string representation of an instance of BaseModel, State, City, Amenity, Place, or Review"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) > 2:
            print("Too many arguments for show command")
            return

        class_name = args[0].capitalize()  # Capitalize the class name
        instance_id = args[1]

        try:
            # Retrieve the instance from storage
            obj_key = "{}.{}".format(class_name, instance_id)
            instance = storage.all().get(obj_key)

            if not instance:
                print("** no instance found **")
            else:
                print(instance)
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance of BaseModel, State, City, Amenity, Place, or Review based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) > 2:
            print("Too many arguments for destroy command")
            return

        class_name = args[0].capitalize()  # Capitalize the class name
        instance_id = args[1]

        try:
            # Retrieve the instance from storage
            obj_key = "{}.{}".format(class_name, instance_id)
            instance = storage.all().get(obj_key)

            if not instance:
                print("** no instance found **")
            else:
                # Delete the instance and save changes
                del storage.all()[obj_key]
                storage.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of all instances of BaseModel, State, City, Amenity, Place, or Review"""
        try:
            if not arg:
                # Print all instances if class name is not provided
                instances = storage.all().values()
            else:
                # Print instances of the specified class
                class_name = arg.capitalize()  # Capitalize the class name
                instances = [v for k, v in storage.all().items() if k.startswith(class_name + ".")]

            if not instances:
                print("** no instance found **")
            else:
                for instance in instances:
                    print(instance)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance of BaseModel, State, City, Amenity, Place, or Review based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        elif len(args) > 4:
            print("Too many arguments for update command")
            return

        class_name = args[0].capitalize()  # Capitalize the class name
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        try:
            # Retrieve the instance from storage
            obj_key = "{}.{}".format(class_name, instance_id)
            instance = storage.all().get(obj_key)

            if not instance:
                print("** no instance found **")
            else:
                # Update the attribute and save changes
                setattr(instance, attribute_name, attribute_value)
                storage.save()
        except KeyError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""console module."""
import cmd
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Implements a simple command interpreter."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when empty line is entered."""
        return

    def do_EOF(self, line):
        """Exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def check_args(self, a_num, a_given):
        """Check if given arguments given match required arguments."""
        a_list = ["cls_name", "id", "attr_name", "attr_value"]

        a_list = a_list[:a_num]
        a_dict = dict(zip(a_list, a_given))
        result = {}

        # check if class name is given
        cls_name = a_dict.get("cls_name")
        if "cls_name" in a_list and cls_name is None:
            print("** class name missing **")
            return None
        elif "cls_name" not in a_list:
            return result
        else:
            result["cls_name"] = cls_name

        # check if the given class name is valid
        cls = storage.get_cls(cls_name)
        if cls is None:
            print("** class doesn't exist **")
            return None
        else:
            result["cls"] = cls

        # check if id is given
        id = a_dict.get("id")
        if "id" in a_list and id is None:
            print("** instance id missing **")
            return None
        elif "id" not in a_list:
            return result
        else:
            result["id"] = id

        # check given id is valid
        obj_id = cls_name + '.' + id
        obj = storage.all().get(obj_id)
        if obj is None:
            print("** no instance found **")
            return None
        else:
            result["obj_id"] = obj_id
            result["obj"] = obj

        # check if attribute name is given
        attr_name = a_dict.get("attr_name")
        if "attr_name" in a_list and attr_name is None:
            print("** attribute name missing **")
            return None
        elif "attr_name" not in a_list:
            return result
        else:
            result["attr_name"] = attr_name

        # check if attribute value is given
        attr_value = a_dict.get("attr_value")
        if "attr_value" in a_list and attr_value is None:
            print("** value missing **")
            return None
        elif "attr_value" not in a_list:
            return result
        else:
            result["attr_value"] = attr_value

        return result

    def do_create(self, line):
        """Create new object.

        Usage: create <class_name>
        """
        # check that the command has valid arguments
        result = self.check_args(1, line.split())
        if result is None:
            return

        # create new object and save it
        cls = result["cls"]
        obj = cls()
        print(obj.id)
        storage.save()

    def do_show(self, line):
        """Print the string representation of a given object.

        Usage: show <class_name> <id>
        """
        # check that the command has valid arguments
        result = self.check_args(2, line.split())
        if result is None:
            return

        # print string representation of the object
        obj = result["obj"]
        print(obj)

    def do_destroy(self, line):
        """Delete a given object.

        Usage: destroy <class_name> <id>
        """
        # check that the command has valid arguments
        result = self.check_args(2, line.split())
        if result is None:
            return

        # delete the object and save
        obj_id = result["obj_id"]
        storage.delete(obj_id)
        storage.save()

    def do_all(self, line):
        """Print string representation of all objects with given class name.

        Usage: all [<class_name>]
        """
        args = line.split()
        cls_name = args[0] if len(args) else ""
        result = []

        # check if the given class name is valid
        if cls_name and storage.get_cls(cls_name) is None:
            print("** class doesn't exist **")
            return

        for obj_id, obj in storage.all().items():
            name = obj_id.split('.')[0]
            if cls_name == "" or cls_name == name:
                result.append(str(obj))

        print(result)

    def do_update(self, line):
        """Update an instance based on the class name and id.

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        result = self.check_args(4, shlex.split(line))
        if result is None:
            return

        obj_id = result["obj_id"]
        attr_name = result["attr_name"]
        attr_value = result["attr_value"]

        # update attribute value
        storage.update(obj_id, attr_name, attr_value)

        # save changes to json file
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

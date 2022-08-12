#!/usr/bin/python3
"""console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Implements a simple command interpreter."""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

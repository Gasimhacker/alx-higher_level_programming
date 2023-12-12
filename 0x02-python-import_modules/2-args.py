#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argstr = "arguments"
    argc = len(argv) - 1
    mark = ":"

    if (argc == 1):
        argstr = "argument"
    if (argc == 0):
        mark = "."

    print("{} {}{}".format(argc, argstr, mark))

    for arg in range(1, argc + 1):
        print("{}: {}".format(arg, argv[arg]))

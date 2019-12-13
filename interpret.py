import sys
import os.path

version = "alpha build 0.0.1"


def interpret(source):
    final = source
    final = final.replace("#defaults c++", "#include <iostream>")
    final = final.replace("#header ", "#include ")
    final = final.replace("#set ", "#define ")
    final = final.replace("integer ", "int ")
    final = final.replace("dfloat ", "double ")
    final = final.replace("procedure ", "")
    return final


if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("""S++ """ + version + """ interpreter usage

     -h | --help : Opens the help menu.
     -i <code file> | --interpret <code file> : Changes the given file to a standard C++ source code file.
     -c <code file> | --compile <code file> : Uses the Embarcadero C++ Compiler to compile the given file to an Windows Executable File.
     -v | --version : Checks the S++ interpreter version. """)

elif sys.argv[1] == "-i" or sys.argv[1] == "--interpret":
    if len(sys.argv) == 2:
        print("S++ Error : source file is not given.")
    elif len(sys.argv) > 3:
        print("S++ Error : source file should be only one.")
    else:
        if os.path.isfile(sys.argv[2]):
            sourcefile = open(sys.argv[2], 'rt')
            sourcecode = sourcefile.read()
            interpreted = interpret(sourcecode)
            print(interpreted)
        else:
            print("S++ Error : File does not exists.")

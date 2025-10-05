import sys

arguments = sys.argv

if len(arguments) > 2:
    sys.exit("Too many command-line arguments")
elif len(arguments) < 2:
    sys.exit("Too few command-line arguments")
elif not arguments[1].endswith('.py'):
    sys.exit('Not a Python file')

try:
    with open(arguments[1], 'r') as file:
        lines_python_file = file.readlines()

    #for line in lines_python_file:
        #if line.startswith('#') or not line.strip():
            #del line

    #Filters Comments with # and WhiteSpaces
    final_lines = [line.strip() for line in lines_python_file if not (line.strip().startswith('#') or not line.strip())]

    print(len(final_lines))

except FileNotFoundError:
    sys.exit('File does not exist')

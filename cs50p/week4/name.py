import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") 
 
print("hello, my name is", sys.argv[1]) # sys.argv[0] - name of the program
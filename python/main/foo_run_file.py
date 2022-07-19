# The other module is the main program and it imports your module. 
# The interpreter will search for your foo.py file (along with searching for a few other variants),
#  and prior to executing that module, it will assign the name "foo" from the import statement to the __name__ variable

import foo


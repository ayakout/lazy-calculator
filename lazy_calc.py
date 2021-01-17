import sys
import fileinput


# Use a dictionary to hold register values. Since lazy evaluation is a requirement, the value 
# shall be a list of operation sets which shall be evaluated at print time
# The dictionary is defined as register_dict = {REGISTER_NAME: [OPERATION_SET], ..} 
# where REGISTER_NAME is alphanumeric string and OPERATION_SET is a tuple of (OPERATION, ARGUMENT)
# e.g. register_dict = {
#       'A': [('add', '10')],
#       'B': [('add', 'A'), ('add', '1')],
#       'result': [('add', 'revenue'), ('subtract', 'costs')],
#       'revenue': [('add', '200')],
#       'costs': [('add', 'salaries'), ('add', '10')],
#       'salaries': [('add', '20'), ('multiply', '5')]
#      }
register_dict = dict()

# A tail recursive function to evaluate the list of operations for each register
# - operation_list is a list of opertion sets
# - register_value is the current value of the register and is initially set to zero value
def lazy_evaluate(operation_list, register_value = 0):
    if len(operation_list) == 0:
        # Return the register value when there is no more operations to perform
        return register_value
    [operation_set, *operation_list_rest] = operation_list
    return lazy_evaluate(operation_list_rest, do_operation(register_value, operation_set))


# Perform the arithmatic operation as described by the operation string
def do_operation(register_value, operation_set):
    (operation, argument) = operation_set
    if not argument.isnumeric():
        # Argument is a register so lets find its value
        argument = lazy_evaluate(register_dict[argument])
    argument = int(argument)
    if operation == 'add':
        return register_value + argument
    elif operation == 'subtract':
        return register_value - argument
    elif operation == 'multiply':
        return register_value * argument
    else:
        print('WARN: Invalid operation {}'.format(operation_set), file=sys.stderr)
        return register_value


# This iterates over the lines of files listed in sys.argv[1:], 
# default to sys.stdin if the list is empty. 
script_input = fileinput.input()


# Loop through user input and make it case insensitve
# Continue to read the input from STDIN until 'quit' is entered
# When reading from input file, 'quit' in not required
user_input = script_input.readline().lower().rstrip()
while (script_input.isstdin() and user_input != 'quit') or (not script_input.isstdin() and user_input):
    # Tokenize input string
    args_list = user_input.split()
    # Print a specific register to the terminal
    if len(args_list) == 2 and args_list[0] == 'print' and args_list[1] in register_dict:
        register_name = args_list[1]
        print(lazy_evaluate(register_dict[register_name]))
    # Store a register operation set in the register dictionary
    elif len(args_list) == 3:
        register_name = args_list[0]
        operation_set = (args_list[1], args_list[2])
        # Register dictionary holds list of operation sets for each register
        # e.g. register_dict[REGISTER_NAME] = [OPERATION_SET, ..]
        if register_name not in register_dict:
            register_dict[register_name] = list()
        register_dict[register_name].append(operation_set)
    user_input = script_input.readline().lower().rstrip()
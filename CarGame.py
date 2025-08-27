is_started = False
is_stopped = False
print("Type \'help\' to get instructions")
instruction = input(">")
while instruction.lower() != 'help':
    instruction = input(">")
print("start - to start car")
print("stop - to stop car")
print("quit - to exit")
instruction = input("Enter command: ")
while instruction.lower() != 'quit':
    if instruction.lower() == 'start':
        if is_stopped == True or is_started == False:
            print("Car started")
            is_started = True
            is_stopped = False
        else:
            print("Car already started")
    elif instruction.lower() == 'stop':
        if is_stopped == False or is_started == True:
            print("Car stopped")
            is_stopped = True
            is_started = False
        else:
            print("Car already stopped")
    else:
        print("Please enter correct command")
    instruction = input("Enter command: ")
print("Car exited")

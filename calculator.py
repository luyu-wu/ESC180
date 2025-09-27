 # Luyu VK Step 4-8

value = [0]
mem = 0

def display_current_value():
    print(value[-1])

def add(to_add):
    global value
    value.append(value[-1]+to_add)

def mult(to_mult):
    global value
    value.append(value[-1]*to_mult)

def div(to_div):
    global value
    value.append(value[-1]/to_div)

def undo():
    global value
    value[-2],value[-1] = value[-1],value[-2]

def undo2():
    global value
    value[-1],value[-2],value[-3] = value[-3],value[-1],value[-2]


def memory():
    global mem
    mem = value[-1]

def restore():
    global value
    value.append(mem)

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current value:",value)

    # Addition
    display_current_value() # should display 0
    add(5)
    display_current_value() # should display 5
    add(10)
    display_current_value() # should display 15
    memory()

    # Multiplication
    mult(2)
    display_current_value() # should display 30

    undo()
    display_current_value() # should display 15
    undo()
    display_current_value() # should display 5

    restore()
    display_current_value() # should display 15

    div(5)
    display_current_value() # should display 3.0

    mult(2)
    display_current_value() # should display 6
    undo()
    display_current_value() # should display 3.0
    undo()
    display_current_value() # should display 3.0

    undo2()
    display_current_value() # should display 3.0
    print("\n\n UNDO2 TESTING \n\n")

    value = [0]
    add(1)
    display_current_value() # should display 3.0

    mult(2)
    display_current_value() # should display 3.0
    undo()
    display_current_value() # should display 3.0
    add(5)
    display_current_value() # should display 3.0
    undo2()
    display_current_value() # should display 3.0


    # div(0) # Woopsies!

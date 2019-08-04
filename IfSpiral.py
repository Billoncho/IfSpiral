# IfSpiral.py
# Billy Ridgeway
# Creates a square spiral.

# Asks the user if they want to see a spiral.
answer = input("Do you want to see a spiral? y/n:")

if answer == 'y':           # If the anser is yes, run the program.
    print("Working...")     # Display a message the the program is working.
    import turtle           # Import turtle graphics.
    t = turtle.Pen()        # Creates a new turtle called t.
    t.speed(0)              # Sets the pen's speed to fast.
    t.width(2)              # Sets the width of the pen to 2.
# Creates a for loop.
    for x in range(100):    # Sets the variable 'x' to 100.
        t.forward(x*2)      # Moves the pen forward the value of 'x' times 2.
        t.left(89)          # Turns the pen left by 89 degrees.
print("Okay, we're done!")  # Prints "Okay, we're done! if the answer was no,
                            # or the for loop completed successfully.

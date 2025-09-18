undo_stack = []
redo_stack = []
def action():
    action = int(input("Enter the data: "))
    undo_stack.append(action)
    print("Action Performed" , action)
def undo():
    if not undo_stack:
        print("No Action Performed")
    else :
        action = undo_stack.pop()
        redo_stack.append(action)
        print("Undo Operation is performed" , action)
def redo():
    if not redo_stack:
        print("Nothing to Redo")
    else :
        action = redo_stack.pop()
        undo_stack.append(action)
        print("Redo Operation is performed" , action)


while(1):
 print("\nMenu")
 print("1. Push an Element")
 print("2. Undo")
 print("4. Redo")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        action()
    case 2:
        undo()
    case 3:
         redo()
    case _:
        print("Invalid Input")
    

        
 



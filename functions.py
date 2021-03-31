coffee_is_grinding = True

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding == True:
        print("Stopping the grind")
        coffee_is_grinding = False
    elif coffee_is_grinding == False:
        print("Grinding is about to begin")    
        coffee_is_grinding = True

coffee_is_grinding = False
press_grind_beans()
print(coffee_is_grinding)    
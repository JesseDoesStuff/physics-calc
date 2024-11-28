import math

def kinematics():
    print("Enter a integer or floating point number for each of the following prompts that you know. \n If you do not know a value, return an empty string")

    v0 = input("What is your initial velocity? ")
    vF = input("What is your final velocity? ")
    a = input("What is your (constant) acceleration? ")
    d = input("What is the displacement? ")
    t = input("What is the time? ")

    if vF == "" and d == "":
        which = input("Solve for displacement (d) or final velocity (vF)? ")
        if (which.lower() == "d" or which.lower() == "displacement"):
            d = (float(v0) * float(t)) + 0.5 * (float(a) * (float(t) * float(t)))
            print(f"Displacement is equal to {d} meters")
        else:
            vF = float(v0) + (float(a) * float(t))
            print(f"Final velocity is equal to {vF}m/s")
    elif vF == "" and t == "":
        which = input("Solve for time (t) or final velocity (vF)? ")
        if (which.lower() == "vf" or which.lower() == "final velocity"):   
            vF = math.sqrt((float(v0) * float(v0)) + (2 * float(a) * float(d)))
            print(f"Final velocity is {vF}m/s")
        else:
            t1 = (-float(v0) + math.sqrt((float(v0) * float(v0)) - (4 * float(a) / 2 * (-float(d))))) / float(a)
            t2 = (float(v0) + math.sqrt((float(v0) * float(v0)) - (4 * float(a) / 2 * (-float(d))))) / float(a)
            if (t1 > 0):
                print(f"Time is equal to {t1}s")
            else:
                print(f"Time is equal to {t2}s")
    elif vF == "" and v0 == "":
        which = input("Solve for initial velocity (v0) or final velocity (vF)? ")
        if (which.lower() == "vf" or which.lower() == "final velocity"):   
            v0 = (float(d) / float(t)) - ((float(a) * float(t)) / 2)
            vF = v0 + (float(a) * float(t))
            print(f"Final velocity is {vF}m/s")
        else:
            v0 = (float(d) / float(t)) - ((float(a) * float(t)) / 2)
            print(f"Initial velocity is {v0}m/s")
    elif vF == "" and a == "":
        which = input("Solve for acceleration (a) or final velocity (vF)? ")
        if (which.lower() == "vf" or which.lower() == "final velocity"):   
            vF = ((float(d) * 2) / float(t)) - float(v0)
            print(f"Final velocity is {vF}m/s")
        else:
            vF = ((float(d) * 2) / float(t)) - float(v0)
            a = (vF - float(v0)) / float(t)
            print(f"Acceleration is {a} meters per second squared")
    elif v0 == "" and a == "":
        which = input("Solve for acceleration (a) or initial velocity (v0)? ")
        if (which.lower() == "v0" or which.lower() == "initial velocity"):   
            v0 = ((2 * float(d)) / float(t)) - float(vF)
            print(f"Initial velocity is {v0}m/s")
        else: 
            v0 = ((2 * float(d)) / float(t)) - float(vF)
            a = (float(vF) - v0) / float(t)
            print(f"Acceleration is {a} meters per second squared")
    elif v0 == "" and d == "":
        which = input("Solve for displacement (d) or initial velocity (v0)? ")
        if (which.lower() == "v0" or which.lower() == "initial velocity"):
            v0 = float(vF) - (float(a) * float(t))
            print(f"Initial velocity is {v0}m/s")
        else:
            v0 = float(vF) - (float(a) * float(t))
            d = ((float(v0) + float(vF)) / 2) * float(t)
            print(f"Displacement is {d} meters")
    elif v0 == "" and t == "":
        which = input("Solve for time (t) or initial velocity (v0)? ")
        if (which.lower() == "v0" or which.lower() == "initial velocity"):
            t1 = (-float(vF) + math.sqrt((float(vF) * float(vF)) - (4 * float(a) / 2 * (float(d))))) / (-(float(a)))
            t2 = (-float(vF) - math.sqrt((float(vF) * float(vF)) - (4 * float(a) / 2 * (float(d))))) / (-(float(a)))
            if (t1 >= 0): 
                v0 = float(vF) - (float(a) * t1)
                print(f"Initial velocity is {v0}m/s")
            else:
                v0 = float(vF) - (float(a) * t2)
                print(f"Initial velocity is {v0}m/s")
        else:
            t1 = (-float(vF) + math.sqrt((float(vF) * float(vF)) - (4 * float(a) / 2 * (float(d))))) / (-(float(a)))
            t2 = (-float(vF) - math.sqrt((float(vF) * float(vF)) - (4 * float(a) / 2 * (float(d))))) / (-(float(a)))
            if (t1 >= 0): 
                print(f"Time is {t1}s")
            else:
                print(f"Time is {t2}s")
    elif a == "" and d == "":
        which = input("Solve for the acceleration (a) or displacement (d)? ")
        if (which.lower() == "a" or which.lower() == "acceleration"):
            a = (float(vF) - float(v0)) / float(t)
            print(f"Acceleration is {a} meters per second squared")
        else:
            d = ((float(v0) + float(vF)) / 2) * float(t)
            print(f"Displacement is {d} meters")
    elif a == "" and t == "":        
        which = input("Solve for the acceleration (a) or time (t)? ")
        if (which.lower() == "a" or which.lower() == "acceleration"):
            t = (2 * float(d)) / (float(v0) + float(vF))
            a = (float(vF) - float(v0)) / float(t)
            print(f"Acceleration is {a} meters per second squared")
        else:
            t = (2 * float(d)) / (float(v0) + float(vF))
            print(f"Time is {t}s")
    elif d == "" and t == "":
        which = input("Solve for displacement (d) or time (t)? ")
        if (which.lower() == "d" or which.lower() == "displacement"):
            d = ((float(vF) * float(vF)) - (float(v0) * float(v0))) / (2 * float(a))
            print(f"Displacement is {d} meters")
        else:
            t = (float(vF) - float(v0)) / float(a)
            print(f"Time is {t}s")
    elif v0 == "":
        v0 = float(vF) - (float(a) * float(t))
        print(f"Initial velocity is {v0}m/s")
    elif vF == "":
        vF = float(v0) + (float(a) * float(t))
        print(f"Final velocity is {vF}m/s")
    elif a == "":
        a = (float(vF) - float(v0)) / float(t)
        print(f"Acceleration is {a} meters per second squared")
    elif t == "":
        t = (float(vF) - float(v0)) / float(a)
        print(f"Time is {t}s")
    elif d == "":
        d = ((float(v0) + float(vF)) / 2) * float(t)
        print(f"Displacement is {d} meters")
    else:
        print("I cannot perform a calculation with the provided values.")
            
kinematics()

restart = input("Type 'y' to run the program again, type 'n' to stop the program: ")

while (restart.lower() != "n"):
    kinematics()
    restart = input("Type 'y' to run the program again, type 'n' to stop the program: ")

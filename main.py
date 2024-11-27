import math

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
    v0 = (float(d) - (0.5 * float(a) * (float(t) * float(t)))) / float(t)
    print(f"Initial velocity is {v0}m/s")

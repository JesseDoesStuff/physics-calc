import math

print("Enter a integer or floating point number for each of the following prompts that you know. \n If you do not know a value, return an empty string")

v0 = input("What is your initial velocity? ")
vF = input("What is your final velocity? ")
a = input("What is your (constant) acceleration? ")
d = input("What is the displacement? ")
t = input("What is the time? ")

if vF == "" and d == "":
    d = (float(v0) * float(t)) + 0.5 * (float(a) * (float(t) * float(t)))
    print(f"Displacement is equal to {d} meters")
elif vF == "" and t == "":
    vF = math.sqrt((float(v0) * float(v0)) + (2 * float(a) * float(d)))
    print(f"Final velocity is {vF}m/s")
elif vF == "" and v0 == "":
    v0 = (float(d) - (0.5 * float(a) * (float(t) * float(t)))) / float(t)
    print(f"Initial velocity is {v0}m/s")
temperature=(int(input("enter the tempreture==>")))

if temperature<0:
    print("Freezing Atmosphere")
elif temperature<=10:
    print("Very cold atmosphere")
elif temperature<=20:
    print("cold atmosphere")
elif temperature<=30:
    print("Normal Atmosphere")
elif temperature<40:
    print("hot temperature")
elif temperature>=40:
    print("very hot temperature")
else:
    print(" invalid ")
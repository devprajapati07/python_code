print("green")
print("yello")
print("red")

signal_light=input("enter the signal light==>")

if signal_light=="green":
    print("Car is allowed to go.")
elif signal_light=="yellow":
    print("Car has to wait.")
elif signal_light=="red":
    print("Car has to stop.")
else:
    print("Unrecognized signal ")

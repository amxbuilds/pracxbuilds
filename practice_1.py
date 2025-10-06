import time
print("Hello")
time.sleep(0.5)
name_raw = input("\nWhat is your name? ").strip()
print(f"\nHello, {name_raw}!")
time.sleep(1)
age_raw = int(input("\nHow old are you? ").strip())
time.sleep(0.2)
print(f"\nhmm, {age_raw} years old.")
time.sleep(1)
if age_raw < 18:
    print("\nYou are just a fetus.")
elif age_raw == 18:
    print("\nYour free trial of this world has come to an end. Pay tax.")
else:
    print("\nhowever did you survive this long?")
time.sleep(1)
city_raw = input("\nWhat city do you live in? ").strip()
time.sleep(0.5)
print(f"\nalright.... {city_raw}.")
time.sleep(1)
if city_raw == "London":
    print("\nstabbing capital of the world; be careful out there")
elif city_raw == "Dhaka":
    print("\ntraffic must be horrible")
else:
    print("\nuhh, never heard of it")
time.sleep(1)
allowed_colors = {"red", "blue", "green", "yellow", "lavender", "orange"}
color_raw = input("\nWhat's your favorite color? ").strip()
time.sleep(0.5)
print(f"\nhmm... {color_raw}")
time.sleep(0.5)
if color_raw == "red":
    print("\nroses are red")
elif color_raw == "blue":
    print("\nviolets are blue")
elif color_raw == "lavender":
    print("\nbest color")
else:
    print(f"\n{color_raw} is nice, I guess")
time.sleep(1)
if city_raw != ("London", "Dhaka") and age_raw >= 18 and color_raw != "lavender":
    print(f"\nGoodbye, old loser from {city_raw} who likes {color_raw}.")
else:
    print(f"\nNice to meet you, {name_raw}, you seem like a decent person.")
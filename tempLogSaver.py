temps = []

for i in range(5):
    temp = float(input(f"Enter temperature {i+1}: "))
    temps.append(temp)

with open("temperature_log.txt", "w") as file:
    for t in temps:
        file.write(str(t) + "\n")

print("Temperatures saved in temperature_log.txt")

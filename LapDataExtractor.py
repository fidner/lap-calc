fileName = "LapData.txt" # put the name of your txt file here

with open(fileName, "r") as file:
    gemCost = 0
    timeTaken = 0
    i = 0
    data = file.readlines()

    while i < len(data):
        while i < len(data) and not data[i].strip():
            i += 1

        if i >= len(data):
            break

        lap_number = int(data[i].strip())
        i += 1
        i += 1

        if i + 1 < len(data):
            gem_cost = int(data[i].strip())
            gemCost += gem_cost
            i += 1 
            time_taken = int(data[i].strip())
            timeTaken += time_taken
            i += 1
        i += 1

x = int(input("How much gems do your league stamina refills cost?\n"))
y = int(input("How much gems do you earn upon completing your league battles?\n"))
z = int(input("How many league battles do you get per set?\n"))

gemCost += int((95 * (x - y)) / z) # very very rough estimate of how much extra gems you'll spend on leagues

print(f"ESTIMATED TOTAL GEM COST: {gemCost}")
print(f"ESTIMATED TOTAL TIME TAKEN: {timeTaken} minutes")
print(f"\nLEFTOVER TIME: {15840 - timeTaken} minutes")  # rough estimate of how much leftover time you'll have, if its in the negatives you need to gem more
print(f"AVERAGE WASTED TIME ALLOWED PER DAY: {int((15840-timeTaken)/11)} minutes")


"""
LAPDATA'S TXT FILE'S FORMAT:
[LapNumber]     <-- only remove laps that you don't want to include in the calculation (i.e. remove 47-49 if you're going to stop at lap 47 / remove laps 1-20 if you're already at lap 21)
[NewLine]
[GemCost]       <-- total amount of gems you'll spend on a single lap
[TimeTaken]     <-- total amount of time you'll spend on a single lap (in minutes)
[NewLine]
[NewLine]
"""


# trench solos

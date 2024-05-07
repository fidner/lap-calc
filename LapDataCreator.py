fileName = "LapData.txt" # replace with your txt file's name
totalGemCost = 0
totalTimeTaken = 0
startLap = int(input("What lap are you starting from?\n"))
endLap = int(input("What lap are you stopping at?\n"))

with open('LapData.txt', 'w') as file:
    for i in range(startLap, endLap):
        file.write(f"{i}\n")
        print(f"\nLAP: {i}")
        gemCost = int(input("TOTAL GEM COST: "))
        timeTaken = int(input("TOTAL TIME SPENT: "))
        file.write(f"{gemCost}\n")
        file.write(f"{timeTaken}\n\n")
        totalGemCost += gemCost
        totalTimeTaken += timeTaken

x = int(input("How much gems do your league stamina refills cost?\n"))
y = int(input("How much gems do you earn upon completing your league battles?\n"))
z = int(input("How many league battles do you get per set?\n"))

gemCost += int((95 * (x - y)) / z) # very rough estimate of how much extra gems you'll spend on leagues

print(f"ESTIMATED TOTAL GEM COST: {gemCost}")
print(f"ESTIMATED TOTAL TIME TAKEN: {timeTaken} minutes")
print(f"\nLEFTOVER TIME: {14400 - timeTaken} minutes")  # rough estimate of how much leftover time you'll have, if it's in the negatives you need to gem more
print(f"AVERAGE WASTED TIME ALLOWED PER DAY: {int((14400-timeTaken)/11)} minutes")

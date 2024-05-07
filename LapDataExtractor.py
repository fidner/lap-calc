fileName = "LapData.txt" # put the name of your txt file here

with open(fileName, "r") as file:
    gemCost = 0
    timeTaken = 0
    i = 0
    data = file.readlines()

    while i < len(data):
        if not data[i].strip():
            i += 1
            continue

        try:
            lap_number = int(data[i].strip())
            i += 1

            if i >= len(data):
                break

            i += 1

            gems_spent = int(data[i].strip())
            gemCost += gems_spent
            i += 1

            if i >= len(data):
                break
                # trench solos

            time_taken = int(data[i].strip())
            timeTaken += time_taken

            days = time_taken // (24 * 60)
            hours = (time_taken % (24 * 60)) // 60
            minutes = (time_taken % (24 * 60)) % 60

            print(f"Lap: {lap_number}, Gems Spent: {gems_spent}, Time Taken: {days} days, {hours} hours, {minutes} minutes")

            overall_days = timeTaken // (24 * 60)
            overall_hours = (timeTaken % (24 * 60)) // 60
            overall_minutes = (timeTaken % (24 * 60)) % 60

            print(f"Overall Gems Spent: {gemCost}, Overall Time Taken: {overall_days} days, {overall_hours} hours, {overall_minutes} minutes\n")

            i += 1
        except ValueError:
            print("Invalid data format. Skipping to the next lap.")
            i += 1

x = int(input("How much gems do your league stamina refills cost?\n"))
y = int(input("How much gems do you earn upon completing your league battles?\n"))
z = int(input("How many league battles do you get per set?\n"))

gemCost += int((95 * (x - y)) / z) # VERY rough estimate of how much extra gems you'll spend on leagues
total_days = timeTaken // (24 * 60)
total_hours = (timeTaken % (24 * 60)) // 60
total_minutes = (timeTaken % (24 * 60)) % 60

leftover_minutes = 14400 - timeTaken # rough estimate of how much leftover time you'll have, if its in the negatives you need to gem more
leftover_days = leftover_minutes // (24 * 60)
leftover_hours = (leftover_minutes % (24 * 60)) // 60
leftover_minutes = (leftover_minutes % (24 * 60)) % 60

print(f"\nTotal Gems Spent: {gemCost}")
print(f"Total Time Taken: {total_days} days, {total_hours} hours, {total_minutes} minutes")
print(f"Leftover Time: {leftover_days} days, {leftover_hours} hours, {leftover_minutes} minutes")

average_wasted_time_per_day = (14400 - timeTaken) / 11 
avg_wasted_days = average_wasted_time_per_day // (24 * 60)
avg_wasted_hours = (average_wasted_time_per_day % (24 * 60)) // 60
avg_wasted_minutes = (average_wasted_time_per_day % (24 * 60)) % 60

print(f"Average Wasted Time Per Day: {avg_wasted_days} days, {avg_wasted_hours} hours, {avg_wasted_minutes} minutes")


"""
LAPDATA'S TXT FILE'S FORMAT:
[LapNumber]     <-- only remove laps that you don't want to include in the calculation (i.e. remove 47-49 if you're going to stop at lap 47 / remove laps 1-20 if you're already at lap 21)
[NewLine]
[GemCost]       <-- total amount of gems you'll spend on a single lap
[TimeTaken]     <-- total amount of time you'll spend on a single lap (in minutes)
[NewLine]
[NewLine]
"""


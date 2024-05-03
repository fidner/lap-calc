## if you want to use my lap data
download LapDataExtractor.py raw / copy the code and paste it into your interpreter *(feel free to look at the code if you want to double check whether or not it's safe)*
then download LapData.txt and run the code. *(ditlep was used to collect this data)*

the gem spending per lap consisted of (more or less):
gemming all battles for 3/4 gems,
gemming the final item when the waittime for the final item was more than 1h. *(only applies to breeding/hatching missions)*


## if you want to make your own lap data
download LapDataCreator.py raw / copy the code and paste it into your interpreter *(again feel free to check the code)*,
then create a blank txt file,
set the fileName variable to the name of your txt file,
run the code,
sit for an eternity typing up the amount of gems you'll spend per lap and the time it'll take to complete said lap. *(ditlep will help / #guides in official dc server)*


it'll save into your txt file once you're done, so you can edit your data directly from the txt file if the gem cost / time taken is too high

you'll be given the extracted data after adding the data, but you have to use LapDataExtractor.py to extract the data out of your txt file afterwards

# LAPDATA'S TXT FILE'S FORMAT:
[LapNumber]         <-- only remove laps that you don't want to include in the calculation (i.e. remove 47-49 if you're going to stop at lap 47 / remove laps 1-20 if you're already at lap 21)\
[NewLine]\
[GemCost]           <-- total amount of gems you'll spend on a single lap\
[TimeTaken]         <-- total amount of time you'll spend on a single lap (in minutes)\
[NewLine]\
[NewLine]\

For example:
-------
1

5\
10

<br>

-------
Lap: 1

Gem cost: 5\
Time taken: 10

<br>

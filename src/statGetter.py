#Used for the fromRoman function
import roman

numLines = 0
numWords = 0
numChars = 0
numParts = 0
romNum = 0
#Opens the Coinbase file
f = open("data/Coinbase2022.txt", "r")
for line in f:
    numLines+=1
    #The number of characters would be equal to the length of the line
    numChars+=len(line)
    #Words are seperated by spaces, so the length of the array created by splitting the line by spaces gives the words
    numWords+=len(line.split())
    #Checks to see if the hard coded "PART" is in the line
    if("PART" in line):
        #If it is then there is a roman number after the "PART"
        items = line.split()
        #Converts the roman numeral to an actual number
        romNum = roman.fromRoman(items[items.index("PART")+1])
        #If the roman numeral is greater than the amount of parts than it replaces the number of parts
        if romNum > numParts:
            numParts = romNum
f.close()

#Opens the Companystats.txt file and writes the statistics information to it
with open('data/Companystats.txt','w') as f:
    f.write("Coinbase:")
    f.write("\n\tNumber of lines: "+str(numLines))
    f.write("\n\tNumber of words: "+str(numWords))
    f.write("\n\tNumber of characters: "+str(numChars))
    f.write("\n\tNumber of parts: "+str(numParts))
f.close()


#This is essentially a duplicate of the above code modified for the CampbellSoup2022.txt file
numLines = 0
numWords = 0
numChars = 0
numParts = 0
romNum = 0
f = open("data/CampbellSoup2022.txt", "r")
for line in f:
    numLines+=1
    numChars+=len(line)
    numWords+=len(line.split())
    if("PART" in line):
        items = line.split()
        romNum = roman.fromRoman(items[items.index("PART")+1])
        if romNum > numParts:
            numParts = romNum
f.close()

#The only change is that it appends to Companystats.txt to not overwrite it
with open('data/Companystats.txt','a') as f:
    f.write("\n\nCampbell Soup:")
    f.write("\n\tNumber of lines: "+str(numLines))
    f.write("\n\tNumber of words: "+str(numWords))
    f.write("\n\tNumber of characters: "+str(numChars))
    f.write("\n\tNumber of parts: "+str(numParts))
f.close()
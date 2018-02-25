#Script to perform shift substitutions

textfile = input("Enter filename: ")
fh = open(textfile, "r") #read file
fh.seek(0)

#Read from file and save each line to array
lines = []
for line in fh:
    line_array = line.split("\n")
    lines.append(line_array[0]) #Add to lines[]
    #print(line_array[0]) #Testing
fh.close()

#Open output file to save shifted texts
textfile = input("Enter filename to save shifted plaintexts: ")
fh = open(textfile, "w") #write to file
fh.seek(0)

#Initialize string to store shifted strings
shifted = ""

#Loop to go through each line in lines[] list
for line in lines:
    print("Original: \n" + line)

    #print(ord('Z')) #Testing
    #print(chr((ord('Z') -25))) #Testing

    #Split line into characters for easier shifting
    letters = list(line)

    #Loop to shift line by up to 25
    for i in range(1, 26):
        print("Shifting by..." + str(i)) #Testing

        #Loop to go through each letter in each line and shift
        for character in letters:
            #Shift each letter and append to shifted string
            if (ord(character) + i) > 90:
                shifted += chr(ord(character) + i - 26) #make it A by subtracting 26
            else:
                shifted += chr(ord(character) + i)


        #print(shifted) #Testing
        #Save string to file
        fh.write(shifted + "\n")
        #Clear string for next iteration
        shifted = ""

        #answ = input("Press enter for next shift.") #Optional

fh.close()

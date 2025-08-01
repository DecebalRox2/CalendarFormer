import os

with open("basecal.ics","r") as f1:
    data1 = f1.readlines()

with open("infocal.ics","r") as f2:
    data2 = f2.readlines()

with open("transformedcal.txt","w") as f3:
    f3.write("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:uci.edu\nX-WR-TIMEZONE:America/Los_Angeles\nBEGIN:VTIMEZONE\nTZID:America/Los_Angeles\nX-LIC-LOCATION:America/Los_Angeles\nBEGIN:DAYLIGHT\nTZOFFSETFROM:-0800\nTZOFFSETTO:-0700\nTZNAME:PDT\nDTSTART:19700308T020000\nRRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\nEND:DAYLIGHT\nBEGIN:STANDARD\nTZOFFSETFROM:-0700\nTZOFFSETTO:-0800\nTZNAME:PST\nDTSTART:19701101T020000\nRRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\nEND:STANDARD\nEND:VTIMEZONE")
    k = 25
    while k < len(data2) - 9:
        if "Final" not in data2[k+1]:
            f3.write("\nBEGIN:VEVENT\n")
            f3.write(data2[k]) # Adds UID
            f3.write(data2[k+3]) # Adds start date and time
            f3.write("SEQUENCE:0\nTRANSP:OPAQUE\n") # Prints parameters I have no clue about
            f3.write(data2[k+4]) # Adds end date and time
            f3.write(data2[k+6]) # Adds location
            f3.write("SUMMARY:" + ((data2[k+1].split(":"))[1].split(" ")[0]).upper() + " " + (data2[k+1].split(":"))[1].split(" ")[1] + " " + (data2[k+5].split("\\n"))[0].split(":")[1] + " " + "(" + (((data2[k+1].split(":"))[1].split(" ")[2]).upper()).strip("\n") + ")") # Adds summary
            f3.write("\nCLASS:PUBLIC\n") # Adds another parameter I have no clue about
            f3.write(data2[k+7]) # Adds repetiton rule if event is not a final
            f3.write("END:VEVENT")
            k += 10
        else:
            f3.write("\nBEGIN:VEVENT\n")
            f3.write(data2[k]) # Adds UID
            f3.write(data2[k+3]) # Adds start date and time
            f3.write("SEQUENCE:0\nTRANSP:OPAQUE\n") # Prints parameters I have no clue about
            f3.write(data2[k+4]) # Adds end date and time
            f3.write(data2[k+1]) # Adds summary
            f3.write("\nCLASS:PUBLIC\n") # Adds another parameter I have no clue about
            f3.write("END:VEVENT")
            k += 8
    f3.write("\nEND:VCALENDAR")

# Convert txt to ics file

thisFile = "transformedcal.txt"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".ics")

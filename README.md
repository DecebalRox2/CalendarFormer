# CalendarFormer
Transforms a .ics file from AntAlmanac into a .ics file from the now-retired MyEEE+

The .ics file from UCI's now-retired MyEEE+ was very informative, and AntAlmanac's one just doesn't cut it. So, I wrote up a program to transform one file to another so my calendar can still look as aesthetic as usual! The sacrifice? My sanity. Writing this was honestly frustrating sometimes.

Anyway, the main program is in calendarformer.py. It takes in an input file infocal.ics (the .ics file from AntAlmanac), uses the file basecal.ics (an old .ics file from MyEEE+) as the basis for the transformation, and spits out transformedcal.ics, your new .ics file which (arguably) looks better on Google Calendar than AntAlmanac's does.

Most people probably wouldn't care about this, but I really loved the way MyEEE+ .ics files looked. If you feel the same, go ahead, use it too!

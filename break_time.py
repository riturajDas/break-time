#this program alerts that 2 hours have passed since staring at the computer
#screen and its now time to take a break with a soothing youtube video
import time
import webbrowser

total_breaks = 3
total_counts = 0

print "PROGRAM STARTED ON: "+time.ctime()
while(total_breaks > total_counts):
    time.sleep(2*60*60)
    print "BREAK TIME #"+total_breaks+" !!!"
    webbrowser.open("https://www.youtube.com/watch?v=MV4hrOBC2zc&list=UULP1LFCaIifzrpyUX2o0xiA")
    total_breaks += 1

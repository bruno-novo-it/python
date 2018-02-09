import time
import webbrowser

# Function to calculate the passing time between the breaks
def calc_seconds_passing(seconds):
    print("\nThe Break Started at: {}".format(time.ctime()))
    finish_time = time.time() + seconds
    print("\nWill End At: {}".format(time.ctime(finish_time)))
    print("\nStarting Counting The Remaining Time...")
    remaining_time = finish_time - time.time()
    while(time.time() < finish_time):
        print("Time Remaining For The Break: {}".format(time.strftime('%H:%M:%S', time.gmtime(round(remaining_time,2)))))
        time.sleep(1)
        remaining_time -= 1

# Just to use in the while loop
starting_time = 0

# Getting the Number of Breaks the User Wants
break_time = int(input("\nEnter Amount Of Breaks You Want: "))

# Get the Time the User Wants Between the Breaks
seconds = int(input("\nEnter Amount Of Time Before Break You Want, in seconds: "))

# Start the While Loop
while(starting_time < break_time):
    calc_seconds_passing(seconds)
    print("\nAbrindo Navegador...")
    webbrowser.open("https://www.youtube.com/watch?v=o5D7wuhxATY")
    starting_time += 1

# Just some Functions Using Time

# print(time.strftime("%a %b %d %H:%M:%S %Y"))

# print("Print the Month: {}".format(time.strftime("%b")))
# print("Print the Day of The Month: {}".format(time.strftime("%d")))
# print("Print the Day of The Week: {}".format(time.strftime("%a")))
# print("Print the Hour: {}".format(time.strftime("%H")))
# print("Print the Minutes: {}".format(time.strftime("%M")))
# print("Print the Seconds: {}".format(time.strftime("%S")))
# print("Print the Year: {}".format(time.strftime("%Y")))

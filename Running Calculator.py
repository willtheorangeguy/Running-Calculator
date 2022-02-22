# Running Calculator Concept
# (C) 2022 - For the Sada's

# MATH CONSTANTS
ft = 3.281
miles = 1609.344
half_marathon = 21097.5
marathon = 42195

# CONVERSION VARIABLES
unit = ""

# WELCOME
run = True
length_run = True

print(r"""
                                        ,////,
                                        /// 6|
                                        //  _|
                                       _/_,-'
                                  _.-/'/   \   ,/;,
                               ,-' /'  \_   \ / _/
                               `\ /     _/\  ` /
                                 |     /,  `\_/
                                 |     \'
                     /\_        /`      /\
                   /' /_``--.__/\  `,. /  \
                  |_/`  `-._     `\/  `\   `.
                            `-.__/'     `\   |
                                          `\  \
                                            `\ \
                                              \_\__
                                               \___)""")
print(r"""
                                        _             
                                       (_)            
                 _ __ _   _ _ __  _ __  _ _ __   __ _ 
                | '__| | | | '_ \| '_ \| | '_ \ / _` |
                | |  | |_| | | | | | | | | | | | (_| |
                |_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
                                                 __/ |
                                                |___/ 
""")
print("              WELCOME TO THE RUNNING SPEED CALCULATOR \n    Please answer each question to receive your time and speed! \nNote: Currently, the program only displays results in metric values. \n")

# LENGTH ENTRY
# Type
while run == True:
    while length_run == True:
        length_type = str(input("What is the name of unit you will be inputting? "))
        if length_type.lower() == "marathons":
            unit="marathon"
            print("You are now entering in marathons! \n")
            length_run = False
        elif length_type.lower() == "half marathons":
            unit="halfmarathon"
            print("You are now entering in half-marathons! \n")
            length_run = False
        elif length_type.lower() == "miles":
            unit="miles"
            print("You are now entering in miles! \n")
            length_run = False
        elif length_type.lower() == "feet":
            unit="feet"
            print("You are now entering in feet! \n")
            length_run = False
        elif length_type.lower() == "kilometers":
            unit="kilometers"
            print("You are now entering in kilometers! \n")
            length_run = False
        elif length_type.lower() == "meters":
            unit="meters"
            print("You are now entering in meters! \n")
            length_run = False
        elif length_type.lower() == "quit":
            length_run = False
            run = False 
            exit()
        else:
            length_run = True
            print("Please try again. Options are: \n - Marathons \n - Half Marathons \n - Miles \n - Feet  \n - Kilometers \n - Meters \n - Quit (to exit) \n")

    # Value - needs to be in meters
    distance = 0
    length = float(input("How far did you run? "))
    hours = int(input("How many hours did it take you? (if < 1, enter 0) "))
    mins = int(input("How many minutes did it take you? (if < 1, enter 0) "))
    secs = int(input("How many seconds did it take you? (if < 1, enter 0) "))

    # DISTANCE CALCULATION
    if unit == "marathon":
        distance = length*marathon
        unit == "meters"
    elif unit == "halfmarathon":
        distance = length*half_marathon
        unit == "meters"
    elif unit == "miles":
        distance = length*miles
        unit == "meters"
    elif unit == "feet":
        distance = length/ft
        unit == "meters"
    elif unit == "kilometers":
        distance = length*1000
        unit == "meters"
    elif unit == "meters":
        distance = length
        unit == "meters"
    else:
        pass

    # TIME CALCULATION
    time = 0
    time = (hours*3600) + (mins*60) + secs
    
    # SPEED CALCULATION
    metersps = distance/time
    kmph = metersps*3.6

    # PRINT FINAL RESPONSES
    # Change very long meters to kms
    if distance >= 1000:
        distance = distance/1000
        unit = "kilometers"
    else:
        distance = distance
        unit = "meters"

    print("")
    if unit == "meters":
        print("You travelled " + str(round(distance, 2)) + " meters.")
    else:
        print("You travelled " + str(round(distance, 2)) + " kilometers.")
    print("At a speed of " + str(round(metersps, 2)) + " meters per second or " + str(round(kmph, 2)) + " kilometers per hour. \n\n")
    length_run = True 

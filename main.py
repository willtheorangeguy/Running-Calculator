"""
Running Calculator Concept - for the Sada's
Copyright (C) 2022-2023 @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# pylint: disable=locally-disabled, invalid-name, too-many-locals, too-many-branches, too-many-statements

# Running Calculator
import sys


def calculate_distance(distance, unit):
    """Calculate the distance in meters."""
    if distance > 1000:
        distance = distance / 1000
        unit = "kilometers"
    else:
        unit = "meters"
    return distance, unit


def display_result(distance, unit, metersps, kmph):
    """Display the result."""
    print("")
    if unit == "meters":
        print("You traveled " + str(round(distance, 2)) + " meters.")
    else:
        print("You traveled " + str(round(distance, 2)) + " kilometers.")
    print(
        "Your speed was "
        + str(round(metersps, 2))
        + " meters per second or "
        + str(round(kmph, 2))
        + " kilometers per hour. \n\n"
    )


def main():
    """Main entry point of the app."""
    # MATH CONSTANTS
    FT = 3.281
    MILES = 1609.344
    HALF_MARATHON = 21097.5
    MARATHON = 42195

    # CONVERSION VARIABLES
    unit = ""

    # WELCOME
    run = True
    length_run = True
    time_run = True

    print(
        r"""
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
                                                  \___)"""
    )
    print(
        r"""
                                        _
                                        (_)
                    _ __ _   _ _ __  _ __  _ _ __   __ _
                | '__| | | | '_ \| '_ \| | '_ \ / _` |
                | |  | |_| | | | | | | | | | | | (_| |
                |_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
                                                 __/ |
                                                |___/
    """
    )
    print("              WELCOME TO THE RUNNING SPEED CALCULATOR")
    print("    Please answer each question to receive your time and speed!")
    print("Note: Currently, the program only displays results in metric values. \n")

    # LENGTH ENTRY
    while run:
        # Type of Measurement
        while length_run:
            length_type = str(input("What unit will you be inputting? "))
            if length_type.lower() == "marathons" or length_type.lower() == "marathon":
                unit = "marathon"
                print("You are now entering in marathons! \n")
                length_run = False
            elif (
                length_type.lower() == "half marathons"
                or length_type.lower() == "half marathon"
            ):
                unit = "halfmarathon"
                print("You are now entering in half-marathons! \n")
                length_run = False
            elif length_type.lower() == "miles" or length_type.lower() == "mile":
                unit = "miles"
                print("You are now entering in miles! \n")
                length_run = False
            elif length_type.lower() == "feet" or length_type.lower() == "foot":
                unit = "feet"
                print("You are now entering in feet! \n")
                length_run = False
            elif (
                length_type.lower() == "kilometers"
                or length_type.lower() == "kilometer"
            ):
                unit = "kilometers"
                print("You are now entering in kilometers! \n")
                length_run = False
            elif length_type.lower() == "meters" or length_type.lower() == "meter":
                unit = "meters"
                print("You are now entering in meters! \n")
                length_run = False
            elif length_type.lower() == "license":
                print("Running Calculator Copyright (C) 2022-2023 @willtheorangeguy")
                print(
                    "This program comes with ABSOLUTELY NO WARRANTY;"
                    " for details view the license."
                )
                print("This is free software, and you are welcome to redistribute it")
                print("under certain conditions; view the license for details. \n")
                length_run = True
            elif length_type.lower() == "quit" or length_type.lower() == "exit":
                length_run = False
                run = False
                sys.exit()
            else:
                print("Please try again. Options are:")
                print("Marathons\t 42195m")
                print("Half Marathons\t 21907.5m")
                print("Miles\t\t 1069.3m")
                print("Feet\t\t 0.38m")
                print("Kilometers\t 1000m")
                print("Meters\t\t 1m")
                print("license\t\t View the license file.")
                print("exit\t\t Exit the program. \n")
                print("quit\t\t Exit the program. \n")
                length_run = True

        # Value
        distance = 0
        while time_run:
            try:  # enable only numerical values
                time_run = False
                length = float(input("How far did you run? "))
                hours = int(input("How many hours did it take you? (if < 1, enter 0) "))
                mins = int(
                    input("How many minutes did it take you? (if < 1, enter 0) ")
                )
                secs = float(input("How many seconds did it take you? "))
            except ValueError:
                print(
                    "Values must be in numerical form, "
                    "and only seconds can be a decimal! \n"
                )
                time_run = True

        # DISTANCE CALCULATION - conversion to meters
        if unit == "marathon":
            distance = length * MARATHON
        elif unit == "halfmarathon":
            distance = length * HALF_MARATHON
        elif unit == "miles":
            distance = length * MILES
        elif unit == "feet":
            distance = length / FT
        elif unit == "kilometers":
            distance = length * 1000
        elif unit == "meters":
            distance = length
        else:
            pass

        # TIME CALCULATION
        time = 0
        time = (hours * 3600) + (mins * 60) + secs

        # SPEED CALCULATION
        metersps = distance / time
        kmph = metersps * 3.6

        # PRINT FINAL RESPONSES
        distance, unit = calculate_distance(distance, unit)
        display_result(distance, unit, metersps, kmph)

        length_run = True
        time_run = True


# Execute only if run as the entry point into the program
if __name__ == "__main__":
    main()

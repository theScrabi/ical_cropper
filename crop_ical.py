#!/usr/bin/env python3

import sys
from os import system

from typing import Final

USAGE_STRING: Final = """usage: crop_ical.py input_file year1 [year2 ...]
    input_file: this needs to be an ics file.
    year1, year2, etc.: Years to include in your cropped ics file."""

if len(sys.argv) < 3:
    print(USAGE_STRING)
    exit(1)


if system("which unix2dos > /dev/null") != 0:
    print("$ which unix2dos failed. Please ensure unix2dos is installed.")
    exit(2)

filename: Final = sys.argv[1]
cropped_file_name: Final = filename.replace(".ics", "_cropped.ics")

years_to_include: Final = sys.argv[1:]


def does_line_contain_accepted_date(line: str) -> bool:
    for year in years_to_include:
        if year in line:
            return True
    return False


cropped_event_list: list[str] = []

current_event: list[str] = []
date_in_event = False

with open(filename, "r") as ics_file:
    for line in ics_file.readlines():

        if "BEGIN:VEVENT" in line or "BEGIN:VTODO" in line or "BEGIN:VTIMEZONE" in line:
            current_event = []
            date_in_event = False
            current_event.append(line)
        elif len(current_event) == 0:
            cropped_event_list.append(line)
        else:
            current_event.append(line)

        if (
            "BEGIN:VTIMEZONE" in line
            or "BEGIN:STANDARD" in line
            or "BEGIN:DAYLIGHT" in line
            or does_line_contain_accepted_date(line)
        ):
            date_in_event = True

        if (
            "END:VEVENT" in line or "END:VTODO" in line or "END:VTIMEZONE" in line
        ) and date_in_event:
            cropped_event_list.extend(current_event)
            current_event = []

cropped_calendar = "".join(cropped_event_list)
with open(cropped_file_name, "w+") as cropped_file:
    cropped_file.writelines(cropped_calendar)

system(f"unix2dos {cropped_file_name} 2> /dev/null")

iCalendar Cropper
=================

Supply this script with an iCalendar file, and some years to crop that file to only contain dates and tasks within these years.
If you don't trust this script, you can check its output agains the [iCalendar validator](https://icalendar.org/validator.html).
Furthermore, its not garateed that some dates of other years will slip into the output, because this script will just check through
each line of the input iCalendar file to see if one of the supplied year dates can be found in that line.
This script is GPLv3 licensed.

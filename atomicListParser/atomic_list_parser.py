""" Parser for data provided by http://www.johnstonsarchive.net/nuclear/tests/index.html.

Autor: Juri Berlanda
License: MIT

This script takes the values from the right columns (they unfortunately differ in the various files), filters the data
for explosions having more then 1 kiloton, parses the dates, maps the date to the position within the track and sorts
the data chronologically. Finally the data is wrapped in a function call, one per row, and saved to a file, so it can
be copied to SuperCollider.

Note: I know, this script is kind of quick and dirty and a lot of copy and paste, but it does the job.
"""
import datetime

# Date to be mapped to the end of the track as unix timestamp in seconds
MAX_TIME = 2016000000
# Length of the track in seconds
TRACK_DURATION = 120


def parse_date(date_str):
    """ Date parser function for the date format used by the data source.

        Maps a date string of type like '2017  JUN  12' to a date object.
    """
    return datetime.datetime.strptime(date_str.strip(), "%Y  %b  %d")


def relative_date(date_str):
    """ Helper function for mapping the the date to seconds from track begin.

        The date equivalent to reference_date (see below) will return 0, the date equivalent to MAX_TIME will return
        TRACK_DURATION. Between these 2 values the dates are mapped linearly.
    """
    return str((parse_date(date_str) - reference_date).total_seconds() / MAX_TIME * TRACK_DURATION)

# The date equivalent to the begin of the track
reference_date = parse_date('1945  JUL  15')

parsed_list = []

with open('list-us.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[46:59])

        # Who?
        party = '\\US'

        # Where
        lat = atomic_test[83:93].strip()
        lon = atomic_test[94:104].strip()

        # Yield
        try:
            explosion_yield = atomic_test[171:179].strip()
            if float(explosion_yield) > 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

with open('list-gb.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[46:59])

        # Who?
        party = '\GB'

        # Where
        lat = atomic_test[83:93].strip()
        lon = atomic_test[94:105].strip()

        # Yield
        try:
            explosion_yield = atomic_test[171:179].strip()
            if float(explosion_yield) > 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

with open('list-fr.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[48:62])

        # Who?
        party = '\FR'

        # Where
        lat = atomic_test[86:96].strip()
        lon = atomic_test[97:108].strip()

        # Yield
        try:
            explosion_yield = atomic_test[176:182].strip()
            if float(explosion_yield) > 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

with open('list-ussr.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[48:62])

        # Who?
        party = '\\USSR'

        # Where
        lat = atomic_test[86:95].strip()
        lon = atomic_test[98:107].strip()

        # Yield
        try:
            explosion_yield = atomic_test[175:181].strip()
            if float(explosion_yield) > 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

with open('list-ch.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[48:62])

        # Who?
        party = '\CH'

        # Where
        lat = atomic_test[86:95].strip()
        lon = atomic_test[98:107].strip()

        # Yield
        try:
            explosion_yield = atomic_test[176:181].strip()
            if float(explosion_yield) > 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

with open('list-others.txt') as atomic_list:
    for atomic_test in atomic_list:

        # Date
        date = relative_date(atomic_test[48:62])

        # Who?
        party = '\OTHERS'

        # Where
        lat = atomic_test[86:95].strip()
        lon = atomic_test[97:107].strip()

        # Yield
        try:
            explosion_yield = atomic_test[177:181].strip()
            if float(explosion_yield) >= 1:
                parsed_list.append([date, party, explosion_yield, lat, lon])
        except Exception:
            pass

# Sort the list by timestamp
parsed_list = sorted(parsed_list, key=lambda atomic_test: float(atomic_test[0]))

# Write list as function calls to a file
with open('list-full.csv', 'w') as full_list:
    for line in parsed_list:
        full_list.write('\t~parseData.(' + ', '.join(line) + '),\n')

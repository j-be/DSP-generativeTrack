import datetime


MAX_TIME = 2016000000
TRACK_DURATION = 210

def parse_date(date_str):
    return datetime.datetime.strptime(date_str.strip(), "%Y  %b  %d")


def relative_date(date_str):
    return str((parse_date(date_str) - reference_date).total_seconds() / MAX_TIME * TRACK_DURATION)


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

with open('list-full.csv', 'w') as full_list:
    for line in parsed_list:
        full_list.write('\t~parseData.(' + ', '.join(line) + '),\n')

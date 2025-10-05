"""
This script tests the parsing of the time log file and the computation of the
job duration.
"""

import math
import sys
filename = "logtime.real.1"
with open(filename, 'r') as f:
    state = 0
    duration = 0
    for line in f:
        result = str.split(line, sep=":")
        if state == 0 and result[0] == 'inizio':
            duration -= int(result[1])
            state = 1
        elif state == 1 and (result[0] == 'pausa' or result[0] == 'fine'):
            duration += int(result[1])
            state = 2
        elif state == 2 and result[0] == 'ripresa':
            duration -= int(result[1])
            state = 1
        else:
            print('time log file is inconsistent', file=sys.stderr)
            exit()

    print(f'duration: {duration}')
    result = math.modf(duration/60)
    print(f'result: {result}')
    secs = math.ceil(result[0]*60)
    print(f'secs: {secs}')
    _mins = int(result[1])
    print(f'_mins: {_mins}')
    result = math.modf(_mins/60)
    print(f'result: {result}')
    mins = math.ceil(result[0]*60)
    print(f'mins: {mins}')
    _hours = int(result[1])
    print(f'_hours: {_hours}')
    result = math.modf(_hours/24)
    print(f'result: {result}')
    hours = math.ceil(result[0]*24)
    print(f'hours: {hours}')
    days = int(result[1])
    f.close()

print(f'{days:2d}d {hours:2d}h {mins:2d}m {secs:2d}s\n')

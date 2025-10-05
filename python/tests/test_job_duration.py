"""
This script tests the parsing of the time log file and the computation of the
job duration.
"""

import math
import sys
filename = "logtime.example"
with open(filename, 'r') as f:
    state = 0
    duration = 0
    for line in f:
        result = str.split(line, sep=":")
        if state == 0 and result[0] == 'start':
            duration -= int(result[1])
            state = 1
        elif state == 1 and (result[0] == 'pause' or result[0] == 'end'):
            duration += int(result[1])
            state = 2
        elif state == 2 and result[0] == 'resume':
            duration -= int(result[1])
            state = 1
        else:
            print('time log file is inconsistent', file=sys.stderr)
            exit()

    result = math.modf(duration/60)
    secs = math.ceil(result[0]*60)
    result = math.modf(int(result[1])/60)
    mins = math.ceil(result[0])*60
    result = math.modf(int(result[1])/24)
    hours = math.ceil(result[0]*24)
    days = int(result[1])
    f.close()

print(f'{days}d {hours}h {mins}m {secs}s\n')

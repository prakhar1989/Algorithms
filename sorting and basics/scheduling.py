""" data of the form -> wi, li 
(wi -> wieght of job i, li -> length of job i)
"""
test_data = """8 50
74 59
31 73
45 79
24 10
41 66
93 43
88 4
28 30
41 13
4 70
10 58
61 34
100 79
17 36
98 27
13 68
11 34
"""

def get_times(data):
    lines = [l for l in data.splitlines()]
    jobs = ((int(l.split()[0]), int(l.split()[1])) for l in lines)
    times = ((j[0]/float(j[1]), j[0], j[1]) for j in jobs)
    length, total_completion_time = 0,0
    for job in sorted(times, reverse=True):
        length += job[2]
        total_completion_time += job[1]*length
    print total_completion_time

get_times(test_data) # ans -> 164566

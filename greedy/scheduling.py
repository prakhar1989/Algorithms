def get_times():
    lines = [l for l in open("test.txt")]
    lines = lines[1:]
    jobs = ((int(l.split()[0]), int(l.split()[1])) for l in lines)
    times = [(j[0]/float(j[1]), j[0], j[1]) for j in jobs]
    length, total_completion_time = 0,0
    for job in sorted(times, reverse=True):
        length += job[2]
        total_completion_time += job[1]*length
    print total_completion_time

def average_mark(*args):
    marks_sum = 0
    for mark in args:
        marks_sum += mark
    return round(marks_sum / len(args), 1)

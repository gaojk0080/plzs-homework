#!/usr/bin/python3

def my_range(start, stop = None, step = None):
    if not isinstance(start, int):
        raise(ValueError)

    if stop is None:
        stop = start
        start = 0
    elif not isinstance(stop, int):
        raise(ValueError)

    if step is None:
        if stop > start:
            step = 1
        else:
            step = -1
    elif not isinstance(step, int) or step == 0:
        raise(ValueError)

    if stop > start and step < 0:
        raise(ValueError)
    elif stop < start and step > 0:
        raise(ValueError)

    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
        else:
            pass
    else:
        while i > stop:
            yield i
            i += step
        else:
            pass

test_cases = [
    {'input': (5)},
    {'input': (7)},
    {'input': (2, 10)},
    {'input': (2, 2)},
    {'input': (2, 10, 2)}
]

for test_case in test_cases:
    input_params = test_case['input']
    if isinstance(input_params, int):
    	l = list(my_range(input_params))
    else:
    	l = list(my_range(*input_params))
    print(l)


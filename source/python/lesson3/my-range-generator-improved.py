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
    {
        'input': (5,),
        'expected_output': [0, 1, 2, 3, 4]
    },
    {
        'input': (2, 10),
        'expected_output': [2, 3, 4, 5, 6, 7, 8, 9]
    },
    {
        'input': (2, 2),
        'expected_output': []
    },
    {
        'input': (2, 10, 2),
        'expected_output': [2, 4, 6, 8]
    }
]

for test_case in test_cases:
    input_params = test_case['input']
    expected_output = test_case['expected_output']
    if isinstance(input_params, int):
    	actual_output = list(my_range(input_params))
    else:
    	actual_output = list(my_range(*input_params))
    if actual_output == expected_output:
        print(input_params, "验证完成！输出与预期结果一致，输出结果为", actual_output)
    else:
        print(input_params, "验证失败！输出与预期结果不一致，预期输出结果为", expected_output, " 但实际输出结果为", actual_output)
    


total_num = len(boxes)
    if total_num == 0:
        return 0
    elif total_num <= 2:
        return max(boxes)
    else:
        select = [0 for i in range(total_num)]
        select[0] = boxes[0]
        select[1] = max(boxes[0], boxes[1])
        
        for i in range(2, total_num):
            select[i] = max(select[i-1], select[i-2]+boxes[i])
    
    return select[-1]



from operator import itemgetter
from itertools import groupby
    
def ranges(numbers):
    # Write your code here
    numbers = list(numbers)
    print(numbers)
    results = []
    for i, j in groupby(enumerate(numbers), lambda x:x[0]-x[1]):
        group = (map(itemgetter(1), j))
        group = list(map(int, group))
        results.append((group[0], group[-1]))

    output = ""
    for result in results:
        if result[0] != result[-1]:
            output += "{0}-{1},".format(result[0], result[-1])
        elif result[0] == result[-1]:
            output += "{0},".format(result[0])

    output = output.strip(",")
    return output


# Write your code here
    max_value = 999
    n, m = len(cave_layout), len(cave_layout[0])
    start_x, start_y = 0, 0
    end_x, end_y = n, m
    
    dist = [[max_value for i in range(m)] for j in range(n)]
    pre = [[None for i in range(m)] for j in range(n)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
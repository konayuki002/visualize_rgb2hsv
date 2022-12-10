# calculate_coordinate.py

# time: t, 
# t = 0: (x, y) ----> t = 1: (X, Y) 
def calculate_coordinate(t, x, y, X, Y):
    return (1 - t)*x + t*X, (1 - t)*y + t*Y


def calculate_coordinate_ndim(time, pos_a, pos_b):
    if len(pos_a) != len(pos_b):
        raise Exception('次元が違うのはダメぽよ')
    if time < 0 or 1 < time:
        raise Exception('時刻は 0 以上 1 以下でお願いするぽよ')

    dim = len(pos_a)
    result = []
    for i in range(dim):
        result.append((1 - time)*pos_a[i] + time*pos_b[i])
    return result


# Todo: move this into test.py later
if __name__ == '__main__':
    print(calculate_coordinate(0.5, 0, 0, 0, 1))
    print(calculate_coordinate(0.3, 0, 0, 0, 1))
    print(calculate_coordinate(0.2, 1, 1, 2, 9))
    print(calculate_coordinate(0.8, 0, 1, 0, 1))
    print(calculate_coordinate_ndim(0.5, [0, 0], [0, 1]))
    print(calculate_coordinate_ndim(0.3, [0, 0], [0, 1]))
    # print(calculate_coordinate_ndim(-1, [0, 0], [0, 1]))
    # print(calculate_coordinate_ndim(0.5, [1, 2, 3], [4, 5, 6, 7]))
    print(calculate_coordinate_ndim(0.5, [1, 2, 3], [4, 5, 6]))

# calculate_coordinate.py

# time: t, 
# t = 0: (x, y) ----> t = 1: (X, Y) 
def calculate_coordinate(t, x, y, X, Y):
    return (1 - t)*x + t*X, (1 - t)*y + t*Y

# Todo: move this into test.py later
if __name__ == "__main__":
    print(calculate_coordinate(0.5, 0, 0, 0, 1))
    print(calculate_coordinate(0.3, 0, 0, 0, 1))
    print(calculate_coordinate(0.2, 1, 1, 2, 9))
    print(calculate_coordinate(0.8, 0, 1, 0, 1))

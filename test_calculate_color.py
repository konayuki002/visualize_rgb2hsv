from matplotlib import pyplot as plt
from calculate_color import *

if __name__ == '__main__':
    
    O = Position_RGB(0, 0, 0, 0, 0, 0)
    W = Position_RGB(0, 1, 0, 1, 1, 1)
    R = Position_RGB(2**0.5/3, 1/3, 0, 1, 0, 0)
    C = Position_RGB(-2**0.5/3, 2/3, 0, 0, 1, 1)

    color_list = [O, W, R]
    step = 0.1
    s = t = 0 
    cnt = 0
    while s < 1:
        while s + t <= 1:
            color_list.append(calculate_color([O, W, R], s, t))
            color_list.append(calculate_color([O, W, C], s, t))
            t = t + step
            cnt = cnt + 1
        t = 0
        s = s + step
    print(cnt)

    f, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    for obj in color_list:
        col = (obj.r, obj.b, obj.b)
        ax.scatter(obj.x, obj.y, color = col)
    

    plt.xlim([-1, 1])
    plt.ylim([0, 1])
    plt.savefig('test_calculate_color.png')
    plt.show()

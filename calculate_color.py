# calculate_color.py

# 座標と色を同時に扱うクラス
# なんかこういうの欲しくないですか?
class Position_RGB:
    def __init__(self):
        self.x = self.y = self.z = self.r = self.g = self.b = 0

    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.z = 0
        self.r = r
        self.g = g
        self.b = b
    
    def __init__(self, x, y, z, r, g, b):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.g = g
        self.b = b
    
    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z, \
                                self.r + other.r, self.g + other.g, self.b + other.b)
    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z, \
                                self.r - other.r, self.g - other.g, self.b - other.b)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) \
                    + ", " + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + "]"


# ([[x, y(, z), r, g, b] x 3], s, t) --> [R, G, B]
# def calculate_color(list_of_position_rgb: list[Position_RGB], s, t) -> Position_RGB:
# ↑ こういう風に書きたいけど書き方が分からない (Type Hints 的な)
def calculate_color(list_of_position_rgb, s, t):
    if len(list_of_position_rgb) != 3:
        raise Exception('3 頂点欲しい!!')

    A = list_of_position_rgb[0]
    B = list_of_position_rgb[1]
    C = list_of_position_rgb[2]

    AB = B - A
    AC = C - A

    result_x = A.x + s*AB.x + t*AC.x
    result_y = A.y + s*AB.y + t*AC.y
    result_z = A.z + s*AB.z + t*AC.z
    result_r = A.r + s*AB.r + t*AC.r
    result_g = A.g + s*AB.g + t*AC.g
    result_b = A.b + s*AB.b + t*AC.b
    result = Position_RGB(result_x, result_y, result_z, result_r, result_g, result_b)
    return result


if __name__ == '__main__':
    # __sub__ の確認
    obj1 = Position_RGB(2, 1, 3, 0.2, 0.5, 0.7)
    obj2 = Position_RGB(2, 5, 0, 0, 0, 1)
    obj3 = obj2 - obj1
    print("obj3: ")
    print(obj3)

    # 
    O = Position_RGB(0, 0, 0, 0, 0, 0)
    W = Position_RGB(0, 1, 0, 1, 1, 1)
    P = Position_RGB(2**0.5/3, 1/3, 0, 1, 0, 0)
    s = 0.2
    t = 0.3

    print("color_st")
    color_st = calculate_color([O, W, P], s, t)
    print(color_st)
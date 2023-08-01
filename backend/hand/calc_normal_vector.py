import numpy as np


def calc_normal_vector(point1, point2, point3):
    vector1 = [point2.x - point1.x, point1.y - point2.y, point2.z - point1.z]
    vector2 = [point3.x - point1.x, point1.y - point3.y, point3.z - point1.z]

    # 法線ベクトル
    normal = np.cross(vector1, vector2)
    return normal * 5

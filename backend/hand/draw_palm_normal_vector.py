from functools import reduce


def _calc_palm_center(landmarks):
    palm_index = [0, 1, 2, 5, 9, 13, 17]
    palm_points_x = [landmarks.landmark[i].x for i in palm_index]
    palm_points_y = [landmarks.landmark[i].y for i in palm_index]
    palm_points_z = [landmarks.landmark[i].z for i in palm_index]

    x = reduce(lambda a, b: a + b, palm_points_x) / len(palm_index)
    y = reduce(lambda a, b: a + b, palm_points_y) / len(palm_index)
    z = reduce(lambda a, b: a + b, palm_points_z) / len(palm_index)
    return [x, y, z]


def draw_palm_normal_vector(ax_list, landmarks, label, vector):
    start_point = _calc_palm_center(landmarks)
    # start_point = [
    #     landmarks.landmark[0].x,
    #     landmarks.landmark[0].y,
    #     landmarks.landmark[0].z,
    # ]

    ax_list_index = 0
    if label == "Left":
        ax_list_index = 0
        vector = vector * -1
    elif label == "Right":
        ax_list_index = 1

    ax_list[ax_list_index].quiver(
        start_point[0],
        start_point[2],
        -1 * start_point[1],
        vector[0],
        vector[2],
        -1 * vector[1],
    )

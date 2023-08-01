def plot_world_landmarks(ax_list, landmarks, label):
    ax_list_index = 0
    if label == "Left":
        ax_list_index = 0
    elif label == "Right":
        ax_list_index = 1

    landmark_point = [
        (landmark.x, landmark.y, landmark.z) for landmark in landmarks.landmark
    ]

    palm_list = [0, 1, 2, 5, 9, 13, 17, 0]
    thumb_list = [2, 3, 4]
    index_finger_list = [5, 6, 7, 8]
    middle_finger_list = [9, 10, 11, 12]
    ring_finger_list = [13, 14, 15, 16]
    pinky_list = [17, 18, 19, 20]

    # 掌
    palm_x, palm_y, palm_z = [], [], []
    for idx in palm_list:
        point = landmark_point[idx]
        palm_x.append(point[0])
        palm_y.append(point[2])
        palm_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(palm_x, palm_y, palm_z)

    # 親指
    thumb_x, thumb_y, thumb_z = [], [], []
    for idx in thumb_list:
        point = landmark_point[idx]
        thumb_x.append(point[0])
        thumb_y.append(point[2])
        thumb_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(thumb_x, thumb_y, thumb_z)

    # 人差し指
    index_finger_x, index_finger_y, index_finger_z = [], [], []
    for idx in index_finger_list:
        point = landmark_point[idx]
        index_finger_x.append(point[0])
        index_finger_y.append(point[2])
        index_finger_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(index_finger_x, index_finger_y, index_finger_z)

    # 中指
    middle_finger_x, middle_finger_y, middle_finger_z = [], [], []
    for idx in middle_finger_list:
        point = landmark_point[idx]
        middle_finger_x.append(point[0])
        middle_finger_y.append(point[2])
        middle_finger_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(middle_finger_x, middle_finger_y, middle_finger_z)

    # 薬指
    ring_finger_x, ring_finger_y, ring_finger_z = [], [], []
    for idx in ring_finger_list:
        point = landmark_point[idx]
        ring_finger_x.append(point[0])
        ring_finger_y.append(point[2])
        ring_finger_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(ring_finger_x, ring_finger_y, ring_finger_z)

    # 小指
    pinky_x, pinky_y, pinky_z = [], [], []
    for idx in pinky_list:
        point = landmark_point[idx]
        pinky_x.append(point[0])
        pinky_y.append(point[2])
        pinky_z.append(point[1] * (-1))
    ax_list[ax_list_index].plot(pinky_x, pinky_y, pinky_z)

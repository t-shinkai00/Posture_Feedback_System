import cv2
import numpy as np


def _calc_bounding_rect(img, landmarks):
    height, width, _ = tuple(img.shape)

    landmark_array = np.empty((0, 2), int)

    for landmark in landmarks.landmark:
        landmark_x = min(int(landmark.x * width), width - 1)
        landmark_y = min(int(landmark.y * height), height - 1)

        landmark_point = [np.array((landmark_x, landmark_y))]

        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv2.boundingRect(landmark_array)

    return [x, y, x + w, y + h]


def draw_bounding_rect(img, landmarks):
    # 外接矩形
    brect = _calc_bounding_rect(img, landmarks)
    cv2.rectangle(img, (brect[0], brect[1]), (brect[2], brect[3]), (255, 0, 0), 2)

    return img

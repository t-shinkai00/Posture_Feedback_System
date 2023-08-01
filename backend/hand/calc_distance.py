from math import tan, radians, atan, cos


def _calc_L_px(h, fovy):
    return h / (2 * tan(radians(fovy) / 2))


def _calc_angle(y_px, L_px):
    return atan(y_px / L_px)


def calc_distance(img, landmarks, fovy, mean_size=18):
    h = img.shape[0]
    L_px = _calc_L_px(h, fovy)
    y_min = min(landmarks.landmark, key=lambda landmark: landmark.y)
    y_max = max(landmarks.landmark, key=lambda landmark: landmark.y)
    theta = _calc_angle((y_min.y - 0.5) * h, L_px)
    y_px = (y_max.y - y_min.y) * h
    L_cm = L_px * mean_size / y_px
    distance = L_cm / cos(theta)
    return round(distance, 2)

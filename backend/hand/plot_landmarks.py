import mediapipe as mp


def plot_landmarks(img, label, landmarks):
    mpDraw = mp.solutions.drawing_utils
    if label == "Right":
        drawing_spec = mpDraw.DrawingSpec(color=(48, 255, 48))
    elif label == "Left":
        drawing_spec = mpDraw.DrawingSpec(color=(48, 48, 255))
    mpDraw.draw_landmarks(
        img, landmarks, mp.solutions.hands.HAND_CONNECTIONS, drawing_spec
    )

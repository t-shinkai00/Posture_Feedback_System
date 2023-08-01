import os
import threading

import mediapipe as mp


def mediapipe_hands_model(
    model_complexity, max_num_hands, min_detection_confidence, min_tracking_confidence
):
    return mp.solutions.hands.Hands(
        model_complexity=model_complexity,
        max_num_hands=max_num_hands,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )


class GestureRecognizer:
    def __init__(
        self, max_num_hands, min_detection_confidence, min_tracking_confidence
    ):
        base_options = mp.tasks.BaseOptions
        gesture_recognizer = mp.tasks.vision.GestureRecognizer
        gesture_recognizer_options = mp.tasks.vision.GestureRecognizerOptions
        vision_running_mode = mp.tasks.vision.RunningMode

        options = gesture_recognizer_options(
            base_options=base_options(
                model_asset_path=os.path.abspath("hand/gesture_recognizer.task")
            ),
            running_mode=vision_running_mode.LIVE_STREAM,
            num_hands=max_num_hands,
            min_hand_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            result_callback=self._result_callback,
        )

        self.model = gesture_recognizer.create_from_options(options)
        self.lock = threading.Lock()
        self.current_gestures = []
        self.timestamp = 0

    def _result_callback(self, result, output_image, timestamp_ms):
        self.lock.acquire()
        self.current_gestures = []
        # print(f"gesture recognition result: {result.gestures[0][0]}")
        for single_hand_gesture_data in result.gestures:
            gesture_name = single_hand_gesture_data[0].category_name
            # print(gesture_name)
            self.current_gestures.append(gesture_name)
        self.lock.release()

    def get_gestures(self):
        return self.current_gestures

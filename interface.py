# interface.py

from recognition_module.Afacerecog import recognize_person


def recognize_face():
    """
    Adapter for RL system
    Converts recognition output → (bool, confidence)
    """

    status, name = recognize_person()

    # convert to RL format
    if status == "KNOWN":
        return True, 0.9   # high confidence
    else:
        return False, 0.3  # low confidence
# state.py

import random

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def get_confidence_level(conf):
    """
    Convert confidence score (0–1) into categories
    """
    if conf is None:
        return "low"

    if conf < 0.5:
        return "low"
    elif conf < 0.8:
        return "medium"
    else:
        return "high"


def get_attempts_category(attempts):
    """
    Convert number of attempts into categories
    """
    if attempts is None:
        return "0"

    if attempts >= 3:
        return "3+"
    else:
        return str(attempts)


def get_time_category(hour):
    """
    Convert hour (0–23) into day/night
    """
    if hour is None:
        return "day"

    if 6 <= hour < 18:
        return "day"
    else:
        return "night"


def get_face_label(is_known):
    """
    Convert recognition result into label
    """
    return "known" if is_known else "unknown"


# -------------------------------
# THREAT LEVEL FUNCTION (NEW)
# -------------------------------

def get_threat_level(face, conf, att, time):
    """
    Estimate threat level based on state
    """

    if face == "unknown" and conf == "low" and att == "3+":
        return "high"

    elif face == "unknown":
        return "medium"

    elif time == "night" and conf == "low":
        return "medium"

    else:
        return "low"


# -------------------------------
# MAIN STATE FUNCTION
# -------------------------------

def get_state(face_result, confidence, attempts, hour, mode):

    face = get_face_label(face_result)
    conf = get_confidence_level(confidence)
    att = get_attempts_category(attempts)
    time = get_time_category(hour)

    threat = get_threat_level(face, conf, att, time)

    return (face, conf, att, time, mode, threat)


# -------------------------------
# OPTIONAL: RANDOM STATE GENERATOR
# -------------------------------

def random_state():
    """
    Generate random valid state (for RL simulation/testing)
    """
    return (
        random.choice(["known", "unknown"]),
        random.choice(["low", "medium", "high"]),
        random.choice(["0", "1", "2", "3+"]),
        random.choice(["day", "night"]),
        random.choice(["protector", "defender"]),
        random.choice(["low", "medium", "high"])
    )


# -------------------------------
# OPTIONAL: VALIDATION (DEBUG USE)
# -------------------------------

def validate_state(state):
    """
    Ensures state format is correct
    """
    if len(state) != 6:
        raise ValueError("State must have 6 elements")

    face, conf, att, time, mode, threat = state

    assert face in ["known", "unknown"]
    assert conf in ["low", "medium", "high"]
    assert att in ["0", "1", "2", "3+"]
    assert time in ["day", "night"]
    assert mode in ["protector", "defender"]
    assert threat in ["low", "medium", "high"]

    return True


# -------------------------------
# TEST
# -------------------------------

if __name__ == "__main__":
    test_state = get_state(False, 0.42, 4, 23, "protector")
    print("Test State:", test_state)
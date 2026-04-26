# learning.py

import random

# IMPORTANT: correct import path
from DecisionEngine.agent import Q, initialize_state, choose_action

# -------------------------------
# HYPERPARAMETERS
# -------------------------------

alpha = 0.1   # learning rate
gamma = 0.9   # discount factor


# -------------------------------
# REWARD FUNCTION
# -------------------------------

def get_reward(state, action):
    """
    state = (face, conf, att, time, mode, threat)
    """

    face, conf, att, time, mode, threat = state

    # HIGH THREAT
    if threat == "high":
        if mode == "protector":
            return 10 if action in [2, 3] else -5
        else:  # defender
            return 10 if action in [4, 5] else -5

    # MEDIUM THREAT
    elif threat == "medium":
        if mode == "protector":
            return 5 if action == 1 else -2
        else:
            return 5 if action in [4, 5] else -2

    # LOW THREAT
    else:
        return 3 if action == 0 else -3


# -------------------------------
# Q-UPDATE
# -------------------------------

def update_q(state, action, reward, next_state):
    initialize_state(state)
    initialize_state(next_state)

    best_next = max(Q[next_state])

    Q[state][action] += alpha * (
        reward + gamma * best_next - Q[state][action]
    )


# -------------------------------
# RANDOM STATE (FOR TRAINING)
# -------------------------------

def random_state():
    return (
        random.choice(["known", "unknown"]),
        random.choice(["low", "medium", "high"]),
        random.choice(["0", "1", "2", "3+"]),
        random.choice(["day", "night"]),
        random.choice(["protector", "defender"]),
        random.choice(["low", "medium", "high"])
    )


# -------------------------------
# TRAINING LOOP
# -------------------------------

def train(episodes=5000):
    for _ in range(episodes):

        state = random_state()

        action = choose_action(state)

        reward = get_reward(state, action)

        next_state = random_state()

        update_q(state, action, reward, next_state)
# agent.py

import random

# -------------------------------
# ACTIONS
# -------------------------------

ACTIONS = {
    0: "do_nothing",
    1: "send_notification",
    2: "call_user",
    3: "call_emergency",
    4: "activate_buzzer",
    5: "activate_led"
}

NUM_ACTIONS = len(ACTIONS)

# -------------------------------
# Q-TABLE
# -------------------------------

Q = {}  # {state: [q_values]}

# -------------------------------
# HYPERPARAMETERS
# -------------------------------

epsilon = 0.2  # exploration


# -------------------------------
# INITIALIZE STATE
# -------------------------------

def initialize_state(state):
    if state not in Q:
        Q[state] = [0.0] * NUM_ACTIONS


# -------------------------------
# ACTION SELECTION (TRAINING)
# -------------------------------

def choose_action(state):
    initialize_state(state)

    if random.uniform(0, 1) < epsilon:
        return random.randint(0, NUM_ACTIONS - 1)
    else:
        return Q[state].index(max(Q[state]))


# -------------------------------
# FINAL DECISION (NO EXPLORATION)
# -------------------------------

def decide_action(state):
    initialize_state(state)
    return Q[state].index(max(Q[state]))
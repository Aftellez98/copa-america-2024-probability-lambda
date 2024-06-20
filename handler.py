import random

def predict_goal(event, context):

    return lambda: random.randint(1, 3)
from datetime import datetime, timedelta
GIGASECOND = 1e9
def add(moment):
    ""Given a moment, determine the moment after a gigasecond has passed."""
    return moment + timedelta(seconds=GIGASECOND)

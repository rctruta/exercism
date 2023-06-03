class Clock:
    """Implement a clock that handles times without dates."""
    def __init__(self, hour, minute):
        self.hour = (hour + minute // 60) %  24
        self.minute = minute % 60 

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        """Two clocks that represent the same time should be equal to each other."""
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        """Add minutes to a clock."""
        return Clock(hour=self.hour, minute=self.minute+minutes)

    def __sub__(self, minutes):
        """Subtract minutes from a clock."""
        return Clock(hour=self.hour, minute=self.minute-minutes)



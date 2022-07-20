from clock.Clock import Clock


class SpeakingClock:

    def __init__(self):
        self.clock = Clock()

    def say_time(self):
        current_time = self.clock.get_time()
        if current_time.hour == 12 and current_time.minute == 0:
            return "midday"
        elif current_time.hour == 0 and current_time.minute == 0:
            return "midnight"
        else:
            return "don't know"

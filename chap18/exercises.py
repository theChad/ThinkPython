# Exercise from Section 18.3

class Time:

    def time_to_int(self):
        return self.second + 60 * (self.minute + 60* self.hour)

    def __lt__(self, other):
        return self.time_to_int() < other.time_to_int()



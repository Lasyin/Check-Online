class PingEvent:
    def __init__(self, ping_location, curr_date, curr_time, success):
        self._ping_location = ping_location
        self._curr_date = curr_date
        self._curr_time = curr_time
        self._success = success

    def __str__(self):
        return("PING EVENT: " + str(self._ping_location) + " " + str(self._curr_date) + " " + str(self._curr_time) + " " + str(self._success))

    @property
    def ping_location(self):
        return self._ping_location
    @ping_location.setter
    def ping_location(self, value):
        self._ping_location=value
    @ping_location.deleter
    def ping_location(self):
        del self._ping_location

    @property
    def curr_date(self):
        return self._curr_date
    @curr_date.setter
    def curr_date(self, value):
        self._curr_date=value
    @curr_date.deleter
    def curr_date(self):
        del self._curr_date

    @property
    def curr_time(self):
        return self._curr_time
    @curr_time.setter
    def curr_time(self, value):
        self._curr_time=value
    @curr_time.deleter
    def curr_time(self):
        del self._curr_time

    @property
    def success(self):
        return self._success
    @success.setter
    def success(self, value):
        self._success=value
    @success.deleter
    def success(self):
        del self._success

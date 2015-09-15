class OutOfOfficeException(Exception):
    def __init__(self):
        self.message = 'We are out of office space'

    def __str__(self):
        return repr(self.message)


class OutOfLivingSpaceException(Exception):
    def __init__(self):
        self.message = 'We are out of living space'

    def __str__(self):
        return repr(self.message)

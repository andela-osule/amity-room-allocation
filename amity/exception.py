#!/usr/bin/python
# title          :amity/exception.py
# description    :This package allocates people to rooms in a building.
# author         :Oluwafemi Sule
# email          :oluwafemi.sule@andela.com
# date           :20150915
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================


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


class RoomTypeDoesNotExist(Exception):
    def __init__(self):
        self.message = 'Room type does not exist'

    def __str__(self):
        return repr(self.message)

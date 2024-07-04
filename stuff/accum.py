class Accumulator:
    def __init__(self):
        self._count = 0

    '''
    Python programming provides us with a built-in @property decorator
    which makes usage of getter and setters much easier in Object-Oriented Programming.
    '''

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more



class baseClass():
    text = 'hello Warren'
    id = 1
    beer = 0

    def giveBeer(self):
        self.beer += 1

    def isHappy(self):
        if self.beer >= 1:
            return True
        else:
            return False


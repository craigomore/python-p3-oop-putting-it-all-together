
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None

    # brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if type(value) is not str:
            raise TypeError("brand must be a string")
        self._brand = value

    # size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) not in [int, float]:
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, color, size):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Brand must be a string")

        if isinstance(color, str):
            self._color = color
        else:
            print("Color must be a string")

        if isinstance(size, int):
            self._size = size
        else:
            print("Size must be an integer")

    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Brand must be a string")

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            print("Color must be a string")

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("Size must be an integer")

    def condition(self):
        print("You've worn these shoes 0 times. They're brand new!")

    def wear(self):
        print("You've worn these shoes 1 time. They're still fresh!")

    brand = property(get_brand, set_brand)
    color = property(get_color, set_color)
    size = property(get_size, set_size)

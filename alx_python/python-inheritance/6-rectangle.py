class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = "name"
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            self.value = value
        else:
            raise TypeError(" {} must be an integer".format(name))

            
class Rectangle(BaseGeometry):
    
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
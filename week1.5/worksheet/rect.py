# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width,int):
            raise TypeError("Width must be an integer.")
        if not isinstance(height,int):
            raise TypeError("Height must be an integer.")      
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be greater than 0.")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        if self.width == self.height:
            return True

     def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.height + self.width)*2
        return perimeter       

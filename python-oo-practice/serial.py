"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes
    -------------
    start: int 
        starting number
    next: int
        sequentially generated number
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initialize starting number"""
        self.start = self.next = start
    
    # creates string description of the instance
    def __repr__(self):
        return f"SerialGenerator(start={self.start} next={self.next})"

    def generate(self):
        """Generate next consecutive number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to start number"""
        self.next = self.start
        # return self.next


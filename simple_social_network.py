"""A simple social network for tracking connections between people.
"""

class Person:
    """Represents person in social network
    
    Attributes:
        name (str): person's name.
        connections (set of Person): other people in social network that know
            this person.
    """
    def __init__(self, name):
        """Initializes a new Person object.
        """
        self.name = name
        self.connections = set()
        
    def connect(self, person2):
        """Connect with person2.
        
        Args:
            person2 (Person): the other person to connect to.
        """
        
        
        
        
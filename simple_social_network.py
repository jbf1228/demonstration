"""A simple social network for tracking connections between people.
"""

class Person:
    """Represents person in social network
    
    Attributes:
        name (str): person's name.
        connections (set of Person): other people in social network that know
            this person.
    """
#!/usr/bin/env python3

class Person:
    """
    A Person class with instance methods for basic human behaviors.
    """
    
    def talk(self):
        """
        Instance method that makes the person talk.
        Prints "Hello World!" to the console.
        """
        print("Hello World!")
    
    def walk(self):
        """
        Instance method that makes the person walk.
        Prints "The person is walking." to the console.
        """
        print("The person is walking.")


# Test the class (you can run this file directly to test)
if __name__ == "__main__":
    # Create an instance of Person
    guido = Person()
    
    # Test the talk method
    print("Testing talk method:")
    guido.talk()
    
    # Test the walk method
    print("Testing walk method:")
    guido.walk()
    
    # Create another instance to show each instance can use the methods
    alice = Person()
    print("\nTesting with another person instance:")
    alice.talk()
    alice.walk()
#!/usr/bin/env python3

class Dog:
    """
    A Dog class with instance methods for basic dog behaviors.
    """
    
    def bark(self):
        """
        Instance method that makes the dog bark.
        Prints "Woof!" to the console.
        """
        print("Woof!")
    
    def sit(self):
        """
        Instance method that makes the dog sit.
        Prints "The dog is sitting." to the console.
        """
        print("The dog is sitting.")


# Test the class (you can run this file directly to test)
if __name__ == "__main__":
    # Create an instance of Dog
    fido = Dog()
    
    # Test the bark method
    print("Testing bark method:")
    fido.bark()
    
    # Test the sit method
    print("Testing sit method:")
    fido.sit()
    
    # Create another instance to show each instance can use the methods
    snoopy = Dog()
    print("\nTesting with another dog instance:")
    snoopy.bark()
    snoopy.sit()
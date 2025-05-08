
"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  
    inches: float = feet * INCHES_IN_FOOT  
    print("That is", inches, "inches!")
    
    

if __name__ == '__main__':
    main()
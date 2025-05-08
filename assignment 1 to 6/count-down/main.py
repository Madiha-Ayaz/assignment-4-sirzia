import time

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrites the previous line
        time.sleep(1)
        t -= 1
    print("Time's up!")

# Get user input
try:
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)
except ValueError:
    print("Invalid input! Please enter an integer.")

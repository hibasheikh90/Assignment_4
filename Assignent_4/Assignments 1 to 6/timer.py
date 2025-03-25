import time

def countdown_timer(seconds):
    # Countdown loop
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        print(f"Time remaining: {minutes:02d}:{secs:02d}", end='\r')  # Display time in MM:SS format
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrement the time by 1 second

    print("Time's up!")  # Notify when time is up

def main():
    try:
        # Get the countdown time from the user
        time_in_seconds = int(input("Enter the countdown time in seconds: "))
        
        if time_in_seconds <= 0:
            print("Please enter a time greater than zero.")
        else:
            print("Starting the countdown...")
            countdown_timer(time_in_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")

if __name__ == '__main__':
    main()

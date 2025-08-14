import time

def pomodoro_time():
    # welcome message
    print("Welcome to the Pomodoro Timer!")

    # Get the number of minutes from the user and convert it to an integer
    mins = int(input("Enter time in minutes: "))
    
    # Convert minutes to total seconds
    total_Seconds = mins * 60

    # Loop until seconds count down to zero
    while total_Seconds >= 0:

        # Calculate the remaining minutes
        mins = total_Seconds // 60

        # Calculate the remaining seconds
        secs = total_Seconds % 60

        # Formt time as mm:ss
        clock = f"{mins:02d}:{secs:02d}"

        # Print the time on the same line (overwrite previous time)
        print(f"\rTime remaining: {clock}",end = "")

        # Waiting for 1 second before updating the timer
        time.sleep(1)

        # Decrease total seconds by 1
        total_Seconds-=1

    # Print final message when the timer finishes
    print("\nTime's up, Take a break!")


pomodoro_time()







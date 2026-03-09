def get_current_time():
    while True:
        try:
            time_now = int(input("Enter current time (0-23): "))
            if 0 <= time_now <= 23:
                return time_now
            else:
                print("Time must be between 0 and 23.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def get_wait_time():
    while True:
        try:
            wait_time = int(input("Enter number of hours to wait: "))
            if wait_time >= 0:
                return wait_time
            else:
                print("Wait time cannot be negative.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


current_time = get_current_time()
hours_to_wait = get_wait_time()

alarm_time = (current_time + hours_to_wait) % 24


print("Alarm set!")
print(f"It will be {alarm_time:02d}:00 when the alarm goes off.")

# room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# prompt for a course number
course = input("Enter a course number (e.g., CSC101): ").upper()

# check if course exists
if course in room_numbers:
    print("\nCourse Information:")
    print("Room Number:", room_numbers[course])
    print("Instructor:", instructors[course])
    print("Meeting Time:", meeting_times[course])
else:
    print("\nCourse not found.")

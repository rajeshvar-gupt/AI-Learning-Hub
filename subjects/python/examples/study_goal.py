"""PY-002: Validate whole-number minutes, then compare against a goal."""
raw_minutes = input("Minutes studied today: ")
try:
    minutes = int(raw_minutes)
except ValueError:
    print("Please enter a whole number, such as 30.")
else:
    if minutes < 0:
        print("Minutes cannot be negative.")
    elif minutes >= 30:
        print("Daily goal reached.")
    else:
        remaining = 30 - minutes
        print(f"Keep going: {remaining} more minutes to reach your goal.")

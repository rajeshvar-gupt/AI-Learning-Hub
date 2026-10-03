"""Collect study sessions until the learner enters q. Python built-ins only."""

total_minutes = 0
session_count = 0

while True:
    raw_minutes = input("Session minutes (q to finish): ").strip()
    if raw_minutes.lower() == "q":
        break

    try:
        minutes = int(raw_minutes)
    except ValueError:
        print("Please enter a whole number or q.")
        continue

    if minutes < 0:
        print("Minutes cannot be negative.")
        continue

    total_minutes += minutes
    session_count += 1
    print(f"Recorded {minutes} minutes.")

print(f"Sessions: {session_count}")
print(f"Total: {total_minutes} minutes")
if session_count == 0:
    print("No sessions recorded.")
else:
    average = total_minutes / session_count
    print(f"Average: {average:.1f} minutes")

"""PY-001: A fixed-input study profile. Uses only Python built-ins."""

learner_name = "Asha"
minutes_per_day = 30
study_days = 5
has_python = True

weekly_minutes = minutes_per_day * study_days
weekly_hours = weekly_minutes / 60

print(f"Learner: {learner_name}")
print(f"Weekly study: {weekly_minutes} minutes ({weekly_hours:.1f} hours)")
print(f"Python ready: {has_python}")

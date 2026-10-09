"""A fixed-data collections example; all learner IDs are fictional."""


def group_enrollments(enrollments):
    """Group (learner_id, course) pairs, preserving repeated enrollments."""
    by_course = {}
    for learner_id, course in enrollments:
        if course not in by_course:
            by_course[course] = []
        by_course[course].append(learner_id)
    return by_course


def main():
    enrollments = [
        ("L01", "Python"),
        ("L02", "Python"),
        ("L01", "ML"),
        ("L01", "Python"),
    ]
    by_course = group_enrollments(enrollments)
    print(f"Records: {len(enrollments)}")
    for course, learner_ids in by_course.items():
        print(f"{course}: {learner_ids}")
    python_learners = set(by_course.get("Python", []))
    ml_learners = set(by_course.get("ML", []))
    print(f"Unique Python learners: {sorted(python_learners)}")
    print(f"Both courses: {sorted(python_learners & ml_learners)}")
    print(f"Python only: {sorted(python_learners - ml_learners)}")


if __name__ == "__main__":
    main()

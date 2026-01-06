from datetime import datetime

LOG_FILE = "student_registration_updates.txt"

def record_update(update_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {update_message}\n")

# Example usage
record_update("Added email validation to student registration form")
record_update("Fixed bug in roll number generation")
record_update("Updated UI for student details page")

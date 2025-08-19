events = {}
participants = {}
attendance = {}

def add_event(event_id, name, date, age_limit, club):
    event = (event_id, name, date, age_limit, club)
    events[event_id] = event
    participants[event_id] = []
    attendance[event_id] = []
    print(f"Event '{name}' added successfully.\n")

def register_participant(name, age, event_id):  # Register participants
    if event_id not in events:
        print("Event ID not found.\n")
        return
    age_limit = events[event_id][3]
    if age > age_limit:
        print(f"{name} is over the age limit ({age_limit}) for this event.\n")
        return
    participant = {'name': name, 'age': age, 'present': False}
    participants[event_id].append(participant)
    print(f"{name} has been registered for event '{events[event_id][1]}'.\n")

def mark_attendance(event_id, name):
    found = False
    for p in participants[event_id]:
        if p['name'] == name:
            p['present'] = True
            found = True
            print(f"Marked {name} as present for event '{events[event_id][1]}'.\n")
            break
    if not found:
        print(f"{name} is not registered for this event.\n")

def attendance_report(event_id):
    if event_id not in participants:
        print("Invalid event ID.\n")
        return
    total = len(participants[event_id])
    present = sum(1 for p in participants[event_id] if p['present'])
    absent = total - present
    
    print(f"\nAttendance Report for '{events[event_id][1]}':")
    print(f"Total registered: {total}")
    print(f"Present: {present}")
    print(f"Absent: {absent}\n")

# Adding an event and registering participants
add_event("p", "Chess Tournament", "2025-09-01", 18, "Chess Club")
register_participant("Alice", 17, "p")  # Valid registration
register_participant("Bob", 19, "p")  # Over age limit
register_participant("Alice", 17, "p")  # Duplicate

mark_attendance("p", "Alice")
attendance_report("p")
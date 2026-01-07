from datetime import date

events = {
    "Tech Conference": date(2026, 1, 10),
    "Project Submission": date(2026, 1, 5)
}

today = date.today()

for event, event_date in events.items():
    days_left = (event_date - today).days
    if days_left >= 0:
        print(f"{event} in {days_left} days")

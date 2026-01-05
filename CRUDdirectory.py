events = {}

def add_event(event_id, title):
    events[event_id] = title

def delete_event(event_id):
    events.pop(event_id, None)

def show_events():
    for k, v in events.items():
        print(k, v)

add_event(1, "Tech Conference")
add_event(2, "AI Workshop")
delete_event(1)
show_events()

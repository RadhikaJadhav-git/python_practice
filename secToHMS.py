# Convert seconds to hours, minutes, and seconds

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

# Example usage
total_seconds = int(input("Enter time in seconds: "))
h, m, s = convert_seconds(total_seconds)
print(f"{h:02d}:{m:02d}:{s:02d}")

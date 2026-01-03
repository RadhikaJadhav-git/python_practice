log_data = [
    "INFO Server started",
    "ERROR Database connection failed",
    "INFO User logged in",
    "ERROR Timeout occurred",
    "ERROR Invalid credentials"
]

error_count = 0

for line in log_data:
    if "ERROR" in line:
        error_count += 1

print("Total Errors Found:", error_count)

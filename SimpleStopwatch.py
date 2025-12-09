import time

start = input("Press Enter to start...")

start_time = time.time()
input("Press Enter to stop...")

end_time = time.time()
elapsed = end_time - start_time

print("Elapsed time:", round(elapsed, 2), "seconds")

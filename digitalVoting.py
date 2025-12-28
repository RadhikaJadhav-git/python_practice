voters = []
votes = {"A": 0, "B": 0}

while True:
    voter_id = input("Enter voter ID (or exit): ")
    if voter_id == "exit":
        break

    if voter_id in voters:
        print("Already voted")
        continue

    choice = input("Vote A or B: ").upper()
    if choice in votes:
        votes[choice] += 1
        voters.append(voter_id)
        print("Vote recorded")
    else:
        print("Invalid choice")

print("Final Results:", votes)

from datetime import datetime

with open("counter.txt", "a") as file:
    file.write(f"Commit at {datetime.now()}\n")

from datetime import datetime

def log_result(test_name, result):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {test_name} | {result}\n")
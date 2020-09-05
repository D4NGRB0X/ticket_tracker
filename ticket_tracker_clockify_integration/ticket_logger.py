from datetime import datetime
import os
from csv import writer
from pathlib import Path

file_name = datetime.now().strftime("%Y-%m-%d")


def does_log_dir_exist():
    if not Path("./Logs").exists():
        os.mkdir("./Logs")


def does_daily_log_file_exist():
    os.chdir("./Logs")
    if not Path(f'{file_name}.csv').exists():
        with open(f'{file_name}.csv', "a+", newline='') as log:
            log_writer = writer(log)
            log_writer.writerow(["Client", "Ticket", "Start", "End", "Notes"])


def daily_log_add_entry(client, payload, notes=None):
    with open(f'{file_name}.csv', "a+", newline='') as log:
        log_writer = writer(log)
        log_writer.writerow(
            [client,
             payload["description"],
             datetime.fromisoformat(payload["start"].replace("Z", "+00:00")).astimezone().strftime('%H:%M:%S'),
             datetime.fromisoformat(payload["end"].replace("Z", "+00:00")).astimezone().strftime('%H:%M:%S'),
             notes]
        )

import time
from datetime import datetime as dt
import os


def block_websites(start_hour, end_hour):
    # Site to block
    sites_to_block = [
        "twitter.com",
    ]

    # Mac host file path
    mac_host = "/etc/hosts"
    redirect = "127.0.0.1"

    while True:
        try:
            current_time = dt.now()
            start_time = dt(current_time.year, current_time.month, current_time.day, start_hour)
            end_time = dt(current_time.year, current_time.month, current_time.day, end_hour)

            if start_time < current_time < end_time:
                print("Do the work ....")
                update_hosts(mac_host, sites_to_block, redirect)
            else:
                clear_hosts(mac_host, sites_to_block)
                print("Good Time")

            time.sleep(3)

        except PermissionError as e:
            print(f"Permission error: {e}. Try Running as Admin.")
            break


def update_hosts(host_file, sites, redirect):
    with open(host_file, "r+") as hostfile:
        content = hostfile.read()
        for site in sites:
            if site not in content:
                hostfile.write(f"{redirect} {site}\n")


def clear_hosts(host_file, sites):
    with open(host_file, "r+") as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites):
                hostfile.write(line)
        hostfile.truncate()


if __name__ == "__main__":
    block_websites(9, 21)

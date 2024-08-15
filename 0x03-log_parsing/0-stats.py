#!/usr/bin/python3
import sys
import signal

# Initialize the total file size and a dictionary to store status code counts
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0  # Counter to track the number of lines processed


def print_stats():
    """Function to print the current statistics."""
    print(f"File size: {total_size}")
    # Print each status code and (asc) been encountered
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Function to handle the CTRL + C signal."""
    print_stats()  # Print statistics when the script is interrupted
    sys.exit(0)  # Exit the program


# Register the signal handler for handling CTRL + C interruptions
signal.signal(signal.SIGINT, signal_handler)

# Read input from stdin line by line
for line in sys.stdin:
    line_count += 1
    try:
        # Split the line into parts and ensure it has the correct format
        parts = line.split()
        if len(parts) < 7:
            continue  # Skip lines that don't match the expected format

        # Extract the file size and add it to the total size
        file_size = int(parts[-1])
        total_size += file_size

        # Extract the status code (second to last part of the line)
        status_code = parts[-2]
        # Update the count of the status code if it's one of the expected codes
        if status_code in status_codes:
            status_codes[status_code] += 1

    except Exception:
        continue  # Skip the line if an error occurs during processing

    # Print statistics after every 10 lines are processed
    if line_count % 10 == 0:
        print_stats()

# Final statistics printout when the input ends
print_stats()

Here's a sample `README.md` file for your log parsing script:

```markdown
# Log Parsing Script

This Python script reads logs from standard input line by line, calculates metrics such as the total file size, and counts the occurrences of specific HTTP status codes. The script outputs statistics after every 10 lines or when interrupted by a keyboard signal (CTRL + C).

## Features

- Parses log lines in the format:
  ```
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  ```
- Computes and prints:
  - Total file size processed
  - Count of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)
- Outputs statistics every 10 lines or on keyboard interruption (CTRL + C).
  
## Installation

Ensure you have Python 3 installed on your system.

Clone the repository or download the script:

```bash
git clone https://github.com/yourusername/log_parsing.git
cd log_parsing
```

## Usage

To use the script, pipe log data into it. For example, you can use the provided log generator script:

```bash
./0-generator.py | ./0-stats.py
```

The script will read the log data, process it, and periodically output the computed metrics.

### Example Output

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

This output indicates that the total file size is 5213 bytes, with 2 occurrences of status code 200, 1 of 401, 2 of 403, and so on.

## Handling Interruptions

If the script is interrupted with CTRL + C, it will print the final statistics before exiting:

```
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Notes

- The script skips lines that do not match the expected format.
- Only the specified status codes are counted. If a status code is not present in the logs, it is not included in the output.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
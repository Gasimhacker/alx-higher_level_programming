#!/usr/bin/python3

"""Print statistics collected from the standard input"""


def print_metrics(file_size, status_codes):
    """Print the collected data

    Args:
        file_size (int): The accumulated size
        status_codes (dict): The accumulated status codes
    """

    print(f"File size: {file_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    from sys import stdin

    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    lines = 0

    try:
        for line in stdin:
            line = line.split(" ")
            file_size += int(line[-1])
            if line[-2] in status_codes:
                status_codes[line[-2]] += 1

            lines += 1

            if ((lines % 10) == 0):
                print_metrics(file_size, status_codes)
        print_metrics(file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise

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
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    lines = 0

    try:
        for line in stdin:
            line = line.split(" ")

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if (status_codes.get(line[-2], -1) == -1):
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

            lines += 1

            if ((lines % 10) == 0):
                print_metrics(file_size, status_codes)
        print_metrics(file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise

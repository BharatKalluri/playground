from typing import Iterator


def convert_str_time_to_timestamp_in_ms(time_str: str):
    split_on_comma = time_str.split(",")
    ms = int(split_on_comma[1])
    hours, minutes, seconds = map(int, split_on_comma[0].split(":"))
    return ms + (seconds * 1000) + (minutes * 60 * 1000) + (hours * 60 * 60 * 1000)


def is_line_with_timestamps(line_contents: str):
    return '-->' in line_contents


def str_iter_arr_to_single_line(str_iter: Iterator[str]):
    return '\n'.join([str(g) for g in str_iter])

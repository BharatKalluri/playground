import json
import os.path
import re
import sys
from itertools import groupby, count
from typing import Iterator

from constants import TIMESTAMPS_REGEX
from cue_block import CueBlock
from utils import is_line_with_timestamps, str_iter_arr_to_single_line


def get_cue_blocks_from_srt_string(srt_string: str):
    all_cue_blocks = []
    cue_count = count(0)

    srt_lines: [str] = srt_string.splitlines()
    filter_numbers: Iterator[str] = filter(lambda x: not x.isdigit(), srt_lines)
    filter_empty_lines: Iterator[str] = filter(lambda x: len(x) > 0, filter_numbers)

    groupby_iter: Iterator[tuple[bool, Iterator[str]]] = groupby(filter_empty_lines, is_line_with_timestamps)

    for key, group in groupby_iter:
        current_line = str_iter_arr_to_single_line(group)
        if is_line_with_timestamps(current_line):
            timestamp_data_str = current_line
            regex_matches: dict[str, str] = re.match(
                TIMESTAMPS_REGEX,
                timestamp_data_str,
                re.DOTALL
            ).groupdict()
            cue_contents = str_iter_arr_to_single_line(next(groupby_iter)[1])
            all_cue_blocks.append(
                CueBlock(
                    start_time_str=regex_matches.get('start'),
                    end_time_str=regex_matches.get('end'),
                    content=cue_contents,
                    index=next(cue_count)
                ).to_json()
            )

    return all_cue_blocks


if __name__ == '__main__':
    srt_path = sys.argv[1]
    if not srt_path:
        raise Exception('script needs srt path on system')
    srt_contents = open(os.path.expanduser(srt_path)).read()
    print(json.dumps(get_cue_blocks_from_srt_string(srt_contents)))

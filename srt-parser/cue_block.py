from utils import convert_str_time_to_timestamp_in_ms


class CueBlock:
    def __init__(
            self, index: int, start_time_str: str, end_time_str: str, content: str
    ) -> None:
        self.index = index
        self.start_time = convert_str_time_to_timestamp_in_ms(start_time_str)
        self.end_time = convert_str_time_to_timestamp_in_ms(end_time_str)
        self.content = content.strip()

    def to_json(self):
        return {
            "index": self.index,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "content": self.content,
        }

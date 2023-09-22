import re
from re import Match

# The Validator class checks whether the given line matches the pattern.
class Validator:
    @staticmethod
    def check_if_correct(line: str, pattern: str) -> Match[str] | None:
        return re.match(pattern, line)
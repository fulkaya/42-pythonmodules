from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output")

        rank, data_str = self._storage.pop(0)
        return (rank, data_str)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and data and all(isinstance(x, (int, float)) and not isinstance (x, bool) for x in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improrer numeric data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True
        if isinstance(data, list) and data and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, x))
                self._counter += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    def _is_valid_dict(self, d: Any) -> bool:
        return isinstance(d, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())

    def validate(self, data: Any) -> bool:
        if self._is_valid_dict(data):
            return True
        if isinstance(data, list) and data and all(self._is_valid_dict(x) for x in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improrer log data")

        def format_log(d: dict[str, str]) -> str:
            level = d.get("log_level", "UNKNOWN")
            msg = d.get("log_message", "")
            return f"{level}: {msg}"

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, format_log(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

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
        super().__init__()

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and data and all(
          isinstance(x, (int, float)) and not isinstance(x, bool) for x in data
        ):
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True
        if isinstance(data, list) and data and all(
            isinstance(x, str) for x in data
        ):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
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
        super().__init__()

    def _is_valid_dict(self, d: Any) -> bool:
        return isinstance(d, dict) and all(
            isinstance(k, str) and isinstance(v, str) for k, v in d.items())

    def validate(self, data: Any) -> bool:
        if self._is_valid_dict(data):
            return True
        if isinstance(data, list) and data and all(
            self._is_valid_dict(x) for x in data
        ):
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

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
    print()

    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'Hello': {num.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        invalid_str = "foo"
        num.ingest(invalid_str)
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    num.ingest([1, 2, 3, 4, 5])
    for i in range(3):
        print(f"Numeric value {i}: {num.output()[1]}")

    print()
    print("Testing Text Processor...")
    string = TextProcessor()
    print(f"Trying to validate input '42': {string.validate(42)}")
    str_list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {str_list}")
    print("Extracting 1 value...")
    string.ingest(str_list)
    print(f"Text value 0: {string.output()[1]}")

    print()
    print("Testing Log Processor...")
    print()
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    dictionary = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {dictionary}")
    print("Extracting 2 values...")
    log.ingest(dictionary)
    for i in range(2):
        print(f"Log entry {i}: {log.output()[1]}")


if __name__ == "__main__":
    main()

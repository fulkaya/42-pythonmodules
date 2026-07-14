from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0
        self.total_processed: int = 0

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
                self.total_processed += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1
            self.total_processed += 1


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_str = ",".join(item[1] for item in data)
        print("CSV Output:")
        print(csv_str)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts = []
        for rank, value in data:
            parts.append(f'"item_{rank}": "{value}"')
        json_str = "{" + ", ".join(parts) + "}"
        print("JSON Output:")
        print(json_str)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process "
                      f"element in stream: {element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            exported_data = []
            for _ in range(nb):
                try:
                    item = proc.output()
                    exported_data.append(item)
                except IndexError:
                    break
            if exported_data:
                plugin.process_output(exported_data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc.total_processed
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()

    stream = DataStream()
    stream.print_processors_stats()

    print()
    print("Registering Processors")

    print()
    first_batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print(
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'\nlog_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is"
        "\nconnected'}], 42, ['Hi', 'five']]"
    )
    stream.process_stream(first_batch)
    print()
    stream.print_processors_stats()

    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    print()
    stream.print_processors_stats()

    second_batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate\nexpires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print()
    print(
        "Send another batch of data: [21, ['I love AI', "
        "'LLMs are wonderful', 'Stay healthy'], "
        "[{'log_level': '\nERROR', 'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE', 'log_message': 'Certificate\n"
        "expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']"
    )
    stream.process_stream(second_batch)
    print()
    stream.print_processors_stats()

    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)

    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

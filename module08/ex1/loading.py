from importlib.metadata import version
import sys

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    HAS_DEPENDENCIES = True
except ImportError as e:
    HAS_DEPENDENCIES = False
    missing_module = str(e)


def check_dependencies() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    print(f"[OK] numpy ({version('numpy')}) - Numerical computation ready")
    print(f"[OK] matplotlib ({version('matplotlib')}) - Visualization ready")
    print()


def generate_and_analyze_data() -> None:
    print("Analyzing Matrix data...")
    data_points = 1000
    print(f"Processing {data_points} data points...")

    np.random.seed(42)
    matrix_signal = np.random.normal(loc=0, scale=1, size=data_points)
    cumulative_density = np.cumsum(matrix_signal)

    df = pd.DataFrame(
        {"Signal": matrix_signal, "Matrix_Density": cumulative_density}
    )

    print("Generating visualization...")
    print()

    plt.figure(figsize=(10, 5))
    plt.plot(
        df["Matrix_Density"],
        color="#00FF00",
        linewidth=1.5,
        label="Matrix Data Stream",
    )
    plt.title("Matrix System Density Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Density Level")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    output_filename = "matrix_analysis.png"
    plt.savefig(output_filename)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")


def main() -> None:
    if not HAS_DEPENDENCIES:
        print("LOADING STATUS: Loading programs...")
        print("Checking dependencies:")
        print("[ERROR] Missing required packages!")
        print()
        print("To install dependencies using pip:")
        print("  pip install -r requirements.txt", end="\n\n")
        print("or", end="\n\n")
        print("To install dependencies using Poetry:")
        print("  poetry install")
        sys.exit(1)

    check_dependencies()
    generate_and_analyze_data()


if __name__ == "__main__":
    main()

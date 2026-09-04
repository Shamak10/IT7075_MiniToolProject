import platform
import subprocess

import torch


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout
    except FileNotFoundError:
        return f"command not found: {cmd[0]}"


def main():
    print("=== platform ===")
    print(platform.platform())
    print(platform.processor())

    print("\n=== system_profiler: hardware ===")
    print(run(["system_profiler", "SPHardwareDataType"]))

    print("=== system_profiler: displays/GPU ===")
    print(run(["system_profiler", "SPDisplaysDataType"]))

    print("=== torch framework query ===")
    print(f"torch version: {torch.__version__}")
    print(f"cuda available: {torch.cuda.is_available()}")
    print(f"mps (Apple Silicon GPU) available: {torch.backends.mps.is_available()}")


if __name__ == "__main__":
    main()

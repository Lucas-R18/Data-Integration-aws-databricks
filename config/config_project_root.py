import subprocess
from pathlib import Path

PROJECT_ROOT = str(Path(__file__).resolve().parents[1])

subprocess.run([
    "setx",
    "PROJECT_ROOT",
    f"{PROJECT_ROOT}"
])

print(PROJECT_ROOT)
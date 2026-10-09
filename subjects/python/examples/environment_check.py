"""Report interpreter details without reading credentials."""
import json
import platform
import sys
from pathlib import Path

def describe_environment():
    return {"python_version": platform.python_version(),
            "executable": sys.executable,
            "virtual_environment": sys.prefix != sys.base_prefix,
            "working_directory": str(Path.cwd())}

if __name__ == "__main__":
    print(json.dumps(describe_environment(), indent=2))

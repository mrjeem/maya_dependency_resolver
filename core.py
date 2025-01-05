import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    prog="Maya Dependency Resolver",
    description="Resolves dependent maya files in the given maya file.",
)

parser.add_argument("filepath")
args = parser.parse_args()

file_path = args.filepath

file_path: Path = Path(file_path)

for dir_path, dir_names, file_names in file_path.walk():
    for each_file_name in file_names:
        if each_file_name.endswith(".ma"):
            each_file_path = dir_path / each_file_name

            with open(each_file_path, "r") as f:
                content: list[str] = f.readlines()

            print(f"Traversing {each_file_path}...")
            for each_line in content:
                if "file -r -ns" in each_line:
                    print(each_line)

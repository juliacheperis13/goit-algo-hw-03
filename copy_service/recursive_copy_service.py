import argparse
from pathlib import Path
import shutil
import os

default_output_directory = "dist"


class RecursiveCopyService:
    def init(self):
        print('Welcome to copy service!')

    def parse_argv(self, output_directory=default_output_directory):
        parser = argparse.ArgumentParser(description="Copy files to folder and sort by subfolders by file extension.")
        parser.add_argument(
            "-s", "--source", type=Path, required=True, help="Source folder."
        )
        parser.add_argument(
            "-d", "--dist", type=Path, default=Path(output_directory), help="Destination folder."
        )
        return parser.parse_args()

    def file_copy(self, source: Path, output: Path):
        self.recursive_copy(source, output)
        print('File copying was completed.')

    def recursive_copy(self, source: Path, output: Path):
        for el in source.iterdir():
            if el.is_dir():
                self.recursive_copy(el, output)
            else:
                _, extension = os.path.splitext(el.name)
                folder = output / extension

                if not folder.is_dir():
                    folder.mkdir(exist_ok=True, parents=True)
                    print(f'Folder "{folder}" created.')

                shutil.copy(el, folder)
                print(f'File "{el.name}" was copied to "{folder}"')

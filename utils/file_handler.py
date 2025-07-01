import os
import shutil
from pathlib import Path
import logging

log_file = 'logs/autosort.log'
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.INFO)

def sort_by_extension(source, destination):
    source = Path(source)
    destination = Path(destination)

    if not source.exists():
        print("Source path does not exist.")
        return

    for file in source.iterdir():
        if file.is_file():
            ext = file.suffix[1:] or 'no_ext'
            dest_folder = destination / ext
            dest_folder.mkdir(parents=True, exist_ok=True)

            new_path = dest_folder / file.name
            shutil.move(str(file), str(new_path))

            msg = f"Moved {file.name} to {dest_folder}"
            print(msg)
            logging.info(msg)

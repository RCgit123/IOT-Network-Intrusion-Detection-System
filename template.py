import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ='NidsDetection'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}"
]
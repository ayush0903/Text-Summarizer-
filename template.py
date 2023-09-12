#this is to design the files and the basic structure of the project

import os
from pathlib import Path
import logging #for taking log during runtime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",#for deployment  keep file is just to not make it empty
    f"src/{project_name}/__init__.py",#f string, init is contructor file  to consider the file in local pacakage
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",#keep all modulated paramater 
    "app.py",
    "main.py",
    "Dockerfile", 
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)#detect the OS
    filedir, filename = os.path.split(filepath)  

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)#exist_ok is for if you have dont create it or else create it 
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#size should be zero and not present the create it 
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
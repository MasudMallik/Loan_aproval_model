import os
from pathlib import Path

files=[
    "frontend/main.py",
    "frontend/pages/login_reg.py",
    "frontend/pages/home_page.py",
    "frontend/requirements.txt",
    "backend/main.py",
    "backend/data_ingestion.py",
    "backend/data_preprocess.py",
    "backend/model_train.py",
    "backend/requirements.txt",
    "dockerfile",
    "logger.py",
    "dvc.yaml",
]

for file in files:
    path=Path(file)

    file_dir,file_path=os.path.split(path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        print(f"{file_dir} created succesfully")
    if not os.path.exists(path) or os.path.getsize(path)==0:
        with open(path,"w") as f:
            print(f"{file_path} created succesfully")
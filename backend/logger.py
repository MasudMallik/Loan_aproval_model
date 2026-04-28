import os
import logging
from datetime import datetime

dir=os.getcwd()
file_dir=os.path.join(dir,"logs")
os.makedirs(file_dir,exist_ok=True)

file_path=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file=os.path.join(file_dir,file_path)
logging.basicConfig(
    filename=file,
    format="%(asctime)s- %(levelname)s -%(message)s",
    level=logging.INFO,
)

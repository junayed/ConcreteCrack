import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from ConcreteCrack.entity import DataIngestionConfig
from ConcreteCrack import logger 
from ConcreteCrack.utlis import get_size


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
            logger.info("Trying to download file...")
            if not os.path.exists(self.config.local_data_file):
                logger.info("Download started...")
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")   

    def _get_updated_list_of_files(self, list_of_files):
        filtered_files = [
            f for f in list_of_files 
            if f.lower().endswith(('.jpg', '.jpeg', '.png')) and 
            ("background" in f.lower() or "defects" in f.lower())
        ]
        # print("Filtered files:", filtered_files)  # Debugging statement
        return filtered_files

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info(f"unzipping file and removing unawanted files")
        if not os.path.exists(self.config.local_data_file):
            print(f"File {self.config.local_data_file} does not exist.")
            return
        
        with ZipFile(self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            # print("List of files in the zip:", list_of_files)  # Debugging statement
            
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            
            if not updated_list_of_files:
                print("No files matched the criteria.")
            
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)




from src.utils import save_json
import time
from src import logging
from src.constants import *
from src.components import DataIngestionPrepration


STAGE = "Data ingestion and prepration" ## <<< change stage name 

# init logger
#logger()

def main():
    data_ing_prep_obj = DataIngestionPrepration()
    data_ing_prep_obj.load_data()
    data_ing_prep_obj.shuffle_and_batch()
    data_ing_prep_obj.encode_on_trainning_data()



if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
# import module
import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging
from src.utils import save_bin

class DataIngestionPrepration:
    
    def __init__(self):
        self.dataset_name = "imdb_reviews"

    def load_data(self):
        dataset, info = tfds.load(
                                   name=self.dataset_name,
                                   with_info=True,
                                   as_supervised=True)
        self.train_ds, self.test_ds = dataset["train"], dataset["test"]
        logging.info(f"{self.dataset_name}, dataset downloaded with info: \n{info}")


    def shuffle_and_batch(self):
        self.train_ds=self.train_ds.shuffle(TRAINING_BUFFER_SIZE).batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        self.test_ds=self.test_ds.batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        logging.info(f"Datasets are now batched and shuffled!")

    
    def encode_on_trainning_data(self):
        encoder = tf.keras.layers.TextVectorization(max_tokens=TRAINING_VOCAB_SIZE)
        encoder.adapt(self.train_ds.map(lambda text, label:text))
        logging.info(f"Encoding on training ds is done!")

    def save_encoder(self):
        pass

    def save_train_test_ds(self):
        pass





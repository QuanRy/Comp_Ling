from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2VecModel
from pyspark.sql import DataFrame
import string

def spark(text):

    MODEL_PATH = "spark_app/model"

    spark = SparkSession \
        .builder \
        .appName("word2vec") \
        .getOrCreate()

    model = Word2VecModel.load(MODEL_PATH)

    try:
        mass = []
        word = text
        massSyn = model.findSynonymsArray(word, 10)
        for item in massSyn:
            mass.append(item[0].translate(str.maketrans('','', string.punctuation)))
        return mass
    except Exception as ex:
        return 'notExist'

    spark.stop()


# spark("волга")
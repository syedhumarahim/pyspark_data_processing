import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

LOG_FILE = "summary.md"

def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")

def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(
    url='https://raw.githubusercontent.com/'
        'syedhumarahim/syedhumarahim-dataset_medical_records/main/'
        'heart_attack_prediction_dataset.csv',
    file_path="data/heart_attack_prediction_dataset.csv",
    directory="data"
):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if url:
        r = requests.get(url)
        r.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

def load_data(spark, data="data/heart_attack_prediction_dataset.csv", name="HeartData"):
    """Load medical data and infer schema."""
    # Use Spark to infer schema and load CSV
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(data)
    # Log first 10 rows
    log_output("load data", df.limit(10).toPandas().to_markdown())
    return df

def query(spark, df, query, name): 
    """Run a SQL query on the dataframe"""
    df.createOrReplaceTempView(name)
    result = spark.sql(query)
    log_output("query data", result.limit(10).toPandas().to_markdown(), query)
    return result.show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)
    return df.describe().show()

def example_transform(df):
    """
    Example transformation:
    Create a new column 'RiskCategory' based on 'Heart Attack Risk' column.
    If Heart Attack Risk == 1 => 'High Risk'
    Else => 'Low Risk'
    """
    df = df.withColumn("RiskCategory", when(col("Heart Attack Risk") == 1, "High Risk").otherwise("Low Risk"))
    log_output("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()



import pandas as pd
from pyspark.sql import SparkSession

def process_with_pandas():
    """
    Processes the downloaded CSV file using Pandas to clean and transform the data.
    
    Returns:
        None
    Raises:
        FileNotFoundError: If the input CSV file is not found.
    """
    # Load the CSV file into a Pandas DataFrame
    try:
        df = pd.read_csv("/tmp/remote_data.csv")
    except FileNotFoundError as e:
        print(f"Input CSV file not found: {e}")
        raise
    
    # Example cleaning: Remove rows with missing values
    df = df.dropna()
    
    # Save the processed data to a temporary CSV file
    df.to_csv("/tmp/pandas_processed.csv", index=False)
    print("Pandas processing completed. Saved to /tmp/pandas_processed.csv")

def process_with_spark():
    """
    Processes the Pandas-processed CSV file using Spark for distributed computation.
    
    Returns:
        None
    Raises:
        Exception: If Spark processing fails.
    """
    # Initialize a Spark session
    spark = SparkSession.builder.appName("SparkProcessing").getOrCreate()
    
    # Load the Pandas-processed CSV file into a Spark DataFrame
    try:
        df = spark.read.csv("/tmp/pandas_processed.csv", header=True, inferSchema=True)
    except Exception as e:
        print(f"Failed to load CSV into Spark: {e}")
        spark.stop()
        raise
    
    # Example processing: Filter rows where a column value is greater than 100
    # Replace "column_name" with an actual column from your CSV
    df_filtered = df.filter(df["column_name"] > 100)
    
    # Save the filtered data to a new CSV file
    df_filtered.write.mode("overwrite").csv("/tmp/spark_processed.csv")
    spark.stop()
    print("Spark processing completed. Saved to /tmp/spark_processed.csv")

def process_with_pandas_and_spark():
    """
    Orchestrates the processing of the CSV file using both Pandas and Spark.
    
    Returns:
        None
    """
    process_with_pandas()
    process_with_spark()

if __name__ == "__main__":
    process_with_pandas_and_spark()
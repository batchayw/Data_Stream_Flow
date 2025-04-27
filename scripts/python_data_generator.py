import pandas as pd
import json

def python_data_generator():
    """
    Generates new data based on the Spark-processed CSV file and saves it as JSON.
    
    Returns:
        None
    Raises:
        FileNotFoundError: If the input CSV file is not found.
    """
    # Load the Spark-processed CSV file
    try:
        df = pd.read_csv("/tmp/spark_processed.csv")
    except FileNotFoundError as e:
        print(f"Input CSV file not found: {e}")
        raise
    
    # Generate new data by adding a new column
    generated_data = []
    for _, row in df.iterrows():
        data = {
            "original_column": row["column_name"],  # Replace with actual column
            "generated_value": row["column_name"] + "_generated"
        }
        generated_data.append(data)
    
    # Save the generated data as JSON
    with open("/tmp/generated_data.json", "w") as f:
        json.dump(generated_data, f)
    print("Data generation completed. Saved to /tmp/generated_data.json")

if __name__ == "__main__":
    python_data_generator()
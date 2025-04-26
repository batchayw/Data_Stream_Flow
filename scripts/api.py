from flask import Flask, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

@app.route('/trigger-pipeline', methods=['POST'])
def trigger_pipeline():
    """
    Endpoint to manually trigger the Airflow data pipeline.

    This endpoint executes the Airflow DAG 'data_pipeline_dag' by running a command
    in the Airflow container. It is designed to allow external systems to initiate
    the pipeline on demand.

    Returns:
        JSON response with the status of the trigger operation.
        - 200: Pipeline triggered successfully.
        - 500: Failed to trigger the pipeline, with an error message.
    """
    try:
        # Execute the Airflow command to trigger the DAG
        # This assumes the Airflow container is named 'airflow' (as defined in docker-compose.yml)
        result = os.system("docker exec airflow airflow dags trigger -r manual-run data_pipeline_dag")
        
        # Check if the command executed successfully (os.system returns 0 on success)
        if result != 0:
            raise RuntimeError("Airflow command failed with exit code: {}".format(result))
        
        # Return a success response
        return jsonify({
            "status": "success",
            "message": "Pipeline triggered successfully."
        }), 200
    
    except Exception as e:
        # Return an error response if the trigger fails
        return jsonify({
            "status": "error",
            "message": f"Failed to trigger pipeline: {str(e)}"
        }), 500

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 and port 5000
    # This makes the API accessible externally (e.g., from the host machine or other containers)
    app.run(host='0.0.0.0', port=5000)
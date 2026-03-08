import subprocess
import os

def run_command(cmd):
    print(f"\nRunning: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():

    print("Starting OpenBank Lakehouse Pipeline")

    # Start docker environment
    run_command("docker compose up -d")

    # Run bronze ingestion
    run_command("docker exec -it openbank_spark python3 ingest_bronze.py")

    # Run silver transformation
    run_command("docker exec -it openbank_spark python3 transform_silver.py")

    # Run dbt models
    os.chdir("dbt/openbank_dv")
    run_command("dbt run")

    print("\nPipeline execution completed!")

if __name__ == "__main__":
    main()
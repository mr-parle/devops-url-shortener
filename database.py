import os
import time
import psycopg2


def get_connection(retries=5, delay=2):

    for attempt in range(retries):
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
            )

            print("Database connection successful")

            return connection

        except psycopg2.OperationalError as error:
            print(
                f"Database connection failed: {error}"
            )

            if attempt < retries - 1:
                print(
                    f"Retrying in {delay} seconds..."
                )

                time.sleep(delay)

    raise Exception(
        "Could not connect to PostgreSQL after multiple attempts"
    )
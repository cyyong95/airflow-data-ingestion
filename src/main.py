import pandas as pd
import constants
import threading
from sqlalchemy import create_engine


def main():

    df = pd.read_parquet(constants.DATASET_PARQUET)
    retries = 0
    max_retries = 5
    event = threading.Event()
    while True:
        if retries > max_retries:
            print("Max retries exceeded")
            break

        try:
            engine = create_engine(
                f"postgresql://{constants.POSTGRES_USER}:{constants.POSTGRES_PASSWORD}@"
                f"{constants.DATABASE_CONTAINER_NAME}:{constants.CONTAINER_PORT}/{constants.POSTGRES_DB}")

            df.head(100).to_sql(constants.POSTGRES_TABLE_NAME, engine, method="multi", if_exists="replace")
            break
        except Exception as err:
            print(f"Error: {err}")
            retries += 1
            event.wait(5)


if __name__ == '__main__':
    main()

import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def get_param_value(parameter: str) -> str:
    engine = create_engine(f'postgresql+psycopg2://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@192.168.86.192:5433/postgres')
    statement = f'select * from jdp.params where parameter={parameter}'
    result = engine.execute(statement)

    return result.first()["value"]


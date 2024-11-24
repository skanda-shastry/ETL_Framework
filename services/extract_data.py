import pandas as pd
import pymongo
import boto3
from sqlalchemy import create_engine
from app.config import Config

def extract_from_csv(file_path: str):
    return pd.read_csv(file_path)

def extract_from_postgres(query: str):
    engine = create_engine(Config.POSTGRES_URI)
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

def extract_from_mongodb(collection_name: str, db_name: str):
    client = pymongo.MongoClient(Config.MONGO_URI)
    db = client[db_name]
    collection = db[collection_name]
    return pd.DataFrame(list(collection.find()))

def extract_from_s3(file_name: str):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=Config.AWS_S3_BUCKET, Key=file_name)
    return pd.read_csv(obj['Body'])

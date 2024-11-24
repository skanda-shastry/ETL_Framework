def load_to_postgres(df, table_name: str):
    engine = create_engine(Config.POSTGRES_URI)
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)

def load_to_mongodb(df, collection_name: str, db_name: str):
    client = pymongo.MongoClient(Config.MONGO_URI)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(df.to_dict(orient='records'))

def load_to_s3(df, file_name: str):
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=Config.AWS_S3_BUCKET,
        Key=file_name,
        Body=df.to_csv(index=False),
    )

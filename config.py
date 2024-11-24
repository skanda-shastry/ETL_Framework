import os

class Config:
    # Datasource Configurations
    POSTGRES_URI = os.getenv("POSTGRES_URI", "postgresql://user:password@localhost:5432/mydb")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "my-bucket")

from fastapi import APIRouter, UploadFile, File, Query
from app.services.extract_data import extract_from_csv, extract_from_postgres
from app.services.transformation_data import clean_column_names
from app.services.load_data import load_to_postgres

router = APIRouter()

@router.post("/etl/csv-to-postgres/")
async def csv_to_postgres(file: UploadFile = File(...), table_name: str = Query(...)):
    # Extract
    data = extract_from_csv(file.file)
    
    # Transform
    data = clean_column_names(data)
    
    # Load
    load_to_postgres(data, table_name)
    return {"message": f"Data loaded into {table_name} successfully!"}

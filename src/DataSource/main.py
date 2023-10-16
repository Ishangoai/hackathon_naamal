import pandas as pd
from decouple import config
from sqlalchemy import create_engine
from cleaning_utils import column_name_mapping, data_types

sheet_id = config("SPREADSHEET_ID")
db_url = config('DATABASE_URL')

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


df.rename(columns=column_name_mapping, inplace=True)



engine = create_engine(db_url, echo=True)
df.to_sql('alumni', con=engine, if_exists='replace', index=False, dtype=data_types)

engine.dispose()
import pandas as pd
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cleaning_utils import column_name_mapping, data_types
from create_db import Alumni

sheet_id = config("SPREADSHEET_ID")
db_url = config('DATABASE_URL')

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


df.rename(columns=column_name_mapping, inplace=True)



engine = create_engine(db_url, echo=True)


Session = sessionmaker(bind=engine)
session = Session()


for index, row in df.iterrows():
    alumni_record = Alumni(**row.to_dict())
    session.merge(alumni_record)


session.commit()
session.close()

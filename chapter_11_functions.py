from scipy.stats import linregress
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import pandas as pd


def process_sdg_data(input_excel_file, columns_to_drop):
    df = pd.read_excel(input_excel_file)
    df = df.drop(columns_to_drop, axis=1)
    df = df.set_index("GeoAreaName").transpose()
    return df
    

def fit_trendline(year_timestamps, data):
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    return slope, r_squared


def country_trendline(country_name):
    df = process_sdg_data("data/SG_GEN_PARL.xlsx", 
                          ["Goal", "Target", "Indicator", "SeriesCode", "SeriesDescription", "GeoAreaCode", "Reporting Type", "Sex", "Units"])
    timestamps = [int(i) for i in df.index.tolist()]
    country_data = df[country_name].tolist()
    slope, r_squared = fit_trendline(timestamps, country_data)
    return slope, r_squared


app = FastAPI()


@app.get("/country_trendline/{country}")
def calculate_country_trendline(country: str):
    slope, r_squared = country_trendline(country)
    return {"slope": slope, "r_squared": r_squared}


class TrendlineInput(BaseModel):
    timestamps: List[int]
    data: List[float]


# @app.post("/fit_trendline/")
@app.post("/fit_trendline/", 
          summary="Fit a trendline to any data",
          description="Provide a list of integer timestamps and a list of floats")
def calculate_trendline(trendline_input: TrendlineInput):
    slope, r_squared = fit_trendline(trendline_input.timestamps,
                                     trendline_input.data)
    return {"slope": slope, "r_squared": r_squared}

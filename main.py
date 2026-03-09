from fastapi import FastAPI
from data_collection import search_sector_news
from ai_analysis import analyze_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sector AI API running"}

@app.get("/analyze/{sector}")
def analyze_sector(sector: str):

    news = search_sector_news(sector)

    report = analyze_data(news, sector)

    return {
        "sector": sector,
        "analysis": report
    }
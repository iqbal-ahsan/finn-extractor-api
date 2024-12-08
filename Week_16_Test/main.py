import requests
import uvicorn
from bs4 import BeautifulSoup
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["finn_data"] 
collection = db["items"]


class Finn(BaseModel):
    finn_code: str

@app.post("/extract/")
def data(request : Finn):
    finn_code = request.finn_code

    url  = f'https://www.finn.no/mobility/item/{finn_code}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Modellår = soup.find("s-text-subtle", text="Modellår".find_next)
    modellår = soup.find(text='Modellår').find_next().text
    kilometer = soup.find(text='Kilometer').find_next().text
    girkasse = soup.find(text='Girkasse').find_next().text
    drivstoff = soup.find(text='Drivstoff').find_next().text

    scrap_data = {
        "Modellår": modellår,
        "Kilometer": kilometer,
        "Girkasse": girkasse,
        "Drivstoff": drivstoff,
        "finn_code": finn_code
    }
    return scrap_data


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8000)

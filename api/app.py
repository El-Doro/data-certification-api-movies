from fastapi import FastAPI
from api.predict import get_predict

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# Implement a /predict endpoint
@app.get("/predict")
def predict(
    original_title,
    title,
    release_date,
    duration_min,
    description,
    budget,
    original_language,
    status,
    number_of_awards_won,
    number_of_nominations,
    has_collection,
    all_genres,
    top_countries,
    number_of_top_productions,
    available_in_english,
):

    popularity = get_predict(
        original_title,
        title,
        release_date,
        duration_min,
        description,
        budget,
        original_language,
        status,
        number_of_awards_won,
        number_of_nominations,
        has_collection,
        all_genres,
        top_countries,
        number_of_top_productions,
        available_in_english,
    )

    answer = {"title": title, "popularity": popularity}

    return answer

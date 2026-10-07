from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from goals import router as goals_router
from saved import router as saved_router

app = FastAPI()

app.include_router(goals_router)


app.include_router(saved_router)
# Photos folder
photos_folder = Path("Photos")

# Make the photos accessible
app.mount(
    "/Photos",
    StaticFiles(directory=photos_folder),
    name="Photos"
)


@app.get("/")
def home():
    return {
        "message": "Motivation API is running"
    }


@app.get("/all-photos")
def get_all_photos():

    photos = []

    for file in photos_folder.iterdir():

        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:

            photos.append({
                "name": file.name,
                "url": f"/Photos/{file.name}"
            })

    return {
        "Photos": photos
    }

@app.get("/photos/{category}")
def get_category_photos(category: str):

    category_folder = photos_folder / category

    if not category_folder.exists():
        return {
            "error": "Category not found"
        }

    photos = []

    for file in category_folder.iterdir():

        if file.is_file() and file.suffix.lower() in [
            ".jpg", ".jpeg", ".png", ".webp"
        ]:

            photos.append({
                "name": file.name,
                "category": category,
                "url": f"/Photos/{category}/{file.name}"
            })

    return {
        "category": category,
        "photos": photos
    }


from fastapi import APIRouter, HTTPException

router = APIRouter()


# Temporary in-memory storage
saved_quotes = []
saved_posters = []


# =========================
# GET ALL SAVED ITEMS
# =========================

@router.get("/saved")
def get_saved():

    return {
        "quotes": saved_quotes,
        "posters": saved_posters
    }


# =========================
# SAVE MULTIPLE QUOTES
# =========================

@router.post("/saved/quotes")
def save_quotes(quotes: list[dict]):

    for quote in quotes:

        quote_id = quote.get("id")

        # Don't save duplicate quote
        if not any(item.get("id") == quote_id for item in saved_quotes):
            saved_quotes.append(quote)

    return {
        "message": "Quotes saved successfully",
        "quotes": saved_quotes
    }


# =========================
# SAVE MULTIPLE POSTERS
# =========================

@router.post("/saved/posters")
def save_posters(posters: list[dict]):

    for poster in posters:

        poster_id = poster.get("id")

        # Don't save duplicate poster
        if not any(item.get("id") == poster_id for item in saved_posters):
            saved_posters.append(poster)

    return {
        "message": "Posters saved successfully",
        "posters": saved_posters
    }


# =========================
# DELETE / UNSAVE QUOTE
# =========================

@router.delete("/saved/quotes/{quote_id}")
def delete_quote(quote_id: int):

    for quote in saved_quotes:

        if quote.get("id") == quote_id:

            saved_quotes.remove(quote)

            return {
                "message": "Quote removed successfully",
                "quote_id": quote_id
            }

    raise HTTPException(
        status_code=404,
        detail="Quote not found"
    )


# =========================
# DELETE / UNSAVE POSTER
# =========================

@router.delete("/saved/posters/{poster_id}")
def delete_poster(poster_id: int):

    for poster in saved_posters:

        if poster.get("id") == poster_id:

            saved_posters.remove(poster)

            return {
                "message": "Poster removed successfully",
                "poster_id": poster_id
            }

    raise HTTPException(
        status_code=404,
        detail="Poster not found"
    )
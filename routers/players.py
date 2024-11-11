# routers/players.py
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/api/{league}/{playerId}")
async def get_player_info(league: str, playerId: str):
    # Validate the league parameter
    if league not in {"nfl", "mlb", "nba"}:
        raise HTTPException(status_code=400, detail="Invalid league specified")

    # Dummy response - in a real app, you'd query a database or API here
    return {
        "league": league,
        "playerId": playerId,
        "info": f"Info about player {playerId} in the {league.upper()} league"
    }
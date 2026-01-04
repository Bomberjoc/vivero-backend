from fastapi import APIRouter
from app.core.supabase import supabase

router = APIRouter()

@router.get("/")
def get_plants():
    # Fetch plants with their related images and common names
    res = supabase.table("plants").select("*, plant_images(*), plant_common_names(*)").execute()
    return res.data

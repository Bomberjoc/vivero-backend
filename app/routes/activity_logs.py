from fastapi import APIRouter, HTTPException
from app.core.supabase import supabase
from app.schemas.activity_log import ActivityLogCreate

router = APIRouter()

@router.get("/")
def get_activity_logs():
    """
    Obtiene todos los logs de actividad ordenados por fecha descendente.
    Solo accesible por administradores (verificado por RLS en Supabase).
    """
    try:
        res = supabase.table("activity_logs").select("*").order("created_at", desc=True).execute()
        return res.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
def create_activity_log(log: ActivityLogCreate):
    """
    Crea un nuevo log de actividad.
    """
    try:
        log_data = log.model_dump()
        res = supabase.table("activity_logs").insert(log_data).execute()
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

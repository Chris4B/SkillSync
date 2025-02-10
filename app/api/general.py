from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API SkillSync 🚀"}

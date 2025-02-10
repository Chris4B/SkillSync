from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import general  # Import du module API

# Création de l'application FastAPI
app = FastAPI(title="SkillSync API", version="1.0")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(general.router)

# Lancement du serveur
def start():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()

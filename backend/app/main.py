from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from . import routes

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Controle de Entregas",
    description="API para controle de mercadorias",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(routes.router, prefix="/api", tags=["mercadorias"])

@app.get("/")
def root():
    return {"message": "Sistema de Controle de Entregas API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
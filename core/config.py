from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Hexagonal Microservicios"
    description: str = "Usuarios Microservicios"
    version: str = "1.0.0"

    # Puertos por defecto
    api_v1_port: int = 8000
    api_v2_port: int = 8001

    # Configuración de desarrollo
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
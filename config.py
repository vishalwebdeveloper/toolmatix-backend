from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DATABASE_HOST:str
    DATABASE_PORT:int
    DATABASE_USER:str
    DATABASE_PASSWORD:str
    DATABASE_NAME:str

    SSL_CA:str

    CLOUDINARY_CLOUD_NAME:str
    CLOUDINARY_API_KEY:str
    CLOUDINARY_API_SECRET:str

    class Config:
        env_file=".env"

settings=Settings()
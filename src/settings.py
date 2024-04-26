from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):

    # app
    debug: bool = False

    # env
    environment: str = "local"

    # supabase creds
    supabase_url: str
    supabase_secret_key: str

    # db

    db_connection_link: str

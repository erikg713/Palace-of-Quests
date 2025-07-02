import os
from supabase import create_client, Client
from config import Config

def get_supabase() -> Client:
    url = Config.SUPABASE_URL
    key = Config.SUPABASE_KEY
    if not url or not key:
        raise RuntimeError("Supabase credentials are not set in environment.")
    return create_client(url, key)

supabase = get_supabase()

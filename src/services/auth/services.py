from gotrue.types import (
    AuthResponse,
    SignInWithEmailAndPasswordCredentials,
    SignUpWithEmailAndPasswordCredentials,
)

from src.errors.services import RefreshTokensError, SignInError, SignUpError
from src.infrastructure.supabase import SupabaseClient
from src.interfaces.services.auth import ISignUpSignInService


class SignUpSignInService(ISignUpSignInService):
    def __init__(self, supabase_client: SupabaseClient):
        self._supabase_client = supabase_client

    async def sign_in(self, email: str, password: str) -> AuthResponse:
        try:
            async with self._supabase_client as supabase_client:
                return await supabase_client.client.auth.sign_in_with_password(
                    SignInWithEmailAndPasswordCredentials(
                        email=email,
                        password=password,
                    )
                )
        except Exception:
            raise SignInError()

    async def sign_up(self, email: str, password: str) -> AuthResponse:
        try:
            async with self._supabase_client as supabase_client:
                return await supabase_client.client.auth.sign_up(
                    SignUpWithEmailAndPasswordCredentials(
                        email=email,
                        password=password,
                    )
                )
        except Exception:
            raise SignUpError()

    async def refresh_tokens(self, token: str) -> AuthResponse:
        try:
            async with self._supabase_client as supabase_client:
                return await supabase_client.client.auth.refresh_session(
                    refresh_token=token
                )
        except Exception:
            raise RefreshTokensError()

from typing import Optional, Type

from supabase_py_async import create_client
from supabase_py_async.client_async import AsyncClient
from supabase_py_async.lib.client_options import ClientOptions


class SupabaseClient:
    def __init__(self, url: str, key: str) -> None:
        self._url = url
        self._key = key

        self.client: AsyncClient | None = None

    async def __aenter__(self) -> "SupabaseClient":
        self.client = await create_client(
            self._url,
            self._key,
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
            ),
        )
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_val: Optional[Exception],
        traceback,
    ):
        if self.client:
            self._client = None

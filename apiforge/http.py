import httpx
from .retry import retry


class AsyncHTTPClient:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout
        )

    async def request(self, method: str, url: str, **kwargs):
        async def call():
            r = await self._client.request(method, url, **kwargs)
            r.raise_for_status()
            return r.json()

        return await retry(call)

    async def close(self):
        await self._client.aclose()

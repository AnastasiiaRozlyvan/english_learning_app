import aiohttp
from config import FASTAPI_APP_HOST


class FastAPIClient:
    def __init__(self):
        self.host = FASTAPI_APP_HOST

    async def get(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.host}/{endpoint}/") as resp:
                response = await resp.json(content_type=None)
                return response

    async def post(self, endpoint, json):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f"{self.host}/{endpoint}/", json=json
            ) as resp:
                response = await resp.json(content_type=None)
                return response

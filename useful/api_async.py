import asyncio
import aiohttp
import json

from text_api_config import apikey
# more examples
#https://testdriven.io/blog/flask-async/
# example
async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)
    async def sem_task(task):
        async with semaphore:
            return await task

async def main():
    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)
    urls = [summarize_url, ner_url, mcp_url]
    conc_req = 3
    summary, ner, mcp = await gather_with_concurrency(conc_req, *[post_async(url, session, headers, body) for url in urls])
    await session.close()
    print(summary["summary"])
    print(ner["ner"])
    print(mcp["most common phrases"])
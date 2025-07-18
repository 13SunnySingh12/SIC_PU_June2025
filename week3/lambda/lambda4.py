import asyncio

async def fetch_data(url):
    print(f"Fetching data from {url}...")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    process_data = lambda result: print(f"Processed: {result.upper()}")
    result = await fetch_data("https://example.com")
    process_data(result)

asyncio.run(main())

import asyncio
import pprint

from ai_extractor import extract
from schemas import news_schema
from scrape import ascrape_playwright

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    # News sites mostly have <span> tags to scrape
    bbc_url = "https://www.bbc.com/"

    async def scrape_with_playwright(url: str, tags, **kwargs):
        html_content = await ascrape_playwright(url, tags)

        print("Extracting content with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content =  extract(**kwargs,content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_playwright(
        url=bbc_url,
        tags=["a"],
        schema=news_schema
    ))

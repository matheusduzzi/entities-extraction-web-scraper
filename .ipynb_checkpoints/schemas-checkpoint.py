from typing import List, Optional

from pydantic import BaseModel
    
news_schema = {
    "properties": {
        "news_full_article_url": {"type": "string"},
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
        "news_article_extra_info": {"type": "string"},
    },
    "required": ["news_full_article_url","news_article_title", "news_article_summary","news_article_extra_info"],
}


from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "api_key": "gsk_rV**************    ",
        "model": "groq/llama-3.1-8b-instant",
    },
    "verbose": True,
    "headless": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="Extract purpose of this website: https://qaul.ai/",
    source="https://qaul.ai/",
    config=graph_config
)

result = smart_scraper_graph.run()

print(result)
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
from browser_use import BrowserConfig
from browser_use import Browser
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    
    config = BrowserConfig(
     browser_binary_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )

    browser = Browser(config=config)
    agent = Agent(
        browser=browser,
        task="Send mail to xxxx, write Hi from smit",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
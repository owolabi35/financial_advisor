

from agno.agent import Agent
from agno.models.groq import Groq
#from agno.model.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
#from agno.tools.duckduckgo import DuckDuckGo
from agno.tools.duckduckgo import DuckDuckGoTools
import os


from dotenv import load_dotenv


financial_agent=Agent(
    name="Financial Analyst",
    model=Groq(id="DeepSeek-R1-Distill-Llama-70b"),
    #model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
        )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always create tables for comparisons"],
)


web_researcher=Agent(
    name="Web Researcher",
    model=Groq(id="DeepSeek-R1-Distill-Llama-70b"),
    #model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources of the information that you gather"],
)


agents_team=Agent(
    team=[financial_agent, web_researcher],
    model=Groq(id="DeepSeek-R1-Distill-Llama-70b"),
   # model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include source of the information gathered", "Always create tables for comparisons"],
    debug_mode=True
)

agents_team.print_response("Summarise the analyst recommendations and share the latest information about Nvidia?")
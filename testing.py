from agno.agent import Agent
from agno.models.groq import Groq
#from agno.model.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

def get_company_symbol(company: str) -> str:
    """
    Use this function to get the symbol for a company
    Args:
        company (str): The name of the company
    Returns:
        str: The symbol for the company
    """
    symbols={
        "AIwithHassan": "AAPL",
        "Tesla": "TSLA",
        "Google": "GOOGL"
    }
    return symbols.get(company, "Unknown")



test_agent=Agent(
    model=Groq(id="DeepSeek-R1-Distill-Llama-70b"),
    #model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
        ), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always take the symbols from the get_company_symbol tool and only use that symbol for further analysis, if the symbol doesnot exist, abort",
                  "Always create tables for comparisons"],
    debug_mode=True
)

test_agent.print_response("Summarise and compare the analyst recommendations for the stocks of AIwithHassan and Tesla")
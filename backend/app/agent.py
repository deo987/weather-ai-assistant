import os

from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from app.weather_tool import get_weather


llm = ChatOpenAI(
   model="meta-llama/llama-3-8b-instruct",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

weather_tool = Tool(
    name="Weather Tool",
    func=get_weather,
    description="Use this tool to get weather of a city"
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(query: str):
    return agent.run(query)

import asyncio
from config import config
from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool

# enable_verbose_stdout_logging()

@function_tool
async def get_weather(location: str) -> str:
    """Get weather from given location."""
    return f"Weather of {location} is sunny."

weather_agent : Agent = Agent(
    name="Weather_Agent",
    instructions="You are a weather agent. Always use tools.",
    tool_use_behavior={"stop_at_tool_names": ["get-weather"]},
    tools=[get_weather]
)

async def main():    
    result = await Runner.run(weather_agent, "Tell me today's weather of karachi?", run_config=config)
    
    print("="*70)
    
    print(result.final_output)

asyncio.run(main())    
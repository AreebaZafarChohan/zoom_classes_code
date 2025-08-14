import asyncio
from config import config
from agents import Agent, Runner, enable_verbose_stdout_logging
from pydantic import BaseModel
from dataclasses import dataclass

enable_verbose_stdout_logging()

class WeatherAnswer(BaseModel):
    location: str
    temperature_c: float
    summary: str

weather_agent : Agent = Agent(
    name="Structured_Weather_Agent",
    instructions="Use the final_output tool with WeatherAnswer schema.",
    output_type=WeatherAnswer
)

basic_agent : Agent = Agent(
    name="Simple_Agent",
    instructions="You are a helpfull asssistant.",
)

async def main():
    result1 = await Runner.run(weather_agent, "Tell me karachi's temperature?.", run_config=config)
    
    result2 = await Runner.run(basic_agent, "Hello?", run_config=config)
    
    print(result1.final_output)
    print(result1.final_output.temperature_c)
    print(type(result1.final_output))
    
    print("="*70)
    
    print(result2.final_output)
    print(type(result2.final_output))

asyncio.run(main())    
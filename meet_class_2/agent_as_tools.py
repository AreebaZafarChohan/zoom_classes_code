import asyncio
from agents import Agent, Runner, enable_verbose_stdout_logging 
from config import config, model

# enable_verbose_stdout_logging()

# Agents as tool

spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate the user's message to Spanish",
    handoff_description="An english to spanish translator",
    model=model,
)

french_agent = Agent(
    name="french_agent",
    instructions="You translate the user's message to French",
    handoff_description="An english to french translator",
    model=model,
)

italian_agent = Agent(
    name="italian_agent",
    instructions="You translate the user's message to Italian",
    handoff_description="An english to italian translator",
    model=model,
)

pathan_agent = Agent(
    name="pathan_agent",
    instructions="You translate the user's message to pathani language of pakistan",
    handoff_description="An english to pathani translator",
    model=model,
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools in order."
        "You never translate on your own, you always use the provided tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message into spanish.",
        ),
        
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message into italian."
        ),
        
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message into french."
        ),
        
        pathan_agent.as_tool(
            tool_name="translate_to_pathani",
            tool_description="Translate the user's message into pathani."
        ),
    ],
    model=model,
)
    
async def main():
    print("="*70)
    msg = input("Hi! What would you like translated, and to which languages? \nYou: ")
    
    orchestrator_result = await Runner.run(orchestrator_agent, input=msg, run_config=config)
    print(f"\n\nFinal response:\n{orchestrator_result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
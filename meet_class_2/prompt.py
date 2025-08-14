from agents import Agent, Prompt, Runner, enable_verbose_stdout_logging
from config import config        

enable_verbose_stdout_logging()

my_prompt = Prompt(
    id="travel_prompt",
    system_prompt="You are a travel agent.",
)  # type: ignore

agent: Agent = Agent(
    name="Math Agent",  
    prompt=my_prompt,
    instructions=""
)

result = Runner.run_sync(agent, "Tell me the best tourist spots of paris in list and short.", run_config=config)
print("\n🤖 CALLING AGENT\n")
print(result.final_output)
   
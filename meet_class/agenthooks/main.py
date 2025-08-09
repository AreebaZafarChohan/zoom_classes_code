from typing import Any
from agents import Agent, AgentHooks, CodeInterpreterTool, ComputerTool, FileSearchTool, FunctionTool, HostedMCPTool, ImageGenerationTool, LocalShellTool, RunContextWrapper, RunHooks, Runner, WebSearchTool, function_tool, enable_verbose_stdout_logging
import rich
from config import config

# enable_verbose_stdout_logging()

class MyCustomHooksAgent(AgentHooks):
    def __init__(self) -> None:
        super().__init__()
        
    async def on_start(self, context: RunContextWrapper[Any], agent: Agent[Any]) -> None:
        print(f"👀 Agent is starting... {agent.name}")
        return await super().on_start(context, agent)
    
    async def on_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any) -> None:
        print(f"👀 Agent is ending... {agent.name}")
        return await super().on_end(context, agent, output)
    
    async def on_handoff(self, context: RunContextWrapper[Any], agent: Agent[Any], source: Agent[Any]) -> None:
        print(f"Handsoff from {source.name} to {agent.name}")
        return await super().on_handoff(context, agent, source)
    
    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: FunctionTool | FileSearchTool | WebSearchTool | ComputerTool | HostedMCPTool | LocalShellTool | ImageGenerationTool | CodeInterpreterTool) -> None:
        print(f"Tool is calling... {tool.name}")
        return await super().on_tool_start(context, agent, tool)
    
    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: FunctionTool | FileSearchTool | WebSearchTool | ComputerTool | HostedMCPTool | LocalShellTool | ImageGenerationTool | CodeInterpreterTool, result: str) -> None:
        print(f"Tool is ending... {tool.name}- {result}")
        return await super().on_tool_end(context, agent, tool, result)
    
# class MyCustomHooksRun(RunHooks):
#     def __init__(self) -> None:
#         super().__init__()
        
#     async def on_agent_start(self, context: RunContextWrapper[Any], agent: Agent[Any]) -> None:
#         print(f"RunHooks: 👀 Agent is starting... {agent.name}")
#         return await super().on_agent_start(context, agent)
    
#     async def on_agent_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any) -> None:
#         print(f"RunHooks: 👀 Agent is ending... {agent.name}")    
#         return await super().on_agent_end(context, agent, output)
    
#     async def on_handoff(self, context: RunContextWrapper[Any], from_agent: Agent[Any], to_agent: Agent[Any]) -> None:
#         print(f"RunHooks: Handsoff from {from_agent.name} to {to_agent.name}")
#         return await super().on_handoff(context, from_agent, to_agent)
    
#     async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: FunctionTool | FileSearchTool | WebSearchTool | ComputerTool | HostedMCPTool | LocalShellTool | ImageGenerationTool | CodeInterpreterTool) -> None:
#         print(f"RunHooks: Tool is calling... {tool.name}")
#         return await super().on_tool_start(context, agent, tool)
    
#     async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: FunctionTool | FileSearchTool | WebSearchTool | ComputerTool | HostedMCPTool | LocalShellTool | ImageGenerationTool | CodeInterpreterTool, result: str) -> None:
#         print(f"RunHooks: Tool is ending... {tool.name}- {result}")
#         return await super().on_tool_end(context, agent, tool, result)
        

@function_tool
async def fetch_weather():
    return "Today's weather is rainny."

history_agent: Agent = Agent(
    name="History_Agent",
    instructions="You are a history specialist."
)

math_agent: Agent = Agent(
    name="Math_Agent",
    instructions="You are a math specialist."
)

agent: Agent = Agent(
    name="Areeba_Agent",
    instructions="You are a helping agent. If user ask about weather use `fetch_weather` tool. Your name is Zehal Khan Afandi. Your owner is Areeba Zafar and when user ask about history so handsoff to `history_agent`.",
    hooks=MyCustomHooksAgent(),
    tools=[fetch_weather],
    handoffs=[history_agent, math_agent],
    handoff_description="We have two agents a history_agent and a math_agent."
)

result = Runner.run_sync(
    agent,
    """1. What is your name and who is your owner?
       2. Tell me about today's weather.
       3. Tell me about world war 2.
       4. What is 9 + 3?
    """,
    run_config=config,
)

print(result.final_output)
print("="*50)
# rich.print(result.new_items)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain artificial intelligence in two simple sentences.",
    "Calculate the total and average of 92, 78, 55, 70 and 80.",
    "Write a 150-word beginner explanation of how LangChain and LangSmith work together."
]

for number, prompt in enumerate(prompts, start=1):
    print(f"\n--- Prompt {number} ---")
    print(prompt)
    response = llm.invoke(prompt)
    print("Answer:", response.content)
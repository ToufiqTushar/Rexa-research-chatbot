from utils.llm import ask_llm


question = "What is artificial intelligence?"

answer = ask_llm(question)

print("\nAI Response:")
print(answer)
from search import SearchManager
from utils.load_env import EnvManager

def main():
	EnvManager.load_env()
	search_manager = SearchManager()
	
	while True:
		try:
			question = input("PERGUNTA: ")
			if question.lower() in ["exit", "quit"]:
					break
			
			response = search_manager.search_prompt(question)
			print(f"RESPOSTA: {response}\n")

		except (EOFError, KeyboardInterrupt):
			break

if __name__ == "__main__":
	main()

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('FinancialChatbot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with English corpus
trainer.train('chatterbot.corpus.english')

# Function to chat with the bot
def chat_with_bot():
    print("Hello, I am your Financial Assistant. Ask me anything about finance!")
    while True:
        try:
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            # Get response from the chatbot
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Start the chatbot
if __name__ == "__main__":
    chat_with_bot()

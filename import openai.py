import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

class Chatbot:
    def __init__(self):
        self.conversation_history = []
    
    def get_response(self, user_input):
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Get response from OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history
            )
            
            # Extract assistant's message
            assistant_message = response.choices[0].message['content']
            
            # Add assistant's response to conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
            
        except Exception as e:
            return f"An error occurred: {str(e)}"

def main():
    chatbot = Chatbot()
    print("AI Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

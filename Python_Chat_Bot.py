from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]


def chatbot(knowledge: dict):
    """Chatbot"""

    while True:
        user_input: str = input('You: ')

        # Finds the best match, otherwise returns None
        best_match: str | None = get_best_match(user_input, knowledge)

        # Gets the best match from the knowledge base
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand... Could you try rephrasing that?')


if __name__ == "__main__":
    brain: dict = {
        'hello': 'Hey there! How can I brighten your day today?',
        'how are you?': 'I’m doing great, thanks for asking! How about you?',
        'do you know what the time is?': 'I’m afraid I don’t have a watch, but I’m always here for you!',
        'what time is it?': 'Time flies when you’re chatting with me, doesn’t it?',
        'what can you do?': 'I can chat with you, share knowledge, crack jokes, and even make your day better!',
        'ok': 'Awesome! Let’s keep rolling!',
        'who are you?': 'I’m your friendly Python-powered chatbot, here to make life a little easier.',
        'what is your name?': 'You can call me ChatBot, your virtual buddy!',
        'tell me a joke': 'Why don’t skeletons fight each other? They don’t have the guts!',
        'what is python?': 'Python is a versatile programming language that powers apps, websites, AI models, and more!',
        'bye': 'Goodbye! Hope to chat with you again soon!',
        'who created you?': 'I was crafted by none other than Rehan Aslam Khan, a certified data scientist!',
        'can you help me?': 'I’m here to help you the best I can! Ask away!',
        'what is AI?': 'Artificial Intelligence, or AI, refers to machines designed to think and learn like humans—pretty cool, right?',
        'what is machine learning?': 'Machine Learning lets computers learn from data and get smarter with experience—think of it as teaching machines new tricks!',
        'what is data science?': 'Data Science is the art of turning raw data into valuable insights, and it’s revolutionizing industries!',
        'who is Rehan Aslam Khan?': 'Rehan Aslam Khan is a certified data scientist with a passion for teaching and building smart solutions!',
        'how do you work?': 'I work by matching your questions to my knowledge base, and I try to give the best possible answer!',
        'tell me a fun fact': 'Did you know that octopuses have three hearts? Talk about a lot of love!',
        'what’s your favorite language?': 'Python, of course! Simple, powerful, and always evolving.',
        'can you learn new things?': 'With the right programming, I can grow smarter every day!',
        'what’s the meaning of life?': 'Some say it’s 42, but I’d say it’s to keep learning and exploring!',
        'what’s the weather like?': 'I’m not connected to the web yet, but I bet it’s a beautiful day wherever you are!'
    }

    chatbot(knowledge=brain)
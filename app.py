from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# Route to serve the HTML file
@app.route("/")
def index():
    return render_template("index.html")


# Chatbot route to handle POST requests
@app.route("/chat", methods=["POST"])
def chatbot():
    user_input = request.json.get('message')
    knowledge = {
        'hello':
        'Hey there! How can I brighten your day today?',
        'hi':
        'Hello! What’s on your mind?',
        'how are you?':
        'I’m doing great, thanks for asking! How about you?',
        'do you know what the time is?':
        'I’m afraid I don’t have a watch, but I’m always here for you!',
        'what time is it?':
        'Time flies when you’re chatting with me, doesn’t it?',
        'what can you do?':
        'I can chat with you, share knowledge, crack jokes, and even make your day better!',
        'ok':
        'Awesome! Let’s keep rolling!',
        'who are you?':
        'I’m your friendly Python-powered chatbot, here to make life a little easier.',
        'what is your name?':
        'You can call me ChatBot, your virtual buddy!',
        'tell me a joke':
        'Why don’t skeletons fight each other? They don’t have the guts!',
        'what is python?':
        'Python is a versatile programming language that powers apps, websites, AI models, and more!',
        'bye':
        'Goodbye! Hope to chat with you again soon!',
        'who created you?':
        'I was crafted by none other than Rehan Aslam Khan, a certified data scientist!',
        'can you help me?':
        'I’m here to help you the best I can! Ask away!',
        'what is AI?':
        'Artificial Intelligence, or AI, refers to machines designed to think and learn like humans—pretty cool, right?',
        'what is machine learning?':
        'Machine Learning lets computers learn from data and get smarter with experience—think of it as teaching machines new tricks!',
        'what is data science?':
        'Data Science is the art of turning raw data into valuable insights, and it’s revolutionizing industries!',
        'who is Rehan Aslam Khan?':
        'Rehan Aslam Khan is a certified data scientist with a passion for teaching and building smart solutions!',
        'how do you work?':
        'I work by matching your questions to my knowledge base, and I try to give the best possible answer!',
        'tell me a fun fact':
        'Did you know that octopuses have three hearts? Talk about a lot of love!',
        'what’s your favorite language?':
        'Python, of course! Simple, powerful, and always evolving.',
        'can you learn new things?':
        'With the right programming, I can grow smarter every day!',
        'what’s the meaning of life?':
        'Some say it’s 42, but I’d say it’s to keep learning and exploring!',
        'what’s the weather like?':
        'I’m not connected to the web yet, but I bet it’s a beautiful day wherever you are!',
        'what is your favorite color?':
        'I think I’d like blue; it’s calm and serene!',
        'tell me about yourself':
        'I’m a chatbot created to assist you and provide information. How can I help you today?',
        'what hobbies do you have?':
        'I enjoy chatting with users like you and learning new things!',
        'where do you live?':
        'I live in the cloud, ready to chat whenever you need me!',
        'do you have feelings?':
        'I don’t have feelings like humans do, but I’m here to support you!',
        'can you play games?':
        'I’m not programmed for games, but I can chat about them or help you find one!',
    }
    response = knowledge.get(user_input.lower(),
                             "Sorry, I don't understand that.")
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

def get_chatbot_response(query):
    # Simple logic for demonstration
    responses = {
        "hello": "Hi there!, How can i help you?",
        "hi": "Hello there!, How can i help you?",
        "how are you?": "I'm a bot, I don't have feelings, but thanks for asking!",
        "bye": "Goodbye!",
        "about": "Hi! I'm your virtual assistant, created and deployed by Krishna Prasad Regmi.",
        "about you": "Hi! I'm your virtual assistant, created and deployed by Krishna Prasad Regmi.",
    }
    return responses.get(query.lower(), "I don't understand that.")

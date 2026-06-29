from chatbot import Chat, register_call
import wikipedia
import os
import warnings
warnings.filterwarnings("ignore")


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return f"Sorry, I couldn't find any information about '{query}'. Please try another topic."


first_question = "Welcome! 👋 I am your AI Chatbot. Ask me anything."
chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Example.template"))
chat.converse(first_question)

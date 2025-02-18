from langchain_google_genai import ChatGoogleGenerativeAI

import config


def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", api_key=config.setings.GOOGLE_AI_API_KEY
    )
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg)


if __name__ == "__main__":
    main()

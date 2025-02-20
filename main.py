import google.generativeai as genai
import config


def main():
    genai.configure(api_key=config.setings.GOOGLE_AI_API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content("Who is Ho Chi Minh")

    print(response.text)


if __name__ == "__main__":
    main()

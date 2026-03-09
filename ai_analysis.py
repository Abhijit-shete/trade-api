import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AIzaSyAv4PAv3Zvs7e9lQc-aRn8tLgmiEcM9sSM")

# model define
model = genai.GenerativeModel("gemini-pro")


def analyze_data(news, sector):

    prompt = f"""
    Analyze the following news about the {sector} sector in India.
    Give a short market analysis and future outlook.

    News:
    {news}
    """

    response = model.generate_content(prompt)

    return response.text
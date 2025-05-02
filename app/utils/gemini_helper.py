import google.generativeai as genai
import os


class GeminiHelper:
    @staticmethod
    def query(question, context):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')

        prompt = f"""
        Answer this question based on the provided context:
        Question: {question}
        Context: {context['text']}
        """

        response = model.generate_content(prompt)
        return response.text
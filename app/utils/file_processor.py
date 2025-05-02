from PyPDF2 import PdfReader
import docx
import os


class FileProcessor:
    @staticmethod
    def search_knowledge(folder_path, query):
        context = {'text': '', 'sources': []}

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(('.pdf', '.docx', '.txt')):
                    file_path = os.path.join(root, file)
                    text = ""

                    if file.endswith('.pdf'):
                        reader = PdfReader(file_path)
                        text = " ".join([page.extract_text() for page in reader.pages])
                    elif file.endswith('.docx'):
                        doc = docx.Document(file_path)
                        text = " ".join([para.text for para in doc.paragraphs])
                    else:
                        with open(file_path, 'r') as f:
                            text = f.read()

                    if query.lower() in text.lower():
                        context['text'] += f"\n\n[{file}]: {text[:2000]}..."
                        context['sources'].append(file_path)

        return context
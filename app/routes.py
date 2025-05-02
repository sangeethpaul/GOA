from flask import Blueprint, request, jsonify, render_template
from app.utils.gemini_helper import GeminiHelper
from app.utils.file_processor import FileProcessor
import os

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            question = data['question']

            # Search knowledge base
            knowledge_path = os.path.join(current_app.config['UPLOAD_FOLDER'])
            context = FileProcessor.search_knowledge(knowledge_path, question)

            # Get Gemini response
            response = GeminiHelper.query(question, context)

            return jsonify({
                'question': question,
                'response': response,
                'sources': [os.path.basename(f) for f in context['sources']]
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('index.html')
from flask import Blueprint, request, jsonify
from app.services.core import CVGenerator

api = Blueprint('api', __name__)
generator = CVGenerator()

@api.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        cv_content = generator.generate_ats_content(data['input'])
        return jsonify({'content': cv_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/health', methods=['GET'])
def health_check():
    return 'OK'

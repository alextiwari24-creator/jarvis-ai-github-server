from flask import Flask, request, jsonify
import logging
from config import SERVER_PORT, SERVER_HOST
from ai_engine import JarvisAI
from task_executor import TaskExecutor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
ai_engine = JarvisAI()
executor = TaskExecutor()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'online', 'message': 'JARVIS AI is running'})

@app.route('/api/command', methods=['POST'])
def command():
    data = request.get_json()
    cmd = data.get('command', '')
    if not cmd:
        return jsonify({'error': 'No command'}), 400
    response = ai_engine.process_command(cmd)
    return jsonify({'command': cmd, 'response': response})

@app.route('/api/repos', methods=['GET'])
def repos():
    return jsonify({'repos': executor.list_repos()})

@app.route('/api/issue', methods=['POST'])
def create_issue():
    data = request.get_json()
    result = executor.create_issue(data.get('repo'), data.get('title'), data.get('body', ''))
    return jsonify({'result': result})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    logger.info(f'Starting JARVIS on {SERVER_HOST}:{SERVER_PORT}')
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False)

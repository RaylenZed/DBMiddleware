from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# 读取配置文件
with open('config.json', 'r') as f:
    config = json.load(f)

def verify_api_key(api_key):
    for db_config in config['databases'].values():
        if api_key in db_config['api_keys']:
            return True
    return False

def get_db_config_by_api_key(api_key):
    for db_name, db_config in config['databases'].items():
        if api_key in db_config['api_keys']:
            return db_name, db_config
    return None, None

@app.route('/get_connection_info', methods=['GET'])
def get_connection_info():
    api_key = request.headers.get('X-API-Key')
    if not verify_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    db_name, db_config = get_db_config_by_api_key(api_key)
    if not db_config:
        return jsonify({'error': 'Database not found'}), 404

    connection_info = {
        'host': db_config['host'],
        'user': db_config['user'],
        'database': db_config['database']
    }
    return jsonify(connection_info)

@app.route('/get_password', methods=['GET'])
def get_password():
    api_key = request.headers.get('X-API-Key')
    if not verify_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    db_name, db_config = get_db_config_by_api_key(api_key)
    if not db_config:
        return jsonify({'error': 'Database not found'}), 404

    return jsonify({'password': db_config['password']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


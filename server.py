from flask import Flask, jsonify, request

app = Flask(__name__)

# Список постов блога
posts = []

# Эндпоинт для получения всех постов
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Эндпоинт для добавления нового поста
@app.route('/api/posts', methods=['POST'])
def add_post():
    new_post = request.json
    posts.append(new_post)
    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
from ai import assign_department_and_category

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_response():  # put application's code here
    data = request.json
    subject = data.get('subject')
    description = data.get('description')

    department, category = assign_department_and_category(subject, description)

    return jsonify({
        'department': department,
        'category': category
    })


if __name__ == '__main__':
    app.run()

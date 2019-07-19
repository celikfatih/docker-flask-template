from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def get():
    return Response('Welcome to Docker Container Flask Application!')


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

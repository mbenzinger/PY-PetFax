from flask import Flask, request


#facotry function
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Go to /pets!"

    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app
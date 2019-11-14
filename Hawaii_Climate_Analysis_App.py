import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hawaii Climate Data App</h1>
        <h2>Available Static Routes</h2>
        <h3>Precipitation</h3>
        '''

app.run()
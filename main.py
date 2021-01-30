import json
from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
from data.RedditInterface import RedditInterface

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/Popular")
@cross_origin(origin='localhost')
def popular_page():
    subreddits = request.args.get('subreddits')
    limit = int(request.args.get('limit'))

    if not subreddits or not limit:
        abort(404)

    subreddits_list = subreddits.split(',')

    stock_w_count =  RedditInterface.find_submissions_stock_symbols(subreddits_list, limit)

    dict_list = []

    for (symbol, count) in stock_w_count.items():
        dict_list.append({'symbol': symbol, 'count': count})

    return json.dumps(dict_list)

if __name__ == "__main__":
    app.run()
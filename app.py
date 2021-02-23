import flask from Flask , g
import sqlite


app = Flask(__name__)


def connect_db():
    sql= sqlite.connect('/database.db')
    sql.row_factory= sqlite.Row
    return sql

def get_db():
    if not hasattr (g,'sqlite'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(erroe):
    if hasattr(g. 'sqlite_db');
    g.sqlite_db.close()


@app.route('/')
def index():
    return'<h1>hello , world</h1>'




if __name__== '__main__':
    app.run(debug=True)
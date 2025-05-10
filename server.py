from flask import Flask, jsonify, request, abort,render_template,redirect, url_for
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from climbDAO import climbDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/climbs')
@cross_origin()
def showClimbs():
    climbs = climbDAO.getAll_climbs()
    return render_template('climbs.html', climbs=climbs)

@app.route('/newclimb', methods=['GET'])
def newClimbForm():
    return render_template('new_climb.html')

@app.route('/newclimb', methods=['POST'])
def submitNewClimb():
    form = request.form
    data = {
        "name": form['name'],
        "grade": form['grade'],
        "crag_id": int(form['crag_id']),
        "style_id": int(form['style_id']),
        "completed": bool(int(form['completed'])),
        "attempts": int(form['attempts']),
        "personal_grade_feeling": form.get('personal_grade_feeling'),
        "date_climbed": form.get('date_climbed') or None
    }
    climbDAO.create_climb_with_log(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
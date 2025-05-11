from flask import Flask, jsonify, request, abort,render_template,redirect, url_for
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from climbDAO import climbDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

# To display the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# To display the climbs.html page
@app.route('/climbs')
@cross_origin()
def showClimbs():
    climbs = climbDAO.getAll_climbs()
    return render_template('climbs.html', climbs=climbs)

# To add a new climb
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

#@app.route('/deleteclimb/<int:climb_id>', methods=['POST'])
#def deleteClimb(climb_id):
#    climbDAO.delete_climb_with_log(climb_id)
#    return redirect(url_for('showClimbs'))  # goes back to /climbs

# To display the crag and style boxes in the new climb form
@app.route('/newclimb', methods=['GET'])
def newClimbForm():
    cursor = climbDAO.getcursor()
    
    cursor.execute("SELECT id, name, location, country FROM crags")
    crags = [dict(id=row[0], name=row[1], location=row[2], country=row[3]) for row in cursor.fetchall()]
    
    cursor.execute("SELECT id, style_name FROM styles")
    styles = [dict(id=row[0], style_name=row[1]) for row in cursor.fetchall()]
    
    climbDAO.closeAll()
    return render_template('new_climb.html', crags=crags, styles=styles)

# Display the crag using a leaflet map
@app.route('/crags')
def viewCrags():
    cursor = climbDAO.getcursor()
    sql = """
            SELECT name, location, country, lat, lon, more_info 
            FROM crags 
            WHERE lat IS NOT NULL AND lon IS NOT NULL
        """
    cursor.execute(sql)
    crags = []
    for row in cursor.fetchall():
        crags.append({
            "name": row[0],
            "location": row[1],
            "country": row[2],
            "lat": float(row[3]),
            "lon": float(row[4]),
            "more_info": row[5]
        })
    climbDAO.closeAll()
    return render_template('view_crags.html', crags=crags)

    

if __name__ == '__main__':
    app.run(debug=True)
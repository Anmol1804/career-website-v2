from flask import Flask, render_template, jsonify
from database import engine

app = Flask(__name__)




@app.route("/")
def helloWorld():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)



# we store the data in an api route (json data)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

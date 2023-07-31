from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  
  # list to map values
  keys = ['id','title','location','salary','currency','responsibilities','requirements']
  
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))  
  
    jobs = []
    for row in result.all():
      row_val_ls = list(row)
      jobs.append(dict(zip(keys,row_val_ls)))
  
    return jobs

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

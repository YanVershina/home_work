from flask import Flask, render_template
from utils import load_candidates_from_json, get_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)

@app.route('/candidate/<int:uid>')
def profile(uid):
   items = get_by_id(uid)
   return render_template('single.html', items=items)


@app.route('/search/<candidate_name>')
def search_name(candidate_name):
   items = get_candidates_by_name(candidate_name)
   count_name = str(len(items))
   return render_template('search.html', items=items, count_name=count_name)


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
   items = get_candidates_by_skill(skill_name)
   count_name = str(len(items))
   return render_template('skill.html', skill_name=skill_name, items=items, count_name=count_name)



app.run()
from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

candidates = load_candidates()

app = Flask(__name__)


@app.route('/')
def page_main():
    return get_all(candidates)

@app.route("/candidates/<int:uid>")
def profile_candidate(uid):
    return get_by_pk(uid)

@app.route("/skills/<skill_name>")
def pages_skill(skill_name):
    return get_by_skill(skill_name)



app.run()

# text_candidates = load_candidates(file_candidates)
# all_candidates = get_all(text_candidates)


# print(get_by_pk(3, text_candidates))

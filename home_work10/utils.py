import json


def load_candidates() -> list[dict]:
    ''' Переводим информацию о кандидатах в список'''

    with open("candidates.json", "r", encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates

def get_all(candidates):
    candidates_name ="<pre>"
    for i in candidates:
        candidates_name += f'{i["name"]}\n{i["position"]}\n{i["skills"]}\n'
    candidates_name += "</pre>"
    return candidates_name

def get_by_pk(uid): #которая вернет кандидата по pk
    candidates = load_candidates()
    candidate = ""
    for i in candidates:

        if uid == i["pk"]:
            candidate += f"<img src='({i['picture']})'>"
            candidate += "<pre>"
            candidate += f"{i['name']}\n{i['position']}\n{i['skills']}\n\n"
            break
        else:
            continue
    candidate +="</pre>"
    return candidate


def get_by_skill(skill_name): #которая вернет кандидатов по навыку
    candidates = load_candidates()
    candidates_by_skill = "<pre>"
    for i in candidates:
        if skill_name in i["skills"]:
            candidates_by_skill += f"{i['name']}\n{i['position']}\n{i['skills']}\n\n"

    candidates_by_skill += "</pre>"
    return candidates_by_skill
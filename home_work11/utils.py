import json

def load_candidates() -> list[dict]:
    with open("candidates.json", "r", encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates


def load_candidates_from_json():
    candidates = load_candidates()
    candidates_name =""
    for i in candidates:
        candidates_name += f'{i["name"]}\n{i["position"]}\n{i["skills"]}\n'
    return candidates_name

def get_by_id(uid): # возвращает одного кандидата по его id
    candidates_list = load_candidates_from_json()
    for item in candidates_list:
        if uid == item["id"]:
            candidate = item
            break
        else:
            continue
    return candidate


def get_candidates_by_name(candidate_name): # возвращает кандидатов по имени
    candidates_list = load_candidates_from_json()
    candidate_by_name = []
    for item in candidates_list:
        if candidate_name in item["name"]:
            candidate_by_name.append({"id":item["id"], "name":item["name"]})

    return candidate_by_name


def get_candidates_by_skill(skill_name): # возвращает кандидатов по навыкуpa
    candidates_list = load_candidates_from_json()
    candidate_by_skill = []
    for item in candidates_list:
        if skill_name in item["skills"]:
            candidate_by_skill.append({"id": item["id"], "name": item["name"]})
    print(candidate_by_skill)
    return candidate_by_skill


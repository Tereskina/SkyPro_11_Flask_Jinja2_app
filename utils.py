import json


class Candidate:
    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills


def load_candidates_from_json(filename):
    """Возвращает список всех кандидатов"""
    with open(filename, 'r', encoding='utf-8') as f:
        raw_str = json.load(f)

    candidates_ = []

    for candidate in raw_str:
        temp = Candidate(
            candidate["id"],
            candidate["name"],
            candidate["picture"],
            candidate["position"],
            candidate["gender"],
            candidate["age"],
            candidate["skills"],
        )

        candidates_.append(temp)
    return candidates_


def get_candidate(uid):
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate.id == uid:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    result = []
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate.name == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates_from_json("candidates.json"):
        if skill_name.lower() in candidate.skills.lower().split(', '):
            result.append(candidate)
    return result

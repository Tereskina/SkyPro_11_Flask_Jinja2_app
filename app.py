from flask import Flask, render_template, request

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/',)
def get_all_candidates():
    """Список всех кандидатов"""
    candidates = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:uid>',)
def candidate_page(uid):
    """Выводит данные кандидата"""
    candidate = get_candidate(uid)
    if not candidate:
        return 'Кандидат не найден'
    return render_template("card.html", candidate=candidate)


@app.route('/search/<candidate_name>',)
def page_candidates_by_name(candidate_name):
    """Поиск кандидата по имени"""
    candidates = get_candidates_by_name(candidate_name)
    if not candidates:
        return 'Кандидат не найден'
    return render_template("search.html", candidates=candidates)


@app.route('/skill/<skill_name>',)
def search_by_skill(skill_name):
    """Поиск кандидата по навыку"""
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()

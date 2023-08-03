import json
import os

path_student = os.path.join('data', 'students.json')
path_professions = os.path.join('data', 'professions.json')


def load_student_file(path):  # Загружает список студентов из файла
    """
    :param path:  список студентов из файла --os.path.join('data', 'students.json')--
    :return: список словарей из json данные о студенте
    """
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def load_professions(path):  # Загружает список профессий из файла
    """
    :param path: список профессий из файла os.path.join('data', 'professions.json')
    :return: список словарей из json данные о необходимых навыков для профессии
    """
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def get_student_by_pk(pk):  #
    """
    :param pk:Получает словарь с данными студента по его pk
    :return:возвращает список: данные о студенте
    """
    file = load_student_file(path_student)

    for data in file:
        if data["pk"] == pk:
            i = file.index(data)
            return file[i]
    else:
        print("У нас нет такого студента")
        quit()


def get_profession_by_title(title):  #
    """
    :param title: Получает словарь с инфо о профессии по названию
    :return:возвращает список необходимых навыков для профессии
    """
    file = load_professions(path_professions)
    for data in file:
        if data["title"] == title:
            i = file.index(data)
            return file[i]
    else:
        print("У нас нет такой специальности")
        quit()


def check_fitness(student, profession):
    """
    получив студента и профессию, возвращает словарь типа:
    {"has": ["Python", "Linux"], "lacks": ["Docker, SQL"], "fit_percent": 50}
    """
    student_set = set(student)  # преобразуем в множестово
    profession_set = set(profession)  # преобразуем в множестово
    has = list(student_set.intersection(profession_set))  # пересечение, то чем владеет студент
    lacks = list(profession_set.difference(student_set))  # разница, то чего не хватает для выбранной профессии
    fit_percent = len(has) * 100 / len(profession_set)  # какой процент знаний есть студента для выбранной профессии
    # сборка словаря
    student_in_profession = {}
    student_in_profession["has"] = has
    student_in_profession["lacks"] = lacks
    student_in_profession["fit_percent"] = fit_percent
    return student_in_profession
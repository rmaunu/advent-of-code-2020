import logging

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_customs_questions(input_file):
    lines = read_list_file(input_file)
    groups_questions = []
    current_group_questions = []
    for line in lines:
        if len(line.rstrip()) == 0:
            groups_questions.append(current_group_questions)
            current_group_questions = []
        else:
            current_group_questions.append(line.rstrip())

    groups_questions.append(current_group_questions)
    return groups_questions


def compile_group_questions(group_questions, check='any'):
    group_question_set = set([question for question in group_questions[0]])
    for questions in group_questions[1:]:
        if check == 'any':
            group_question_set = group_question_set.union(
                set([question for question in questions])
            )
        elif check == 'all':
            group_question_set = group_question_set.intersection(
                set([question for question in questions])
            )
    return group_question_set


def day_6(part, input_file):
    groups_questions = read_customs_questions(input_file)
    if part == 1:
        total_questions = sum([
            len(compile_group_questions(group_questions, check='any'))
            for group_questions in groups_questions
        ])
        logger.info(f"For all groups, {total_questions} questions were answered 'yes'")
    elif part == 2:
        total_questions = sum([
            len(compile_group_questions(group_questions, check='all'))
            for group_questions in groups_questions
        ])
        logger.info(f"For all groups, {total_questions} questions were answered 'yes'")

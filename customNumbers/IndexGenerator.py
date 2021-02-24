import random

def isResultNot(result, index_correct_answer, wrong_answer001, wrong_answer002):
    return result != index_correct_answer and result != wrong_answer001 and result != wrong_answer002

def generate_random_number_for_wrong_answer(index_correct_answer, wrong_answer001, wrong_answer002, number_of_jurisdictions):
    result = random.randint(0, number_of_jurisdictions - 1)
    return result if isResultNot(result, index_correct_answer, wrong_answer001, wrong_answer002) else generate_random_number_for_wrong_answer(index_correct_answer, wrong_answer001, wrong_answer002, number_of_jurisdictions)
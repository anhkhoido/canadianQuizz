from provinces_dictionary import canadian_provinces
from pathlib import Path
import random

filename_quizz = "quizz_"
filename_capacity_answerkey = "capitalcity-answers_quizz_"

def isResultNot(result, index_correct_answer, wrong_answer001, wrong_answer002):
    return result != index_correct_answer and result != wrong_answer001 and result != wrong_answer002

def generate_random_number_for_wrong_answer(index_correct_answer, wrong_answer001, wrong_answer002, number_of_jurisdictions):
    result = random.randint(0, number_of_jurisdictions - 1)
    return result if isResultNot(result, index_correct_answer, wrong_answer001, wrong_answer002) else generate_random_number_for_wrong_answer(index_correct_answer, wrong_answer001, wrong_answer002, number_of_jurisdictions)

def create_each_quizz(directory_for_quizzes, directory_for_answer_keys):
    dictionary_of_jurisdictions = canadian_provinces
    for quizNumber in range(35):
        print("Creation of quizz " + f"{quizNumber + 1}")
        quizz_filename = filename_quizz + str(quizNumber + 1) + ".txt"
        quizz_answerkey_filename = filename_capacity_answerkey + str(quizNumber + 1) + ".txt"
        quizz_file = open(directory_for_quizzes / quizz_filename, "w")
        quizz_answerkey_file = open(directory_for_answer_keys / quizz_answerkey_filename, "w")
        quizz_file.write("Name:_______________________\nGroup:______________________\nDate:_______________________\n\n")
        quizz_file.write("Midterm exam - Geography\n\n")
        quizz_answerkey_file.write("Answer keys for: " + str(quizz_filename) + "\n")
        list_of_provinces = list(dictionary_of_jurisdictions.keys())
        random.shuffle(list_of_provinces)
        for index in range(len(list_of_provinces)):
            correctAnswer = dictionary_of_jurisdictions[list_of_provinces[index]]
            wrong_answer001 = generate_random_number_for_wrong_answer(index, -1, -1, len(list_of_provinces))
            wrong_answer002 = generate_random_number_for_wrong_answer(index, wrong_answer001, -1, len(list_of_provinces))
            wrong_answer003 = generate_random_number_for_wrong_answer(index, wrong_answer001, wrong_answer002, len(list_of_provinces))
            wrong_city001 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer001]]
            wrong_city002 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer002]]
            wrong_city003 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer003]]
            answerOptions = [correctAnswer, wrong_city001, wrong_city002, wrong_city003]
            random.shuffle(answerOptions)
            quizz_file.write(f'{index + 1}. What is the capital city of {list_of_provinces[index]}?\n')
            for choice in range(4):
                quizz_file.write(f"    {'ABCD'[choice]}. {answerOptions[choice]}\n")
                if answerOptions[choice] == correctAnswer:
                    quizz_answerkey_file.write(f"{index + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
        quizz_answerkey_file.close()
        quizz_file.close()

def start_creation_of_quizzes():
    print("Starting the creation of the quizzes.")
    directory_for_quizzes = Path(Path.cwd() / 'quizzes/')
    directory_for_answer_keys = Path(Path.cwd() / 'correction/')
    if directory_for_quizzes.exists() == False:
        directory_for_quizzes.mkdir()
    if directory_for_answer_keys.exists() == False:
        directory_for_answer_keys.mkdir()
    create_each_quizz(directory_for_quizzes, directory_for_answer_keys)

def main():
    print("Hello, world! You are about to create your quizzes.")
    start_creation_of_quizzes()
    print("Your quizzes are now ready!")

if __name__ == "__main__":
    main()
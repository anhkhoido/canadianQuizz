from provinces_dictionary import canadian_provinces
from pathlib import Path
from customNumbers import IndexGenerator as ig
import logging
import random

logging.basicConfig(filename="canadianQuizz.log", format='%(asctime)s %(message)s', filemode='w')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

filename_quizz = "quizz_"
filename_capacity_answerkey = "capitalcity-answers_quizz_"
QUIZZ_NAME = "Midterm exam - Geography\n\n"

def create_each_quizz(directory_for_quizzes, directory_for_answer_keys):
    dictionary_of_jurisdictions = canadian_provinces
    LOGGER.info("randomQuizGenerator.py : create_each_quizz(directory_for_quizzes, directory_for_answer_keys)")
    LOGGER.info(f"  {dictionary_of_jurisdictions.keys()}")
    for quizNumber in range(35):
        LOGGER.info("  Creation of quizz " + f"{quizNumber + 1}")
        quizz_filename = filename_quizz + str(quizNumber + 1) + ".txt"
        quizz_answerkey_filename = filename_capacity_answerkey + str(quizNumber + 1) + ".txt"
        quizz_file = open(directory_for_quizzes / quizz_filename, "w")
        quizz_answerkey_file = open(directory_for_answer_keys / quizz_answerkey_filename, "w")
        quizz_file.write("Name:_______________________\nGroup:______________________\nDate:_______________________\n\n")
        quizz_file.write(QUIZZ_NAME)
        quizz_answerkey_file.write("Answer keys for: " + str(quizz_filename) + "\n")
        list_of_provinces = list(dictionary_of_jurisdictions.keys())
        random.shuffle(list_of_provinces)
        for index in range(len(list_of_provinces)):
            LOGGER.info(f"  Quizz {quizNumber + 1} - Creation of question {index + 1}")
            correctAnswer = dictionary_of_jurisdictions[list_of_provinces[index]]
            wrong_answer001 = ig.generate_random_number_for_wrong_answer(index, -1, -1, len(list_of_provinces))
            wrong_answer002 = ig.generate_random_number_for_wrong_answer(index, wrong_answer001, -1, len(list_of_provinces))
            wrong_answer003 = ig.generate_random_number_for_wrong_answer(index, wrong_answer001, wrong_answer002, len(list_of_provinces))
            wrong_city001 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer001]]
            wrong_city002 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer002]]
            wrong_city003 = dictionary_of_jurisdictions[list_of_provinces[wrong_answer003]]
            answerOptions = [correctAnswer, wrong_city001, wrong_city002, wrong_city003]
            random.shuffle(answerOptions)
            quizz_file.write(f'{index + 1}. What is the capital city of {list_of_provinces[index]}?\n')
            for choice in range(4):
                LOGGER.info(f"  Choice {choice + 1}")
                quizz_file.write(f"    {'ABCD'[choice]}. {answerOptions[choice]}\n")
                if answerOptions[choice] == correctAnswer:
                    quizz_answerkey_file.write(f"{index + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
        quizz_answerkey_file.close()
        quizz_file.close()

def start_creation_of_quizzes():
    LOGGER.info("randomQuizGenerator.py : start_creation_of_quizzes()")
    directory_for_quizzes = Path(Path.cwd() / 'quizzes/')
    directory_for_answer_keys = Path(Path.cwd() / 'correction/')
    if directory_for_quizzes.exists() == False:
        LOGGER.info("  Creation of directory canadianQuizz/quizzes")
        directory_for_quizzes.mkdir()
    if directory_for_answer_keys.exists() == False:
        LOGGER.info("  Creation of directory canadianQuizz/correction")
        directory_for_answer_keys.mkdir()
    LOGGER.info("  Directories for quizzes and answer keys already exist.")
    create_each_quizz(directory_for_quizzes, directory_for_answer_keys)

def main():
    LOGGER.info("randomQuizGenerator.py : main()")
    print("Hello, world! You are about to create your quizzes.")
    start_creation_of_quizzes()
    print("Your quizzes are now ready!")

if __name__ == "__main__":
    main()
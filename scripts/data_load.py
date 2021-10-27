import csv
from biologicalquizapp.models import * 

def run():
    # CSV file path name
    csv_questions = ".\\data\\question_pipe.csv"
    csv_answers = ".\\data\\answer_pipe.csv"
    csv_images = ".\\data\\image_pipe.csv"

    # Read files
    dataReaderQ = csv.reader(open(csv_questions), delimiter='|', quotechar='"')
    dataReaderA = csv.reader(open(csv_answers, encoding="utf8"), delimiter='|', quotechar='"')
    dataReaderI = csv.reader(open(csv_images, encoding="utf8"), delimiter='|', quotechar='"')

    # Parse files
    for row in dataReaderQ:
        question = Question()
        question.question = row[1]
        question.type = row[2]
        question.imagefield = row[3]
        question.points = row[4]
        question.n_answer = row[5]
        question.n_image = row[6]
        question.save()

    for row in dataReaderA:
        answer=Answer()
        answer.question_id = row[1]
        answer.answer = row[2]
        answer.definition = row[3]
        answer.save()

    for row in dataReaderI:
        image=Image()
        image.name = row[1]
        image.description = row[2]
        image.mode = row[3]
        image.celltype = row[4]
        image.components = row[5]
        image.doi = row[6]
        image.organism = row[7]
        image.save()
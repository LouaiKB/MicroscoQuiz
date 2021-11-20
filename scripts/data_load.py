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
    for row in dataReaderI:
        image=Image()
        question = Question()
        image.name = row[1]
        image.description = row[2]
        image.mode = row[3]
        image.celltype = row[4]
        image.components = row[5]
        image.doi = row[6]
        image.organism = row[7]
        image.save()

    for row in dataReaderQ:
        question = Question()
        answer = Answer()
        
        question.question = row[1]

        if row[1] == '1':
            image = Image.objects.values('mode').distinct()
            question.imagefield.add(image)

        elif row[1] == '2':
            image = Image.objects.values('components').distinct()
            question.imagefield.add(image)

        question.type = row[2]
        question.points = row[4]
        question.n_answer = row[5]
        question.n_image = row[6]
        question.save()

    for row in dataReaderA:
        answer=Answer()

        if row[1] == '1':
            question = Question.objects.get(id=1)

        elif row[1] == '2':
            question = Question.objects.get(id=2)

        answer.question_id = question
        answer.answer = row[2]
        answer.definition = row[3]
        answer.save()

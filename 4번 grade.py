class Grade:

    def __init__(student, name, kor, eng, math):
        student.name = name
        student.kor = kor
        student.eng = eng
        student.math = math
        student.sum = student.kor + student.eng + student.math

    def score(student, sub):
        student.sub = sub
        if student.sub == 'kor':
            print("{}의 국어 점수는 {} 점 입니다".format(student.name, student.kor))
        elif student.sub == 'eng':
            print("{}의 영어 점수는 {} 점 입니다".format(student.name, student.eng))
        elif student.sub == 'math':
            print("{}의 수학 점수는 {} 점 입니다".format(student.name, student.math))

    def average(student):
        print("{}의 평균 점수는 {}점 입니다".format(student.name, student.sum/3))

    def __del__ (student):
        print("{} 학생 객체는 삭제되었습니다.".format(student.name))

kim = Grade("Kim", 60, 80, 65)
park = Grade("Park", 80, 49, 93)
kim.score("kor")
park.score("eng")
park.average()
del(park)
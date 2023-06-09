class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score

    def get_info(self):
        return "이름: ", self.name, "학번: ", self.student_id, "학년: ", self.year, "전공: ", self.major,"평균점수: ", self.avg_score

class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        print(f"{student.name} 학생 추가")
        self.student_list.append(student)        
    
    def remove_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                print(f"{student_id}번의 {student.name} 학생이 삭제되었습니다.")
                return
        print(f"{student_id}학번을 가진 학생이 존재하지 않습니다.")
            
    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print(f"학번 {student_id}번의 {student.name} 학생이 존재합니다")
                return
        print(f"{student_id}학번을 가진 학생이 존재하지 않습니다.")

    def show_all_student(self):
        for i in self.student_list:
            print(i.get_info())

student_manager = StudentManager()
student1 = Student("홍길동", "20230001", 2, "컴퓨터공학", 60.5)
student2 = Student("이예진", "20230002", 1, "경영학", 90.8)
student3 = Student("박수현", "20230003", 3, "수학", 87.5)
student4 = Student("조원준", "20230004", 2, "경제학", 45.6)

student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)
student_manager.add_student(student4)
student_manager.show_all_student()
print("+" * 20)

student_manager.remove_student("20230001")
print("+" * 20)
student_manager.find_student("20230003")
print("+" * 20)

student_manager.show_all_student()

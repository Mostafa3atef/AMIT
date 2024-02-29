class Quiz:
    def __init__(self):
        self.your_result=0

    def quiz_answers(self,answers):
        list_index=0
        for y in answers:
            list_index+=1
            print(f'{list_index}. {y}')
        return str(input("\nYour answer: "))
    
    def check(self,the_correct_answer,given_answer):
        if given_answer==the_correct_answer:
            self.your_result += 20
            
    def final_result(self):
        print(self.your_result)
        if self.your_result == 0:
            print(f"\nyour result: {self.your_result}%\nGrade: F")
        elif self.your_result == 20:
            print(f"\nyour result: {self.your_result}%\nGrade: P")
        elif self.your_result == 40:
            print(f"\nyour result: {self.your_result}%\nGrade: D")
        elif self.your_result == 60:
            print(f"\nyour result: {self.your_result}%\nGrade: C")
        elif self.your_result == 80:
            print(f"\nyour result: {self.your_result}%\nGrade: B")
        elif self.your_result == 100:
            print(f"\nyour result: {self.your_result}%\nGrade: A")


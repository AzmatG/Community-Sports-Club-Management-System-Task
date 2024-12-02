class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    def set_details(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    def get_details(self):
        return f"Name {self.name}\n Age: {self.age}\n Contact Number: {self.contact}"
class Member(Person):
    def __init__(self, name, age, contact, membership_id, sport):
        super().__init__(name, age, contact)
        self.membership_id = membership_id
        self.sport = sport
        self.performance = []  
    def set_member_details(self, membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport
    def add_performance_score(self, score):
        self.performance.append(score)
    def calculate_average_score(self):
        try:
            return round(sum(self.performance)/len(self.performance), 2)
        except:
            return 0
    def get_member_summary(self):
        return f"{self.get_details()}\nMembership ID: {self.membership_id}\nSport: {self.sport}\nAverage Performance: {self.calculate_average_score}"
class Coach(Person):
    def __init__(self, name, age, contact, coach_id, specialisation, salary):
        super().__init__(name, age, contact)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
        self.mentorship_group = []
    def set_coach_details(self, coach_id, specialisation, salary):
        self,coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
    def assign_mentee(self, member):
        self.mentees.append(member)
        return f"Coach {self.name} is now mentoring {member.name} in {member.sport}"
    def get_mentees(self):
        for mentee in self.mentees:
            print(f"Student: {mentee.name}")
    def increase_salary(self, percentage):
        self.salary += self.salary*percentage/100
    def mentor_coach(self, coach):
        self.mentorship_group.append(coach)
        print(f"Coach {self.name} is now mentoring now mentoring Coach {coach.name} in {self.specialisation}")
    def get_mentorship_group(self):
        for coach in self.mentorship_group:
            print(f"Coach: {coach.name} || Specialisation: {coach.specialisation}") 
        
class Staff(Person):
    def __init__(self, name, age, contact, staff_id, position, years_of_service):
        super().__init__(name, age, contact)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    def increment_years_of_service(self):
        self.years_of_service += 1
    def assist_member(self, member):
        return f"Staff {self.name} has assisted {member.name} in resolving an issue."
    def get_staff_summary(self):
        return f"{self.get_details}\n\nStaff ID: {self.staff_id}\nPosition: {self.position}\nYears of Service: {self.years_of_service}"





  
member1 = Member("Hinata", 16, 12094757, "Hin16", "Volleyball")
member2 = Member("Shizuka", 16, 314159, "Shiz16", "Table Tennis")
coach1 = Coach("Uzui", 30, 123, "Uz30", "Volleyball", 10000)
coach2 = Coach("Rose", 23, 123, "30", "Table Tennis", 15000)
staff = Staff("Rale", 50, 62839, "Rale50", "Principal", 20)

#Functionality

coach1.assign_mentee(member1)
print(f"{coach1.name} is coaching {coach1.get_mentees()}")
member1.add_performance_score(80)
member1.add_performance_score(40)
member1.add_performance_score(90)
print(f"{member1.name}'s average performance: {member1.calculate_average_score()}")
print(staff.assist_member(member2))
coach1.increase_salary(15)
staff.increment_years_of_service()
member1.get_member_summary()
member2.get_member_summary()
staff.get_staff_summary()
coach1.mentor_coach(coach2)
coach1.get_mentorship_group()
coach1.get_mentees()


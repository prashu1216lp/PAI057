class Student:
    def __init__(self, name, skills, level):
        self.name = name
        self.skills = skills
        self.level = level
        self.assigned_project = None


class Project:
    def __init__(self, title, required_skills, difficulty):
        self.title = title
        self.required_skills = required_skills
        self.difficulty = difficulty
        self.is_assigned = False


class AIProjectAssignmentSystem:
    def __init__(self, students, projects):
        self.students = students
        self.projects = projects

    def calculate_match_score(self, student, project):
        score = 0
        for skill in project.required_skills:
            if skill in student.skills:
                score += 2
        if student.level == project.difficulty:
            score += 3
        return score

    def assign_projects(self):
        for student in self.students:
            best_project = None
            best_score = -1
            for project in self.projects:
                if not project.is_assigned:
                    score = self.calculate_match_score(student, project)
                    if score > best_score:
                        best_score = score
                        best_project = project
            if best_project:
                student.assigned_project = best_project.title
                best_project.is_assigned = True

    def display_assignments(self):
        for student in self.students:
            if student.assigned_project:
                print(student.name, "->", student.assigned_project)
            else:
                print(student.name, "-> No Project Assigned")


students = [
    Student("Alice", ["Python", "AI", "Machine Learning"], "Advanced"),
    Student("Bob", ["HTML", "CSS", "JavaScript"], "Beginner"),
    Student("Charlie", ["Python", "Data Analysis"], "Intermediate")
]

projects = [
    Project("AI Chatbot System", ["Python", "AI"], "Advanced"),
    Project("Website Development", ["HTML", "CSS"], "Beginner"),
    Project("Data Analytics Dashboard", ["Python", "Data Analysis"], "Intermediate")
]

system = AIProjectAssignmentSystem(students, projects)
system.assign_projects()
system.display_assignments()
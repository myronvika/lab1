from __future__ import annotations
from typing import List, Any, Dict
from datetime import datetime, timedelta


class Developer:
    """Developer representation.

       Attributes:
           id_ (int): Developers ID, is incremented for each instance.
           name (str): Name.
           address (str): Registration address.
           email (str): Personal company e-mail.
           phone_number (str) : Person's working phone number.
           position (str): Persons company position (e.g., 'Junior').
           salary (str): Salary amount (can be re-calculated).
           projects (List[Projects]): List of assigned projects
       """

    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str, position: str, rank: str,
                 salary: float, ) -> None:
        self.id_ = id_
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.assignments: List[Assignment] = []
        self.projects: List[Any] = []

        # функція призначення проекту
        def assign(self, project):
            self.projects.append([project])

        # функція перегляду проекту
        def assigned_projects(self):
            return self.projects

        # функція скасування
        def unassign(self, project_title: str):
            self.projects = list(filter(lambda x: x.title == project_title,
                                        self.projects))


class Project:
    """Project representation.

        Attributes:
            title (str): Project's name.
            start_date (str): Start date.
            developers (List[Developer]): List of assigned developers.
            limit (int): Maximum number of workers.
        """

    def __init__(self, title: str, start_date: datetime, developers: list[str], limit: int):
        # list[str] is  developers
        self.title = title
        self.start_date = start_date
        self.developers = developers
        self.limit = limit

    def add_developer(self, developer: Developer) -> bool:
        if len(self.developers) < self.limit:
            developer.assign(self)
            self.developers.append(developer)
            print(f'Developer {developer.name} has been added to the project {self.title}')
            return True
        else:
            print("Limit has been exceeded")
            return False

    def remove_developer(self, which_developer_remove) -> None:  # Attributes:  With developer should be removed
        if which_developer_remove not in self.developers:
            print(f"There is no developer named {which_developer_remove}")
        else:
            self.developers.remove(which_developer_remove)
            print(f"The developer named {which_developer_remove} is removed")


class QAEngineer:
    """QA engineer representation.
    Attributes:
        id_ (int): QAEngineer ID, is incremented for each instance.
        name (str): name.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position.
        salary (str): Salary amount .

    """

    # Оголосити змінні QaEngineer class
    def __init__(self, id_: int, name: str, address: str,
                 phone_number: str, email: str, salary: float,
                 rank: str, position: str,
                 ) -> None:
        self.id_ = id_
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    # Функція для перевірки true project
    def test_feature(self, project: Project):
        if project.title == 'Pattern Design':
            print('It\'s your project -- start to do ')
        else:
            print(f'{developer.name} it\'s not your task.Change the project')


class Assignment():
    """
    Attributes:

        received_tasks (Dict): dictionary in form of
                        {date1: task1, date2: task2,...}.
        is_done (bool): True, if all tasks are completed.
        description (str): General assignment description.
        status (str): Percent of completed tasks.

    """

    def __init__(self, tasks: Dict, description: str, is_done: bool, status: str, ) -> None:
        self.received_tasks = tasks
        self.description = description
        self.status = status
        self.is_done = is_done

    # функція для надсилання завдання по datetime
    def get_tasks_to_date(self, date: datetime) -> List[Dict]:
        return [value for key, value in self.received_tasks.items()
                if key <= date]


class ProjectManager:
    """
           Attributes:
               id_ (int): PM's ID, is incremented for each instance.
               name (str): First + last names.
               address (str): Registration address.
               phone_number (str) : Person's working phone number.
               email (str): Personal company e-mail.
               salary (str): Salary amount (can be re-calculated).
               project (Projects): Assume PM -> Project relation.
           """

    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str, salary: float,
                 project: Project):
        self.id_ = id_
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = list([project])

    # Для перевірки прогресу
    def discuss_progress(self, assignment) -> str:  # discuss_progress
        return f"Discussion about the progress of the project with such a task: {assignment}"


project_01 = Project("Mars", (2021, 10, 9), ["Liza", "Com", "Inna", "Sasha", "Alina"], 6)

print(project_01.developers)

# добавляємо developer

project_01.add_developer("Vika")
print(project_01.developers)

project_01.remove_developer("Tom")

print(project_01.developers)
project_01.remove_developer("Jin")
print(project_01.developers)

assignment_01 = Assignment({(2020, 1, 12): "Create a loop",
                            (2021, 2, 13): "Create a drop-down list",
                            (2022, 3, 14): "Create artificial intelligence",
                            (2023, 4, 15): "Delete all your work"}, True, "Good assignment!", "Done!")

print(len(assignment_01.received_tasks))
print(assignment_01.get_tasks_to_date((2020, 1, 12)))  # test get tasks to date

man_01 = QAEngineer(1, "Alina", "Lviv ", "+380692775376", "myronvika@gmail.com",
                    1334.1, "Junior", "Junior")

print(man_01.email)
print(QAEngineer.test_feature(QAEngineer, "Create a loop"))

print(ProjectManager.discuss_progress(ProjectManager, "Create a loop"))

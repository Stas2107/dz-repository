# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.task_list = []

    class SingleTask():
        def __init__(self, description, deadline, status):
            self.description = description
            self.deadline = deadline
            self.status = status

    def add_task(self, description, deadline):
        new_task = self.SingleTask(description, deadline, 'Not Completed')
        self.task_list.append(new_task)

    def mark_completed(self, description):
        for task in self.task_list:
            if task.description == description:
                task.status = 'Completed'

    def get_current_tasks(self):
        current_tasks = [task.description for task in self.task_list if task.status == 'Not Completed']
        return current_tasks


TaskManager = Task()
TaskManager.add_task('Полить цветы', '08:00')
TaskManager.add_task('Покормить кота', '09:00')
TaskManager.add_task('Убрать квартиру', '10:00')

TaskManager.mark_completed('Полить цветы')

print(TaskManager.get_current_tasks())
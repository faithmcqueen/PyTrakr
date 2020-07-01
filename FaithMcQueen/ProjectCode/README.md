# PyTrackr: Work Tracking System
A freelance work tracking system, with a timer that can track hours and holds a total that the user could charge for that work. Could also hold tasks and upcoming projects, for task management

## Contributions
###Task & Project Dashboard
Tasks can be added, edited, and deleted from the task management system. They will also be able to be grouped into a project, so specific projects can have specific tasks assigned to them. These will display when users click into a project, so they can see all of the tasks assigned to a specific project. When the taskboard is displayed, the user can see the task name, due date, priority, and hour allotment. When they click into a task, they can see more details including task notes, the timer start button, and the amount of time already spent on the task (if any).
####Templates:
- templates/PyTraker/tasklist.html
- templates/PyTraker/task_detail.html
- templates/PyTraker/new_task.html
- templates/PyTraker/details_project.html (Added "New Task" button and tasks associated with project)
- templates/PyTraker/header.html (linking to correct stylesheet)
#### models.py:
- class Tasks(models.Model):
#### views.py
- tasklist
- task_detail
- new_task
- edit_task
- delete_task
- change_status
#### forms.py
- TaskForm
###Styling
- static/Sass/style.sass
- static/Sass/style.css (CSS file compiled from sass file)

 
 
 



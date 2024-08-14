class SmartAssistant:
    def __init__(self):
        self.meetings = []
        self.tasks = []

    def schedule_meeting(self, title, date_time, participants):
        self.meetings.append({
            'title': title,
            'date_time': date_time,
            'participants': participants
        })
        print(f"Meeting '{title}' scheduled for {date_time} with participants: {', '.join(participants)}")

    def add_task(self, task_description, deadline):
        self.tasks.append({
            'description': task_description,
            'deadline': deadline
        })
        print(f"Task added: '{task_description}' with deadline {deadline}")

    def list_meetings(self):
        print("Scheduled Meetings:")
        for meeting in self.meetings:
            print(f"- {meeting['title']} at {meeting['date_time']} with {', '.join(meeting['participants'])}")

    def list_tasks(self):
        print("Tasks to Complete:")
        for task in self.tasks:
            print(f"- {task['description']}, Deadline: {task['deadline']}")

# Example usage
if __name__ == "__main__":
    assistant = SmartAssistant()

    # Schedule meetings
    assistant.schedule_meeting("Project Kickoff", "2024-07-10 10:00 AM", ["Alice", "Bob", "Charlie"])
    assistant.schedule_meeting("Budget Review", "2024-07-12 2:00 PM", ["Alice", "David"])

    # Add tasks
    assistant.add_task("Prepare presentation slides", "2024-07-09")
    assistant.add_task("Review quarterly reports", "2024-07-11")

    # List scheduled meetings and tasks
    assistant.list_meetings()
    assistant.list_tasks()

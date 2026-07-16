from firebase_config import db
from google.cloud import firestore


class FirestoreService:

    def create_task(self, user_id, title, description, priority):

        task = {
            "userId": user_id,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "createdAt": firestore.SERVER_TIMESTAMP
        }

        db.collection("tasks").add(task)

    def get_tasks(self, user_id):

        docs = (
            db.collection("tasks")
            .where("userId", "==", user_id)
            .stream()
        )

        tasks = []

        for doc in docs:
            task = doc.to_dict()
            task["id"] = doc.id
            tasks.append(task)

        return tasks

    def update_task(self, task_id, title, description, priority, completed):

        db.collection("tasks").document(task_id).update({

            "title": title,
            "description": description,
            "priority": priority,
            "completed": completed

        })

    def delete_task(self, task_id):

        db.collection("tasks").document(task_id).delete()
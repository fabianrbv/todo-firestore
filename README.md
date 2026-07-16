# Overview

As a software developer, I am continually expanding my knowledge of modern technologies used in real-world applications. The purpose of this project was to learn how to integrate a cloud database with a web application while implementing secure user authentication and basic data management operations.

This project is called **ToDo Cloud**, a task management web application built with Python, Flask, Google Firebase Authentication, and Google Firestore. Users can create an account, sign in securely, and manage their own personal tasks. Each authenticated user can create, view, edit, and delete tasks, with all information stored in a cloud database. Every user only has access to their own tasks.

To use the application, users first create an account or sign in with an existing account. After logging in, they can add new tasks by entering a title, description, and priority level. Existing tasks can be edited or deleted directly from the dashboard, and all changes are automatically synchronized with Firestore.

The purpose of writing this software was to gain hands-on experience with cloud databases, user authentication, and the integration of frontend and backend technologies commonly used in modern web development.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

This project uses **Google Firebase Firestore**, a NoSQL cloud database that stores data as collections of documents. Firestore provides real-time access, scalability, and seamless integration with Firebase Authentication.

The database contains a single collection named **tasks**. Each document represents one task and includes the following fields:

- userId
- title
- description
- priority
- completed

The `userId` field stores the unique identifier of the authenticated user, allowing the application to retrieve only the tasks that belong to the currently logged-in user.

# Development Environment

The software was developed using the following tools:

- Visual Studio Code
- Python 3.12
- Flask
- Google Firebase Console
- Google Firestore
- Firebase Authentication
- Git and GitHub

Programming languages and libraries used:

- Python
- HTML5
- CSS3
- JavaScript (ES6 Modules)
- Bootstrap 5
- Flask
- firebase-admin
- Google Firebase Web SDK

# Useful Websites

- https://firebase.google.com/docs
- https://firebase.google.com/docs/firestore
- https://firebase.google.com/docs/auth
- https://flask.palletsprojects.com/
- https://getbootstrap.com/
- https://developer.mozilla.org/

# Future Work

- Add the ability to mark tasks as completed.
- Sort tasks by creation date or priority.
- Improve the user interface with filtering and search functionality.
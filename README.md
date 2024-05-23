<p align="center">
  <img width="150" src="/readme/logo.svg" alt="Logo">
</p>

---

## Introduction

In today's digital age, managing time and tasks has become a challenge for many people. With the development of information technology, applying digital applications and tools to support task management is becoming more necessary and important than ever. In this context, developing a Todo List application becomes a significant project, not only for enhancing individual productivity but also as a crucial step in applying technology to solve practical life issues.

The Todo List project we have undertaken aims to provide users with an efficient tool to manage and organize daily tasks in the most scientific and convenient way possible. Using modern web technologies, combined with popular programming languages like Python and the Flask framework, we have built a Todo List application that meets users' needs in managing time and tasks.

In the following sections of this report, we will present in detail the development process of the project, the main features of the application, as well as the lessons learned and the results achieved from implementing this project.

---

## Reasons for Choosing the Topic

Real-world need: In modern society, life moves at a fast pace and there are many pressures from work, study, and personal life. This creates a pressing need for effective time and task management. A Todo List application can help users organize their tasks, track progress, and prioritize tasks naturally and scientifically.

1. **Practicality**: Todo List is not only a popular application but also a useful and necessary tool in people's daily lives. Developing a Todo List application not only brings practical value but also helps us better understand the needs and desires of users.

2. **Application of Knowledge**: Through the implementation of the Todo List project, we have the opportunity to apply and practice the knowledge we have learned. From backend programming with Python, using the Flask framework, to developing user interfaces with HTML and CSS, we can apply our knowledge and skills to a real project.

3. **Skill Development**: Developing a Todo List application requires not only technical knowledge but also organizational, project management, and teamwork skills. Through the project implementation process, we have the opportunity to develop and improve these skills, from requirements analysis to deployment and maintenance of the application.

4. **Market Potential**: With the development of technology, the demand for using time and task management applications and tools is increasing. A Todo List application has the potential to develop and attract users in various fields, from individuals to businesses.

For these reasons, we decided to choose the Todo List topic for this project, hoping that the project will bring practical value and provide useful experiences for both users and the development team.

---

## Features

Below are the main features of the Todo List application:

1. **Login**: Users can log in to the system to manage their personal tasks.
2. **Register**: New users can create an account to use the application.
3. **Home**: Display a list of tasks and main functions.
4. **Add Task**: Users can add a new task.
5. **Edit Task**: Allow editing details of a task.
6. **Complete Task**: Mark a task as completed.
7. **Incomplete Task**: Mark a task as incomplete.
8. **Update Progress**: Update the progress of a task.
9. **Delete Task**: Delete a task from the list.
10. **Add Category**: Create a new category to classify tasks.
11. **Delete Category**: Delete a category and all related tasks.

---

## Application Screens

### Login

The login screen allows users to enter their username and password to access the system.

![Login](/readme/login.png)

### Register

The registration screen allows new users to create an account by entering their personal information.

![Register](/readme/register.png)

### Home

The home page displays a list of all the user's tasks, including both completed and incomplete tasks.

![Home](/readme/home.png)

### Add Task

The add task screen allows users to enter the title, description, deadline, and category for a new task.

![Add Task](/readme/create_task.png)

### Edit Task

The edit task screen allows users to edit the details of an existing task.

![Edit Task](/readme/update_task.png)

### Add Category

The add category screen allows users to create a new category to classify tasks.

![Add Category](/readme/create_category.png)

---

## Database Schema

### Table: categories
This table stores information about the categories of tasks.
- **slug**: Unique identifier of the category.
- **name**: Name of the category.
- **created_by**: User who created the category.

### Table: users
This table contains information about the system users.
- **username**: User's login name.
- **password**: User's password.
- **role**: User's role in the system.

### Table: tasks
This table stores information about the tasks.
- **id**: Unique identifier of the task.
- **title**: Title of the task.
- **description**: Detailed description of the task.
- **priority**: Priority level of the task.
- **category**: Category of the task.
- **created_by**: User who created the task.
- **completed**: Completion status of the task.
- **progress**: Progress of the task.
- **created_date**: Date when the task was created.

### File Usage
In this project, files are used to store data. Specifically, each table will be stored in a file in CSV format.
- **categories.csv**: Stores information about categories.
- **users.csv**: Stores information about users.
- **tasks.csv**: Stores information about tasks.

Each row in the CSV file corresponds to a record in the corresponding table. Data fields are separated by commas (,).

To ensure data consistency and safety, file operations will be performed using functions and data handling methods.

---

## How to Use

### Sign Up or Log In
1. Visit the application's website.
2. If you already have an account, log in by entering your username and password into the login form.
3. If you don't have an account, sign up by filling in the registration form with your personal information and click the sign-up button.

### Create Category
1. After successfully logging in, go to the category management page.
2. Click on the "Create Category" button or fill in the information in the category creation form.
3. Enter the name and description for the new category and click the "Save" button to create the category.

### Create Task
1. Go to the task management page.
2. Click on the "Create Task" button or fill in the information in the task creation form.
3. Enter the title, description, and other details for the new task.
4. Select a category for the task from the previously created list (if needed).
5. Click the "Save" button to create the new task.

### Update Progress
1. Go to the details of the task that needs progress update.
2. Drag the "Update Progress" button to update.

### Complete Task
1. Go to the details of the task to be completed.
2. Click on the "Complete" button to mark the task as completed.

---

## Application Deployment

### 1. Set Up Development Environment
- Ensure that the computer being used has Python installed and necessary development tools like pip.

### 2. Download Source Code and Installation
- Download the application source code from a Git repository or a reliable compressed file source.
- Extract the file if necessary and navigate to the project directory.

### 3. Set Up Virtual Environment (If Necessary)
- Create a Python virtual environment using tools like `virtualenv` or `conda`.
- Activate the virtual environment and install necessary packages using pip.

### 4. Configure the Application
- Configure the database: Ensure that the database connection information is provided correctly and configured in the application.

### 5. Start the Application
- Open a terminal and navigate to the project directory.
- Run the command `python app.py` to start the Flask development server.

### 6. Check and Debug
- Open a web browser and access the localhost:port address (default port is usually 5000) to check the application.
- Monitor any error messages that appear and debug if necessary.

### 7. Develop and Test
- Develop and test the application on the development environment.
- Use tools like Flask Debug Toolbar or loggers to monitor errors and performance.

### 8. Maintain and Upgrade
- Perform regular maintenance to ensure the stability and security of the application.
- Update and upgrade the application as needed and according to new standards.

---

## Development Team

- **Founder:** [Dubravko Luka](https://github.com/dubravko-luka)
- **Developer:** [Dubravko Luka](https://github.com/dubravko-luka)
- **UI/UX Designer:** [Dubravko Luka](https://github.com/dubravko-luka)

--- 

## Conclusion and Thanks

During the development of the Todo List project, we have learned a lot and had valuable experiences. This project is not only a significant step in improving our programming and web application development skills but also an opportunity for us to apply the knowledge we have learned into practice.

We would like to express our deep gratitude to those who have supported and encouraged us throughout the development of this project. In particular, we want to extend special thanks to the team members, mentors, friends, and family.

The Todo List project is not just our product but also a small part of the programming and web application community. We hope that this application will bring value and usefulness to users, and we will continue to develop and improve it in the future.

Sincerely thank you!

---

## Contact

If you have any questions, suggestions, or encounter any issues with the application, please contact us through the following information:

- Email: [dev.richard.npm98@gmail.com](mailto:dev.richard.npm98@gmail.com)
- Phone: +84 3xx xxx xxx
- Address: Number 000, City XYZ, Country ABC

We are always ready to listen and support you.

## Copyright

The Todo List application is developed and protected by copyright law. All rights reserved.

This is an open-source and free-to-use application. You can use, copy, modify, and distribute the application under the terms of the open-source license.

For more information about the terms and conditions, please see the LICENSE file in the application source code.

## Version

Current version: 1.0.0

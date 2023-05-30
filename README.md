# Student Hive

Welcome to the Student HIVE Project, a student residence manager web application built with Django!

We're a one-of-a-kind company that's all about providing students with an awesome experience. Our online platform lets
you explore and interact with your residence mates creating events and activities. Here you will be able to take your
stay to the next level being able to book rooms, check the laundry, ask for maintenance, get a copy of the contract,
make payments and more.

At the following YouTube link you can have a quick overview of the application:
[Student Hive Features Video](https://youtu.be/uAjraFGgdp0).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Project](#project)

## Introduction

Student HIVE is a web application designed to streamline the management of student residences. It provides a centralized
platform for managing various aspects of student accommodations, making it easier for residence managers to handle tasks
efficiently. It also has a focus on the student's experience by providing them with a convenient way to interact with
other students, residence staff and access important information.

This project is part of the Final Project of a group of 5 exchange students at VIA University College, Denmark. It
only contains the first two iterations of the project, **is not a final product**.

## Features

On the Wiki section of this GitHub project further information about the features on the first and second sprints,
with all it's SCRUM documentation, can be found. 

The main functionalities of the web application are:

- **Home Page:** Provide information about the residence, for non-registered and logged users.
- **User Management:** Allow students and administrators to register and login.
- **Event Management:** Allow students to create and search events.
- **Maintenance Requests:** Allow students to submit maintenance requests, enabling residence staff to address
  them promptly.

The next features have been half implemented in the second iteration:

- **Contract Management:** Manage student contracts, including contract terms, payment details, and contract renewals.
- **Maintenance Management:** Manage maintenance requests, including assigning requests to staff, tracking progress,
  and closing requests.

The following features are some of the multiple planned for future iterations:

- **Announcements:** Broadcast important announcements and notices to all residents through the application.
- **Study Room Management:** Manage studying rooms, booking them and inviting other residents.
- **Laundry Management:** Check availability of laundry machines and recharge the laundry card.
- **Payment Management:** Manage student payments, including rent, utilities, and other fees.
- **Much more:** The possibilities are endless!

More details about the features can be found on the Project Report submitted to VIA University College.

## Installation

To install and run the Student HIVE application locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/martiserrase/student-hive.git
   ```

2. Change into the project directory:

   ```shell
   cd student-hive
   ```

3. Create a virtual environment:

You can create a virtual environment using your IDE or, **for Linux/macOS users**, by running the following command in
the project directory:

   ```shell
   python3 -m venv env
   ```

4. Activate the virtual environment: **(Only Linux/macOS users that executed the previous command)**

     ```shell
      source env/bin/activate
      ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Set up the Django project, database and create a superuser account:

6.1. For Linux/macOS users:

Run the make command inside the virtual environment terminal:

   ```shell
   make reset 
   ```

With the command you have created a superuser account with username **admin** and password **admin**.

6.2. For Windows users:

Run the following commands inside the virtual environment terminal. First check if the migrations folder is empty, 
if not delete all the files inside it.

   ```shell
  rm -rf media/*.pdf
  rm -rf manager/migrations
  rm -f db.sqlite3
  ```

Then run the following commands:

   ```shell
   python .\manage.py makemigrations
   python .\manage.py migrate
   python .\manage.py createsuperuser
   ```
For the superuser account the recommendation is username **admin** and password **admin**.

7. Start the development server:

7.1. For Linux/macOS users:

   ```shell
   python manage.py runserver
   ```

7.2. For Windows users:

   ```shell
   python .\manage.py runserver
   ```

8. Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

- Create your user account to access as a student or use the superuser account to access as an administrator.
- Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials to access the Django 
administration interface.
- Use the various features and tools of the application.

## Project insights

The project has been developed using the Agile methodology, more specifically implementing the SCRUM technics. There 
can be found a detailed documentation of the GitHub repository Wiki.
We are a team of 5 students from the VIA University Collage of Campus Horsens, Denmark. We are currently in our exchange
semester studying Global Business Engineering and we are very excited to be working on this project. We are looking 
forward to making your stay at the residence a next level experience.

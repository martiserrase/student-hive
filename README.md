# Student HIVE Project

Welcome to the Student HIVE Project, a student residence manager web application built with Django!

We're a one-of-a-kind company that's all about providing students with an awesome experience. Our online platform lets
you explore and interact with your residence mates creating events and activities. Here you will be able to take your
stay to the next level being able to book rooms, check the laundry, ask for maintenance, get a copy of the contract,
make payments and more.

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
only contains the first iteration of the project, **is not a final product**.

## Features

The main functionalities of the web application in the first iteration are:

- **Home Page:** Provide information about the residence, for non-registered and logged users.
- **User Management:** Allow students and administrators to register and login.
- **Event Management:** Allow students to create and search events.
- **Inventory Management:** Keep track of room inventory, including furniture, appliances, and other amenities.
- **Maintenance Requests:** Allow students to submit maintenance requests, enabling residence staff to address
  them promptly.

The next features are planned for the second iteration and have been half implemented in the first iteration:

- **Contract Management:** Manage student contracts, including contract terms, payment details, and contract renewals.
- **Maintenance Management:** Manage maintenance requests, including assigning requests to staff, tracking progress,
  and closing requests.

The following features are some of the multiple planned for future iterations:

- **Announcements:** Broadcast important announcements and notices to all residents through the application.
- **Study Room Management:** Manage studying rooms, booking them and inviting other residents.
- **Laundry Management:** Check availability of laundry machines and recharge the laundry card.
- **Payment Management:** Manage student payments, including rent, utilities, and other fees.
- **Much more:** The possibilities are endless!

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

   ```shell
   python3 -m venv env
   ```

4. Activate the virtual environment:

    - On Linux or macOS:

      ```shell
      source env/bin/activate
      ```

    - On Windows:

      ```shell
      .\env\Scripts\activate
      ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the make command inside the virtual environment terminal to set up the database and create a superuser account:

   ```shell
   make reset 
   ```

With the command you have created a superuser account with username **admin** and password **admin**.

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

8. Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

- Create your user account to access as a student or use the superuser account to access as an administrator.
- Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials to access the administration interface.
- Use the various features and modules of the application.

## Project

The project has been developed using the Agile methodology, more specifically implementing the SCRUM technics.
We are a team of 5 students from the VIA University Collage of Campus Horsens, Denmark. We are currently in our exchange semester
studying Global Business Engineering and we are very excited to be working on this project. We are looking forward to
making your stay at the residence a next level experience.

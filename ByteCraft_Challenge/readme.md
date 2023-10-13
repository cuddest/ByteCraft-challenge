# Auth App

The "Auth App" is a Django-based web application that provides user authentication and task management capabilities. It is designed to be a secure and user-friendly solution for managing tasks, offering user registration and login features, as well as the ability to create, view, update, and delete tasks.

## Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Description

The "Auth App" is built using Django 4.2.5 and Django Rest Framework 3.14.0, and it leverages Django Rest Framework Simple JWT 5.3.0 for secure user authentication using JSON Web Tokens (JWT). The project provides user registration and login functionality, as well as the ability to create, manage, and view tasks.

### Key Features

- **User Registration:** Users can sign up for an account by providing their email and password.
- **User Login:** Registered users can log in to their accounts securely.
- **Task Management:** Users can create, update, delete, and view tasks.
- **Authentication:** Secure user authentication using JWT (JSON Web Tokens).
- **Custom User Model:** The application uses a custom user model that extends Django's built-in User model.
- **RESTful API:** The project provides a RESTful API for creating and managing tasks.

This project can be used as a foundation for building applications that require user authentication and task management features, such as to-do list applications, project management tools, and more.

## Technologies

- Django 4.2.5
- Django Rest Framework 3.14.0
- Django Rest Framework Simple JWT 5.3.0
- SQLite (default database)
- Python 3.11
- Other dependencies specified in the `requirements.txt` file.

## Installation

Follow these steps to set up the "Auth App" on your local machine:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/auth-app.git
Navigate to the project directory:

2. Navigate to the project directory:
cd auth-app 

3. cd auth-app
python -m venv venv

4. Activate the virtual environment:

On Windows:venv\Scripts\activate
On macos or linux : source venv/bin/activate
 
5. Install project dependencies using pip:
pip install -r requirements.txt

6. Apply database migrations to create the database:
python manage.py migrate

*****

## Usage

***a***

 o run the "Auth App," follow these steps:

Start the development server: python manage.py runserver

The application will be available at http://localhost:8000/.

You can access the API endpoints for user registration, login, and task management using the provided API documentation


***b***


Using the API with Postman : 

1. To interact with the Auth App API, you can utilize Postman, a popular API testing tool. Follow these steps to use the API:

2. Login and Obtain JWT Token: Start by making a POST request to the /login/ endpoint. Provide your login credentials (email and password) as JSON data. Upon successful authentication, you will receive a JWT token in the response. Copy this token.

3. Add JWT Token to Authorization Header: To authenticate your subsequent requests, set the "Authorization" header in Postman. Choose "Bearer Token" and paste the JWT token obtained in the previous step. This token is used for user-specific actions.

4. Managing Tasks: As an authenticated user, you can add and view tasks. To add a task, make a POST request to /addT/, providing the task details in the request body. To view your tasks, send a GET request to /list/.

5. Admin Capability: If you have admin privileges, you can manage all tasks. As an admin, you can add, view, update, and delete tasks through the API. To do so, you will use the same endpoints as regular users but with administrative authentication.

6. This README provides a brief overview of using the Auth App API with Postman. Detailed API documentation is available at the /swagger/ and /redoc/ endpoints, where you can explore and test the API further. Please note that this explanation can be placed at the beginning of your README file, offering users a clear guide on how to interact with your API.


***** API Endpoints *****
User Registration: POST /api/register/
User Login: POST /api/login/
User Logout: POST /api/lout/
User Profile: GET /api/userv/
Create Task: POST /api/addT/
Update Task: PUT /api/det/{task_id}/
Delete Task: DELETE /api/del/{task_id}/
List Tasks: GET /api/list/
For detailed information on API usage and request/response examples, refer to the API documentation.



***** API Documentation *****

We've provided comprehensive documentation for our API to help you get started quickly. You can explore our API endpoints, understand the available resources, and learn how to make requests by following these simple steps:

1. View the API Schema: To get an overview of the available endpoints and their functionalities, you can check out the API Schema. It provides you with insights into the structure and data types of our API resources.

2. Interactive API Documentation: For an interactive and user-friendly documentation experience, you can explore our Swagger documentation using drf-spectacular. It offers a well-organized interface that allows you to test API endpoints directly from the documentation, making it easy to understand the available functionalities.

Feel free to explore and test our API with the help of this documentation. It provides a clear path to get started with user registration, authentication, task management, and more. If you have any questions or need assistance, don't hesitate to reach out to us.




 

:) Contributing :)
If you'd like to contribute to the project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and write tests if necessary.
Ensure your code passes all tests.
Submit a pull request to the main branch.


enjoy ! for any questions dont bother contacting me 
EMAIL : a_touati@estin.dz 
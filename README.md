# Django ToDo Application

The Django ToDo application is a web-based task management system designed using the Django framework. It demonstrates the effective implementation of core Django features, making it a robust and reliable task management solution.

---

## Key Features

### 1. User Authentication
- Implemented using JWT (JSON Web Tokens) for secure, stateless authentication.
- Ensures secure login, signup, and session management.

### 2. CRUD Functionality
- Provides Create, Read, Update, and Delete operations for managing tasks efficiently.

### 3. MVC Architecture
- Adheres to the Model-View-Controller pattern for clean and maintainable code.

### 4. Form Handling
- Utilizes Django's forms for data validation and rendering.

---

## Technical Stack

- **Backend**: Django framework
- **Frontend**: HTML templates with Bootstrap for styling
- **Authentication**: JWT for stateless user authentication
- **Database**: SQLite for task and user data storage

---

## Workflow

### 1. User Signup/Login
- New users register using the signup form.
- Returning users log in to access their task list.

### 2. Task Management
- Users can create tasks with relevant details.
- Tasks can be updated or deleted as needed.

### 3. Secure Access
- Non-authenticated users are redirected to the login page for security.

---

## Testing and Validation

Comprehensive manual testing was performed, covering:
- User authentication
- Task management features
- Input validation

The application passed all test cases, ensuring the reliability of its core functionalities.

---

## Strengths

- Stateless and secure user authentication using JWT.
- Simple and intuitive user interface.
- Modular and scalable codebase with Django’s robust architecture.

---

## Conclusion and Analysis

The Django ToDo application effectively demonstrates the use of Django's framework for creating a functional, user-friendly task management system. Key aspects include:

- **MVC Architecture**: Ensures clean and maintainable code.
- **Form Handling and Validation**: Provides reliable input processing.
- **JWT Authentication**: Enhances security with stateless user sessions.

This project highlights best practices in web application development by integrating backend logic with frontend templates to provide a seamless user experience.

---

## Installation and Setup

### Prerequisites
- Python 3.7+
- Django 4.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shwetasugure/Todo_List.git
   ```

2. Navigate to the project directory:
   ```bash
   cd todo-backend
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at `http://127.0.0.1:8000/`.

---
## Contact
For any queries, feel free to reach out at [shwetasugure333@gmail.com](mailto:shwetasugure333@gmail.com).

---

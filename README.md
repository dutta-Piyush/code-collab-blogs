# Code Collab Blogs

## Overview
This project is a collaborative blogging platform built using Flask, a lightweight Python web framework. It consists of two main services: **Content Management** and **User Authentication**. The project is designed to allow users to register, log in, manage their profiles, and create/edit content.

## Technologies & Frameworks

### Backend
- **Flask**: A micro web framework for Python used to build the web application.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) library for database interactions.
- **Flask-Login**: Extension for managing user sessions and authentication.
- **Flask-WTF**: Extension for handling forms and CSRF protection.
- **Flask-SQLAlchemy**: Extension that integrates SQLAlchemy with Flask for database operations.

### Frontend
- **HTML/CSS**: Used for structuring and styling the web pages.
- **JavaScript**: Used for client-side interactivity and dynamic content.

### Database
- **SQLite**: A lightweight, file-based database used for storing user data and content.

### Development Tools
- **Python**: The primary programming language used for backend development.
- **Virtual Environment**: Used to manage project dependencies and isolate the development environment.

## Project Structure

### Root Directory
- **services/**: Contains the main application services.
  - **contentManagement/**: Service for managing blog content.
    - **app/**: Main application code for content management.
      - **blueprints/**: Modular components for different functionalities.
        - **contentPage/**: Blueprint for content-related views and forms.
      - **templates/**: HTML templates for rendering web pages.
      - **static/**: Static files like CSS and JavaScript.
    - **vcontentManagement/**: Virtual environment for content management.
    - **db_creation.py**: Script for creating the database.
    - **db_fetch.py**: Script for fetching data from the database.
    - **db_manualInsert.py**: Script for manually inserting data into the database.
    - **db_tableview.py**: Script for viewing database tables.
    - **run.py**: Script to run the content management service.
  - **authUser/**: Service for user authentication and profile management.
    - **app/**: Main application code for user authentication.
      - **blueprints/**: Modular components for different functionalities.
        - **user_profile/**: Blueprint for user profile views.
        - **register/**: Blueprint for user registration.
        - **login/**: Blueprint for user login.
        - **edit_profile/**: Blueprint for editing user profiles.
        - **contentPage/**: Blueprint for content-related views.
      - **templates/**: HTML templates for rendering web pages.
      - **static/**: Static files like CSS and JavaScript.
    - **vauthUser/**: Virtual environment for user authentication.
    - **instance/**: Contains the SQLite database file.
    - **db_creation.py**: Script for creating the database.
    - **db_fetch.py**: Script for fetching data from the database.
    - **api_checker.py**: Script for checking API endpoints.
    - **run.py**: Script to run the user authentication service.

## Features
- **User Registration**: Users can register with a username, email, and password.
- **User Login**: Users can log in using their credentials.
- **User Profile Management**: Users can view and edit their profiles.
- **Content Management**: Users can create, edit, and view blog content.

## Getting Started
1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   ```
2. **Set Up Virtual Environment**:
   - For Content Management:
     ```bash
     cd services/contentManagement
     python -m venv vcontentManagement
     source vcontentManagement/bin/activate  # On Windows: vcontentManagement\Scripts\activate
     pip install -r requirements.txt
     ```
   - For User Authentication:
     ```bash
     cd services/authUser
     python -m venv vauthUser
     source vauthUser/bin/activate  # On Windows: vauthUser\Scripts\activate
     pip install -r requirements.txt
     ```
3. **Run the Application**:
   - For Content Management:
     ```bash
     python run.py
     ```
   - For User Authentication:
     ```bash
     python run.py
     ```

## Dependencies
- **Flask**: `pip install Flask`
- **Flask-Login**: `pip install Flask-Login`
- **Flask-WTF**: `pip install Flask-WTF`
- **Flask-SQLAlchemy**: `pip install Flask-SQLAlchemy`
- **SQLAlchemy**: `pip install SQLAlchemy`

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors
- [Your Name](https://github.com/yourusername)

## Acknowledgments
- Thanks to the Flask community for their excellent documentation and support.
- Special thanks to all contributors who have helped in the development of this project.

## Detailed Description

### Purpose
The Code Collab Blogs project aims to provide a platform where users can collaborate on blog content. It allows users to register, log in, manage their profiles, and create/edit content. The project is designed to be user-friendly and scalable, making it easy for users to interact with the platform.

### Key Features
- **User Authentication**: Secure user registration and login functionality.
- **Profile Management**: Users can view and edit their profiles, including personal information and preferences.
- **Content Creation**: Users can create, edit, and view blog content, fostering collaboration and sharing of ideas.
- **Responsive Design**: The platform is designed to be responsive, ensuring a good user experience on various devices.

### Technical Details
- **Flask**: The project uses Flask, a lightweight Python web framework, to handle routing, request processing, and rendering of templates.
- **SQLAlchemy**: An ORM library that simplifies database interactions, allowing for easy querying and manipulation of data.
- **Flask-Login**: Manages user sessions and authentication, ensuring secure access to user-specific features.
- **Flask-WTF**: Handles form creation and validation, protecting against CSRF attacks.
- **Flask-SQLAlchemy**: Integrates SQLAlchemy with Flask, providing a seamless way to interact with the database.
- **SQLite**: A lightweight, file-based database used for storing user data and content, making it easy to set up and manage.

### Future Enhancements
- **User Roles**: Implement different user roles (e.g., admin, moderator) to manage content and users.
- **Comment System**: Allow users to comment on blog posts, fostering discussion and engagement.
- **Search Functionality**: Implement a search feature to help users find specific content quickly.
- **Analytics**: Add analytics to track user engagement and content performance.

## Conclusion
The Code Collab Blogs project is a robust platform for collaborative blogging, leveraging modern web technologies to provide a seamless user experience. With its focus on user authentication, profile management, and content creation, it offers a solid foundation for future enhancements and scalability. 
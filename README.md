# Personal-Photo-Gallery-Web-App
# Photo Gallery Website

**User Authentication**  
- **Username**: `test`  
- **Password**: `test`

## Running the App

**To run the application, use the following commands:**
- `docker build -t my_app .`
- `docker run -p 5000:5000 -it my_app`


## Overview

This website enables authenticated users (credentials above) to upload photos to create their own personal photo gallery. Photos are displayed in a visually pleasing manner using a CSS grid layout for an organized and aesthetic presentation.

Logged-in users have access to an "Edit" button. This button reveals options to either delete specific uploaded photos or add new ones. By clicking the "+" icon, users are directed to an upload page where they can add additional photos.  

There's also an "About" page where users can add a description for their current photo gallery. If non-logged-in users attempt to access the upload menu, they are redirected to the login page and shown an alert indicating that login is required to upload photos. A logout button is also available, but only visible to logged-in users.

## Implementation Details

### Technologies Used

- **Flask**: Chosen for handling server-side logic and dynamic page routing.
- **Flask-Login**: Integrated to simplify the authentication process and manage user sessions.
- **Werkzeug**: Used for secure file upload management, ensuring filenames are safe.
- **HTML/CSS**: Employed for structuring and styling web pages.
- **Jinja2 Templating**: Utilized to render dynamic content in web pages through templating.

### Design Choices

- **Flask Framework**: Flask was selected for its simplicity and flexibility in building web applications.
- **Separation of Responsibilities**: The MVC model was followed to organize code, ensuring maintainability.
- **User Authentication**: Authentication is implemented with Flask-Login to ensure secure access to features.
- **Responsive Design**: CSS media queries are used to make the site accessible across various devices.
- **Dynamic Rendering**: Jinja2 enables dynamic content rendering, allowing seamless data flow from server to client.

### Libraries Utilized

- **Flask**: Core web framework for handling application logic.
- **Flask-Login**: Manages user authentication and session handling.
- **Flask-Uploads**: Facilitates file upload management within Flask.
- **Pillow**: Image processing library, used to handle and display image files.
- **Werkzeug**: Utility library for basic web application functions, including routing and file handling.
- **Flask-SQLAlchemy**: Extension that integrates SQLAlchemy with Flask for database management and interaction within the app.
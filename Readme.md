TodoList
Getting Started
Installing Dependencies
Python 3.7.7
Follow instructions to install the latest version of python for your platform in the python docs

1. Virtual Enviornment
Install python 3.7.7 and setup virtual environement and you can follow the instruction at below link to configuration the environment
https://www.python.org/downloads/release/python-377/
https://docs.python.org/3/library/venv.html

2. PIP Dependencies
Once completeing the setup of virtual enviroment, install PIP3 and run the below commands to install dependencies

pip3 install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

3. Key Dependencies
This project written in python with Postgresql and SQLAlchemy, and run with gunicorn web server. For Authentication, we use Auth0 as service for authentication and authorization. For more detail you can download and read the requirement.txt in the root folder.

4. Running the server
After the installed the dependencies, run "export FLASK_APP=app.py FLASK_DEBUG=true flask run" in the terminal
Run and Test the app

Each time you open a new terminal session, run:

5. URL of the project:
https://todolist-udacity2020.herokuapp.com/

6. API key for the two roles

User:
(Have the right to create, edit, read and delete his own tasks)
The API keys are submit in the Student Note
Please login with the /login route and enter the below username and password to get the token from the link
username: user@todo.com
password: Passwordtest1

Admin:
(Have the right to read all users's tasks)
The API keys are submit in the Student Note
Please login with the /login route and enter the below username and password to get the token from the link
username: admin@todo.com
password: Passwordtest1

Logout wiht the /logout route

7. List of files included in the project.

A. venv, the Python virtualenv folder
B. Root folder, auth.py and server.py consisting login logout and authentication method
app.py the consisting the function of all APIs, models.py to map the database
test_todo.py for app API testing

8. Copyright and licensing information.

This software is only shared by Udacity and the writer. To share this software, the consent of both parties should be obtained.


9. Acknowledgements and credits for any resources or blogs that helped you create the project.

Thank you to stackoverflow, and the contributors for all the plugins of Flask and Flask

10. Motivation for project
The purpose of this app is to make a alpha version of a web todo list application. Under current purpose it is still under development and testing.


11. local development
Refer to the instructions to install the app, after installing the app. You can find the app.py including all APIs, models.py including all the database models, server.py and auth.py including the authentication configuration to Auth0. You can allowed to change all the configuration after get the agreement of the author and Udacity

12. hosting instruction
This app is based in Flask and able to run on Gunicorn, you can deploy it to AWS or Heroku or any hosting services that Support CICD.

This project deployed to Heroku

13. Documentation of API behavior and RBAC controls
This project consist of five APIs:
A. two Get API to get the task and list detail /task and /list, each list contains many of tasks
B. one Post API to post the new task data to the list. /addtask
C. one Patch API to update the exisitng task. /task/update/<int:taskid>
D. one Delete API to delete exisitng task. /task/delete/<int:taskid>

This project consist of two roles:
A. The admin role, able to read all the task and list of any user, but cannot update delete or change the content
B. The user role, able to read all the own data and able to update delete or change the content

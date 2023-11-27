# Python
## Overview
A command line application that allows the creation of a recipe, modify them with ingredients, cooking time, and difficulty parameter that will be calculated automatically. The user will be able to search recipes by ingredients. 
## KeyFeatures
+ Create and manage the user’s recipes on a locally hosted MySQL database.
+ Option to search for recipes that contain a set of ingredients specified by the user.
+ Automatically rate each recipe by their difficulty level.
+ Display more details on each recipe if the user prompts it, such as the ingredients, cooking time,
and difficulty of the recipe
## Installation 
+ **Prerequisites**
- Python 3.x
- MySQL
## Dependencies
- pip install -r requirements.txt

- requirements.txt should include:
* **asttokens**==2.4.0
* **backcall**==0.2.0
* **bcrypt**==4.0.1
* **colorama**==0.4.6
* **decorator**==5.1.1
* **distlib**==0.3.7
* **executing**==2.0.0
* **filelock**==3.12.4
* **ipython**==8.16.1
* **jedi**==0.19.1
* **matplotlib-inline**==0.1.6
* **parso**==0.8.3
* **pickleshare**==0.7.5
* **platformdirs**==3.11.0
* **prompt-toolkit**==3.0.39
* **pure-eval**==0.2.2
* **Pygments**==2.16.1
* **six**==1.16.0
* **stack-data**==0.6.3
* **traitlets**==5.11.2
* **virtualenv**==20.24.5
* **wcwidth**==0.2.8
## Initial Setup
### Make sure you already satisfy the prerequisites!
1. Clone the Repository:
First, clone the project repository from GitHub to your local machine. Use the following command:
```
 git clone https://github.com/YourUsername/YourRepositoryName.git
```
Replace YourUsername and YourRepositoryName with the appropriate GitHub username and repository name.

2. Create a Virtual Environment:
It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate. To create a virtual environment, navigate to the project directory and run:
``` 
python -m venv name-of-venv

```
Replace name-of-venv with your preferred name for the virtual environment.

3. Activate the Virtual Environment:
To activate the virtual environment, use the following command:

On Windows:
```
name-of-venv\Scripts\activate
```
4. Install Dependencies:
With the virtual environment activated, install the project dependencies using:
```
pip install -r requirements.txt
```
5. Set Up the Database (MySQL):
Install MySQL: [link to download MySQL](https://dev.mysql.com/downloads/windows/installer/8.0.html)
And follow the instructions.
Through SQLAlchemy module you will establish a connection with MySQL database in the format mysql://username:password@host/database specifies the database type (MySQL), username, password, host, and database name.
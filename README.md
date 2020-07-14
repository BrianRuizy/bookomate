<h1 align="center">
   <img src="https://raw.githubusercontent.com/Bookomate/bookomate/master/bookomate/static/assets/logo/banner.png" ></br>
   <a href="https://gitter.im/Bookomate/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge">
      <img src="https://img.shields.io/badge/Chat-Gitter-ff69b4.svg?label=Chat&logo=gitter">
   </a>
   <a href="https://travis-ci.com/github/Bookomate/bookomate">
      <img src="https://img.shields.io/travis/TheAlgorithms/Python.svg?label=Travis%20CI&logo=travis">
   </a>
   <a href="https://stats.uptimerobot.com/A9o1Ac9l6L">
      <img alt="Uptime Robot status" src="https://img.shields.io/uptimerobot/status/m785527224-227cbcf616fa62639c11d308?label=UptimeRobot">
    </a>
   <a href="https://github.com/Bookomate/bookomate/blob/master/CONTRIBUTING.md">
      <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3">
   </a>
</h1>


# Bookomate?

- BookOMate aims at simplifying peer-to-peer calendar booking, with an intuitive design and lightning speed functionality. Also, some integration to existing popular calendar apps.
- This project is inspired by Bookomatic project: https://github.com/KalleHallden/BookOmatic and created to be continuously updated and completely open-source. Contributions welcomed :)

Coming soon!

## Installation

### Dependencies

These things will need to be installed before developing BookOMate.
- **PostgreSQL** Is the database used by BookOMate and installation of python dependencies will not work if [PostgreSQL](https://www.postgresql.org/download/) is not installed.
On Mac Postgresql can be installed using brew ```brew install postgresql```. Windows users can install it with the installer ensuring that postgresql is added to the system path.

### Environment Setup

Get the project running, and start coding in just 5 quick steps.

1. [Fork](https://github.com/Bookomate/bookomate/fork) this repository and
   [Clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) to your   local machine. Then  **cd** into the project

   ```bash
   git clone https://github.com/your_username/bookomate.git

   cd bookomate
   ```

2. Create your virtual environment, and activate it.

   ```bash
   python -m venv env

   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure you create file `.env` in the root directory of the project using `.env.template` guide and update the values of corresponding environment variables

   or

    make sure you exported the following environment variables

   For Linux/Mac use:

   ```
   export DEBUG=<True or False>
   export SECRET_KEY='PUT-YOUR-SECRET-KEY-HERE'
   export DATABASE_URL='postgres://USER:PASSWORD@HOST:PORT/DB_NAME'
   ```
   For Windows use:

   ```
   set DEBUG=<True or False>
   set SECRET_KEY='PUT-YOUR-SECRET-KEY-HERE'
   set DATABASE_URL='postgres://USER:PASSWORD@HOST:PORT/DB_NAME'
   ```

5. Migrate your database

   ```bash
   python manage.py migrate
   ```

6. Run local server to verify, and **DONE**!

   ```bash
   python manage.py runserver

   June 06, 2020 - 11:22:23
   Django version 3.0.7, using settings 'core.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```

## Contribution

Read our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.

### Contributors

This project exists thanks to all the people who [contribute](CONTRIBUTING.md)!

[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/0)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/0)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/1)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/1)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/2)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/2)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/3)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/3)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/4)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/4)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/5)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/5)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/6)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/6)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/images/7)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/bookomate/links/7)

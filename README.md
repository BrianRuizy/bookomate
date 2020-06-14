<h1 align="center">
  <img src="https://raw.githubusercontent.com/Bookomate/bookomate/master/assets/banner.png" ></br>
  <a href="https://gitter.im/Bookomate/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge">
        <img src="https://badges.gitter.im/Bookomate/community.svg">
    </a>
    <a href="https://travis-ci.com/github/Bookomate/bookomate">
        <img src="https://travis-ci.com/Bookomate/bookomate.svg?branch=master">
    </a>
</h1>

## What is Bookomate?

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

3. Install dependancies

   ```bash
   pip install -r requirements.txt
   ```

4. Migrate your database

   ```bash
   python manage.py migrate
   ```

5. Run local server to verify, and **DONE**!

   ```bash
   python manage.py runserver

   June 06, 2020 - 11:22:23
   Django version 3.0.7, using settings 'core.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```
## Contribution

Read our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.

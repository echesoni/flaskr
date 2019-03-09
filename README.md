# Flask Blog
This project is a basic blog app. Users will be able to register, log in, create posts, and edit and delete their own posts. I created this project to practice Unit Testing with Python and Flaskr.

## Getting Started
To get this up and running locally, you will need to do three things.
1. Ensure that you have the proper set up
2. Clone the repository
3. Create and activate a virtual environment

<pre>
# Install
git clone <i>remote_repository_url</i>
</pre>

Create a virtual environment:
<pre>
python3 -m venv venv
. venv/bin/activate
</pre>

Or on Windows:
<pre>
py -3 -m venv venv
venv\Scripts\activate/bat
</pre>

Install Flaskr:
<pre>
pip install -e
</pre>

## Run
<pre>
export FLASK_APP=flaskr
flask run
</pre>

Or on windows:
set FLASK_APP=flaskr
flask run

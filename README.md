
persyaratan 
1. virtual env
2. pip
3. python
4. code editor
5. flask
6. postman
7. postgresql
8. web browser

- mkdir nama_project
- cd nama_project

-----berjalan dalam cmd-----


instalasi virtualenv dan setup
- pip install virtualenv
- virtualenv --version 
- virtualenv env atau python -m venv myvenv

beberapa cara activkan env (windows)
- env\Scripts\activate.bat atau myvenv\Scripts\activate.bat

sortcut installation syntac (in env):
pip install -r requirements.txt 

untuk auto membuat requitments.txt
pip3 freeze 

nonactive virtualenv 
-deactivate


-- install flask dan setup --
1. pip install flask
2. flask --version
3. pip install flask-dotenv
4. buat folder bernama app

-- RDBMS --
1. buat databse
2. configurasi .env
3. flask db init
4. buat models init,..
5. flask db migrate -m "comment"
6. flask db upgrade

-- running code -- 
flask run

repo setup
- git clone
- git checkout branctname

- git add .-
- git commit -m "commend"
- git fetch origin bratchname
- git pull origin bratchname
- git push -u origin bratchname

This project about library site for deploying a project you need do this steps:

Go to some directore cd ...

git init 

git clone https://github.com/YODAXYZ/week6.git
  Clone project

pyton3 -m env myenv
    create virtual env
    
source myenv/bin/activate
    start virtual env
    
sudo pip intall -r requirment.txt
    Install necessary package
    
python manage.py makemigrations
    MakeMigration
    
python manage.py migrate
    Migrate data
    
python manage.py createsuperuser
    Create superuser
    
python manage.py runserver
    runserver

After this you need go to admin and create book

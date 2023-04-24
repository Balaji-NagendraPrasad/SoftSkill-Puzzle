# SoftSkill-Puzzle
Soft skills assessed : Problem solving, Time management,Critical Thinking, Decision Making

The Puzzle is similar to the Treasure Hunt game where you need to solve the clues and find the locations.

Here the player has totally 4 lives.and every wrong answer leads to a loss of life and every dead-end leads to loss of life and loss of extra 5 points from the points so earned. The maximum points that canbe earned is 100  

The time taken to solve the Puzzle is noted.

Solution : The puzzle has 6 clues which indicates 6 puzzles and every puzzle has only one solution.

Puzzle1 : Here the player is supposed to find the Secret key to unlock the mysterious box, given a number puzzle whose answer is 145

Puzzle2 : Here the player is supposed to find the distance and direction of his first move where a direction puzzle is included whose answer is direction : East ,               Distance : 1km

Puzzle3 : Now the person is in the junction and he is supposed to choose a path which leads to right location. Given an image puzzle and you are supposed to decrypt             the clue. The correct location is Forest (case insensitive).

Puzzle4 : In the 4th puzzle the clues are quite difficult to decide. Their are totally 3 locations only one location leads to the Treasure other are dead-end                     solution is  : House
The other locations specified in puzzle4 are Cave and River
River leads to an empty Treasury Box which is a dead-end and the player loses extra 5 points and also a life.
Cave leads a treasury box which has to be unlocked using a code The result of the the puzzle is "OFNFTJT" But even it leads to dead-end and person will be redirected back to the Puzzle4 page and also he will lose extra 5 points and also a life.

Puzzle5 : In puzzle5 the player has to find the room where the treasure box exists. Given a Picture clue and the result of that clue is the room number.Solution : 5
the other rooms are haunted rooms leads to loss of points and life
 
Puzzle 6 : In the final puzzle he/she is supposed to find the number code to open the treasure box. Solution is : 214673

Once all the puzzles are solved it leads to the treasure and will display a congratulating message along with the points earned and time taken.

After all The leader board is displayed with player name, points earned and time taken in secs, along with that a grade will be alloted which shows the whether the person has a softskill or not
there are 4 grades namely
OutStanding : score >= 85
Good : score >= 70
Average : score >= 50
Poor : score < 50


If the setup is already done just open the command prompt and navigate to project directory and activate the virtual environment and run following command to run in local host. command is 'python manage.py runserver' 


Steps to setup the project :
Step1 : open command prompt
step2 : verify python installation using command 'python -V'
step3 : upgrade pip command is ' python -m pip install --upgrade pip'
step4 : creating a directory for the project using commands
        cd <directory name>
        mkdir <django_project name>
        cd <django_project name>
 step5 : creating virtual environment using command 'python -m venv venv'
 step6 : Activating virtual environment using command 'venv\Scripts\activate'
 step7 : Installing Django using command 'pip install django'
 step8 : creating django project using command
         django-admin startproject <project_name>
         cd <project_name>
 step9 : runserver using command 'python manage.py runserver'
 
once you are done install mysql workbench and start a new connection then run the following commands in the opened connection.
 step1 : create database puzzle;
 step2 : use puzzle;
 step3 : create table user_info(
         user_id int not null,
         user_name varchar(20),
         email varchar(50),
         password varchar(20),
         primary key(user_id)); 
 step4 : insert into user_info values('10000','balaji','balaji@gmail.com','ufdsjfkncCX');
 step5 : create table scores(
         score_id int not null,
         user_id int,
         score1 int,
         score2 int,
         score3 int,
         score4 int,
         score5 int,
         score6 int,
         negative_score int,
         time_taken int,
         final_score int,
         primary key(score_id),
         constraint fk5 foreign key(user_id) references user_info(user_id) on delete cascade);
 step6 : insert into scores values(1,10000,0,0,0,0,0,0,0,49,0); 
 
 
Now open command prompt and make the migrations using following commands.
 
   python manage.py migrate
   python manage.py makemigrations
 
 
 once migrations are done open visual studio code and load your workspace and in settings.py in databases setup the following
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<name of the database>',
        'USER' : 'root',
        'PASSWORD' : '<Password of the database>',
        'PORT' : 3306,
        'HOST' : '127.0.0.1',
    }
}

 
 
 
 
 
         

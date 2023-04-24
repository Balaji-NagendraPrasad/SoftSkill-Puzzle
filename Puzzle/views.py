from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import time


cursor = connection.cursor()

global flag
flag=0
global set
set=0
global signin
global player_lives 
global score
score=0
global hidden
hidden=0
global neg_score
neg_score = 0
global score_id
global start_time
global end_time



def welcome(request):
    global signin
    signin = False
    return render(request,'welcome.html')

def admin1(request):
    return render(request,'Admin1.html')

def adminoptions(request):
    global flag
    global set
    admin=request.POST.get('username','default')
    password=request.POST.get('password','default')
    if (admin != "Admin123@gmail.com" or password != 'Admin16@') and flag==0:
        set=1
        R ={'set':set,'alert':"Invalid userid password"}
        return render(request,'Admin1.html',R)
    flag=1
    return render(request,'Adminoptions.html')


def admin2(request):
    option=request.POST.get('admin','default')
    if option == 'Player Details':
        cursor.execute(''' select user_name,email,count(score_id),max(final_score)
        from user_info u,scores s
         where u.user_id=s.user_id
         group by u.user_id
         ''')
        data = cursor.fetchall()
        R={"R":data}
        return render(request,'Admin3.html',R)

    else:
        cursor.execute(''' select user_name,s.*,
        case when final_score >= 85 then 'Outstanding'
        when final_score >=70 then 'Good'
        when final_score >=55 then 'Average'
        else 'Poor' end as grade 
        from user_info u,scores s
        where u.user_id=s.user_id
        order by score_id desc''')
        data = cursor.fetchall()
        print (data)
        R={"R":data}
        return render(request,'Admin2.html',R)

def userlogin(request):
    return render(request,'userlogin.html',{'flag' : 0})


def signin(request):
    global signin
    signin = True
    return render(request,'signin.html',{'set' : 0})

def skillhunt(request):
    global signin
    global score_id
    global start_time
    user_name=request.POST.get('username','default')
    password=request.POST.get('password','default')
    if(signin) : 
        signin = False
        email = request.POST.get('email','default')
        cursor.execute(''' select user_name, password 
                            from user_info 
                            where user_name = %s''',[user_name])
        data = cursor.fetchone()
        if(data != None):
            return render(request,'signin.html',{'alert' : 'user_name already exists choose different one','set' : 1})

        cursor.execute(''' select max(user_id) from user_info; ''')
        user_id = cursor.fetchone()
        user_id = user_id[0] + 1
        cursor.execute(''' insert into user_info values(%s,%s,%s,%s); ''',[user_id,user_name,email,password])    
        return render(request,'userlogin.html',{'response' : 'Signin Successfull!!','flag' : 1})
    else : 
        cursor.execute(''' select user_name, password, user_id 
                            from user_info 
                            where user_name = %s''',[user_name])
        
        data = cursor.fetchone()
        if(data == None) :
            return render(request,'userlogin.html',{'response' : 'Invalid user_name or password','flag' : 1})
        uname = data[0]
        pword = data[1]
        user_id =  data[2]
        if(uname == user_name and pword == password) :
            cursor.execute(''' select max(score_id) from scores; ''')
            score_id = cursor.fetchone()
            score_id = score_id[0] + 1
            cursor.execute(''' insert into scores(score_id,user_id) values(%s,%s); ''',[score_id,user_id])
            start_time = time.time()
            return render(request,'skillhunt.html')
        else :
            return render(request,'userlogin.html',{'response' : 'Invalid user_name or password','flag' : 1})


def step1(request):
    global player_lives
    global score
    global neg_score
    neg_score = 0
    score = 0
    player_lives = 4
    return render(request,'step1.html',{'life' : player_lives})

def step2(request):
    secretkey = request.POST.get('secretkey','0')
    global player_lives
    global score
    global score_id
    if secretkey == '145':
        lscore=20
        score+=20
        cursor.execute(''' update scores set score1=%s where score_id=%s; ''',[lscore,score_id])
        return render(request,'step2.html',{'life' :player_lives})
    else:
        player_lives -= 1
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score ,'time_taken' : t})
        return render(request,'step1.html',{'response' : 'Invalid secret key you lost a life ','flag' : 1 , 'life' :player_lives})

def step3(request):
    dir = request.POST.get('direction','default')
    dist = request.POST.get('km','0')
    global score
    global player_lives
    global score_id
    if dir == 'East' and dist =='1':
        lscore = 15
        score+=15
        cursor.execute(''' update scores set score2=%s where score_id=%s; ''',[lscore,score_id])
        return render(request,'step3.html',{'life' : player_lives})
    else:
        player_lives -= 1
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
        return render(request,'step2.html',{'response' : 'Invalid direction or distance you lost a life','flag' : 1,'life':player_lives})


def step4(request):
    global hidden
    global score_id
    hidden_message = request.POST.get('message','default')
    global score
    global player_lives
    if hidden == 1 and player_lives > 0:
        hidden = 0
        return render(request,'step4.html',{'life' : player_lives})
    elif hidden ==1 and player_lives == 0:
        end_time = time.time()
        time_lapsed = end_time - start_time
        t= round(time_lapsed,0)
        cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
        return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
    if hidden_message.lower() == 'forest':
        lscore = 15
        score += 15
        cursor.execute(''' update scores set score3=%s where score_id=%s; ''',[lscore,score_id])
        return render(request,'step4.html',{'life' : player_lives})
    else :
        player_lives -= 1
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_take=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
        return render(request,'step3.html',{'response' : 'Invalid Location you lost a life','flag' : 1,'life' : player_lives})

def step5(request):
    global score
    global player_lives
    global hidden
    global neg_score
    global score_id
    location = request.POST.get('location','default')
    if hidden == 1 and player_lives>0:
        return render(request,'step5.html',{'life' : player_lives})
    elif hidden == 1 and player_lives == 0:
        end_time = time.time()
        time_lapsed = end_time - start_time
        t= round(time_lapsed,0)
        cursor.execute(''' update scores set final_score=%s,time_take=%s where score_id=%s; ''',[score,t,score_id])
        return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
    if location == 'River':
        neg_score +=5
        score-=5
        cursor.execute(''' update scores set negative_score=%s where score_id=%s; ''',[neg_score,score_id])
        player_lives-=1
        hidden=1
        return render(request,'river.html')
    elif location == 'Cave':
        return render(request,'cave.html',{'life' : player_lives})
    else:
        lscore = 20
        cursor.execute(''' update scores set score4=%s where score_id=%s; ''',[lscore,score_id])
        score += 20
        return render(request,'step5.html',{'life' : player_lives})


def cave(request):
    secretcode = request.POST.get('code','default')
    global player_lives
    global hidden
    global score
    global neg_score
    global score_id
    if secretcode == 'OFNFTJT':
        hidden=1
        neg_score += 5
        player_lives-=1
        score -=5
        cursor.execute(''' update scores set negative_score=%s where score_id=%s; ''',[neg_score,score_id])
        return render(request,'caveend.html')
    else:
        player_lives -= 1
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
        return render(request,'cave.html',{'response' : 'Invalid secret code you lost a life','flag' : 1,'life' : player_lives})
    

def step6(request):
    global player_lives
    global score
    global hidden
    global neg_score
    global score_id
    room_no = request.POST.get('room','default')
    if room_no == '5':
        lscore = 15
        score += 15
        cursor.execute(''' update scores set score5=%s where score_id=%s; ''',[lscore,score_id])
        return render(request,'step6.html',{'life' : player_lives})
    else:
        player_lives -= 1
        hidden = 1 
        neg_score += 5
        score -=5
        cursor.execute(''' update scores set negative_score=%s where score_id=%s; ''',[neg_score,score_id])
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
        return render(request,'devil.html',{'response' : 'Invalid Room_no you lost a life','flag' : 1})
    

def step7(request):
    global player_lives
    global score
    global score_id
    global end_time
    code = request.POST.get('num','default')
    if code == '214673':
        lscore = 15
        score += 15
        end_time = time.time()
        time_lapsed = end_time - start_time
        t= round(time_lapsed,0)
        cursor.execute(''' update scores set score6=%s, final_score=%s,time_taken=%s where score_id=%s; ''',[lscore,score,t,score_id])
        return render(request,'step7.html',{'life' : player_lives , 'points' : score, 'time_taken' : t})
    else:
        player_lives -= 1
        if(player_lives == 0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            t= round(time_lapsed,0)
            cursor.execute(''' update scores set final_score=%s,time_taken=%s where score_id=%s; ''',[score,t,score_id])
            return render(request,'lost_game.html',{'points' : score,'time_taken' : t})
        return render(request,'step6.html',{'response' : 'Invalid Code you lost a life','flag' : 1,'life' : player_lives})

def leaderboard(request):
    cursor.execute(''' select user_name,max(final_score),min(time_taken),
                    case 
                     when max(final_score) >= 85 then 'Outstanding'
                     when max(final_score) >=70 then 'Good'
                     when max(final_score) >=55 then 'Average'
                     else 'Poor' end
                     from scores s,user_info u
                     where s.user_id = u.user_id
                     group by s.user_id ''')
    data = cursor.fetchall()
    R={"R":data}
    return render(request,'leaderboard.html',R)

from flask import Flask, render_template, request, flash,session
from MyPysql import Helper
from face import encoding_images,facerec_from_webcam_faster


app = Flask(__name__)
app.secret_key = '123456'


@app.route('/qiandao')
def qiandao():

    return render_template('location.html')

@app.route('/qiantui')
def qiantui():
    return render_template('location2.html')


@app.route('/daka2')
def daka2():
    uname2=facerec_from_webcam_faster.getdata()
    print(session.get('utname'))
    print(uname2)
    if uname2==session.get('utname'):
        con2=1
        session['con2']=con2


        return  render_template('personal-check.html')
    else:
        return  render_template('personal-check.html')


@app.context_processor
def cin():
    com2=session.get('con2')
    if com2:
        return {'login_com2':com2}
    return{}


@app.route('/daka')
def daka():
    uname=facerec_from_webcam_faster.getdata()
    print(session.get('utname'))
    print(uname)
    if uname==session.get('utname'):
        con=1
        session['con']=con


        return  render_template('personal-check.html')
    else:
        return  render_template('personal-check.html')


@app.context_processor
def cin():
    com=session.get('con')
    if com:
        return {'login_com':com}
    return{}

# 登陆路由
@app.route('/')
def user_login():
    return render_template('login.html')



# 注册路由
@app.route('/uregister')
def user_uregister():
        return render_template('uregister.html')

@app.route('/main-personal')
def main_personal():
    return render_template('main-personal.html')

@app.route('/personal-main')
def personal_main():
    return render_template('personal-main.html')

@app.route('/personal-check')
def personal_check():
    return render_template('personal-check.html')

@app.route('/personal-vocationmanage')
def personal_vocationmange():
    return render_template('personal-vocationmanage.html')

@app.route('/pv-apply')
def pv_apply():
    return render_template('pv-apply.html')

@app.route('/pv-detail')
def pv_detail():
    return render_template('pv-detail.html')

@app.route('/pc-fillcheck')
def pc_fillcheck():
    return render_template('pc-fillcheck.html')

@app.route('/pc-serev')
def pc_serev():
    return render_template('pc-servey.html')

@app.route('/pc-sign')
def pc_sign():
    return render_template('pc-sign.html')





# 注册并验证注册信息
@app.route('/doregister',methods = ['GET','POST'])
def user_doregister():
    name = request.args.get('uname')
    pwd = request.args.get('upwd1')
    phone = request.args.get('uphone')

    print(name, pwd, phone)
    db1 = Helper()
    args = [name, pwd, phone]
    result=db1.select(name)
    if result:
        flash('用户名重复，请重新注册')
        return render_template('uregister.html')
    else:
        db1.add(args)
        return render_template('login.html')




@app.route('/doland')
def user_doland():
    name = request.args.get('user')
    pwd = request.args.get('password')
    db2=Helper()
    result=db2.select(name)
    if result==None:
        flash('无此用户名，请重新输入')
        return render_template('login.html')
    elif result[2]==pwd:
        result2=db2.select2(name)
        session['uname']=name
        session.permanent = True
        session['utel']=result[3]
        if result2!=None:
            session['utname']=result2[2]
            session['uage']=result2[3]
            session['usex']=result2[4]
            session['ubirth']=result2[5]
        else:
            pass


        return render_template('main-personal.html')
    else:
        flash('密码错误，请重新输入')
        return render_template('login.html')






@app.context_processor
def mycontext_processor():
    user=session.get('uname')
    tel=session.get('utel')
    tname=session.get('utname')
    age=session.get('uage')
    sex=session.get('usex')
    birth=session.get('ubirth')
    if user:
        return {'login_user':user,'login_utel':tel,'login_uname':tname,'login_uage':age,'login_usex':sex,'login_ubirth':birth}
    else:
        return {}



@app.route('/logout')
def user_logout():
    session.clear()
    return render_template('login.html')

@app.route('/doupdate')
def user_doupdate():
    return render_template('update.html')

@app.route('/update',methods=['GET','POST'])
def user_update():

     user=request.args.get('username')
     name=request.args.get('truename')
     age=request.args.get('uage')
     sex=request.args.get('usex')
     birth=request.args.get('ubirth')
     db3=Helper()
     args=[user,name,age,sex,birth]
     result=db3.select1(name)
     result3=db3.select2(user)
     if result==None and result3==None:
         db3.add1(args)
         return render_template('main-personal.html')
     elif result3[2]==name :
         db3.update(user,age,sex,birth,name)
         return render_template('main-personal.html')
     else:
         flash('该用户名已被使用，请重新填写用户名')
         return render_template('update.html')






if __name__ == '__main__':
    app.run()
import pymysql

class Helper:
    def add(self,args):
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='db',
            user='root',
            password='180627ds',
            charset='utf8'
        )   #连接数据库
        cs=conn.cursor()#建立游标
        if args==None:
            return 0
        else:
            row=cs.execute('insert into user_register values(null,%s,%s,%s)',args)#执行添加信息语句
        print('影响的行数',row)
        conn.commit()
        return row



    def select(self,id):
        try:
            conn=pymysql.connect(
                host='127.0.0.1',
                port=3306,
                db='db',
                user='root',
                password='180627ds',
                charset='utf8'
            )
            cs=conn.cursor()
            cs.execute("select * from user_register where uname=%s",[id])
            conn.commit()
            result=cs.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if conn != None:
                conn.close()

    def select1(self,id):
        try:
            conn=pymysql.connect(
                host='127.0.0.1',
                port=3306,
                db='db',
                user='root',
                password='180627ds',
                charset='utf8'
            )
            cs=conn.cursor()
            cs.execute("select * from list where utruename=%s",[id])
            conn.commit()
            result=cs.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if conn != None:
                conn.close()


    def select2(self,id):
        try:
            conn=pymysql.connect(
                host='127.0.0.1',
                port=3306,
                db='db',
                user='root',
                password='180627ds',
                charset='utf8'
            )
            cs=conn.cursor()
            cs.execute("select * from list where username=%s",[id])
            conn.commit()
            result=cs.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if conn != None:
                conn.close()


    def add1(self,args):
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='db',
            user='root',
            password='180627ds',
            charset='utf8',
        )   #连接数据库
        cs=conn.cursor()#建立游标

        row=cs.execute('insert into list values(null,%s,%s,%s,%s,%s)',args)#执行添加信息语句
        print('影响的行数',row)
        conn.commit()
        return row


    def update(self,uname,age,sex,birth,tname):
         conn = pymysql.connect(
             host='127.0.0.1',
             port=3306,
             db='db',
             user='root',
             password='180627ds',
             charset='utf8',
         )  # 连接数据库
         cs = conn.cursor()
         cs.execute('update list set username=%s,uage=%s,usex=%s,ubirth=%s where utruename=%s',[uname,age,sex,birth,tname])
         conn.commit()
         return 0

    #  def update_num(self,num):
    #      conn = pymysql.connect(
    #          host='127.0.0.1',
    #          port=3306,
    #          db='db',
    #          user='root',
    #          password='wuy12345',
    #          charset='utf8',
    #      )  # 连接数据库
    #      cs = conn.cursor()
    #      cs.execute('update  user_list set unum=%s, where uid=1',num)
    #      conn.commit()
    #      return 0
    # #
    # def update_age(self,age):
    #     conn = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         db='db',
    #         user='root',
    #         password='wuy12345',
    #         charset='utf8',
    #     )  # 连接数据库
    #     cs = conn.cursor()
    #     cs.execute('update  user_list set uage=%d, where uid=1',age)
    #     conn.commit()
    #     return 0
    #
    #
    # def update_sex(self,sex):
    #     conn = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         db='db',
    #         user='root',
    #         password='wuy12345',
    #         charset='utf8',
    #     )  # 连接数据库
    #     cs = conn.cursor()
    #     cs.execute('update  user_list set usex=%s, where uid=1',sex)
    #     conn.commit()
    #     return 0
    #
    # def update_tel(self,tel):
    #     conn = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         db='db',
    #         user='root',
    #         password='wuy12345',
    #         charset='utf8',
    #     )  # 连接数据库
    #     cs = conn.cursor()
    #     cs.execute('update  user_list set utel=%s, where uid=1',tel)
    #     conn.commit()
    #     return 0
    #
    #
    # def update_birth(self,birth):
    #     conn = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         db='db',
    #         user='root',
    #         password='wuy12345',
    #         charset='utf8',
    #     )  # 连接数据库
    #     cs = conn.cursor()
    #     cs.execute('update  user_list set ubirth=%s, where uid=1',birth)
    #     conn.commit()
    #     return 0



    def join(self):
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='db',
            user='root',
            password='wuy12345',
            charset='utf8'
        )
        cs=conn.cursor()
        cs.execute('select * from user_register full join user_list on user_register.uid = user_list.uid ')
        conn.commit()

    def addlist1(self,name,tel):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='db',
            user='root',
            password='wuy12345',
            charset='utf8'
        )  # 连接数据库
        cs = conn.cursor()  # 建立游标
        cs.execute('insert  into  user_list1  values (null,%s,null ,null ,null ,null,%s ,null )', [name,tel])  # 执行添加信息语句
        conn.commit()



    def update1(self,args,uunaem):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='db',
            user='root',
            password='180627ds',
            charset='utf8'
        )  # 连接数据库
        cs = conn.cursor()  # 建立游标
        cs.execute('update user_list set * where username=uuname',args)  # 执行添加信息语句
        conn.commit()


# def delete():
#         conn=pymysql.connect(
#             host='127.0.0.1',
#             port=3306,
#             db='db',
#             user='root',
#             password='wuy12345',
#             charset='utf8'
#         )
#         cs=conn.cursor()
#         cs.execute('delete from list where uid=2')
#         conn.commit()
#
# delete()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
import mysql.connector
import re



class Chat(App):
    user=[]
    pas=[]
    def build(self):
        self.l6=None
        self.warning = None
        self.window=FloatLayout()
        Window.clearcolor='#D9DFC6'
        #Define database
        mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='password123'
        )
        #Create cursor for Database
        c=mydb.cursor()
        
        #Create an actual DB
        c.execute("CREATE DATABASE IF NOT EXISTS chat_app")
        
        #Check to see if DataBase works
        #c.execute("SHOW DATABASES")
        
        #for db in c:
        #    print(db)
        
        
        #Create a table
        
        c.execute("USE chat_app")
        c.execute("""CREATE TABLE if not exists customers(name VARCHAR(50), password VARCHAR(50))""")
        mydb.commit()
        mydb.close()
        
        '''self.l1=Label(text='[color=638C6D][b]Welcome ![/b]',font_size=70,markup=True,pos_hint={'center_x':0.5,'center_y':0.7})
        self.window.add_widget(self.l1)
        self.login=Button(text='[b]Login[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.55},background_color='#638C6D')
        self.login.bind(on_press=self.login2)
        self.window.add_widget(self.login)
        self.l2=Label(text='[color=638C6D][b]OR[/b]',font_size=45,markup=True,pos_hint={'center_x':0.5,'center_y':0.45})
        self.window.add_widget(self.l2)
        self.signup=Button(text='[b]Sign Up[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.35},background_color='#638C6D')
        self.signup.bind(on_press=self.register)
        self.window.add_widget(self.signup)'''
        
        x=0
        self.backButton=None
        self.l3=None
        self.input1=None
        self.l4=None
        self.input2=None
        self.check=None
        self.l5=None
        self.l7=None
        self.input3=None
        self.signup2=None
        self.l8=None
        self.login3=None
        self.warning=None
        self.front_page(x)
        return self.window
    
    def front_page(self,x):
        if self.backButton: self.window.remove_widget(self.backButton)
        if self.l3: self.window.remove_widget(self.l3)
        if self.input1: self.window.remove_widget(self.input1)
        if self.l4: self.window.remove_widget(self.l4)
        if self.input2: self.window.remove_widget(self.input2)
        if self.check: self.window.remove_widget(self.check)
        if self.l5: self.window.remove_widget(self.l5)
        if self.l7: self.window.remove_widget(self.l7)
        if self.input3: self.window.remove_widget(self.input3)
        if self.signup2: self.window.remove_widget(self.signup2)
        if self.l8: self.window.remove_widget(self.l8)
        if self.login3: self.window.remove_widget(self.login3)
        if self.warning: self.window.remove_widget(self.warning)
        if self.l6: self.window.remove_widget(self.l6)
        self.l1=Label(text='[color=638C6D][b]Welcome ![/b]',font_size=70,markup=True,pos_hint={'center_x':0.5,'center_y':0.7})
        self.window.add_widget(self.l1)
        self.login=Button(text='[b]Login[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.55},background_color='#638C6D')
        self.login.bind(on_press=self.login2)
        self.window.add_widget(self.login)
        self.l2=Label(text='[color=638C6D][b]OR[/b]',font_size=45,markup=True,pos_hint={'center_x':0.5,'center_y':0.45})
        self.window.add_widget(self.l2)
        self.signup=Button(text='[b]Sign Up[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.35},background_color='#638C6D')
        self.signup.bind(on_press=self.register)
        self.window.add_widget(self.signup)    
    
    def register(self,x):
        self.window.remove_widget(self.l1)
        self.window.remove_widget(self.login)
        self.window.remove_widget(self.l2)
        self.window.remove_widget(self.signup)
        self.backButton=Button(text='[b]Back to Signup Page[/b]',markup=True, font_size=20,size_hint=(.18,.05),pos_hint={'center_x':0.1,'center_y':0.9},background_color='#638C6D')
        self.backButton.bind(on_press=self.front_page)
        self.window.add_widget(self.backButton)
        self.l3=Label(text='[color=638C6D][b]Enter Username:[/b]',font_size=45,markup=True,pos_hint={'center_x':0.3,'center_y':0.7})
        self.window.add_widget(self.l3)
        self.input1=TextInput(multiline=False, padding_y=(30,30), size_hint=(0.4, 0.1),pos_hint={"center_x": 0.7, "center_y": 0.7}, font_size=30)
        self.window.add_widget(self.input1)
        self.l4=Label(text='[color=638C6D][b]Enter Password:[/b]',font_size=45,markup=True,pos_hint={'center_x':0.3,'center_y':0.59})
        self.window.add_widget(self.l4)
        self.input2=TextInput(multiline=False, padding_y=(30,30), size_hint=(0.4, 0.1),pos_hint={"center_x": 0.7, "center_y": 0.57}, font_size=30, password=True)
        self.window.add_widget(self.input2)
        self.check = CheckBox(size_hint=(0.1,0.1),pos_hint={"center_x": 0.51, "center_y": 0.49},color='#000000')
        self.check.bind(active=self.on_checkbox_active)
        self.window.add_widget(self.check)
        self.l5=Label(text='[color=000000]Show Password',font_size=25,markup=True,pos_hint={'center_x':0.6,'center_y':0.49})
        self.window.add_widget(self.l5)
        self.l7=Label(text='[color=638C6D][b]Re-Enter Password:[/b]',font_size=45,markup=True,pos_hint={'center_x':0.3,'center_y':0.41})
        self.window.add_widget(self.l7)
        self.input3=TextInput(multiline=False, padding_y=(30,30), size_hint=(0.4, 0.1),pos_hint={"center_x": 0.7, "center_y": 0.39}, font_size=30, password=True)
        self.window.add_widget(self.input3)
        self.signup2=Button(text='[b]Signup[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.1},background_color='#638C6D')
        self.signup2.bind(on_press=self.sign)
        self.window.add_widget(self.signup2)
        self.l8=Label(text='[color=4C585B]-Username must contain only alphabets & numbers\n-Username length must be greater than 3 and less than 11\n-Password length must be greater than 5 and less than 13\n-Password must contain atleast 1 uppercase letter, 1 lowercase letter,\n1 digit and atleast one of these characters {!,@,#,$,%,^,&,*}',font_size=16,markup=True,pos_hint={'center_x':0.22,'center_y':0.21})
        self.window.add_widget(self.l8)
    
    def login2(self,x):
        self.window.remove_widget(self.l1)
        self.window.remove_widget(self.login)
        self.window.remove_widget(self.l2)
        self.window.remove_widget(self.signup)
        if self.backButton: self.window.remove_widget(self.backButton)
        if self.l3: self.window.remove_widget(self.l3)
        if self.input1: self.window.remove_widget(self.input1)
        if self.l4: self.window.remove_widget(self.l4)
        if self.input2: self.window.remove_widget(self.input2)
        if self.check: self.window.remove_widget(self.check)
        if self.l5: self.window.remove_widget(self.l5)
        if self.l7: self.window.remove_widget(self.l7)
        if self.input3: self.window.remove_widget(self.input3)
        if self.signup2: self.window.remove_widget(self.signup2)
        if self.l8: self.window.remove_widget(self.l8)
        if self.login3: self.window.remove_widget(self.login3)
        if self.warning: self.window.remove_widget(self.warning)
        self.backButton=Button(text='[b]Back to Signup Page[/b]',markup=True, font_size=20,size_hint=(.18,.05),pos_hint={'center_x':0.1,'center_y':0.9},background_color='#638C6D')
        self.backButton.bind(on_press=self.front_page)
        self.window.add_widget(self.backButton)
        self.l3=Label(text='[color=638C6D][b]Enter Username:[/b]',font_size=45,markup=True,pos_hint={'center_x':0.3,'center_y':0.7})
        self.window.add_widget(self.l3)
        self.input1=TextInput(multiline=False, padding_y=(30,30), size_hint=(0.4, 0.1),pos_hint={"center_x": 0.7, "center_y": 0.7}, font_size=30)
        self.window.add_widget(self.input1)
        self.l4=Label(text='[color=638C6D][b]Enter Password:[/b]',font_size=45,markup=True,pos_hint={'center_x':0.3,'center_y':0.59})
        self.window.add_widget(self.l4)
        self.input2=TextInput(multiline=False, padding_y=(30,30), size_hint=(0.4, 0.1),pos_hint={"center_x": 0.7, "center_y": 0.57}, font_size=30, password=True)
        self.window.add_widget(self.input2)
        self.check = CheckBox(size_hint=(0.1,0.1),pos_hint={"center_x": 0.51, "center_y": 0.49},color='#000000')
        self.check.bind(active=self.on_checkbox_active)
        self.window.add_widget(self.check)
        self.l5=Label(text='[color=000000]Show Password',font_size=25,markup=True,pos_hint={'center_x':0.6,'center_y':0.49})
        self.window.add_widget(self.l5)
        self.login3=Button(text='[b]Login[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.1},background_color='#638C6D')
        self.login3.bind(on_press=self.log)
        self.window.add_widget(self.login3)
        
    def on_checkbox_active(self,check,value):
        if value:
            self.input2.password=False
        else:
            self.input2.password=True
            
    def sign(self,x):
        flag1=0
        flag2=0
        if len(self.input1.text)==0:
            if self.warning: self.window.remove_widget(self.warning)
            self.warning=Label(text='[color=FF0000]Username is empty ! Please Try Again',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.warning)
            flag1=1
            flag2=1
        elif len(self.input2.text)==0:
            if self.warning: self.window.remove_widget(self.warning)
            self.warning=Label(text='[color=FF0000]Password is empty ! Please Try Again',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.warning)
            flag1=1
            flag2=1
        elif len(self.input3.text)==0:
            if self.warning: self.window.remove_widget(self.warning)
            self.warning=Label(text='[color=FF0000]Please Re-enter the password',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.warning)
            flag1=1
            flag2=1
        else:
            if len(self.input1.text)>=4 and len(self.input1.text)<=10 and len(self.input2.text)>=6 and len(self.input2.text)<=12:
                for i in range(len(self.input1.text)):
                    if self.input1.text[i].isalpha()==True:
                        continue
                    elif self.input1.text[i].isdigit()==True:
                        continue
                    elif self.input1.text[i]=='_':
                        continue
                    else:
                        flag1=1
                        break
                lc=0
                uc=0
                sc=0
                num=0
                sp_ch=['!','@','#','$','%','^','&','*']
                for i in range(len(self.input2.text)):
                    if self.input2.text[i]==" ":
                        flag1=1
                        break
                    elif re.search("[a-z]",self.input2.text[i]):
                        lc=1
                    elif re.search("[A-Z]",self.input2.text[i]):
                        uc=1
                    elif any(char in sp_ch for char in self.input2.text[i]):
                        sc=1
                    elif re.search("[0-9]",self.input2.text[i]):
                        num=1
                if lc==0 or uc==0 or sc==0 or num==0:
                    flag1=1
            else:
                flag1=1 
        if flag1==1 and flag2==0:
            if self.warning: self.window.remove_widget(self.warning)
            self.warning=Label(text='[color=FF0000]Credentials are not valid ! Please Try Again',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.warning)
        elif flag1==0 and flag2==0:
            if self.input2.text==self.input3.text:
                tmp1=0
                for i in range(len(self.user)):
                    if self.user[i]==self.input1.text:
                        tmp1=1
                        flag1=1
                        break
                #Need to use db query to search username
                if tmp1==1:
                    if self.warning: self.window.remove_widget(self.warning)
                    self.warning=Label(text='[color=FF0000]Username is already taken ! Please Try with a Different one',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
                    self.window.add_widget(self.warning)        
            else:
                flag1=1
                if self.warning: self.window.remove_widget(self.warning)
                self.warning=Label(text='[color=FF0000]Passwords are not matching ! Please Try Again',font_size=30,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
                self.window.add_widget(self.warning)
        if flag1==0 and flag2==0:
            mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='password123',
            database = 'chat_app',
        )
            #Create cursor for Database
            c=mydb.cursor()
            
            #Add a record
            
            sql_command="INSERT INTO customers (name,password) VALUES (%s,%s)"
            values=(self.input1.text,self.input2.text)
          
            c.execute(sql_command,values)
              
            
            #Execute SQL command
            #c.execute(sql_command1,values)
            
            
            #Commit our changes
            mydb.commit()
            
            #Close connection
            mydb.close()
            
            self.user.append(self.input1.text)
            self.pas.append(self.input2.text)
            self.regSuccess()
            
    def regSuccess(self):
        if self.warning: self.window.remove_widget(self.warning)
        if self.backButton: self.window.remove_widget(self.backButton)
        self.window.remove_widget(self.l3)
        self.window.remove_widget(self.input1)
        self.window.remove_widget(self.l4)
        self.window.remove_widget(self.input2)
        self.window.remove_widget(self.check)
        self.window.remove_widget(self.l5)
        self.window.remove_widget(self.l7)
        self.window.remove_widget(self.input3)
        self.window.remove_widget(self.l8)
        self.window.remove_widget(self.signup2)
        self.l3=Label(text='[color=638C6D][b]Account created !!\nStart Chatting Now...[/b]',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.6})
        self.window.add_widget(self.l3)
        self.logout=Button(text='[b]Logout[/b]',markup=True, font_size=30,size_hint=(.1,.07),pos_hint={'center_x':0.5,'center_y':0.45},background_color='#638C6D')
        self.logout.bind(on_press=self.logout2)
        self.window.add_widget(self.logout)
        
    '''def logout2(self,x):
        if self.l3: self.window.remove_widget(self.l3)
        if self.logout: self.window.remove_widget(self.logout)
        if self.l6: self.window.remove_widget(self.l6)
        self.l1=Label(text='[color=638C6D][b]Welcome ![/b]',font_size=70,markup=True,pos_hint={'center_x':0.5,'center_y':0.7})
        self.window.add_widget(self.l1)
        self.login=Button(text='[b]Login[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.55},background_color='#638C6D')
        self.login.bind(on_press=self.login2)
        self.window.add_widget(self.login)
        self.l2=Label(text='[color=638C6D][b]OR[/b]',font_size=45,markup=True,pos_hint={'center_x':0.5,'center_y':0.45})
        self.window.add_widget(self.l2)
        self.signup=Button(text='[b]Sign Up[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.35},background_color='#638C6D')
        self.signup.bind(on_press=self.register)
        self.window.add_widget(self.signup)'''
        
    def log(self,x):
        tmp3=0
        tmp4=0
        if self.input1.text=="":
            self.l6=Label(text='[color=FF0000]Username is empty !',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.l6)
        elif self.input2.text=="":
            if self.l6: self.window.remove_widget(self.l6)
            self.l6=Label(text='[color=FF0000]Password is empty !',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
            self.window.add_widget(self.l6)
        else:
            for i in range(len(self.user)):
                if self.user[i]==self.input1.text:
                    tmp3=1
                    x=i
                    break
            if tmp3==0:
                if self.l6: self.window.remove_widget(self.l6)
                self.l6=Label(text='[color=FF0000]Username is not registered. Please sign in first.',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
                self.window.add_widget(self.l6)
            else:
                if self.pas[x]==self.input2.text:
                    tmp4=1
                if tmp4==0:
                    if self.l6: self.window.remove_widget(self.l6)
                    self.l6=Label(text='[color=FF0000]Wrong Password. Please try again.',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.30})
                    self.window.add_widget(self.l6)
                else:
                    self.window.remove_widget(self.l3)
                    self.window.remove_widget(self.input1)
                    self.window.remove_widget(self.l4)
                    self.window.remove_widget(self.input2)
                    self.window.remove_widget(self.check)
                    self.window.remove_widget(self.l5)
                    self.window.remove_widget(self.login3)
                    if self.l6: self.window.remove_widget(self.l6)
                    if self.backButton: self.window.remove_widget(self.backButton)
                    self.l6=Label(text='[color=638C6D]Welcome Back!!',font_size=40,markup=True,pos_hint={'center_x':0.5,'center_y':0.4})
                    self.window.add_widget(self.l6)
                    self.logout=Button(text='[b]Logout[/b]',markup=True, font_size=30,size_hint=(.1,.07),pos_hint={'center_x':0.5,'center_y':0.45},background_color='#638C6D')
                    self.logout.bind(on_press=self.logout2)
                    self.window.add_widget(self.logout)
                
    def logout2(self,x):
        if self.l3: self.window.remove_widget(self.l3)
        if self.logout: self.window.remove_widget(self.logout)
        if self.l6: self.window.remove_widget(self.l6)
        self.l1=Label(text='[color=638C6D][b]Welcome ![/b]',font_size=70,markup=True,pos_hint={'center_x':0.5,'center_y':0.7})
        self.window.add_widget(self.l1)
        self.login=Button(text='[b]Login[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.55},background_color='#638C6D')
        self.login.bind(on_press=self.login2)
        self.window.add_widget(self.login)
        self.l2=Label(text='[color=638C6D][b]OR[/b]',font_size=45,markup=True,pos_hint={'center_x':0.5,'center_y':0.45})
        self.window.add_widget(self.l2)
        self.signup=Button(text='[b]Sign Up[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.35},background_color='#638C6D')
        self.signup.bind(on_press=self.register)
        self.window.add_widget(self.signup)
        
if __name__=="__main__":
    Chat().run()
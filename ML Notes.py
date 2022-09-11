#!/usr/bin/env python
# coding: utf-8

# # My M/c Learning Journey Start

# In[ ]:





# In[ ]:




-Python is a High level programming language.
-Python has derived properties from C & java,
  C is Procedure based  language {example of opening a lock}.
  java is Object based language {*Class  -blueprint from which object are constructed (attribute + function)
                                 *Object -object exist physically }
-Python is "dynamically typed" language. {auto understandable( no need to define int.,float,char e.t.c) }
-Python is interpreted language.
  (python program) -> [ (python compiler) ->   pyc Files  -> (Python Interpretor) ] -> Low level Lang.
     H.L lang                                  (byte code)    (Pyt. Virtual M/c)
-Python is case sensetive language (a & A is different..)

    
# In[ ]:




-Variable in Python
It allow us to store our data inside memory.
In python variables are LABELS not as MEMORY LOCATION 
In Variables: 1. variables can have a-z,A-Z,NUMBERS and only one special character..> underscore { _ }.
              2. variables name can not start with numbers             
# BEST PRACTICES
 1.keep variables name in small latter.
 2.variables name should be meaningful.
 3.For longer, two words should be separated by underscore.
# In[8]:


# COMMENT 
# THIS IS ONE LINE CMNT
""""
THIS IS MULTI LINE
COMMENT WITH USING OF DOUBLE COMMA.

"""
#BUT AFTER THIS CMNT (STRING) ,SOME CODE SHOULD BE WRITTEN.

""""
THIS IS MULTI LINE
COMMENT WITH USING OF DOUBLE COMMA.

"""
print('some code should be written')

DATA TYPES

 1.premitive builts in 
 2.complex
 
PREMITIVE 
 1.number
 2.float (decimal no.)
 3.boolean (true/false with use of if/else & while loop)  *Interrupt is used for infinite loop
 STRING

 a string is nothing but character & sequence of character.
 For one line string...." 1s " or '1s' .
 For multiLine string... """ MS """ or ''' Ms ''' .
  {my = 323 is integer but my = "323" is STRING.}

# In[1]:


my = 'python's class'


# In[2]:


my = "python's class"


# In[3]:


my = 'python"s class'


# In[4]:


my = 'python\'s class'


# In[5]:


my = "i am adeeb khan\nfrom azamgarh"


# In[6]:


print(my)

PYTHON INDEXING
 python indexing is a way to refer the individual elements of an iterable by its position as PYTHON IS 0 INDEX LANGUAGE.
 
# In[7]:


my = 'adeeb khan'


# In[8]:


my[0]


# In[9]:


my[6]


# In[10]:


len(my)


# In[11]:


for i in my:
     print('BRAND')


# In[12]:


for i in my:
    print(i)

string[start index : end index :step index]
# In[27]:


my[0:4]


# In[28]:


my[0:]


# In[29]:


my[:]


# In[30]:


my[0:4:1]


# In[31]:


my[0:4:2]


# In[32]:


my[::2]


# In[33]:


my[-4:-1]


# In[34]:


my[-4:]


# In[35]:


my[::-1]


# In[36]:


my[::-2]


# In[37]:


my[:-4:-2]


# In[38]:


my[:-4:-1]


# In[39]:


my[:-5:-1]


# In[40]:


my[-5:-1:-1]


# In[41]:


my[-5:-1:1]

INPUT FUNCTION
-we can take input as 'input()'
# In[5]:


age = input("plz enter your age > ")


# In[6]:


age


# In[7]:


type(age)


# In[8]:


age= int(input("plz enter your age > "))


# In[9]:


age


# In[10]:


type(age)

*string can't be multiply with float
*string multiply by int..it print two times that no. like..
# In[1]:


"A"*2


# In[2]:


"a"*1.5


# In[11]:


"adeeb">"Adeeb"

*it consider ASCII value of character of string
# In[13]:


ord("a")


# In[14]:


ord("A")

CONCATENTATION OPERATION IN STRING
-It is usd for combining two string like.. 
# In[18]:


first_name="Adeeb"
last_name="Khan"


# In[19]:


+


# In[20]:


first_name="Adeeb"
last_name="Khan"


# In[21]:


first_name+last_name


# In[22]:


first_name+" "+last_name

IN AND NOT IN OPERATORS
# In[23]:


message="you won a lottery  of 1 cr."


# In[24]:


"won a lottery" in message


# In[25]:


"done a lottery" in message


# In[29]:


if "won a lottery" in message:
    print("its may be spam!")
else :
    print("you're safe!")


# In[30]:


"won a lottery"not in message


# In[3]:


#FORMATTED  STRING
  s1="hey my age is %d & my name is adeeb"%20


# In[4]:


print(s1)


# In[34]:


name= input("your name > ")
age= input("your age > ")


# In[35]:


print(age)


# In[36]:


type(age)


# In[8]:


name= input("your name > ")
age= input("your age in numeric form > ")


# In[9]:


s2=f"hey my age is {age} & my name is {name}"


# In[10]:


print(s2)


# In[46]:


s3="hey my age is {} & my name is {}".format(age,name)


# In[47]:


print(s3)


# In[49]:


s4="hey my age is {1} & my name is {0}".format(name,age)


# In[50]:


print(s4)


# In[12]:


s5="hey my age is "+age+ " and my name is "+name


# In[13]:


print(s5)


# In[5]:


name=(input("hey plz enter your name : "))
exp=float(input("hey plz enter your association with organisation in year : "))
total_experience=float(input("hey plz enter the total experience in years : "))
age=float(input("hey plz enter your age : "))
current_salary=float(input("plz enter your current salary : "))

revised_salary= current_salary + 2*exp + 0.5*total_experience - 0.5*age
print("Hey {}, congrats ! for your {} years contribution in organisation and your revised salary is {}".format(name,exp,revised_salary))


# In[6]:


def salary():
    name=(input("hey plz enter your name : "))
    exp=float(input("hey plz enter your association with organisation in year : "))
    total_experience=float(input("hey plz enter the total experience in years : "))
    age=float(input("hey plz enter your age : "))
    current_salary=float(input("plz enter your current salary : "))

    revised_salary= current_salary + 2*exp + 0.5*total_experience - 0.5*age
    print("Hey {}, congrats ! for your {} years contribution in organisation and your revised salary is {}".format(name,exp,revised_salary))


# In[7]:


salary()


# In[8]:


#string methods


# In[9]:


a=32


# In[10]:


type(a)


# In[11]:


s="Adeeb khan"


# In[14]:


type(s)


# In[15]:


s


# In[17]:


s.capitalize()


# In[18]:


s.capitalize()


# In[19]:


s.lower()


# In[23]:


s.split(" ")


# In[24]:


s.title()


# In[25]:


s.casefold() #it's ised for lowering the case but it is powerful than lower case function


# In[33]:


x='beta'


# In[34]:


x.casefold()


# In[41]:


massage='hello buddy you seems upset...i have a lucrative offer for you !'


# In[45]:


Massage=massage.casefold()


# In[46]:


if  "lucrative offer" in massage:
    print("this massage is to attract you")


# In[50]:


s="praveer,utkarsh,adeeb,prabhakar"


# In[52]:


s[0:7]


# In[53]:


s.split(",")


# In[56]:


s.encode(encoding='utf-8' errors='a')


# In[1]:


s="hey how are you"


# In[2]:


s.split()


# In[3]:


x=s.split()


# In[4]:


x[0]


# In[6]:


for i in x:
    print(i)


# In[7]:


s.split(sep=None , maxsplit=2)


# In[8]:


s="praveer,utkarsh,adeeb,prabhakar"


# In[10]:


s.split(",")[2]


# In[12]:


x="praveer,utkarsh,adeeb,prabhakar"


# In[13]:


x.split(',')

x[2] are 'string' but x is 'list' 
# In[16]:


x.split(",")[2][1]


# In[17]:


x.split(",")[2][1:]


# In[22]:


x.rsplit(sep=',' , maxsplit=1 )


# In[28]:


s="**python**"
"*"+"*"+"python"+"*"+"*"


# In[30]:


s.center(10,*)


# In[31]:


s="python programming"


# In[ ]:


s.count()


# In[32]:


s.count("p")


# In[33]:


s.count("py")


# In[34]:


s.count("p",1)


# In[35]:


s


# In[36]:


s.endswith("ing")


# In[37]:


s.endswith("bing")


# In[39]:


s.endswith("n",0,6)


# In[40]:


password="*123@adeek?*123@456gmail"


# In[41]:


password.endswith("123@45",12,18)


# In[42]:


s


# In[45]:


s.startswith('p',7)


# In[46]:


s.find("th")


# In[49]:


s.find("p",1)


# In[50]:


s.find("bye") # -1 means it is not exist


# In[51]:


s.index("zr") #works like s.find but it will stop execution
print("true")


# In[54]:


if "zr" in s:
    print(s.index("zr"))
else:
        print("it is not exist in 's'")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


#replace method
s="python programming"


# In[2]:


s


# In[3]:


s.replace("p","z")


# In[5]:


s.replace("p","z",1)


# In[4]:


s.replace("pr","zr")


# In[6]:


s.islower()


# In[7]:


s.isupper()

#Arithmatic operation

+,-,*,/,//(floor or integer)
# In[8]:


5+4


# In[9]:


"5"+"4"


# In[10]:


5*4


# In[11]:


5/4


# In[12]:


5//4


# In[13]:


4%2


# In[14]:


round(2.5)


# In[15]:


round(2.7)


# In[16]:


abs(-3.6)


# In[3]:


import math


# In[5]:


math.ceil(4/3)


# In[19]:


4/3


# In[23]:


math.factorial(4)


# In[24]:


math.floor(3.7)

Operator precedence
1.paranthesis
2.exponentiation
3.multipli. and div.
4.add and div
# In[25]:


5/3


# In[26]:


2**3


# In[27]:


10+5/3-2**3


# In[ ]:


10+5/3-8


# In[ ]:


10+1.66-8


# In[28]:


11.66-8


# In[29]:


#Conditional statement


# In[30]:


if expression (true/false):
    statement 1
    statement 2
statement 3


# In[34]:


a=12
b=13


# In[37]:


if a==b:
    print("equal/same")
else:
        print("not equal or same")
print(a,b)


# In[6]:


if 0:
    print("hello")


# In[7]:


if None:
    print("no print")


# In[8]:


if "0":
    print("string will be print")


# In[42]:


#nested if


# In[ ]:


if expression 1:
    s1
    s2
elif expression 2:
    s3
    s4
elif expression 3:
    s5
    s6
else :
    s7


# In[53]:


temp=5


# In[61]:


temp=int(input("enter the temperature :"))
if temp>30:
    print("TURN ON THE AC")
elif temp in range(20,31):
    print("TURN ON THE FAN")
elif temp>=10:
    print("EVEN FAN IS NOT REQUIRED")
else:
    print("TURN ON THE BLOWER")


# In[ ]:





# In[ ]:





# In[5]:


#relational operator


# In[ ]:


">",">=",!


# In[1]:


#augmented assingment operator


# In[2]:


x=11


# In[3]:


x=x+1


# In[4]:


x


# In[6]:


x=11


# In[7]:


x+=1


# In[8]:


x


# In[9]:


x=x-3


# In[10]:


x


# In[11]:


x-=3


# In[12]:


x


# In[13]:


#loops

1.when we want run our loop for known no. of time....for loop
2.when we want run our loop based on a condition is satisfied...while
# In[ ]:


for loopvsriable in sequence(#string,list[1,2,3.5],range()):
    statement 1
    statement 2


# In[16]:


#SEQUENCE :- an ordered set -- it is a way to store multiple values in an organised and efficient manner 


# In[17]:


s="PYTHON"


# In[18]:


s[0]


# In[19]:


for i in range(10):
    print("hello")


# In[22]:


for character in "python":
    print(character)
    print("hello")


# In[23]:


for i in range(len(s)):
    print(s[i])


# In[27]:


#internally mechanism of for function
s="python"
myit= iter(s)
print(next(myit,))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit,"no more element"))


# In[ ]:


range([start] , end ,[step])


# In[28]:


range(10)


# In[29]:


list(range(10))


# In[30]:


list(range(1,11))


# In[31]:


list(range(1,11,2))


# In[32]:


list(range(10,0,-1))


# In[38]:


list(range(10,1))


# In[43]:


for i in range(6):
    print(i)


# In[1]:


#guess game


# In[2]:


pwd="12345@321"


# In[4]:


for number in range(1,4):
    print("hey this is your attempt no. {}".format(number))
    guess=input("please guess the password : ")
    if guess == pwd:
        print("congrats you succeed")
        break #it will take you out of loop
else:
        print("sorry all attempts are executed")


# In[5]:


fruits=["apple","banana","cherry"]


# In[22]:


for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)


# In[10]:


for fruit in fruits:
    print(fruit[0])


# In[11]:


#nested for loops -- loop inside loop
for x in range(5):
    for y in range(3):
        print("({},{})".format(x,y))


# In[12]:


#while loops -- when we want to execute till a condition is satisfied


# In[ ]:


while condition: #booleann condtn
    statement1
    statement2


# In[18]:


number = 100
while number>0:
    print(number)
    number=number*-1


# In[20]:


number=0
while number<10:
    print("hello")
    number=number+11


# In[42]:


while True:
    command =input("enter your command > ")
    if command=="quit":
        print("thanks for this command")
        break


# In[ ]:


pwd = "adeebkhan"


# In[44]:


attempts = 3
while attempts>0:
    guess= input("please guess the password : ")
    attempts=attempts-1
    if guess==pwd:
        print("congrats you succeeded")
    break
else:
    print("sorry all your attempts are executed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


letter=["a","b","c"]


# In[3]:


print(type(letter))


# In[15]:


letter.append("pra")


# In[16]:


letter


# In[8]:


letter.insert(0,"1")


# In[9]:


letter


# In[10]:


letter.insert(3,"Deed")


# In[11]:


letter


# In[17]:


letter.extend("pra")


# In[18]:


letter


# In[22]:


letter.pop()


# In[23]:


print(letter.pop)


# In[24]:


reverse=[]


# In[105]:


mylist=["a","b","c"]


# In[106]:


mylist.pop(0)


# In[116]:


mylist=["a","b","c","d"]


# In[117]:


for i in mylist:
    print(mylist.pop())


# In[176]:


mylist1=[1,2,3,4,5]


# In[177]:


for i in mylist1:
    print(mylist1.append('a'))
    print(mylist1)


# In[2]:


mylist=[1,2,3,4,5]


# In[4]:


mylist.remove(4)


# In[5]:


mylist


# In[8]:


del mylist[0:2]


# In[9]:


mylist


# In[10]:


mylist.clear()


# In[11]:


mylist


# In[12]:


del mylist


# In[13]:


mylist


# In[14]:


letters=["a","b","c"]


# In[15]:


letters.index("b")


# In[16]:


letters.index("v")


# In[17]:


if "v" in letters:
    print(letters.index("v"))


# In[18]:


#sorting of the list
numbers=[1,5,3,2,4]


# In[19]:


numbers.sort()


# In[20]:


numbers


# In[21]:


numbers.sort(reverse=True)


# In[24]:


numbers


# In[27]:


sorted(numbers,reverse=True)


# In[28]:


items=[("p1",40),("p2",30),("p3",45)]


# In[29]:


items.sort()


# In[30]:


items


# In[9]:


def sort_according_price(t):
    return t[1]


# In[35]:


items.sort(key=sort_a)


# In[36]:


items


# In[38]:


#Anonymous/lambda function----function without name


# In[39]:


def sqr(x):
    return x**2


# In[40]:


a=lambda x:x**2


# In[41]:


a(2)


# In[42]:


f=lambda x,y : x+y


# In[43]:


f(2,5)


# In[49]:


s= lambda x :"even" if x%2==0 else "odd"


# In[50]:


s(17)


# In[46]:


items=[("p1",40),("p2",30),("p3",45)]


# In[47]:


items.sort(key = lambda a:a[1])


# In[48]:


items


# In[51]:


#map function


# In[52]:


mylist=[1,2,3]


# In[53]:


map(sqr,mylist)


# In[54]:


for i in map(sqr,mylist):
    print(i)


# In[55]:


list(map(sqr,mylist))


# In[56]:


list(map(lambda x:x**2,mylist))


# In[57]:


#filter function


# In[58]:


mylist=[4,5,6,7,10,3,1]


# In[ ]:





# In[59]:


def test(x):
    return x>6


# In[60]:


test(6)


# In[ ]:


filter(lambda )


# In[ ]:


#list  comprehension


# In[ ]:





# In[ ]:





# In[1]:


x=[1,2,3,4,5]


# In[2]:


mylist=[2*item for item in x]


# In[3]:


mylist


# In[4]:


x="python"


# In[5]:


mylist1=[item for item in x]


# In[6]:


mylist1


# In[7]:


#zip  function


# In[8]:


ID =[1,2,3]
NAME=["adeeb","utkarsh","khan"]
score=[20,60,50]


# In[9]:


zip(ID,NAME,score)


# In[10]:


list(zip(ID,NAME,score))


# In[ ]:





# In[ ]:





# In[ ]:





# In[11]:


tuple("python")


# In[12]:


s1=(1,2)
s2=(3,4)


# In[13]:


test=s1+s2


# In[14]:


test


# In[15]:


test[0:2]


# In[16]:


#tuple unpacking


# In[17]:


x,y,z,w = test


# In[18]:


y


# In[19]:


w


# In[20]:


x,y,*others = test


# In[21]:


x


# In[22]:


others


# In[23]:


x=10
y=20


# In[25]:


g=(10,20)


# In[26]:


y,x=g


# In[27]:


y,x=x,y


# In[28]:


y


# In[29]:


x


# In[30]:


#tuple is immutable


# In[36]:


t=(1,2,4,5,3,4)


# In[38]:


t.count(4)


# In[39]:


t.index(4)


# In[40]:


t.index(4,3)


# In[50]:


#sets
""""  An ordered collection of unique values"""
s1={1,2,4}
s2={1,4,2}


# In[52]:


s1==s2


# In[53]:


s1 = {1,2,3,3,4,3,5,6,7,6,5,8,2}


# In[54]:


s1


# In[5]:


l1=[1,2,2,3,3,4,4,5,6]
l2=[1,2,3,4,4,3,3,2]


# In[6]:


s1=set(l1)
s2=set(l2)


# In[7]:


list(s1)


# In[9]:


list(s2)


# In[10]:


s={1,2,3,[4,5,6]} #sets can take only immutable 


# In[11]:


s={1,2,{3,4}}


# In[12]:


s=set("adeeb")


# In[13]:


s


# In[14]:


if "a" in s:
    print("available")


# In[17]:


s1={"A","B","C","D"} #roll no. of students who participated in cricket
s2={"B","C","A","F"} ##roll no. of students who participated in soccer


# In[18]:


print(s1|s2)


# In[19]:


#tell me the roll no. of the students who're participating in both
print(s1&s2)


# In[20]:


#participation in one sport only
print(s1^s2)


# In[21]:


#sets are mutable object we can add or remove the element


# In[22]:


s={1,2,3,5,4,6}


# In[23]:


s.add("3")


# In[24]:


s


# In[27]:


s.add((4,6))


# In[28]:


s


# In[35]:


s.remove((4,6)) #if we try to remove anything which is not the member of s...it raise keyerror
                #for prevention from this...use "if" function


# In[34]:


s


# In[36]:


s.update((13,14))


# In[37]:


s


# In[39]:


s1={12,14}


# In[40]:


s1.clear()


# In[41]:


s1


# In[43]:


s1={2,3,4,5,6}


# In[44]:


s.difference(s1)


# In[45]:


s1.difference(s)


# In[46]:


s.difference_update(s1)


# In[49]:


s


# In[50]:


s1={1,4,6,8,0,6,11,67}
s2={2,3,4,5,6}


# In[51]:


s1.symmetric_difference(s2)


# In[52]:


s1.remove(12) #we can use .discard in place of this for avoiding crash


# In[53]:


s1.discard(45)


# In[54]:


s1.isdisjoint(s2)


# In[56]:


s2={4,6,8}


# In[57]:


s2.issubset(s1)


# In[58]:


s1.issuperset(s2)


# In[73]:


s1.pop()


# In[72]:


s1


# In[74]:


#frozen set


# In[75]:


s={1,3,4,5}


# In[76]:


frozen=frozenset(s)


# In[77]:


frozen.


# In[78]:


f=frozenset("adeeb")


# In[79]:


f


# In[80]:


len(s)


# In[81]:


#Dictionaries 


# In[82]:


#it is a collection of key value pair
#it is also known as mapping type


# In[83]:


#keys are imutable but values are mutable


# In[84]:


d={"Apple":20,"Soaps":[5,10],"Roll no":(10,20,30)}


# In[85]:


d


# In[86]:


d["Roll no"]=98


# In[87]:


d


# In[2]:


d1=dict(x=1,y="Adeeb",z=[1,2,3],a=3.3)


# In[3]:


d1


# In[7]:


d1["x"]


# In[26]:


d=dict(x=1,y=2,z=3)


# In[27]:


d


# In[28]:


d["y"]


# In[29]:


d["w"]=5


# In[30]:


d


# In[31]:


d["x"]=5


# In[32]:


d


# In[33]:


del d["w"]


# In[34]:


d


# In[35]:


type(d)


# In[36]:


len(d)


# In[37]:


d


# In[38]:


d=dict(x=1,y=2,z=3)


# In[39]:


d1=d.copy()


# In[40]:


d1


# In[41]:


id(d)


# In[42]:


id(d1)


# In[44]:


d.fromkeys("x")


# In[45]:


l=["a","b","c"]
s=d.fromkeys(l)


# In[46]:


s


# In[48]:


d.get("y","not exist")


# In[49]:


d.get("w","not exist")


# In[50]:


d.items()


# In[53]:


list(d.items())


# In[56]:


for loopvariable in d.items():
    print(loopvariable[1])


# In[57]:


d.keys()


# In[58]:


list(d.keys())


# In[60]:


for loopvariable in d.keys():
    print(loopvariable)


# In[ ]:





# In[61]:


l=[1,2,3]


# In[63]:


dx={item:2*item for item in l}


# In[64]:


dx


# In[65]:


for i in dx.keys():
    print(i+10)


# In[67]:


d.pop("z")


# In[68]:


d


# In[69]:


d.pop("z")


# In[70]:


d.pop("z","not exist")


# In[71]:


d["z"]=3


# In[72]:


d


# In[73]:


d.popitem()


# In[74]:


d


# In[75]:


d.popitem()


# In[84]:


d


# In[85]:


d["y"]=2


# In[86]:


d


# In[87]:


d=dict(x=1,y=2,z=3)


# In[88]:


d


# In[89]:


d.setdefault("x")


# In[91]:


d.setdefault("x",7)


# In[92]:


d.setdefault("w",9)


# In[93]:


d


# In[97]:


d1={"a":56,"b":23}


# In[95]:


d.update(d1)


# In[96]:


d


# In[98]:


d.update(d1)


# In[99]:


d


# In[100]:


d.values()


# In[101]:


for i in d.values():
    print(i)


# In[102]:


for loopvariable in d:
    print(loopvariable)


# In[103]:


d


# In[107]:


d.keys()


# In[110]:


K=list(d.keys())
V=list(d.values())


# In[112]:


K


# In[113]:


V


# In[115]:


V.index(56)


# In[116]:


K[4]


# In[117]:


#Errors


# In[118]:


#create a robus program which should not crash even if user enters something wrong


# In[119]:


while True:
    age=int(input("plz enter your age in numeric form : "))
    if age >=18:
        print("you are eligible")
    else:
        print("Not eligible")


# In[120]:


#Exceptional Handling


# In[ ]:


while True:
    try:
        age=int(input("plz enter your age in numeric form : "))
        if age >=18:
            print("you are eligible")
        else:
            print("Not eligible")
    except ValueError as vs:
        print("plz check your input & re-enter")
        print(vs)


# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


# 1 week lecture left


# In[ ]:





# In[ ]:





# In[2]:


#numpy....> Numeric python


# In[3]:


from array import array #know python typecode


# In[4]:


l=[1,2,3]


# In[5]:


a=array("i",l)


# In[6]:


print(a)


# In[7]:


a[0]


# In[8]:


a[-1]


# In[9]:


b=array("u","adeeb")


# In[10]:


print(b)


# In[11]:


b[0]


# In[12]:


import numpy as np


# In[13]:


mylist=[1,2,3,4]


# In[14]:


a=np.array(mylist)


# In[15]:


a


# In[16]:


a[2]


# In[17]:


a.shape


# In[18]:


mylist1=[[1,2,3,],[4,5,6],[6,7,8]]


# In[19]:


twod=np.array(mylist1)


# In[20]:


twod


# In[21]:


twod.shape            


# In[22]:


twod[0]


# In[23]:


twod[0][2]


# In[24]:


twod[2,2]


# In[25]:


twod[:2,1:]


# In[27]:


twod[1:,1:]


# In[31]:


t=(1,1.2)


# In[32]:


x=np.array(t)


# In[33]:


x


# In[39]:


np.arange(6,19,2)


# In[40]:


np.zeros(3,dtype=int)


# In[42]:


np.zeros((3,3),dtype=int)


# In[43]:


np.ones(3)


# In[48]:


np.eye(5,dtype=int)


# In[52]:


np.linspace(1,50,20)


# In[55]:


#uniform distribution (in which all element has same probability of occurence ) & 
#normal distribution (in which one element has highest distribution)
#mean=0 , std. deviation =1 is std. normal destribution


# In[56]:


np.random.rand(3) #numbers from uniform distribution b/w 0 and 1


# In[57]:


np.random.randn(3) # numbers from std. normal distribution


# In[58]:


np.random.randn(3,3)


# In[61]:


np.random.randint(1,100,10)


# In[62]:


bin(20)


# In[63]:


hex(20)


# In[64]:


def binary():
    a= np.random.randint(1,100)
    result=bin(a)[2:]
    return result


# In[65]:


binary()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


import pandas as pd


# In[7]:


df=pd.read_csv("C:\\Users\\Dll\\Downloads\\sample1.csv")


# In[8]:


df


# In[9]:


df=pd.read_csv("C:\\Users\\Dll\\Downloads\\sample1.csv",header=None)


# In[10]:


df


# In[11]:


df=pd.read_csv('sample2.csv',sep="@")


# In[12]:


#if we consider a row or column alone it is called 'series'.
#if we consider roe and column together it is called 'Data Frame'


# In[13]:


type(df)


# In[14]:


df


# In[21]:


df[["2005"]]


# In[22]:


df2=df[["2005","2006","2007"]]


# In[23]:


df.info()


# In[24]:


df.head


# In[1]:


df._


# In[ ]:





# In[ ]:


# *Long break...complete it positively !


# # KNN 

# In[2]:


#divide the dataset into training and testing
import sklearn


# In[3]:


from sklearn.model_selection import train_test_split


# In[4]:


from sklearn.neighbors import KNeighborsClassifier


# In[5]:


model= KNeighborsClassifier(n_neighbors=3)


# In[6]:


model.fit(x_train,y_train)


# In[7]:


# NOMINAL DATA : WHERE TWXT ITEMS DONT HAVE ANY NUMERIC WIEGHTAGE OR ORDER
# ORDINAL DATA :  WHERE TWXT ITEMS HAVE ANY NUMERIC WIEGHTAGE OR ORDER


# In[ ]:





# In[1]:


#SCALING scaling will bring the data in same range....such that no specific colum has more wietage


# In[ ]:


# 1. Min-Max scaling ...NORMALISATION....values will always lie btw 0 and 1
column ...Xmin=1 ,Xmax=50
1......(1-Xmin)/(Xmax-Xmin)
10....(10-Xmin)/(Xmax-Xmin)
20
30
40
50....
10


# In[ ]:


#2. Standard Scaling..Standardisation...mostly used ..tries 
column ..mean of the column(mu)...10 and Standard Deviation of the column(sigma)...z score=(xi-mean)/std dev
1....z score = (1-mean)/std dev
10
20
30
40
50
10


# In[2]:


from sklearn.preprocessing import StandardScaler


# In[3]:


scaler = StandardScaler()


# In[ ]:


x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# In[ ]:





# In[ ]:





#!/usr/bin/python3
a = "qiuyuehao"
b = 30

print("hello world 2 %s"%(a))

print("name:%s, num:%d"%(a,b))

print("This year {0}, try your best {1}!".format(b, a))

print("{:>8}".format(b))
print("{:0>8}".format(b))
print("{:<8}".format(b))
print("{:.2f}".format(3.1415926))
print("{:o}".format(13))
print("0x{:>6x}".format(53))
print("{:,}".format(123456789))

print("name:{name}, age:0x{age:>6x}".format(name=a, age=b))


c = [a, b, "godlike"]
print("{info[0]} {info[1]} {info[2]}".format(info=c))

c[1]=31
c = (a, b, "godlike")
print("{info[0]} {info[1]} {info[2]}".format(info=c))

c = {"name":"qiuyuehao", "age":30, "job":"software engineer", "tall":"166cm"}
print("{name} is {age} years old now, he is a good {job}, he is not so tall:{tall}".format(**c))

class Member:
    def __init__(self, name, age):
        self.name = name;
        self.age = age

    def __str__(self):
        #  return "this guy is {self.age} years old, named {self.name}".format(self=self)
        return "this guy is %d years old, named %s"%(self.age, self.name)


print(str(Member("qiuyuehao", 30)))

a = "{:s}, you are a 怂货".format("qiuyuehao")
print(a)
#  hello world qiuyuehao
#  This year 30, try your best qiuyuehao!
#  30
#  00000030
#  30
#  3.14
#  15
#  0x    35
#  123,456,789
#  name:qiuyuehao, age:0x    1e
#  qiuyuehao 30 godlike
#  qiuyuehao 30 godlike
#  qiuyuehao is 30 years old now, he is a good software engineer, he is not so tall:166cm
#  this guy is 30 old, named qiuyuehao


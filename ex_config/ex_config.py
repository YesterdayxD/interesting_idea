import configparser

conf = configparser.ConfigParser()
conf.read("a.ini")
name = conf.get('test', 'name')
print(name)
age = conf.get('test', 'age')
print(age)

conf.set('test','sex','male')
sex = conf.get('test', 'sex')
print(sex)
conf.write(open('a.ini','w'))
import pickle,student3
f=open("student.dat", "wb")
s=student3.Student(123,"John",90)
pickle.dump(s,f)
f.close()
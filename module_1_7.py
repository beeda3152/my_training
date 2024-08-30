grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_stud={}
list_stud = list(students)
list_stud.sort()
count_stud = len(list_stud)
for i in range(count_stud):
    count_ball=len(grades[i])
    sum_ball=sum(grades[i])
    dict_stud[list_stud[i]]=sum_ball/count_ball
print(dict_stud)

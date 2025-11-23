# If the marks obtained by a student in five different subjects are input through the keyboard, 
#find out the aggregate marks and percentage marks obtained by the student.
#Assume that the maximum marks that can be obtained by a student in each subject is 100.


# input marks obtained by student in five different subjects


sub1=int(input("enter ur marks :"))

sub2=int(input("enter ur marks :"))

sub3=int(input("enter ur marks :"))

sub4=int(input("enter ur marks :"))

sub5=int(input("enter ur marks :"))


# calculating total,aggregate marks and percentage

total=(sub1+sub2+sub3+sub4+sub5)

agg_mark=total/5

pers= total*100/500

#output
print(f"your aggregate mark is : {agg_mark}")
print(f"persentage is  : {pers}%")

## output:
enter ur marks : 98
enter ur marks : 85
enter ur marks : 45
enter ur marks : 78
enter ur marks : 45
your aggregate mark is : 70.2
persentage is  : 70.2%

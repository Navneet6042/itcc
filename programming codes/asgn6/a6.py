
def student_data(student_name,student_class):
    stdn=["ashwin","monalisa"]
    stdc=[4,11] #all the details of the student is stored correspondingly in the lists
    stdid=[22102021,22102022]
    for i in range(0,len(stdn)):
        if stdn[i]==student_name:
            break
        else :
            
            continue
    print(stdn[i],stdc[i],stdid[i])

student_data("monalisa",11)
grades = ['A','B','F','C','F','A']


def remove_fail(grade):
    return (grade != 'F')

print(list(filter(remove_fail,grades)))

filtered_grades = []

#USING FOR LOOP INSTEAD OF FILTERS:
# for grade in grades:
#     if (grade != 'F'):
#         filtered_grades.append(grade) 
    
# print(filtered_grades) 
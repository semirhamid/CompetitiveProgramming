#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# 1 create an empty array to store the elements
# 2 iterate throught the elements
# 3 if grade less than 38 append it
# 4 else find the next five multiple
# 5 find the difference
# 6 if the difference less than 3 append the next five multiple
# 7 else append the grade

def gradingStudents(grades):
    
    roundedGrade = []
    
    for grade in grades:
      
        if (grade < 38):
            roundedGrade.append(grade)
            
        else:
          # divide by five and add 1 the multiply by five
            nextFiveMultiple = ((grade // 5) + 1) * 5
            difference = nextFiveMultiple - grade
            
            if(difference < 3):
                roundedGrade.append(nextFiveMultiple)
            else:
                roundedGrade.append(grade)
        
    return roundedGrade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

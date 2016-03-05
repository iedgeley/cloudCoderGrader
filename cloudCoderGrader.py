# Takes CSV files output from cloudcoder
# Writes out to a CSV with a grade average appended to each student row

# TO DO:
# - GUI
# - Weighting of problems
# - Variety of output formats

from os import listdir

# VARIABLES
CSV_DIRECTORY = "grades"
OUTPUT_FILE = "averages.csv"



def stripQuotes(s):
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s

# Calculates a mean average, ignoring the first two columns (lname/fname)
def appendAverage(g):
    total = 0.0
    for v in range(2,len(g)):
        total += g[v]
    return g.append(total/(len(g)-2))

# turns the CSV file into a list of students
def fileToList(c):
    f = open(CSV_DIRECTORY + "\\" + c)
    s = []
    for line in f:
        splitLine = line.split(",")
        s.append(splitLine)
    # remove header rows
    s = s[3:]
    f.close()
    return s

def getNameAndGrade(s):
    temp = s[0:2]
    temp.append(s[-1])
    return temp    

# Updates the grades list with a new grade from a problem
def appendToGrades(s):
    found = False
    for g in grades:
        if g[0] == s[0]:
            g.append(s[-1])
            found = True
            break
    if not found:
        grades.append(s)

if __name__ == "__main__":
    files = listdir(CSV_DIRECTORY)
    grades = []
    
    for csv in files:
        students = fileToList(csv)
        for student in students:
            for i in range(len(student)):
                student[i] = stripQuotes(student[i])
            # turn into a float
            student[-1] = float(student[-1][1:-2])
            # get only the name and grade
            student = getNameAndGrade(student)
            # insert into grades
            appendToGrades(student)



    for grade in grades:
        appendAverage(grade)
        print(grade)




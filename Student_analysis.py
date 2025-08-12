roll_nos = []
names = []
ph_marks = []
ch_marks = []
m_marks = []
totals = []
percentages = []
grades = []
results = []
def total() :
    return (s_ph + s_ch + s_m ) 
def percentage() : 
    return (s_total/300)*100
def grade() :
    if s_per >= 90 :
        return "A+"
    elif s_per >= 80 :
        return "A"
    elif s_per >= 70 :
        return "B+"
    elif s_per >= 60 :
        return "B"
    elif s_per >= 50 :
        return "C"
    elif s_per >= 33 :
        return "D"
    else :
        return "F"
def result() :
    if s_grade == "F" :
        return "Fail"
    else :
        return "Pass"
def highest() :
    highest = max(totals)
    h = totals.index(highest)
    return h
def lowest() :
    lowest = min(totals)
    l = totals.index(lowest)
    return l
if __name__ == "__main__" :
    print("Welcome to Student Analysis Program")
    print("You can enter the details of students and get their results, grades, and overall performance.")
    print("To exit the program, type 'Q' when prompted for roll number.")
    """---------------------------------------------------------------------------------------------"""
    while True :
        s_roll = input("""Enter student roll number :""").strip()
        if s_roll.upper() == "Q" :
            print("Exiting the program. Thank you!")
            break
        else :
            roll_nos.append(s_roll)
        s_name = input("Enter student name : ").strip().title()
        names.append(s_name)
        """Enter your marks in various subjects"""
        s_ph = int(input("Enter your marks in Physics : "))
        ph_marks.append(s_ph)
        s_ch = int(input("Enter your marks in Chemistry : "))
        ch_marks.append(s_ch)
        s_m = int(input("Enter your marks in Maths : "))
        m_marks.append(s_m)
        s_total = total()
        totals.append(s_total)
        print(f"{s_name}'s marks : {s_total}/500")
        s_per = percentage()
        percentages.append(s_per)
        print(f"{s_name}'s percentage : {s_per}%")
        s_grade = grade()
        grades.append(s_grade)
        print(f"{s_name}'s grade : {s_grade}")
        s_result = result()
        results.append(s_result)
        print(f"{s_name} {s_result}ed")
        """---------------------------------------------------------------------------------------------"""
        for i in range(len(roll_nos)) :
            print(f"""Roll number : {roll_nos[i]}
    Name : {names[i]}
    {names[i]}'s Total marks : {totals[i]}/300
    {names[i]}'s Percentage : {percentages[i]}%
    {names[i]}'s Grade : {grades[i]}
    {names[i]}'s Overall Result : {results[i]}""")
        if len(grades) > 2 :    
            h = highest()
            l = lowest()
            print(f"Highest grade is {grades[h]} seured by {names[h]}")
            print(f"Lowest grade is {grades[l]} secured by {names[l]}")
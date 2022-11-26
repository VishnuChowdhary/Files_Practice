# Highest score calculating
Students_Scores = input("Input a list of students scores : ").split()
for i in range(0, len(Students_Scores)):
    Students_Scores[i] = int(Students_Scores[i])
print(Students_Scores)

highest_Score = 0
for score in Students_Scores:
    if score > highest_Score:
        highest_Score = score
print(highest_Score)
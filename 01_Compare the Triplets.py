# Complete the compareTriplets function below.
def compareTriplets(a, b):
    d = list(zip(a,b))
    score1 = len(list([1 for i in d if i[0]>i[1]]))
    score2 = len(list([1 for i in d if i[0]<i[1]]))
    return (score1, score2)

print(compareTriplets(list([20,20,30]),list([15,20,35])))

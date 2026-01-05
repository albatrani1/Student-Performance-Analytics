scores = [85, 78, 90, 88]
total = 0
count = len(scores)
for score in scores:
    total = total + score
average = total / count
if average >= 80:
    performance = "Excellent"
elif average >= 60:
    performance = "Good"
else:
    performance = "At Risk"

print(performance)

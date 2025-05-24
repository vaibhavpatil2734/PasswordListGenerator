a = "vaibhav ramchandra patil"
l = []
n = len(a)
count = 0
word = ""
for i in a:
    count = count+1
    if i != " ":
        word = word + i
    if i == " " or count == n:
       l.append(word)
       word="" 

print(l)
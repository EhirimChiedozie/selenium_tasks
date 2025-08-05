with open('password.txt', 'r') as file:
    content = file.readlines()

listPass = []
for i in content:
    i = i.replace('\n', '')    
    listPass.append(i)
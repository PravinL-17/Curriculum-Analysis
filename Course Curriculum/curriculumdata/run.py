for i in range(1,4):
    for j in range(1,9):
        print('''subject'''+str(i)+str(j)+'''=request.POST.get("subject'''+str(i)+str(j)+'''")''')

 
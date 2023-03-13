footballer_nation = open("fn.txt", "a+")
footballer_nation.write("\narao -> brazil")
for footballer in footballer_nation.readlines():
    print(footballer)
footballer_nation.close()


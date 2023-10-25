list = """Calcule tabela verdade das seguintes expressões:
1 ¬(p ^ ¬q)
2 (¬p _ ¬q) _ (¬(q $ p))
3 ¬(p _ q) ^ (p ^ q)
4 ¬p _ (q ^ ¬r )
5 ¬(p _ ¬q) ^ (¬p _ r )
6 p _ q $ ¬(¬p ^ ¬q)
7 ¬(¬p _ ¬q)
8 ¬(p ^ q)
9 p _ (p ^ q)
10 (p ^ q) _ (p ^ q)
11 (p _ q) ^ (p _ q)
12 p ^ q _ r
13 ¬q ! (p _ ¬r )
14 (p _ q) ! (p _ r )
15 (p _ q) $ (p _ r )"""

for c in list:
    if c in "0123456789":
        list = list.replace(c, "")

list = list.replace(" ", "").split("\n")

for i in range(len(list)):
    print('''"''', list[i], '''"''', ",", sep="")

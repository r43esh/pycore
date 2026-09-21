"""
●●○○○○○○○○ 2/10 [int(), exceptions, defaults]
Write safe_int(s, default=0) that returns int(s) or the default. Decide what should happen with
" 42 ", "4_2", "3.0", "0x1f", "" and justify each decision by testing
"""
def safe_int(x,default=3):
    for i in x:
        try:
            print(int(i)," from ",repr(i))
        except ValueError,TypeError:
            print("hiii")
           # print(f"error aa gyiiii at{repr(i)} ",e)
            print(default)
            #continue




x=[42,4_2,3.0,"0x1f",""]
safe_int(x)
"""
Q26 ●●●●●●●○○○ 7/10 [chained assignment]
Compare a = b = [] with a, b = [], []. Then predict x = y = 5; x += 1; print(y). Describe a
realistic bug where the first form hurts you.
"""
ans="""
if we use same assignment for  mutable things then it will be saying same obj ie 
harmful when we want saparate data for both
"""
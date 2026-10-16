"""
Q28 ●●●●●●●○○○ 7/10 [NaN, identity shortcut in containers]
nan = float('nan'). Predict nan == nan, nan in [nan], [nan] == [nan]. Explain each result,
especially the container ones.
"""
ans="""
nan==nan -> false (conventional)
nan in [nan] -> true
[nan] == [nan] -> true
"""
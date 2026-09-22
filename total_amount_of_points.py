def points(games):
#     s=0
#     for x, equal, y in games:
#         if x > y:
#             s+=3
#         elif x == y:
#             s+=1
#         else:
#             s=sb
#     return sb
    return sum([3 if x>y else 1 if x==y else 0 for x, equal, y in games]) 


def open_or_senior(data):
#     output=[]
#     for x in data:
#         if x[0]>=55 and x[1]>7:
#             output.append("Senior")
#         else:
#             output.append("Open")
#     return output

    return ["Senior" if (x[0]>=55) and (x[1]>7) else "Open" for x in data]
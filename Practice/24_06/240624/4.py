# def getJoin(argList,argSep):
#     result = ""
#     index = 0
#     while index<len(argList):
#         result += argList[index]
#         index += 1
#         if index<len(argList):
#             result += argSep
#     return result



# def getJoin(argList,argSep):
#     index = 0
#     result = ""
#     while index<len(argList):
#         result += argList[index]
#         index += 1
#         if index<len(argList):
#             result += argSep
#     return result


def getJoin(argList, separator):
    result = ""
    index = 0
    while index < len(argList):
        result += str(argList[index])
        index += 1
        if index < len(argList):
            result += separator
    return result


print(getJoin([10,20,30,40,50,60],"💛"))
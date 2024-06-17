def wrap_in_tag(argTxt1,argTxt2):
    return f"<{argTxt1}>{argTxt2}<{argTxt1}>"
print(wrap_in_tag("p","hello"))
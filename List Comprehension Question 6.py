s=input("ENTER ANY SENTENCE:")
x=[s[i].upper() if s[i] in ['A','E','I','O','U','a','e','i','o','u'] else s[i].lower() for i in range(len(s))]
c="".join(x)
print(c)                                                                                                                         

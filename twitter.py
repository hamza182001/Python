import re


url=input("URL: ").strip()
matches=re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE) # parenthesis captures the value ?: indicates value will not be captures its for ? this operator


if matches:

    print("Username:", matches.group(1))
    


"""username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url) #re.sub means to subsitute and it return a string its function looks like this re.sub(pattern,repl,string,count=0,flag=0)
print("Username:",username)"""

#additional 
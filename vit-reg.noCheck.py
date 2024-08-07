import re
register= input()
if re.match("^[1-9][0-9][a-zA-Z]{3}[0-9]{4}$",register):
    print("valid")
else:
    print("invalid")

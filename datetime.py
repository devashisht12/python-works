import datetime
a = "Hello"
c= 'Friends'
print(f"Hello Dev today, you look handsome {a} {c}")

today = datetime.datetime.today()

print(f"today's date is {today:%B %d, %Y}")
minutes = int(input())
hours = (minutes // 60) % 24
remain = minutes % 60
print(str(hours) + str(':') + str(remain))

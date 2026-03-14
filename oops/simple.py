class std:
    count=0
    def __init__(self):
        std.count=std.count+1
std1=std()
std2=std()
print(std.count)
print(std1.count)
import os

if(not os.path.exists("data")):
    os.mkdir("data")
    for i in range(0,100):
        os.mkdir(f"data/Day{i+1}")
else:
    for i in range(0,100):
        os.rmdir(f"data/Day{i+1}")
    os.rmdir("data")


print(os.getcwd())
os.chdir("d:\study\Course\python in 100 days - cwh")
print(os.getcwd())
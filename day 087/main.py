import shutil

shutil.copy("main.py","main2.py")

shutil.copytree("org.file","copy.file")

shutil.move("main2.py","copy.file/main2.py")

shutil.rmtree("copy.file")
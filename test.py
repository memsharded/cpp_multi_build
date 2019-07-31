import os, shutil

def run(cmd, ignore_error=False):
    r = os.system(cmd)
    if r != 0 and not ignore_error:
        raise Exception("ERROR Failed: %s" % cmd)

shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")
os.chdir("build")

# The CMake generated solution will only have x64 as Configuration, not x86
run('cmake ../src -G "Visual Studio 15 Win64"')
run('cmake --build . --config Release')
run("Release\\app.exe")
run('cmake --build . --config Debug')
run("Debug\\app.exe")

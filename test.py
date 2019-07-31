import os, shutil
from contextlib import contextmanager

def run(cmd, ignore_error=False):
    r = os.system(cmd)
    if r != 0 and not ignore_error:
        raise Exception("ERROR Failed: %s" % cmd)

@contextmanager
def chdir(newdir):
    os.makedirs(newdir)
    current = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(current)

shutil.rmtree("build", ignore_errors=True)
"""with chdir("build/64"):
    # The CMake generated solution will only have x64 as Configuration, not x86
    run('cmake ../../src -G "Visual Studio 15 Win64"')
    run('cmake --build . --config Release')
    run("Release\\app.exe")
    run('cmake --build . --config Debug')
    run("Debug\\app.exe")

with chdir("build/32"):
    # The CMake generated solution will only have x64 as Configuration, not x86
    run('cmake ../../src -G "Visual Studio 15"')
    run('cmake --build . --config Release')
    run("Release\\app.exe")
    run('cmake --build . --config Debug')
    run("Debug\\app.exe")"""

shutil.rmtree("vs/Debug", ignore_errors=True)
shutil.rmtree("vs/Release", ignore_errors=True)
shutil.rmtree("vs/x64", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/Debug", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/Release", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/x64", ignore_errors=True)
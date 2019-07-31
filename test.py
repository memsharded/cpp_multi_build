import os, shutil
from contextlib import contextmanager

def run(cmd, ignore_error=False):
    r = os.system(cmd)
    if r != 0 and not ignore_error:
        raise Exception("ERROR Failed: %s" % cmd)

@contextmanager
def chdir(newdir):
    if not os.path.isdir(newdir):
        os.makedirs(newdir)
    current = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(current)

shutil.rmtree("build", ignore_errors=True)

for shared in ("ON", "OFF"):
    """with chdir("build/mingw_debug"):
        run('cmake ../../src -G "MinGW Makefiles" & cmake ../../src -G "MinGW Makefiles" '
            '-DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS=%s' % shared)
        run('cmake --build .')
        run("app.exe")

    with chdir("build/mingw_release"):
        run('cmake ../../src -G "MinGW Makefiles" & cmake ../../src -G "MinGW Makefiles" '
            '-DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=%s' % shared)
        run('cmake --build .')
        run("app.exe")"""


    with chdir("build/64"):
        # The CMake generated solution will only have x64 as Configuration, not x86
        run('cmake ../../src -G "Visual Studio 15 Win64" -DBUILD_SHARED_LIBS=%s' % shared)
        run('cmake --build . --config Release')
        run("Release\\app.exe")
        run('cmake --build . --config Debug')
        run("Debug\\app.exe")

    with chdir("build/32"):
        # The CMake generated solution will only have x64 as Configuration, not x86
        run('cmake ../../src -G "Visual Studio 15" -DBUILD_SHARED_LIBS=%s' % shared)
        run('cmake --build . --config Release')
        run("Release\\app.exe")
        run('cmake --build . --config Debug')
        run("Debug\\app.exe")

"""shutil.rmtree("vs/Debug", ignore_errors=True)
shutil.rmtree("vs/Release", ignore_errors=True)
shutil.rmtree("vs/x64", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/Debug", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/Release", ignore_errors=True)
shutil.rmtree("vs/HelloWorld/x64", ignore_errors=True)

run("vs\\Release\\HelloWorld.exe")
run("vs\\Debug\\HelloWorld.exe")
run("vs\\x64\\Release\\HelloWorld.exe")
run("vs\\x64\\Debug\\HelloWorld.exe")"""

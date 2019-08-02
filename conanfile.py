from conans import ConanFile

class Pkg(ConanFile):
    generators = "cmake"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
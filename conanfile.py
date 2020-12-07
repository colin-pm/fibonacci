"""
Conan file responsible for installing dependencies, building, testing, and packaging a project.
conanfile.py docs: https://docs.conan.io/en/latest/reference/conanfile.html
"""

from conans import ConanFile, CMake, tools


class FibonacciConanFile(ConanFile):
    name = "fibonacci"
    version = "0.0.1"
    license = "MIT"
    author = "Colin McAllister <colinmca242@gmail.com>"
    url = "https://github.com/colin-pm/fibonacci"
    description = "Test library for evaluating version control"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [False, True]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "include/*", "src/*", "test/*"

    def build_requirements(self):
        if not tools.cross_building(self.settings):
            self.build_requires("gtest/1.8.1@bincrafters/stable")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['CONAN_SPECIFIED_VERSION'] = "{} version v{}".format(self.name, self.version)
        if tools.cross_building(self.settings):
            cmake.definitions["BUILD_TESTING"] = "NO"
        if not tools.cross_building(self.settings):
            cmake.definitions["CODE_COVERAGE"] = "YES"
            cmake.definitions["CMAKE_BUILD_TYPE"] = "Debug"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def test(self):
        cmake = self._configure_cmake()
        cmake.test(args=['--', 'gtest_output="xml:report.xml"'], output_on_failure=True)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def deploy(self):
        self.copy("*", src="bin", dst="bin")
        self.copy("*", src="sbin", dst="sbin")
        self.copy("*", src="lib", dst="lib")
        self.copy("*", src="include", dst="include")

    def deploy(self):
        self.copy("*", src="bin", dst="bin")
        self.copy("*", src="sbin", dst="sbin")
        self.copy("*", src="lib", dst="lib")
        self.copy("*", src="include", dst="include")


from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeDeps, CMakeToolchain


class CppTemplate(ConanFile):
    name = "CppTemplate"
    version = "1.0"
    package_type = "application"

    license = "MIT"
    author = "Arnor Nolen"
    url = "https://github.com/arnor-nolen"
    description = "C++ template."
    topics = ("C++", "Conan", "Template")

    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*"

    default_options = {"fmt/*:shared": True}

    def requirements(self):
        self.requires("fmt/10.1.1")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.user_presets_path = "ConanPresets.json"
        if self.settings.build_type == "Debug":
            tc.cache_variables = {
                "CMAKE_EXPORT_COMPILE_COMMANDS": "ON",
                "CMAKE_COLOR_DIAGNOSTICS": "ON",
            }
        tc.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain


class CppTemplate(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    default_options = {"fmt/*:shared": True}

    def requirements(self):
        assert self.requires is not None

        self.requires("fmt/10.1.1")

    def generate(self):
        # Configure CMakeToolchain
        tc = CMakeToolchain(self)
        tc.user_presets_path = "ConanPresets.json"
        tc.generate()

    def layout(self):
        cmake_layout(self)

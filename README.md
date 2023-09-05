# cpp-template
C++ template project.

## Dependencies
Dependencies are listed in [conanfile.py](./conanfile.py).

## How to build
```sh
conan install . -s build_type=Debug --build=missing
cmake --workflow --preset debug
```
## How to run
```sh
./build/Debug/bin/cpp-template
```

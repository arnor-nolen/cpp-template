cmake_minimum_required(VERSION 3.21)
project(cpp-template)

# Additional options
#
# Prevent command line window from spawning
#
# ENABLE_CMD_WINDOW=OFF

# Set binary output directories
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/$<0:>)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/$<0:>)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/$<0:>)

# Add to find cmake config dependencies
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

# Setting up dependencies (using CONFIG so find_package doesn't conflict with cmake's own
# findX.cmake)
find_package(fmt REQUIRED CONFIG)

# Set standard (C++20)
set(TARGET_COMPILE_FEATURES cxx_std_20)

# -------------------------------------
# Set compiler-specific stuff
# -------------------------------------

if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")

  add_compile_options(/W4)

  # Prevent command line window from spawning
  if(NOT ENABLE_CMD_WINDOW)
    add_link_options(/SUBSYSTEM:WINDOWS /ENTRY:mainCRTStartup)
  endif()

elseif(CMAKE_CXX_COMPILER_ID STREQUAL "AppleClang")

  add_compile_options(-Wall -Wextra -Wpedantic -Wshadow)

elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR CMAKE_CXX_COMPILER_ID STREQUAL "GNU")

  add_compile_options(-Wall -Wextra -Wpedantic -Wshadow)

else()

  message(WARNING "Unknown compiler, proceeding without additional compiler options")

endif()

# -------------------------------------
# End of compiler-specific stuff
# -------------------------------------

# -------------------------------------
# Building executables
# -------------------------------------

# Build the main app
set(SOURCE_FILES "src/main.cpp" "src/example.cpp")
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_compile_features(${PROJECT_NAME} PUBLIC ${TARGET_COMPILE_FEATURES})

# Add "include" to the include path
target_include_directories(${PROJECT_NAME} PUBLIC include)

# -------------------------------------
# End of building executables
# -------------------------------------

# Link libraries
target_link_libraries(${PROJECT_NAME} fmt::fmt)

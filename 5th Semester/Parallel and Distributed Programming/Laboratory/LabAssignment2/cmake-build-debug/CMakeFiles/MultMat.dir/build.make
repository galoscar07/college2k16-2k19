# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/MultMat.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/MultMat.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MultMat.dir/flags.make

CMakeFiles/MultMat.dir/multmat.cpp.o: CMakeFiles/MultMat.dir/flags.make
CMakeFiles/MultMat.dir/multmat.cpp.o: ../multmat.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MultMat.dir/multmat.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MultMat.dir/multmat.cpp.o -c "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/multmat.cpp"

CMakeFiles/MultMat.dir/multmat.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MultMat.dir/multmat.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/multmat.cpp" > CMakeFiles/MultMat.dir/multmat.cpp.i

CMakeFiles/MultMat.dir/multmat.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MultMat.dir/multmat.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/multmat.cpp" -o CMakeFiles/MultMat.dir/multmat.cpp.s

# Object files for target MultMat
MultMat_OBJECTS = \
"CMakeFiles/MultMat.dir/multmat.cpp.o"

# External object files for target MultMat
MultMat_EXTERNAL_OBJECTS =

MultMat: CMakeFiles/MultMat.dir/multmat.cpp.o
MultMat: CMakeFiles/MultMat.dir/build.make
MultMat: CMakeFiles/MultMat.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable MultMat"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MultMat.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MultMat.dir/build: MultMat

.PHONY : CMakeFiles/MultMat.dir/build

CMakeFiles/MultMat.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MultMat.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MultMat.dir/clean

CMakeFiles/MultMat.dir/depend:
	cd "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2" "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2" "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug" "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug" "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/cmake-build-debug/CMakeFiles/MultMat.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/MultMat.dir/depend


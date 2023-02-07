# makeEspArduino
A makefile for ESP8266 and ESP32 Arduino projects.

The main intent for this project is to provide a minimalistic yet powerful and easy configurable
makefile for projects using the ESP/Arduino framework available at: https://github.com/esp8266/Arduino and https://github.com/espressif/arduino-esp32

Using make instead of the Arduino IDE makes it easier to do more production oriented builds of software projects.

This makefile gives you a command line tool for easy building and loading of the ESP/Arduino examples as well as your own projects.

The makefile can use the ESP/Arduino environment either from the installation within the Arduino IDE or in a separate git clone of the environment. The latter can be useful in project where you want stringent control of the environment version e.g. by using it as a git submodule.

You basically just have to specify your main sketch file and the libraries it uses. The libraries can be from arbitrary directories without any required specific hierarchy or any of the other restrictions which normally apply to builds made from within the Arduino IDE. The makefile will find all involved header and source files automatically. The search is made starting at the main sketch and the recursively continued through all #include statements that are found. All source files found in directories where include files were found will automatically be added to the build.

Rules for building the firmware as well as upload it to the ESP board are provided.

It is also possible to let the makefile generate and upload a complete flash file system based on an arbitrary directory of files.

The intention is to use the makefile as is. Possible specific configuration is done via via makefile variables supplied on the command line or in separate companion makefiles.

The makefile can be used on Linux, Mac OSX, Microsoft Windows (Cygwin or WSL) and OpenBSD.

The actual build commands (compile, link etc.) are extracted from the Arduino description files (platform.txt etc.).

Uploading of the built binary can be made via serial channel (esptool), ota (espota.py) or http (curl). Which method to use is controlled by makefile target selection. By default the serial channel is used.

Configuration files for Visual Studio Code can be generated by this makefile as well.


#### Installing

First make sure that you have the environment installed as described at:  https://github.com/esp8266/Arduino

and

https://github.com/espressif/arduino-esp32

If you don't want to use the environment installed in the Arduino IDE, then you can clone it into a separate directory instead, see below.

Then start cloning the makeEspArduino repository.

    cd ~
    git clone https://github.com/plerup/makeEspArduino.git

After this you can test it. Attach your ESP8266 board and execute the following commands:

    cd makeEspArduino
    make -f makeEspArduino.mk DEMO=1 flash

The DEMO definition makes the the makefile choose a typical demo sketch from the ESP examples.
After this you will have the example downloaded onto in your ESP.

If you want to use a clone of the ESP/Arduino environment instead, then do something like this for esp8266:

    cd ~
    git clone https://github.com/esp8266/Arduino.git esp8266
    cd esp8266

Determine which version you want to use. [See releases.](https://github.com/esp8266/Arduino/releases) Example:

    git checkout tags/3.0.0

Then install the required environment tools by issuing the following commands:

    git submodule update --init
    cd tools
    python3 get.py

Please note that you have to rerun the commands above if you checkout another label or branch in the git.

To test this installation you have to specify the location of the environment when running make

    cd ~/makeEspArduino
    make -f makeEspArduino.mk ESP_ROOT=~/esp8266 DEMO=1 flash

For ESP32 just change esp8266 in the commands above to esp32, i.e:

    cd ~
    git clone https://github.com/espressif/arduino-esp32.git  esp32
    cd esp32
    git submodule update --init
    cd tools
    python3 get.py

When building ESP32 projects the variable CHIP must always be defined, example:

    make -f makeEspArduino.mk ESP_ROOT=~/esp32 CHIP=esp32 DEMO=1 flash

If you want to minimize your typing henceforth then there is a rule in the makefile which can be used to generate shortcut commands in /usr/local/bin. These commands are named **espmake** and **espmake32**. To achieve this when using a git clone type:

    make -f makeEspArduino.mk ESP_ROOT=~/esp8266 install

    make -f makeEspArduino.mk ESP_ROOT=~/esp32 CHIP=esp32 install

Sudo access will be required for this operation.

#### Getting help

A description of all available makefile functions and variables is always available via the following command:

    make -f makeEspArduino.mk help

#### Building projects

You can now use the makefile to build your own sketches or any of the examples in the ESP/Arduino environment. The makefile will automatically search for a sketch in the current directory and build it if found. It is also possible to specify the location of the sketch on the command line.

##### Some examples

In current directory:

    cd ~/.arduino15/packages/esp8266/hardware/esp8266/2.3.0/libraries/Ticker/examples/TickerBasic
    espmake

Explicit naming of a default directory:

    espmake -C ~/.arduino15/packages/esp8266/hardware/esp8266/2.3.0/libraries/Ticker/examples/TickerBasic

Explicit naming of the sketch:

    espmake SKETCH=~/.arduino15/packages/esp8266/hardware/esp8266/2.3.0/libraries/Ticker/examples/TickerBasic/TickerBasic.ino
    # Or like this
    espmake SKETCH="\$(ESP_ROOT)/libraries/Ticker/examples/TickerBasic/TickerBasic.ino"

#### Advanced usage

The makefile has several variables which control the build. There are different ways to change the defaults of these variables.

The simplest and most direct way to do this is by specifying the variables and their values on the command line.

The more permanent way is to create a special makefile with the appropriate values for the variables and then include this in the build. This can be achieved
either by including makeEspArduino.mk in this file or the other way around by letting makeEspArduino.mk include it. The advantage with the latter method is that
the makefile doesn't need to know the location of makeEspArduino.mk, more about this in the examples below.

The most important variables in the makefile are listed below:

**SKETCH** is the path to the main source file. As stated above, if this is missing then makeEspArduino will try to locate it in the current directory.

**LIBS** is a variable which is used to specify your own additional library source or linker archive files. As stated above, makeEspArduino will do an automatic search for header files used by all involved source files in the build. This is achieved by checking for *#include* statements and for each found such statement, search for a corresponding existing header file anywhere in a list of directories. The search is started in the sketch source file and then recursively following any found file which in turn will be searched for new *#include* statements. By default this list contains all the directories underneath the ESP/Arduino *libraries* root and possible standard Arduino libraries, but the list can be extended using this variable.

This way you can specify an additional list of directories which contains header and/or source files that you want to be included in the build. The different entries in the list are separated with space. If an entry contains a path to a directory then that directory and all its sub directories will be included in the search list for header files. If a header file is found in that directory then all source files (*.cpp, *.c, *.S) also found there will be added to the build. This is due to the fact that there is not always a one-to-one relationship between a header file name and the corresponding implementation source file.

It is also possible to specify an explicit source file or a wildcard in a list entry. In that case only the source files matching this will be added and the corresponding directory will added to the header file directory search list.

Library files (.a or .lib) can also be specified here and these will be added to the linker command.

If the sketch is located in an */example/* directory the possible corresponding */src/* directory will automatically be added to the directory search list.

Example:

    LIBS = $(MY_ROOT)/lib1 $(MY_ROOT)/lib2/my_file.cpp $(MY_ROOT)/lib3/*.c $(MY_ROOT)/lib3/my_lib.a

You can always use the rule **list_lib** to check what include directories and source files that was found during the search.

The automatic search for used files via included header files does not work if the corresponding implementation source file are located in another directory than the header file. If you have problem with this, you can set the variable **EXPAND_LIBS** and then all source files in the directories specified via the LIBS variable will be added to the build. This may lead to compiling unnecessary files though.

If you for some reason want to exclude some sub directories from the search list you can specify this using the variable **EXCLUDE_DIRS**. The value is interpreted a regular expressions so multiple directories must be separated with | .

**CHIP** Set to either esp8266 (default) or esp32

**BOARD** The type of ESP8266 or ESP32 board you are using, use the rule **list_boards** to show what's available

**BUILD_DIR** All intermediate build files (object, map files etc.) are stored in a separate directory controlled by this variable. By default this is set to a name consisting of the project and board names. This is just the directory name, the root of this directory is controlled by the variable **BUILD_ROOT**. Default for this is /tmp/mkESP but it can be set to a non-temporary location if so is desired.

**BUILD_EXTRA_FLAGS** this variable can be setup to add additional parameters for the compilation commands. It will be placed last and thereby it is possible to override the preceding default ones.

It is also possible to set file specific compilation parameters by defining a variable which starts with the name of the actual source file followed by the string **_CFLAGS**. Example:

    my_class.cpp_CFLAGS = -DOPTION=1

In this case the parameter -DOPTION=1 will be applied when compiling the file *m_class.cpp*. Please note that just the file name, not the path, should be used.

There are some other important variables which corresponds to the settings which you normally do in the "Tools" menu in the Arduino IDE. The makefile will parse the Arduino IDE configuration files and use the same defaults as you would get when after selecting a board in the "Tools" menu.

The result of the parsing is stored as variables in a separate intermediate makefile named 'arduino.mk' in the directory defined by the variable **BUILD_DIR**. Look into this file if you need to control even more detailed settings variables.

**VERBOSE** Define this variable if you want to trace all the executed operations in the build

As stated above you can always get a description of all makefile operations, configuration variables and their default values via the 'help' function

    espmake help

##### Build time and version information

makeESPArduino will also automatically produce header and c files which contain information about the time when the build (link)
was performed. This file also includes the git descriptions (tag) of the used version of the ESP/Arduino environment and the project source (when applicable).
This can be used by the project source files to provide stringent version information from within the software. The information is put into a global struct
variable named "_BuildInfo" with the following string constant fields:

| Name        | Value |
| ----------- |-------------|
| __src_version__ | Source code git version |
| __date__ | Build date |
| __time__ | Build time |
| __env_version__ | ESP Arduino version |


##### Including the makefile

The easiest way to control the makefile is by defining the desired values of the control variables in your own makefile and then include makeEspArduino.mk. Example:


    # My makefile
    SKETCH = $(ESP_ROOT)/libraries/Ticker/examples/TickerBasic/TickerBasic.ino

    UPLOAD_PORT = /dev/ttyUSB1
    BOARD = esp210

    include $(HOME)/makeEspArduino/makeEspArduino.mk

Another possibility is to do this the other way around, i.e. let makeEspArduino include your makefile instead. This can be achieved by naming
your makefile "config.mk". makeEspArduino will always check for a file with this name in the current directory or in the same directory as the sketch.
If you want to use another name for your makefile you can specify this via the variable PROJ_CONF on the command line. Example of such a makefile:

    # config.mk
    THIS_DIR := $(realpath $(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
    ROOT := $(THIS_DIR)/..
    LIBS =  \
      $(ROOT)/libraries \
      $(ROOT)/ext_lib

    UPLOAD_SPEED = 115200

It is of course also always possible to control the variable values in the makefile by defining them as environment variables in the shell. Example:

    export UPLOAD_PORT=/dev/ttyUSB2

A global config file which will apply to all builds can also be defined. The name of this file is also "config.mk". The location of this file can be defined via the variable **MAKEESPARDUINO_CONFIGS_ROOT** The default value is the OS specific standard config directory, i.e.

    Linux:  $(HOME)/.config/makeEspArduino (or $(XDG_CONFIG_HOME)/makeEspArduino)
    Mac:    $(HOME)/Library/makeEspArduino
    CygWin: $(LOCALAPPDATA)/makeEspArduino

Please note that the local config file can always override definitions in the global one.


#### Flash operations for esp8266

Recent versions of esp8266 and esp32 Arduino includes the **esptool** Python script for flashing operations. This script is stored in the tools subdirectory of the repo structure. For esp8266 a Python3 executable (or symblink) is also included here. These are used by makeEspArduino during the build. A special wrapper script is used to avoid the need for explicit installation of the Python modules.

Esptool does however depend on the pyserial module which is also included in the tools directory for esp8266. This is (currently) not the case for esp32 so here you have to install it manually in your system via

    pip3 install pyserial

The used serial port for the flashing operations is controlled by the variable **UPLOAD_PORT**. If not explicitly specified then makeEspArduino tries to find a suitable one. The pattern used for this search is depending on the actual operating system.

The baud rate used is controlled by the variable **UPLOAD_SPEED**. The maximum possible speed may vary between boards and operations. The default is taken from the first value in the board definition and is usually quite low. You can normally increase this but the maximum speed 921600 may or may not work. You have to test out the maximum possible value for your board. The typical error message for too high speed is:

    Invalid head of packet

#### Building a file system

There are also rules in the makefile which can be used for building and uploading a complete flash file system to the ESP. This is basically the same functionality as the one available in the Arduino IDE, https://github.com/esp8266/Arduino/blob/master/doc/filesystem.rst#uploading-files-to-file-system

Both SPIFFS and LittleFS file systems are supported and which type to use is specified via the **FS_TYPE** variable.

The size and flash location parameters are taken from boards.txt for esp8266 and from the partition table for esp32.

The file system content is made up of everything within a directory specified via the variable **FS_DIR**. By default this variable is set to a subdirectory named **data** in the sketch directory.

Use the rule **flash_fs** or **ota_fs** to generate a file system image and upload it to the ESP.

All the settings for the file system are taken from the selected board's configuration.

It is also possible to dump and recreate the complete file system from the device via the rule **dump_fs**. The corresponding flash section will be extracted and the individual files recreated in a directory in the build structure.

#### Specifying custom partition schemes

You may wish to specify a custom partitioning table, as defined in the [ESP32 docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html). You can do this by changing the **PART_FILE** variable in your make file. By default `$(ESP_ROOT)/tools/partitions/default.csv` will be used.

#### Additional flash I/O operations

The makefile has rules for dumping and restoring the whole flash memory contents to and from a file. This can be convenient for saving a specific state or software for which no source code is available.

The rules are named **dump_flash** and **restore_flash**. The name of the output/input file is controlled by the variable **FLASH_FILE**. The default value for this is "esp_flash.bin". All required parameters for the operations are taken from the variables mentioned above for flash size, serial port and speed etc.

Example:

    espmake dump_flash FLASH_FILE=my_flash.bin


#### Building an object file library

It is also possible to build a library containing all the object files referenced in the build (excluding the sketch itself). This can e.g. be used to build separately compiled version controlled libraries which are then used in other build projects.

Example:

    espmake lib

#### Monitor

makeEspArduino also has a ***monitor*** function, i.e. connecting a terminal program to the esp board serial port. By default it will use the **miniterm** tool of the Python serial package. This can however be changed to any other terminal emulation program via the variable **MONITOR_COM**

The used port is by default same as the upload port and the default baud rate is 115200.

The ***run*** rule of the makefile will do a combined flash and monitor operation.

#### Misc build features

##### Using ccache

If you want to speed up your builds with makeEspArduino you can install ccache on your system, https://ccache.dev/

Once installed makeEspArduino will automatically use if during the build by preceding all C and C++ compilation commands with ccache.

In case you have ccache installed but don't want to use it for the build, you can set the variable **USE_CCACHE=0**

##### Cross compilation

If you want some other prefix to the C compiler command line the following variables are available: **C_COM_PREFIX** and **CPP_COM_PREFIX**

##### Parallel builds

The actual make operation is performed using parallel build compilation threads. By default all the cores of the machine is used. You can however limit the number of compilation threads started by setting the **BUILD_THREADS** variable to a desired alternate number.

##### Automatic rebuild

A record of the command line parameters and git versions used in the last build is stored in the build directory. If any of these are changed during the next build, e.g. changing a variable definition, a complete rebuild is made in order to ensure that all possible changes are applied. If you don't want this function just define the variable **IGNORE_STATE**.

##### Intermediate object archive

By default all object files are put into an archive as this seems to enable the linker to remove 5 kB RAM of unused variables. This is the same method that is used by the Arduino IDE. Unfortunately this might break some builds i.g. if some special linker flags are used. To disable this feature set the **NO_USER_OBJ_LIB** to 1.


#### User defined make rules

makeEspArduino has make rules for all the type of input files that are normally part of a build of Arduino for esp. If you want to add other type of files there are two variables which can be used for this purpose.

**USER_SRC_PATTERN** Files matching this pattern will be included in the automatic search for source files. Must be prefixed with a "|". Example:

    USER_SRC_PATTERN = |my_ext

**USER_RULES** This variable is used to define the path to a makefile which contains the actual make rules for the user specific source files. Example of contents for such a file:

    $(BUILD_DIR)/%.my_ext.o: %.my_ext
      echo Running my make rule for $<
      my_command $<

#### Setting used version of ESP Arduino

The rule **set_git_version** can be used to control which version tag to be used in the git repo specified via **ESP_ROOT**. It will perform the necessary git and copy operations to ensure that the repo is setup correctly for the tag specified via the variable **REQ_GIT_VERSION**. Example:

    espmake set_git_version REQ_GIT_VERSION=2.6.3


#### Using Visual Studio Code

Visual Studio Code is a great editor which can be used together with makeEspArduino. The makefile contains a rule named "vscode". When invoked it will generate a config file for the C/C++ addin. This will contain all the required definitions for the IntelliSense function. The information is based on the parameters of the c/c++ compilation command.

It will also generate contents in the "tasks" configuration file which enables building with makeEspArduino from within the editor. This is convenient for stepping through compilation errors for instance.

The configuration files will have settings with the name of the main sketch.

The workspace directory for the settings files will be ".vscode" and this can either be automatically detected by makeEspArduino or be specified via the variable **VS_CODE_DIR**. Automatic here means checking the parent directories of the sketch for a config directory and if doesn't exist then the sketch directory itself will be used and created if not found. If an existing project file (*.code-workspace) is found in that directory it will be used as input for the launch of VS Code.

After generating the configuration files makeEspArduino will launch Visual Studio (if available in the path)

#### Crash analysis

The rule **crash** will enable you to paste the output of a program crash for esp8266 or esp32. Explanatory reason and call stack traceback will be listed with source file and line number for each call found.

#### Compiler preprocessor

Sometimes it can be useful to see the actual full source file content once all include files and macros have been expanded. The rule **preproc** is available for this purpose. The path of the source file to be analyzed is specified via the variable **SRC_FILE**. Example:

    espmake preproc SRC_FILE=my_file.ino

#### Memory usage analysis

There are two rules which can be used for analyzing the memory usage of a build.

**ram_usage** will show the names of the variables in ram together with their size sorted in descending size order

**obj_info** will show the flash and RAM memory usage for each individual object file. The different portions of the RAM usage will also be shown. A listing is produced with columns for the different values. The listing is formated by space separated constant width fields but this can be change to tab separated instead by defining the variable OBJ_INFO_FORM to 1. The listing is by default sorted by descending RAM values but this can be also be changed by defining the variable OBJ_INFO_SORT to a value between 0 and 4.

#### Operating system specifics

makeEspArduino is intended to work completely on all the operating systems specified above. All the required specific setting for the actual operating system is stored in separate makefiles in the sub director **/os**.

Please note that Cygwin have some special considerations as most executed commands expect Windows notations, e.g. COMx for serial port specification. All paths should also be given in the forward slash format.

Newer versions of Mac OS Big Sur don't work with the pyserial version included in older versions of esp 8266 Arduino. This can be fixed by installing pyserial as described earlier and then set the variable **NO_PY_WRAP=1**

If your project have additional specific requirements you can add them under conditional statements of **$(OS)** in your project makefiles
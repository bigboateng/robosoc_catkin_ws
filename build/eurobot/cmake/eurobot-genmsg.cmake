# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "eurobot: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ieurobot:/home/ubuntu/eurobot_ws/src/eurobot/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(eurobot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg" NAME_WE)
add_custom_target(_eurobot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "eurobot" "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg" ""
)

get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg" NAME_WE)
add_custom_target(_eurobot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "eurobot" "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg" "eurobot/pathData"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/eurobot
)
_generate_msg_cpp(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/eurobot
)

### Generating Services

### Generating Module File
_generate_module_cpp(eurobot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/eurobot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(eurobot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(eurobot_generate_messages eurobot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_cpp _eurobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_cpp _eurobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(eurobot_gencpp)
add_dependencies(eurobot_gencpp eurobot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS eurobot_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/eurobot
)
_generate_msg_lisp(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/eurobot
)

### Generating Services

### Generating Module File
_generate_module_lisp(eurobot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/eurobot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(eurobot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(eurobot_generate_messages eurobot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_lisp _eurobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_lisp _eurobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(eurobot_genlisp)
add_dependencies(eurobot_genlisp eurobot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS eurobot_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot
)
_generate_msg_py(eurobot
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot
)

### Generating Services

### Generating Module File
_generate_module_py(eurobot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(eurobot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(eurobot_generate_messages eurobot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathData.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_py _eurobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/eurobot_ws/src/eurobot/msg/pathArray.msg" NAME_WE)
add_dependencies(eurobot_generate_messages_py _eurobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(eurobot_genpy)
add_dependencies(eurobot_genpy eurobot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS eurobot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/eurobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/eurobot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(eurobot_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/eurobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/eurobot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(eurobot_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/eurobot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(eurobot_generate_messages_py std_msgs_generate_messages_py)

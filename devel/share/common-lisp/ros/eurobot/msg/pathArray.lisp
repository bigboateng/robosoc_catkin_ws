; Auto-generated. Do not edit!


(cl:in-package eurobot-msg)


;//! \htmlinclude pathArray.msg.html

(cl:defclass <pathArray> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type (cl:vector eurobot-msg:pathData)
   :initform (cl:make-array 0 :element-type 'eurobot-msg:pathData :initial-element (cl:make-instance 'eurobot-msg:pathData))))
)

(cl:defclass pathArray (<pathArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pathArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pathArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eurobot-msg:<pathArray> is deprecated: use eurobot-msg:pathArray instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <pathArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eurobot-msg:path-val is deprecated.  Use eurobot-msg:path instead.")
  (path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pathArray>) ostream)
  "Serializes a message object of type '<pathArray>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pathArray>) istream)
  "Deserializes a message object of type '<pathArray>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'path) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'path)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'eurobot-msg:pathData))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pathArray>)))
  "Returns string type for a message object of type '<pathArray>"
  "eurobot/pathArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pathArray)))
  "Returns string type for a message object of type 'pathArray"
  "eurobot/pathArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pathArray>)))
  "Returns md5sum for a message object of type '<pathArray>"
  "b46bdacbeb2b49d061849868c9c44296")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pathArray)))
  "Returns md5sum for a message object of type 'pathArray"
  "b46bdacbeb2b49d061849868c9c44296")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pathArray>)))
  "Returns full string definition for message of type '<pathArray>"
  (cl:format cl:nil "pathData[] path # array to store string, coordinate~%~%~%================================================================================~%MSG: eurobot/pathData~%string function # for example turnLeft~%int16 value # 20 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pathArray)))
  "Returns full string definition for message of type 'pathArray"
  (cl:format cl:nil "pathData[] path # array to store string, coordinate~%~%~%================================================================================~%MSG: eurobot/pathData~%string function # for example turnLeft~%int16 value # 20 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pathArray>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'path) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pathArray>))
  "Converts a ROS message object to a list"
  (cl:list 'pathArray
    (cl:cons ':path (path msg))
))

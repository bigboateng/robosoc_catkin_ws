; Auto-generated. Do not edit!


(cl:in-package eurobot-msg)


;//! \htmlinclude pathData.msg.html

(cl:defclass <pathData> (roslisp-msg-protocol:ros-message)
  ((function
    :reader function
    :initarg :function
    :type cl:string
    :initform "")
   (value
    :reader value
    :initarg :value
    :type cl:fixnum
    :initform 0))
)

(cl:defclass pathData (<pathData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pathData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pathData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eurobot-msg:<pathData> is deprecated: use eurobot-msg:pathData instead.")))

(cl:ensure-generic-function 'function-val :lambda-list '(m))
(cl:defmethod function-val ((m <pathData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eurobot-msg:function-val is deprecated.  Use eurobot-msg:function instead.")
  (function m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <pathData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eurobot-msg:value-val is deprecated.  Use eurobot-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pathData>) ostream)
  "Serializes a message object of type '<pathData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'function))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'function))
  (cl:let* ((signed (cl:slot-value msg 'value)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pathData>) istream)
  "Deserializes a message object of type '<pathData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'function) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'function) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'value) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pathData>)))
  "Returns string type for a message object of type '<pathData>"
  "eurobot/pathData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pathData)))
  "Returns string type for a message object of type 'pathData"
  "eurobot/pathData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pathData>)))
  "Returns md5sum for a message object of type '<pathData>"
  "58f2eabdeb5bb2cf5da92ef285242afb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pathData)))
  "Returns md5sum for a message object of type 'pathData"
  "58f2eabdeb5bb2cf5da92ef285242afb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pathData>)))
  "Returns full string definition for message of type '<pathData>"
  (cl:format cl:nil "string function # for example turnLeft~%int16 value # 20 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pathData)))
  "Returns full string definition for message of type 'pathData"
  (cl:format cl:nil "string function # for example turnLeft~%int16 value # 20 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pathData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'function))
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pathData>))
  "Converts a ROS message object to a list"
  (cl:list 'pathData
    (cl:cons ':function (function msg))
    (cl:cons ':value (value msg))
))

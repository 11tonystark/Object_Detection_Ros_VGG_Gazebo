; Auto-generated. Do not edit!


(cl:in-package ros_service-srv)


;//! \htmlinclude Path-request.msg.html

(cl:defclass <Path-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Path-request (<Path-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Path-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Path-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_service-srv:<Path-request> is deprecated: use ros_service-srv:Path-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Path-request>) ostream)
  "Serializes a message object of type '<Path-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Path-request>) istream)
  "Deserializes a message object of type '<Path-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Path-request>)))
  "Returns string type for a service object of type '<Path-request>"
  "ros_service/PathRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path-request)))
  "Returns string type for a service object of type 'Path-request"
  "ros_service/PathRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Path-request>)))
  "Returns md5sum for a message object of type '<Path-request>"
  "43ede9fa4def9d8ab271ede42f88fcd9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Path-request)))
  "Returns md5sum for a message object of type 'Path-request"
  "43ede9fa4def9d8ab271ede42f88fcd9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Path-request>)))
  "Returns full string definition for message of type '<Path-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Path-request)))
  "Returns full string definition for message of type 'Path-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Path-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Path-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Path-request
))
;//! \htmlinclude Path-response.msg.html

(cl:defclass <Path-response> (roslisp-msg-protocol:ros-message)
  ((lat
    :reader lat
    :initarg :lat
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (lon
    :reader lon
    :initarg :lon
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Path-response (<Path-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Path-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Path-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_service-srv:<Path-response> is deprecated: use ros_service-srv:Path-response instead.")))

(cl:ensure-generic-function 'lat-val :lambda-list '(m))
(cl:defmethod lat-val ((m <Path-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_service-srv:lat-val is deprecated.  Use ros_service-srv:lat instead.")
  (lat m))

(cl:ensure-generic-function 'lon-val :lambda-list '(m))
(cl:defmethod lon-val ((m <Path-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_service-srv:lon-val is deprecated.  Use ros_service-srv:lon instead.")
  (lon m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Path-response>) ostream)
  "Serializes a message object of type '<Path-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'lat))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'lat))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'lon))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'lon))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Path-response>) istream)
  "Deserializes a message object of type '<Path-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'lat) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'lat)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'lon) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'lon)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Path-response>)))
  "Returns string type for a service object of type '<Path-response>"
  "ros_service/PathResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path-response)))
  "Returns string type for a service object of type 'Path-response"
  "ros_service/PathResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Path-response>)))
  "Returns md5sum for a message object of type '<Path-response>"
  "43ede9fa4def9d8ab271ede42f88fcd9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Path-response)))
  "Returns md5sum for a message object of type 'Path-response"
  "43ede9fa4def9d8ab271ede42f88fcd9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Path-response>)))
  "Returns full string definition for message of type '<Path-response>"
  (cl:format cl:nil "float64[] lat~%float64[] lon~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Path-response)))
  "Returns full string definition for message of type 'Path-response"
  (cl:format cl:nil "float64[] lat~%float64[] lon~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Path-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'lat) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'lon) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Path-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Path-response
    (cl:cons ':lat (lat msg))
    (cl:cons ':lon (lon msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Path)))
  'Path-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Path)))
  'Path-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path)))
  "Returns string type for a service object of type '<Path>"
  "ros_service/Path")
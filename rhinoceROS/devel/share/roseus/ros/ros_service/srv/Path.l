;; Auto-generated. Do not edit!


(when (boundp 'ros_service::Path)
  (if (not (find-package "ROS_SERVICE"))
    (make-package "ROS_SERVICE"))
  (shadow 'Path (find-package "ROS_SERVICE")))
(unless (find-package "ROS_SERVICE::PATH")
  (make-package "ROS_SERVICE::PATH"))
(unless (find-package "ROS_SERVICE::PATHREQUEST")
  (make-package "ROS_SERVICE::PATHREQUEST"))
(unless (find-package "ROS_SERVICE::PATHRESPONSE")
  (make-package "ROS_SERVICE::PATHRESPONSE"))

(in-package "ROS")





(defclass ros_service::PathRequest
  :super ros::object
  :slots ())

(defmethod ros_service::PathRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass ros_service::PathResponse
  :super ros::object
  :slots (_lat _lon ))

(defmethod ros_service::PathResponse
  (:init
   (&key
    ((:lat __lat) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:lon __lon) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _lat __lat)
   (setq _lon __lon)
   self)
  (:lat
   (&optional __lat)
   (if __lat (setq _lat __lat)) _lat)
  (:lon
   (&optional __lon)
   (if __lon (setq _lon __lon)) _lon)
  (:serialization-length
   ()
   (+
    ;; float64[] _lat
    (* 8    (length _lat)) 4
    ;; float64[] _lon
    (* 8    (length _lon)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _lat
     (write-long (length _lat) s)
     (dotimes (i (length _lat))
       (sys::poke (elt _lat i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _lon
     (write-long (length _lon) s)
     (dotimes (i (length _lon))
       (sys::poke (elt _lon i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _lat
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _lat (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _lat i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _lon
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _lon (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _lon i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass ros_service::Path
  :super ros::object
  :slots ())

(setf (get ros_service::Path :md5sum-) "43ede9fa4def9d8ab271ede42f88fcd9")
(setf (get ros_service::Path :datatype-) "ros_service/Path")
(setf (get ros_service::Path :request) ros_service::PathRequest)
(setf (get ros_service::Path :response) ros_service::PathResponse)

(defmethod ros_service::PathRequest
  (:response () (instance ros_service::PathResponse :init)))

(setf (get ros_service::PathRequest :md5sum-) "43ede9fa4def9d8ab271ede42f88fcd9")
(setf (get ros_service::PathRequest :datatype-) "ros_service/PathRequest")
(setf (get ros_service::PathRequest :definition-)
      "
---
float64[] lat
float64[] lon

")

(setf (get ros_service::PathResponse :md5sum-) "43ede9fa4def9d8ab271ede42f88fcd9")
(setf (get ros_service::PathResponse :datatype-) "ros_service/PathResponse")
(setf (get ros_service::PathResponse :definition-)
      "
---
float64[] lat
float64[] lon

")



(provide :ros_service/Path "43ede9fa4def9d8ab271ede42f88fcd9")



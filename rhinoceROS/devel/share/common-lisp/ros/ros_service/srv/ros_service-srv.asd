
(cl:in-package :asdf)

(defsystem "ros_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Path" :depends-on ("_package_Path"))
    (:file "_package_Path" :depends-on ("_package"))
  ))
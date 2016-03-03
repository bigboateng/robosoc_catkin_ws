
(cl:in-package :asdf)

(defsystem "eurobot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pathArray" :depends-on ("_package_pathArray"))
    (:file "_package_pathArray" :depends-on ("_package"))
    (:file "pathData" :depends-on ("_package_pathData"))
    (:file "_package_pathData" :depends-on ("_package"))
  ))
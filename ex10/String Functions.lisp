(defun str_op (str)
  (let* ((len (loop for char across str count char))
         (rev (make-string len))
         (is-palindrome t))

    (loop for i from 0 to (1- len)
          do (setf (char rev i) (char str (- len 1 i))))

    (loop for i from 0 to (1- len)
          when (not (char-equal (char str i) (char rev i)))
          do (setf is-palindrome nil))

    (format t "Original: ~a~%" str)
    (format t "Length: ~d~%" len)
    (format t "Reversed: ~a~%" rev)
    (if is-palindrome
        (format t "Result: It is a palindrome~%")
        (format t "Result: It is NOT a palindrome~%"))))

(format t "Enter a string: ")
(finish-output)
(str_op (read-line))


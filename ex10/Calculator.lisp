
(defun calculator ()
  (format t "Enter first number: ")
  (let ((num1 (read)))
    (format t "Enter operator (+, -, *, /, mod, ^): ")
    (let ((op (read)))

      (format t "Enter second number: ")
      (let ((num2 (read)))
        (cond
          ((equal op '+) (format t "Result: ~a~%" (+ num1 num2)))
          ((equal op '-) (format t "Result: ~a~%" (- num1 num2)))
          ((equal op '*) (format t "Result: ~a~%" (* num1 num2)))
          ((equal op '/) (if (/= num2 0)
                             (format t "Result: ~a~%" (/ num1 num2))
                             (format t "Error: Division by zero!~%")))
          ((equal op 'mod) (format t "Result: ~a~%" (mod num1 num2)))
          ((equal op '^)   (format t "Result: ~a~%" (expt num1 num2)))
          (t (format t "Invalid operator!~%")))))))

(calculator)

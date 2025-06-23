(define (over-or-under num1 num2) 
    (if (< num1 num2) -1 
      (if (= num1 num2) 0 1))
)

(define (make-adder num) 
    (lambda (x) (+ x num))  
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define (repeat f n) 
    (lambda (x)
      (if (= n 1) (f x)
        (f ((repeat f (- n 1)) x))))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (define ma (max a b))
  (define mi (min a b))
  (define mo (modulo ma mi))
  (if (zero? mo) mi
    (gcd mi mo))
)

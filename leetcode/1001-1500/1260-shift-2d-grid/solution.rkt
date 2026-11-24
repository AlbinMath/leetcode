(define/contract (shift-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer?
      (listof (listof exact-integer?)))

  (define m (length grid))
  (define n (length (first grid)))
  (define total (* m n))
  (define shift (modulo k total))

  (define flat (apply append grid))

  (define shifted
    (append
     (drop flat (- total shift))
     (take flat (- total shift))))

  (for/list ([i (in-range m)])
    (take (drop shifted (* i n)) n)))

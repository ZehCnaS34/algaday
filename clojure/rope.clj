
(def node {:weight nil :left nil :right nil})
(def leaf {:weight nil :content nil})
(def root {:weight 0 :content ""})

(def sample-rope
  {:weight 22
   :left {:weight 9
          :left {:weight 6
                 :left {:weight 6 :content "Hello "}
                 :right {:weight 3 :content "my "}}
          :right {:weight 6
                  :left {:weight 2
                         :left {:weight 2 :content "na"}
                         :right {:weight 4 :content "me i"}}
                  :right {:weight 1
                          :left {:weight 1 :content "s"}
                          :right {:weight 6 :content " Simon"}}}}
   :right nil})

(defn is-leaf [node] (if (:content node) true false))

(defn rope-get-total-weight [root]
  (loop [node root
         weight 0]
    (if (or (is-leaf node) (nil? node))
      (+ weight (get node :weight 0))
      (recur (:right node)
             (+ weight (:weight node))))))

(defn rope-index [node idx]
  (cond
    (is-leaf node) (:content node)
    (<= idx (:weight node)) (rope-index (:left node) idx)
    (>  idx (:weight node)) (rope-index (:right node) (- idx (:weight node)))
    :default (throw "Error")))

(defn rope-split [root idx]
  (loop [new-root root
         current-node root
         idx idx
         path []
         trees []]
    (cond
      (or 
        (is-leaf current-node))
      [(rope-concat 
         (:left new-root)
         (:right new-root))
       (->> trees 
         (filter (complement nil?))
         (reduce rope-concat))]

      ;; if idx is more than the weight, go right, and add to path
      (> idx (:weight current-node)) 
      (recur
        new-root
        (:right current-node)
        (- idx (:weight current-node))
        (conj path :right)
        trees)

      ;; going left
      (<= idx (:weight current-node)) 
      (recur
        (assoc-in new-root (conj path :right) nil) ; remove 
        (:left current-node)
        idx
        (conj path :left)
        (conj trees (:right current-node))
        )
      ))) 

(defn rope-report [root]
  (loop [fringe [root]
         string-builder ""]
    (cond
      ;; if the fringe is empty, return report the string
      (empty? fringe)
      string-builder

      ;; if curent node is 
      (is-leaf (peek fringe))
      (recur (pop fringe)
             (str string-builder (:content (peek fringe))))

      ;; if children are available, push to stack
      (or (not (nil? (:left (peek fringe))))
          (not (nil? (:right(peek fringe)))) )
      (recur (-> fringe
                 (pop)
                 (conj (:right (peek fringe)))
                 (conj (:left (peek fringe)))
                 )
             string-builder)
      
      ;; probably nil
      :default
      (recur (pop fringe) string-builder)
      )))

(defn rope-insert [root idx string]
  (let [[left right] (rope-split root idx)
        new-node {:weight (count string)
          :content string}]
    (reduce rope-concat [left new-node right])))

(defn rope-concat 
  ([] nil)
  ([left] left)
  ([left right]
   {:weight (rope-get-total-weight left)
    :left left
    :right right}))

(-> sample-rope
    (rope-insert 0 "alex ")
    (rope-insert 0 "alex ")
    rope-report)

; (rope-index
;   sample-rope
;   x)


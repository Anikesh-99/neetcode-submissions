-- Write your query below
SELECT L.left as left_operand, L.lop as operator, L.right as right_operand,
    CASE operator
        WHEN '<'  THEN val1 < val2
        WHEN '>'  THEN val1 > val2
        WHEN '='  THEN val1 = val2
        ELSE FALSE
    END AS value
FROM 
(
    (Select left_operand as left, value as val1, operator as lop, right_operand as right from 
variables JOIN expressions on left_operand = name) l
Join
(Select left_operand, operator, right_operand, value as val2 from variables JOIN expressions on right_operand = name) r on l.left = r.left_operand and l.right = r.right_operand and l.lop = r.operator)
L
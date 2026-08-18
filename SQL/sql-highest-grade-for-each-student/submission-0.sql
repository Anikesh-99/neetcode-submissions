-- Write your query below
Select r.student_id, min(r.exam_id) as exam_id, max(r.score) as score
from (
    Select student_id, Max(score) as mx_score
    from exam_results
    group by student_id
) E join exam_results r on r.student_id = E.student_id and r.score = E.mx_score
group by r.student_id
order by r.student_id
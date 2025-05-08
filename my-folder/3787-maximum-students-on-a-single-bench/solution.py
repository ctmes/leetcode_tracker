from typing import List

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        if not students:
            return 0

        bench_students = {}

        for student_id, bench_id in students:
            if bench_id not in bench_students:
                bench_students[bench_id] = set()
            bench_students[bench_id].add(student_id)

        max_students = 0
        for bench_id in bench_students:
            max_students = max(max_students, len(bench_students[bench_id]))

        return max_students

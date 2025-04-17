class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Dictionary to store scores for each student
        score_map = {}
        
        # Group scores by student ID
        for student_id, score in items:
            if student_id not in score_map:
                score_map[student_id] = []
            score_map[student_id].append(score)
        
        out = []
        # Compute average of top 5 scores for each student
        for student_id in sorted(score_map.keys()):
            # Sort scores in descending order and take top 5
            top_scores = sorted(score_map[student_id], reverse=True)[:5]
            # Calculate average
            avg_score = sum(top_scores) // 5
            out.append([student_id, avg_score])
        
        return out

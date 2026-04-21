required_skills = {'Python', 'SQL', 'Git', 'Docker'}
candidate_1 = {'Python', 'SQL', 'Git', 'Docker', 'Kubernetes'}
candidate_2 = {'Python', 'SQL', 'JavaScript'}
candidate_3 = {'Python', 'SQL', 'Git', 'HTML/CSS'}
print(f'Есть ли все навыки у кандидатов?: \n'
      f'У первого: {required_skills.issubset(candidate_1)}\n'
      f'У второго: {required_skills.issubset(candidate_2)}\n'
      f'У третьего: {required_skills.issubset(candidate_3)}')
print(f'{required_skills - candidate_1}, {required_skills - candidate_2}, {required_skills - candidate_3}')
print(f'{candidate_1 - required_skills}, {candidate_2 - required_skills}, {candidate_3 - required_skills}')

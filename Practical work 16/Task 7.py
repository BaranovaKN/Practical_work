agent_cords = (2, 2)
save_points = {(1, 1), (5, 5), (0, 3)}
close_points = min(save_points, key=lambda x: abs(x[0] - agent_cords[1]))
print('Ближайшая безопасная точка к агенту находится на координатах: ',close_points)
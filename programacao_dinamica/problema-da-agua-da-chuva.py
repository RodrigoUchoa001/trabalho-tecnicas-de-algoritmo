def problema_da_agua_da_chuva(buildings):
  n = len(buildings)
  left = [0 for i in range(n)]
  right = [0 for i in range(n)]
  left[0] = buildings[0]
  right[n - 1] = buildings[n - 1]

  for i in range(1, n):
    left[i] = max(left[i - 1], buildings[i])
  for i in range(n - 2, -1, -1):
    right[i] = max(right[i + 1], buildings[i])

  water = 0
  for i in range(n):
    water += min(left[i], right[i]) - buildings[i]

  return water

buildings = [2, 0, 2]
print("A quantidade de água presa é: ", problema_da_agua_da_chuva(buildings))

buildings = [1, 0, 2, 0, 3]
print("A quantidade de água presa é: ", problema_da_agua_da_chuva(buildings))

buildings = [3, 0, 0, 2, 0, 4]
print("A quantidade de água presa é: ", problema_da_agua_da_chuva(buildings))
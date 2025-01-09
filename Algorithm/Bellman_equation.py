import numpy as np
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

# 그리드 크기 및 목표 상태 설정
grid_size = 5
goal_state = (4, 4)

# 행동 정의 (상, 하, 좌, 우)
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 보상 및 감가율 설정
reward = -1
gamma = 0.9
theta = 1e-4

# 가치 반복(Value Iteration) 알고리즘을 벨만 방정식 기반으로 구현

# 가치 함수 초기화
V = np.zeros((grid_size, grid_size))

# 가치 반복 수행
iteration = 0
delta_history = []  # 변화량 저장
value_history = [V.copy()]  # 각 단계의 가치 함수 저장

while True:
    delta = 0
    new_V = np.copy(V)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if (i, j) == goal_state:
                continue  # 목표 상태는 업데이트 안 함
            
            values = []
            for action in actions:
                ni, nj = i + action[0], j + action[1]
                
                # 격자를 벗어나는 경우, 같은 위치 유지
                if ni < 0 or ni >= grid_size or nj < 0 or nj >= grid_size:
                    ni, nj = i, j
                
                # 벨만 방정식 적용 (최적 가치 함수 업데이트)
                values.append(reward + gamma * V[ni, nj])
            
            # 벨만 최적 방정식 적용: 최적 행동 선택
            new_V[i, j] = max(values)
            
            # 변화량 갱신
            delta = max(delta, abs(new_V[i, j] - V[i, j]))
    
    V = new_V
    value_history.append(V.copy())
    delta_history.append(delta)
    iteration += 1

    # 수렴 조건 확인subplots
    if delta < theta:
        break

# 가치 함수 업데이트 과정 시각화
fig, axes = plt.subplots(2, len(value_history) // 2, figsize=(15, 6))
axes = axes.flatten()
for idx, v in enumerate(value_history):
    sns.heatmap(v, annot=True, fmt=".1f", cmap="coolwarm", cbar=False, ax=axes[idx])
    axes[idx].set_title(f"Iteration {idx}")

plt.tight_layout()

# 델타(변화량) 시각화
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(delta_history, marker="o", linestyle="-")
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Delta (Change in Value Function)")
ax2.set_title("Convergence of Value Iteration")

plt.show()

# 최종 가치 함수 데이터 출력
V_df = pd.DataFrame(np.round(V, 2), columns=[f"Col {i}" for i in range(grid_size)])
print("Final Value Function:")
print(V_df)

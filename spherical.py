import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D 시각화를 위한 모듈 추가
import streamlit as st  # Streamlit 추가

# Streamlit 앱 시작
st.title('2D and 3D Visualization of Random Points')

# 점의 개수를 인풋으로 받기
num_points = st.number_input("Enter the number of points", min_value=1, max_value=10000, value=10000)

# x를 3차원 배열로 생성
x = np.random.randn(3, num_points)

# 드롭다운을 사용하여 2D 또는 3D 선택
dimension = st.selectbox("Select Dimension", ["2D", "3D"])

if dimension == "2D":
    # 2D 공간에 x[0]과 x[1] 시각화
    fig, ax = plt.subplots()
    ax.scatter(x[0], x[1], color='blue', s=1)  # 점을 파란색으로 표시하고 크기를 1로 설정
    ax.set_xlim(-5, 5)  # x축 범위 설정
    ax.set_ylim(-5, 5)  # y축 범위 설정
    ax.set_title('2D Visualization of x[0] and x[1]')  # 제목 설정
else:
    # 슬라이더를 사용하여 시점 조정
    elev = st.slider("Elevation (y-axis)", min_value=0, max_value=180, value=30)  # 고도 조정
    azim = st.slider("Azimuth (x-axis)", min_value=0, max_value=360, value=30)  # 방위각 조정

    # 3D 공간에 x[0], x[1], x[2] 시각화
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # 3D 축 추가
    ax.scatter(x[0], x[1], x[2], color='blue', s=1)  # 점을 파란색으로 표시하고 크기를 1로 설정
    ax.set_xlim(-5, 5)  # x축 범위 설정
    ax.set_ylim(-5, 5)  # y축 범위 설정
    ax.set_zlim(-5, 5)  # z축 범위 설정
    ax.set_title('3D Visualization of x[0], x[1], and x[2]')  # 제목 설정

    # 시점 설정
    ax.view_init(elev=elev, azim=azim)  # 슬라이더 값에 따라 시점 조정

# Streamlit에서 그래프 표시
st.pyplot(fig)  # 그래프 표시
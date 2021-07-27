import math
import streamlit as st

"""
# 手臂第六軸旋轉後的重心座標轉換

數學公式：
- 第六軸旋轉前，TCP 座標系下的夾具重心座標為 (x1, y2, z1) 
- 第六軸逆時鐘旋轉 θ 後，TCP 座標系下的夾具重心座標變為 (x2, y2, z2) 
    - `x2 = x1 * cosθ - y1 * sinθ`
    - `y2 = x1 * sinθ + y1 * cosθ`
    - `z2 = z1`
- 若第六軸順時鐘旋轉 θ，則上述公式使用 -θ

範例：
- 第六軸旋轉前，TCP 座標系下的夾具重心座標為 (-6.86, -27.49, -99.01)
- 第六軸逆時鐘旋轉 90 度後，TCP 座標系下的夾具重心座標變為 (27.49, -6.86, -99.01)
    - `x2 = -6.86 * cos90° - (-27.49) * sin90° = 27.49`
    - `y2 = -6.86 * sin90° + (-27.49) * cos90° = -6.86`
    - `z2 = -99.01`

## 展示
"""
import math

def rotate(point, angle):
    """
    Rotate a point counterclockwise by a given angle around the origin (0,0).
    The angle should be given in degrees.
    """
    radian = math.radians(angle)
    px, py = point[0], point[1]
    qx = math.cos(radian) * px - math.sin(radian) * py
    qy = math.sin(radian) * px + math.cos(radian) * py
    return qx, qy

center_of_gravity1 = (-6.86, -27.49, -99.01)

st.write(f"原始重心座標：{center_of_gravity1}")

degree = st.slider("第六軸逆時鐘旋轉角度", 1, 0, 360)

newcogxy = rotate(center_of_gravity1, degree)
newcog = (round(newcogxy[0], 2), round(newcogxy[1], 2), center_of_gravity1[2])

st.write(f"新的重心座標：{newcog}")

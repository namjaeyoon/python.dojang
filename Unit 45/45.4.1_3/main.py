from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))    # add 함수는 공개되어 있으므로 사용할 수 있음
print(mul(10, 20))    # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음

print(triangle_area(30, 40))    # triangle_area 함수는 공개되어 있으므로 사용할 수 있음
print(rectangle_area(30, 40))   # 에러: rectangle_area 함수는 공개되어 있으므로 사용할 수 있음

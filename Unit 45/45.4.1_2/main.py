import calcpkg    # calcpkg 패키지만 가져옴

print(calcpkg.add(10, 20))   # 패키지.함수 형식으로 operation 모듈의 add 함수 사용
print(calcpkg.mul(10, 20))   # 패키지.함수 형식으로 operation 모듈의 mul 함수 사용

print(calcpkg.triangle_area(30, 40)) # 패키지.함수 형식으로 geometry 모듈의 triangle_area 함수 사용
print(calcpkg.rectangle_area(30, 40))# 패키지.함수 형식으로 geometry 모듈의 rectangle_area 함수 사용

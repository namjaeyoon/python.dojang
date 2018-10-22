__all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개

from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

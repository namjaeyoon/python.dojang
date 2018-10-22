class Knight:
    __item_limit = 10    # 비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음


x = Knight()
x.print_item_limit()    # 10

print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음

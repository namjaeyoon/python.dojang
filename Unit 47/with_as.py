class OpenHello:
    def __enter__(self):
        self.file = open('hello.txt', 'w')    # 파일 객체를 속성에 저장
        return self.file     # __enter__에서 값을 반환하면 as에 지정한 변수에 들어감

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()    # __exit__에서 파일 객체 닫기

with OpenHello() as hello:
    hello.write('Hello, world!')

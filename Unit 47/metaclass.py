def replace(self, old, new):    # 클래스에 들어갈 메서드 정의
    while old in self:
        self[self.index(old)] = new

# list를 상속받음, 속성 desc, 메서드 replace 추가
AdvancedList = type('AdvancedList', (list, ), { 'desc': '향상된 리스트', 'replace': replace })

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)         # [100, 2, 3, 100, 2, 3, 100, 2, 3]
print(x.desc)    # 향상된 리스트

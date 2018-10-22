word = input('단어를 입력하세요: ')

print(word == word[::-1])    # 원래 문자열과 반대로 뒤집은 문자열을 비교
</코드>
<코드>실행 결과
단어를 입력하세요: level (입력)
True
단어를 입력하세요: hello (입력)
False

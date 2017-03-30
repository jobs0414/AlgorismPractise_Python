"""
toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로,
홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.

예를 들어 s가 "try hello world"라면 첫 번째 단어는 "TrY", 두 번째 단어는 "HeLlO",
세 번째 단어는 "WoRlD"로 바꿔 "TrY HeLlO WoRlD"를 리턴하면 됩니다.

주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.

def toWeirdCase(s):
    list = s.lower().split()
    lista = []
    for i in list:
        for j in range((int)(len(i)//2+1)):
            i = i.replace(i[j*2], i[j*2].upper(),1)
        lista.append(i)
    return ' '.join(lista)
"""
def toWeirdCase(s):
	s = s.split()
	i = 0
	j = 0
	while i < len(s):
		for j, v in enumerate(s[i]):
			if j % 2 == 1:
				s[i] = s[i][:j] + s[i][j:].replace(v, v.lower(), 1)
			else:
				s[i] = s[i][:j] + s[i][j:].replace(v, v.upper(), 1)
		i += 1
	return ' '.join(s)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hellso world")));


"""
다른풀이
def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
***enumerate는 리스트 튜플 문자열을 인덱스를 포함한 내용을 넘긴다
"""
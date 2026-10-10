# 생각하는 파이썬 Part 2 · 바이트코드
# (강의 슬라이드: dis 로 번역본을 열어 본다)


import dis

def total(price, fee):          # def — 명령 몇 줄에 이름을 붙여 둔 것, 함수
    return price * 3 + fee      # 단가에 3을 곱하고 배송비를 더한다

dis.dis(total)
# 명령 이름은 파이썬 버전마다 조금씩 다릅니다. 화면과 달라도 정상입니다.
#   LOAD_FAST price   → 스택: 1200
#   LOAD_CONST 3      → 스택: 1200, 3
#   BINARY_OP *       → 스택: 3600
#   LOAD_FAST fee     → 스택: 3600, 500
#   BINARY_OP +       → 스택: 4100
#   RETURN_VALUE      → 4100 을 돌려준다

print(total(1200, 500))         # 4100

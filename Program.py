import streamlit as st
from decimal import Decimal, getcontext

def find_recurring_cycle(n, max_digits=2000):
    """1/n의 순환소수와 순환마디 찾기"""
    getcontext().prec = max_digits
    seen = {}
    digits = []
    remainder = 1
    index = 0

    while remainder != 0 and remainder not in seen:
        seen[remainder] = index
        remainder *= 10
        digit = remainder // n
        digits.append(str(digit))
        remainder %= n
        index += 1

    if remainder == 0:
        return ''.join(digits), ''
    else:
        start = seen[remainder]
        non_repeat = ''.join(digits[:start])
        repeat = ''.join(digits[start:])
        return non_repeat, repeat

st.title("🔁 순환소수 탐색기")
st.write("숫자 `n`을 입력하면 1/n의 소수 표현과 순환마디를 확인할 수 있어요.")

n_input = st.text_input("n의 값 (예: 7, 10^3, 100!, etc):", "7")

try:
    if "!" in n_input:
        import math
        base = int(n_input.replace("!", ""))
        n = math.factorial(base)
    elif "^" in n_input:
        base, exp = n_input.split("^")
        n = int(base) ** int(exp)
    else:
        n = int(n_input)

    if n == 0:
        st.error("0으로 나눌 수 없습니다.")
    else:
        non_repeat, repeat = find_recurring_cycle(n)

        st.subheader(f"1 / {n} 의 결과:")
        st.code(f"0.{non_repeat}[{repeat}]", language='text')

        st.write(f"🔁 순환마디 길이: {len(repeat)}")

except Exception as e:
    st.error(f"입력 오류: {e}")

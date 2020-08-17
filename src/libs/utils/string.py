import random
import string


def generate_random_str(length: int) -> str:
    # 숫자 + 대소문자
    string_pool = string.ascii_letters + string.digits
    result = ''
    for _ in range(length):
        result += random.choice(string_pool)
    return result

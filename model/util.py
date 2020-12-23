import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    generated_id = []
    for i in range(number_of_small_letters):
        generated_id.append(list(string.ascii_lowercase)[random.randint(1,25)])
    for i in range(number_of_capital_letters):
        generated_id.append(list(string.ascii_uppercase)[random.randint(1,25)])
    for i in range(number_of_digits):
        generated_id.append(random.randint(0,9))
    for i in range(number_of_special_chars):
        generated_id.append(allowed_special_chars[random.randint(0,len(allowed_special_chars)-1)])
    generated_id = [str(item) for item in generated_id]
    random.shuffle(generated_id)
    result = ''.join(generated_id)
    return result


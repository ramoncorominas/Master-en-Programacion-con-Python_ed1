print(__name__)
# from ..extramath import *
def _is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def fizzbuzz(up_to: int):
    output = []
    for number in range(1, up_to + 1):
        representation_token = []

        if is_divisible(number, 3):
            representation_token.append('fizz')

        if is_divisible(number, 5):
            representation_token.append('buzz')

        if not representation_token:
            representation_token.append(str(number))

        output.append(' '.join(representation_token))

    print(', '.join(output))


if __name__ == '__main__':
    fizzbuzz(100)

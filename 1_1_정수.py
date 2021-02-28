def 예제():
    print((999).bit_length())
    숫자 ="111"
    # String을 int로 convert 해주는 코드이다 (10진법으로 인식하기)
    십진법 = int(숫자)
    print(십진법)
    # String을 2진법으로 인식하기
    이진법 = int(숫자,2)
    print(이진법)
    # String을 16진법으로 인식하기
    숫자= "A"
    십육진법= int(숫자,16)
    print(십육진법)


if __name__ == '__main__':
    예제()
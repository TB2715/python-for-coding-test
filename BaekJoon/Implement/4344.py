case_count = int(input())

for _ in range(case_count):
    a_case_result = input().split()

    s_count = int(a_case_result[0])
    test_result = [int(x) for x in a_case_result[1:]]

    result_avg = sum(test_result) / s_count

    over_count = 0
    for a_test_result in test_result:
        if a_test_result > result_avg:
            over_count += 1

    """
    round(반올림하고자 하는 값, 자릿수)
    round(1.23456, 0) = 1.0
    round(1.23456, 1) = 1.2
    round(40.0, 3) = 40.0
    round 함수는 소숫점 이하 3번째 자리까지 표시하라고 설정을 해도 40.000% 로 출력되지 않음 
    """

    """
    '%0갯수.자리수f' % 3.6 -> '%08.2f' % 3.6 = 00003.60
    '{인덱스:0개수.자리수f}.format(숫자) -> '{0:08.2f}'.format(150.37) = 00150.37
    """


    percent = over_count/s_count*100
    percent = '{:.3f}'.format(percent)
    print(f'{percent}%')
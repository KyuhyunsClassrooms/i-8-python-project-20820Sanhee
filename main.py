# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번:  20820 한산희
# 프로젝트 주제:  나만의 스마트 공부 습관 점수 분석기

# 나만의 스마트 공부 습관 점수 분석기

def input_log():
    study_logs = []

    subject_count = int(input("오늘 공부한 과목 수를 입력하세요: "))

    for i in range(subject_count):
        print(f"\n[{i + 1}번째 과목 입력]")

        subject = input("과목명: ")
        planned_time = int(input("계획했던 시간(분): "))
        actual_time = int(input("실제 공부한 시간(분): "))

        # 집중도 점수 예외 처리
        while True:
            focus = int(input("집중도 점수(1~5): "))
            if 1 <= focus <= 5:
                break
            print("집중도는 1~5 사이의 2" \
            "숫자만 입력하세요.")

        study_logs.append([subject, planned_time, actual_time, focus])

    return study_logs


def analyze_efficiency(logs):
    total_score = 0
    best_score = -1
    best_subject = ""

    print("\n===== 과목별 분석 결과 =====")

    for row in logs:
        subject = row[0]
        planned = row[1]
        actual = row[2]
        focus = row[3]

        # 0으로 나누기 예외 처리
        if planned == 0:
            achievement = 0
        else:
            achievement = (actual / planned) * 100

        efficiency = (achievement * 0.6) + (focus * 8)

        print(f"\n과목: {subject}")
        print(f"달성률: {achievement:.1f}%")
        print(f"효율 점수: {efficiency:.1f}점")

        total_score += efficiency

        # 최고 효율 과목 찾기
        if efficiency > best_score:
            best_score = efficiency
            best_subject = subject

    average_score = total_score / len(logs)

    return average_score, best_subject


def show_report(avg_score, best_subject):
    print("\n===== 오늘의 종합 리포트 =====")
    print(f"평균 효율 점수: {avg_score:.1f}점")
    print(f"최고 효율 과목: {best_subject}")

    print("\n[내일의 한 줄 조언]")

    if avg_score >= 90:
        print("최고의 공부 습관입니다! 지금의 루틴을 유지해 보세요.")
    elif avg_score >= 70:
        print("좋은 흐름입니다. 집중력을 조금만 더 높여보세요.")
    elif avg_score >= 50:
        print("계획 대비 실천율을 높이면 더 좋은 결과가 나올 거예요.")
    else:
        print("공부한 건 맞죠? 내일은 계획표와 조금 더 친해져 봅시다.")


# 메인 프로그램
logs = input_log()
average, best_subject = analyze_efficiency(logs)
show_report(average, best_subject)


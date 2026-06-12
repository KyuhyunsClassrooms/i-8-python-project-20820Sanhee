# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20820 한산희
# 프로젝트 주제: 나만의 스마트 공부 습관 점수 분석기


def input_log():
    study_logs = []

    # 과목 수 입력 (예외 처리)
    while True:
        try:
            subject_count = int(input("오늘 공부한 과목 수를 입력하세요: "))
            if subject_count > 0:
                break
            print("과목 수는 1개 이상 입력해야 합니다.")
        except:
            print("숫자만 입력하세요.")

    for i in range(subject_count):
        print(f"\n[{i + 1}번째 과목 입력]")

        subject = input("과목명: ")

        # 계획 시간
        while True:
            try:
                planned_time = int(input("계획했던 시간(분): "))
                if planned_time > 0:
                    break
                print("계획 시간은 1 이상이어야 합니다.")
            except:
                print("숫자만 입력하세요.")

        # 실제 시간
        while True:
            try:
                actual_time = int(input("실제 공부한 시간(분): "))
                if actual_time >= 0:
                    break
                print("0 이상 입력하세요.")
            except:
                print("숫자만 입력하세요.")

        # 집중도
        while True:
            try:
                focus = int(input("집중도 점수(1~5): "))
                if 1 <= focus <= 5:
                    break
                print("1~5 사이만 입력하세요.")
            except:
                print("숫자만 입력하세요.")

        study_logs.append([subject, planned_time, actual_time, focus])

    return study_logs


def analyze_efficiency(logs):
    total_score = 0
    best_score = -1
    best_subject = ""

    print("\n===== 과목별 분석 결과 =====")

    for row in logs:
        subject, planned, actual, focus = row

        # 달성률 계산
        if planned > 0:
            achievement = (actual / planned) * 100
        else:
            achievement = 0

        # 공부 안 한 경우 0점 처리
        if actual == 0:
            efficiency = 0
        else:
            efficiency = (achievement * 0.6) + (focus * 8)

        # 100점 제한
        if efficiency > 100:
            efficiency = 100

        print(f"\n과목: {subject}")
        print(f"달성률: {achievement:.1f}%")
        print(f"효율 점수: {efficiency:.1f}점 / 100점")

        total_score += efficiency

        if efficiency > best_score:
            best_score = efficiency
            best_subject = subject

    # 평균 계산 (0 나누기 방지)
    if len(logs) == 0:
        average_score = 0
    else:
        average_score = total_score / len(logs)

    if average_score > 100:
        average_score = 100

    return average_score, best_subject


def show_report(avg_score, best_subject):
    print("\n===== 오늘의 종합 리포트 =====")
    print(f"나의 오늘 공부 점수: {avg_score:.1f}점 / 100점")

    # 등급
    if avg_score >= 90:
        grade = "A"
    elif avg_score >= 80:
        grade = "B"
    elif avg_score >= 70:
        grade = "C"
    elif avg_score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"오늘의 등급: {grade}")
    print(f"최고 효율 과목: {best_subject}")

    print("\n[내일의 한 줄 조언]")

    if avg_score >= 90:
        print("최고의 공부 습관입니다! 유지하세요.")
    elif avg_score >= 70:
        print("좋은 흐름입니다. 집중력을 조금 더 높여보세요.")
    elif avg_score >= 50:
        print("실천률을 조금만 더 높여보세요.")
    else:
        print("계획을 더 잘 세워보는 게 좋아요.")


# 메인 실행
logs = input_log()
average, best_subject = analyze_efficiency(logs)
show_report(average, best_subject)
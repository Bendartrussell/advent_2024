Report = list[int]


def part1(data: str) -> int:
    reports = parse_reports(data)
    results = list(is_safe(report) for report in reports)
    safe_count = sum(results)
    return safe_count


def part2(data: str) -> int:
    reports = parse_reports(data)
    results = list(is_safe(report, dampener=True) for report in reports)
    safe_count = sum(results)
    return safe_count



def parse_reports(data: str) -> list[Report]:
    return [
        list(map(int, line.split())) for line in data.split("\n") if line
    ]


def is_safe(report: Report, *, dampener: bool = False) -> bool:
    diffs = [two - one for one, two in zip(
        report[:-1],
        report[1:],
    )]
    if diffs[0] >= 0:
        level_safety = [1 <= d <= 3 for d in diffs]
    else:
        level_safety = [-1 >= d >= -3 for d in diffs]
    
    safety = all(level_safety)
    if safety or not dampener:
        return safety
    
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if is_safe(new_report):
            return True
    else:
        return False

Report = list[int]


def part1(data: str) -> int:
    reports = parse_reports(data)
    results = list(is_safe(report) for report in reports)
    safe_count = sum(results)
    return safe_count


def part2():
    pass


def parse_reports(data: str) -> list[Report]:
    return [
        list(map(int, line.split())) for line in data.split("\n") if line
    ]


def is_safe(report: Report) -> bool:
    diffs = [two - one for one, two in zip(
        report[:-1],
        report[1:],
    )]
    if diffs[0] >= 0:
        return all(1 <= d <= 3 for d in diffs)
    else:
        return all(-3 <= d <= -1 for d in diffs)

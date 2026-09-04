def job_sequencing(jobs, deadlines, profits):
    data = []

    for i in range(len(jobs)):
        data.append((profits[i], jobs[i], deadlines[i]))

    data.sort(reverse=True)

    max_deadline = max(deadlines)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for profit, job, deadline in data:
        for slot in range(deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job
                total_profit += profit
                break

    selected_jobs = [job for job in slots if job is not None]

    print("Selected jobs =", *selected_jobs)
    print("Maximum profit =", total_profit)


jobs = ["A", "B", "C", "D"]
deadlines = [2, 1, 2, 1]
profits = [100, 19, 27, 25]

job_sequencing(jobs, deadlines, profits)

# job = [(100 , 2 , 'j1'), (19 , 1 , 'j2'), (27 , 2 , 'j3'), (25 , 1 , 'j4'), (15 , 3 , 'j5')]
# def Job_sequnce(job):
#     job.sort(reverse = True)
#     max_deadline = max(job[1] for job in job)
#     total_Profit = Total_count = 0
#     slot = [0] *(max_deadline +1)
#     for profit , deadline , id in job:
#         for j in range(deadline , 0 , -1):
#             if slot[j] == 0:
#                 slot[j] = id
#                 total_Profit += profit
#                 Total_count += 1
#                 break
#     return (total_Profit , Total_count)
# print(Job_sequnce(job))

job = [(100 , 2 , 'j1'), (19 , 1 , 'j2'), (27 , 2 , 'j3'), (25 , 1 , 'j4'), (15 , 3 , 'j5')]
def Job_sequnce(job):
    job.sort(reverse = True)
    max_deadline = max(job[1] for job in job)
    total_Profit = Total_count = 0
    slot = [0] *(max_deadline +1)
    i = 1
    for profit , deadline , id in job:
            if slot[deadline] == 0:
                slot[i] = id
                i +=1
                total_Profit += profit
                Total_count += 1
    return (total_Profit , Total_count)
print(Job_sequnce(job))
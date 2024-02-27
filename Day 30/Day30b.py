# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.
# runner up score is the second highest number in the list

score_sheet = []

while True:
	total_score = input("Enter total score for each team(type done to finish the loop): ")

	if total_score.lower() == "done":
		break
	elif total_score.isdigit():
		score_sheet.append(int(total_score))
	else:
		print("invalid input, it must be an integer")
		continue

runner_up_score = sorted(set(score_sheet))[-2]
print(score_sheet)
print(f"The runner-up score is {runner_up_score}")
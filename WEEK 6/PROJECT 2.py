admitted = []
not_admitted = []

def assess_candidate(name, department, jamb_score, credits, interview_passed):
    if department.lower() == "computer science":
        if jamb_score >= 250 and credits >= 5 and interview_passed:
            admitted.append(name)
        else:
            not_admitted.append(name)
    elif department.lower() == "mass communication":
        if jamb_score >= 230 and credits >= 5 and interview_passed:
            admitted.append(name)
        else:
            not_admitted.append(name)
    else:
        print(f"Unknown department for {name}. Please check the input.")
        not_admitted.append(name)

# Sample usage
assess_candidate("Alice", "Computer Science", 260, 5, True)
assess_candidate("Bob", "Mass Communication", 220, 5, True)
assess_candidate("Chika", "Mass Communication", 230, 5, True)

print("Admitted:", admitted)
print("Not Admitted:", not_admitted)

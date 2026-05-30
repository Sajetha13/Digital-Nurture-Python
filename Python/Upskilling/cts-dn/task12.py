def passFail(score):
    if score >= 75:
        return "Pass"
    else:
        return "Fail"
score = 85
result = passFail(score)
print(f"Score: {score}, Result: {result}")
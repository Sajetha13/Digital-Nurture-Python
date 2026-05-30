def passFail(score):
    if score >= 75:
        return "A"
    elif score >= 55:
        return "B"
    else:
        return "C"
score = 88
result = passFail(score)
print(f"Score: {score}, Result: {result}")
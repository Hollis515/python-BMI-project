def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("體重和身高必須>0")
    
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 25:
        return "正常體重"
    elif 25 <= bmi < 30:
        return "體重過重"
    else:
        return "肥胖"
from BMI import calculate_bmi, get_bmi_category

weight=float(input("請輸入你的體重(kg):"))
height=float(input("請輸入你的升高(cm):"))

bmi=calculate_bmi(weight,height/100)
category=get_bmi_category(bmi)

print(f"你的BMI為:{bmi:.2f}")
print(f"你的BMI分類為:{category}")
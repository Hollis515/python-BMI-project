from bmi import calculate_bmi

weight=float(input("請輸入你的體重(kg):"))
height=float(input("請輸入你的升高(cm):"))

bmi=calculate_bmi(weight,height/100)

print(f"你的BMI為:{bmi:.2f}")
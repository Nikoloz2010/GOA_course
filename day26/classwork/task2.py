#2) შექმენით ერთი ცვლადი რომელშიც შეინახავთ თქვენს სრულ სახელსა და გვარს, ამ სიტყბების პირველი ასოები უნდა იყოს დიდი. შემდეგ for ციკლის მეშვეობით გადაურეთ თქვენს სრულ სახელს და შეამოწმეთ სახელის და გვარის პირველი ასოები თუ დიდი, მათთან აიღეთ კიდევ 3 სხვა დიდი სიმბოლო თქვენი სრული სახელიდან და შეამოწმეთ ასეთი თუ გხვდებათ თქვენი სახელიდან, თუ ასეა მაშინ result ცვლადს (რომელსაც შექმნით for ციკლის გამოყენებამდე და შეინახავთ ცარიელ სტრინგს) დაამატეთ ამ ასოების პატარა ვერსია მაგ: (თუ char == "A": result += "a" 
name="Nika Novikov"
result=""
for symbol in name:
    if symbol == "N":
        result+="n"
    elif symbol=="I":
        result+="i"
    elif result=="K":
        result+="k"
    elif result=="A":
        result+="a"
    elif result=="N":
        result+="n"
    elif result=="O":
        result+="o"
    elif result=="V":
        result+="v"
    elif result=="I":
        result+="i"
    elif result=="K":
        result+="k"
    elif result=="O":
        result+="o"
    elif result=="V":
        result+="v"
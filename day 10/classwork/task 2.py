#მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადებში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე EH (Estimated Height) როდესაც გავა y წელი (რაც მომხმარებლმა შემოიტანა) თუ დაუშვათ  bomjoყოველ წელს სიმაღლე იზრდება 0.5-ით. საბოლოოდ გამოუტანეთ EH
height = input("what is your height")
height = float(height)
age = int(input("what is your age"))
years = input("how many years after?")
height = height(years * 0.5)
print((years * 0.5) + height)
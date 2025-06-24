# ხილის სია - კალათა
basket = ["ვაშლი", "ბანანი", "ატამი", "საზამთრო", "ფორთოხალი"]

# მომხმარებლის საყვარელი ხილის შეყვანა
favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")

# ვადეკლარირებთ ცვლადს რომელიც შეამოწმებს ხილის არსებობას კალათაში
fruit_in_basket = False

# ვამოწმებთ არის თუ არა ხილი კალათაში
for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True
        break

# საბოლოო შემოწმება და შედეგის დაბეჭდვა
if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")
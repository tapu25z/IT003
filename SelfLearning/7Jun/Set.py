
love = {"toan", "li", "hoa"}

love.add("sinh") 
love.discard("li")


need = {"toan", "van", "anh"}


love_and_need = (love & need)

for i in love_and_need:
    print(i)
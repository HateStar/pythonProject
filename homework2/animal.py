# 开发时间 2021/3/21 12:38
# 加油啊测试！！
import yaml

class animal:
    animalName = "name"
    animalColor = "color"
    animalage = 0
    animalGender = "male"
    __level = 0

    def __init__(self,name,color,age,gender):
        self.animalName = name
        self.animalColor = color
        self.animalage = age
        self.animalGender = gender

    def call(self):
        print(f"{self.animalName}在叫了")

    def run(self):
        print(f"{self.animalName}在跑了")

class cat(animal):

    hair = "short"

    def __init__(self,name,color,age,gender):
        super().__init__(name,color,age,gender)

    def catch_mice(self):
        print(f"{self.animalName}在抓老鼠了")
        a = f"{self.animalName}抓住了老鼠"
        return a

    def call(self):
        print(f"{self.animalName}在喵喵叫了")

class dog(animal):

    hair = "long"

    def __init__(self,name,color,age,gender):
        super().__init__(name,color,age,gender)

    def mind_house(self):
        print(f"{self.animalName}在看家了")
        b = f"{self.animalName}看住了家"
        return b

    def call(self):
        print(f"{self.animalName}在汪汪叫了")

if __name__ == '__main__':
    with open("./animal.yaml") as f:
        datas = yaml.safe_load(f)
    data1 = datas["defaultcat"]
    cat1 = cat(name=data1["name"],color=data1["color"],age=data1["age"],gender=data1["gender"])
    cat1.catch_mice()
    print(cat1.animalName,cat1.animalColor,cat1.animalage,cat1.animalGender,cat1.catch_mice())
    data2 = datas["defaultdog"]
    dog1 =dog(name=data2["name"],color=data2["color"],age=data2["age"],gender=data2["gender"])
    dog1.mind_house()
    print(dog1.animalName,dog1.animalColor,dog1.animalage,dog1.animalGender)
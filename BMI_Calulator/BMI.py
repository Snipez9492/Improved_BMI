class BMI:
    num = 703

    def __init__(self, weight: int, height: str, name: str):
        self.weight = weight
        self.height = height
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        if len(name) == 0:
            raise Exception('Please enter your name')

    @name.deleter
    def name(self):
        print('This person has been deleted!')
        del self._name

    def __repr__(self):
        return f'This is from another {self._name}.'

    def get_weight(self):
        if self.isdigit():
            return self.weight
        else:
            raise Exception('Please use an int')

    def get_height(self):
        h = self.height.split("'")
        ft, inches = h[:1], h[1:]
        t = [int(y) for y in inches]
        ft_in = [int(x) for x in ft]
        real_ft = (12 * ft_in[0]) + t[0]
        return real_ft

    def get_bmi(self):
        return round(self.weight / (BMI.get_height(self) ** 2) * BMI.num, 2)

    def get_criteria(self):
        if BMI.get_bmi(self) < 18.5:
            return 'You are underweight, eat a banana!'
        elif 18.5 <= BMI.get_bmi(self) <= 24.9:
            return 'You are in good health'
        elif 25 <= BMI.get_bmi(self) <= 29.9:
            return 'You are overweight, hit the gym!'
        else:
            return 'You need help!!!'


if __name__ == "__main__":
    pass

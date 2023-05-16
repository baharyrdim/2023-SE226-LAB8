from abc import ABC, abstractmethod

class FrequencyCounter(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass

class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_list = []

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        frequency_list.append(char)

        result_list = []
        for char in set(frequency_list):
            frequency = frequency_list.count(char)
            result_list.append(f"{char} = {frequency}")

        for entry in result_list:
            print(entry)

class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_dict = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        if char in frequency_dict:
                            frequency_dict[char] += 1
                        else:
                            frequency_dict[char] = 1

        for letter, frequency in frequency_dict.items():
            print(f"{letter}: {frequency}")

x = ListCount("weirdWords.txt")
x.calculateFreqs()

print("--------------------")

y = DictCount("weirdWords.txt")
y.calculateFreqs()

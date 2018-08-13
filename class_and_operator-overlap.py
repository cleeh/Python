class GeneralMethod:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value
classInstance = GeneralMethod()
print('GeneralMethod.set:',GeneralMethod.set)
print('classInstance.set:',classInstance.set)
GeneralMethod.set(classInstance, 'Unbound Method Call')
print(GeneralMethod.get(classInstance))
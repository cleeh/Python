class GeneralMethod:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value

# Unbound Method Call
classInstance = GeneralMethod()
print('GeneralMethod.set:',GeneralMethod.set)
print('classInstance.set:',classInstance.set)
GeneralMethod.set(classInstance, 'Unbound Method Call')
print(GeneralMethod.get(classInstance))
print('')

# Bound Method Call using instance object
classInstance2 = GeneralMethod()
print('classInstance2:',classInstance2)
print('classInstance2.set:',classInstance2.set)
classInstance2.set("Bound Method Call")
print('classInstance2.get():',classInstance2.get())
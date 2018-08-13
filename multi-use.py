stage = int(input('What stage do you want? '))
for x in range(1,10):
    print(stage,'*',x,'=',int(stage * x))
print('')

queue = []
while True:
    data = input('input data = ')
    if(data == 'q'): break
    queue.append(data)
for x in range(len(queue)):
    print("Sequence:",x + 1,"Data:",queue[x])
print('')

stack = []
while True:
    data = input('input data = ')
    if(data == 'q'): break
    stack.append(data)
for x in range(len(stack)):
    print("Sequence:",x + 1,"Data:",stack[len(stack)-x-1])
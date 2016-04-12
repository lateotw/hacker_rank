N = int(input())

def list_action(my_list, action, params = None):
    if action == 'append':
        my_list.append(params[0])
    elif action == 'extend':
        my_list.extend(params)
    elif action == 'insert':
        my_list.insert(params[0], params[1])
    elif action == 'remove':
        my_list.remove(params[0])
    elif action == 'pop':
        my_list.pop()
    elif action == 'index':
        my_list.index(params[0])
    elif action == 'count':
        my_list.count(params[0])
    elif action == 'sort':
        my_list.sort()
    elif action == 'reverse':
        my_list.reverse()
    elif action == 'print':
        print(my_list)

my_list=[]
for i in range(N):
    int_line = input().split()
    action = int_line[0]
    if len(int_line) > 1:
        params = list(map(int, int_line[1:]))

    if params:
        list_action(my_list, action, params)
        # print(' '.join(list(map(str, my_list))))
    else:
        list_action(my_list, action)
        # print(' '.join(list(map(str, my_list))))

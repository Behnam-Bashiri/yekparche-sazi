import random
sug_dict = {
    'a' : [
        'apple','ant','abs'
    ],
    'b':[
        'banan','branch','bus'
    ],
    'c':[
        'circule','client','client'
    ],
    'd':[
        'dad','dog','danger'
    ],
    'e':[
        'egg','eagle','euro'
    ],
    'f':[
        'fish','file'
    ],
    'g':[
        'gold'
    ],
}
while True:
    input_u = input("enter string :\n->")
    if input_u !="exit":
        last_char = input_u[-1]
        if last_char in sug_dict:
            selector = random.randint(0, len(sug_dict[last_char])-1)
            print(sug_dict[last_char][selector])

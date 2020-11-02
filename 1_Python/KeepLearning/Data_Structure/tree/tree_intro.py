myTree = [
    'a', 
        ['b', 
            ['d',[],[]], 
            ['e',[],[]] 
        ], 
        ['c', 
            ['f',[],[]], 
            []
        ] 
] 

msg = """
{0}
Root: {1}
Left Sub-Tree: {2}
Right Sub-Tree: {3}
""".format(myTree, myTree[0], myTree[1], myTree[2])
print(msg)
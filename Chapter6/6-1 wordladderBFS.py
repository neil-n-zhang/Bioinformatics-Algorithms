#Equivalent Words problem
import string
def new_nodes(words):
    newwords=[]
    nodes=set()
    for l in list(range(len(words))):
        newwords=list(words)
        for j in string.ascii_lowercase:
            newwords[l]=j
            nodes.add(''.join(newwords))
    return nodes

def wordladder(start,end,dictionary=set()):
    node={start}
    while len(node)!=0:
        print(node)
        newnodes =set()
        for word in node:
            newwords=new_nodes(word)
            if end in newwords:
                print(end)
                return
            else:
                newwords={word for word in newwords if word in dictionary}
                newnodes=newwords | newnodes
        node=newnodes.copy()
        #remove the already used words from dictionary, prevent going backwards
        dictionary=dictionary-node
    return print(start,'and',end,'are not equivalent')

wordladder('hit','cog',{"hot","dot","dog","lot","log","cog"})

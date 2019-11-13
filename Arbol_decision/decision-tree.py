import math 
def calculo_entropia(examples):
    si_no =[0,0]
    for i in range (len(examples)):
       if examples[i][4] =="yes":
           si_no[0] =si_no[0]+1
       else:
           si_no[1] =si_no[1]+1

    entropia = (-1*si_no[0]/len(examples))*math.log2(si_no[0]/len(examples))-(si_no[1]/len(examples))*math.log2(si_no[1]/len(examples))
    return entropia

def pluraty_value(examples):##Este la decision que toma la mayoria 
    count_yes = 0
    count_no = 0
    for i in range(len(examples)):
        if examples[i][4] == "yes" :
            count_yes+=1
        else :
            count_no+=1

def same_clasification(examples):"cambiar decision por la columna que toma la decision"
    value = examples[0][4] 
    for i in range(1,len(examples)):
        if examples[i][4] == value:
            continue
        else:
            return False 
    return True
def decision_tree(examples,attributes,parent_examples,entropia):
    #La entropia es facil 
    if len(examples) == 0:
        return parent_examples 
    else: 
        if same_clasification(examples):#aca deberia devolver el atributo que lo clasifica 
            return pluraty_value(examples)
        else:
            if len(attributes)==0:
                pluraty_value(examples)
            else:
                a = importance(examples,Entropia)

                tree = Tree(a)
                m = pluraty_value(examples)

                for i in a :

                    examples = extraer(examples,i)
                    subArbol = decision_tree(examples,attributes.remove(a),m)
                    tree.insert(subArbol)
                return tree
                

        
        

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

a,s,b = (input()).split(' ')

print("operand : ",a,"\noperand : ",b,"\noperator : ",s)

print (ops[s](int(a),int(b)))
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
    '%' : operator.mod,
}

def eval_binary_expr(op1, op2, oper):
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)

print(eval_binary_expr(1,2,'+'))
print(eval_binary_expr(4,2,'/'))
print(eval_binary_expr(6,2,'-'))
print(eval_binary_expr(3,3,'*'))



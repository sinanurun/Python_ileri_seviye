# 1 * Note: You may get different value of id
#
# a = 2
# # Output: id(2)= 10919424
# print('id(2) =', id(2))
#
# # Output: id(a) = 10919424
# print('id(a) =', id(a))

# 2 * Note: You may get different value of id
#
# a = 2
# # Output: id(a) = 10919424
# print('id(a) =', id(a),id(2))
# a = a+1
# # Output: id(a) = 10919456
# print('id(a) =', id(a))
# # Output: id(3) = 10919456
# print('id(3) =', id(3))
# b = 2
# # Output: id(2)= 10919424
# print('id(2) =', id(2),id(b))
# c = 3
# print(id(c),id(c))

# # 3* note
# def printHello():
#     print("Hello")
# a = printHello()
#
# # Output: Hello
# a
# print(id(a),a)

#  4 *Note
# def dis_fonk():
#     b = 20
#     def ic_fonk():
#         c = 30
# a = 10
# print(a)

#  5 * note
# def dis_fonk():
#     a = 20
#     def ic_fonk():
#         a = 30
#         print('a =', a)
#     ic_fonk()
#     print('a =', a)
# a = 10
# dis_fonk()
# print('a =', a)

#  6 * note
# def dis():
#     global a
#     print(a)
#     a = 20
#     print(a)
#     def ic():
#         global a
#         a = 30
#         print('a =', a)
#     ic()
#     print('a =', a)
# a = 10
# dis()
# print('a =', a)

# 7 * note
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
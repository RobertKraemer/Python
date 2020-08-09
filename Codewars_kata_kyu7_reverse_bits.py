#for a better understanding!
'''
>>> '{0:08b}'.format(6)
'00000110'

Just to explain the parts of the formatting string:

    {} places a variable into a string
    0 takes the variable at argument position 0
    : adds formatting options for this variable (otherwise it would represent decimal 6)
    08 formats the number to eight digits zero-padded on the left
    b converts the number to its binary representation

If you're using a version of Python 3.6 or above, you can also use f-strings:

>>> f'{6:08b}'
'00000110'
'''

'''
Write a function that reverses the bits in an integer.

For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative.
'''
def reverse_bits(n):
    reverse = '{0:10b}'.format(n)
    reverse = reverse[::-1]
    #clear_number = '{0:d}'.format(int(reverse)) #not needed!
    return int(reverse, 2)

print(reverse_bits(417))

'''
>>> 'hello world'[::-1]
'dlrow olleh'

This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and 
end off and specifying a step of -1, it reverses a string.
'''

#better version of the code !!!
'''
def reverse_bits(n):
    return int(f'{n:b}'[::-1],2)
'''




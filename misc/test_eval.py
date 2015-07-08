
# eval
def main():
    dictString = "{'Define1':[[63.3,0.00,0.5,0.3,0.0],[269.3,0.034,1.0,1.0,0.5]," \
                 "[332.2,0.933,0.2,0.99920654296875,1],[935.0,0.990,0.2,0.1,1.0]]," \
                 "'Define2':[[63.3,0.00,0.5,0.2,1.0],[269.3,0.034,1.0,0.3,0.5]," \
                 "[332.2,0.933,0.2, 0.4,0.6],[935.0,0.990,1.0, 0.5,0.0]],}"
    dict = eval(dictString)

    print("keys: ", dict.keys())
    print("Define1 value ", dict['Define1'])

# execfile
execfile("test_list.py")

if __name__ == '__main__':
    main()

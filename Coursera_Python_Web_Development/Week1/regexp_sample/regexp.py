def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)[=]([abc]?)([0-9-+]*)")  # Если придумать хорошую регулярку, будет просто
    print("start with", data)
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        print("v1 is",v1,"sign",s,"v2 is",v2,"value", n)
        #print(int(str(n)))
        if n=='':
            n = 0
        if s == "+":
            print("plus sign")
            if v2 == "a" or v2 == "b" or v2 == "c":
                print("second variable")
                data[v1] = data[v1]+data[v2]+int(n)
            else:
                print("add number")
                data[v1] = data[v1] + int(n)
        elif s == "-":
            if v2 == "a" or v2 == "b" or v2 == "c":
                data[v1] = data[v1]-(data[v2]+int(n))
            else:
                data[v1] = data[v1] - int(n)
        else:
            print("no sign")
            if v2 == "a" or v2 == "b" or v2 == "c":
                data[v1] = data[v2]+int(n)
            else:
                data[v1] = int(n)


        #data[v1] = data.get(v2, 0) + int(n or 0)
        print(data)

    return data

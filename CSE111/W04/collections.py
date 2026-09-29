#clist=[1,2,3,['a','b','c']]
#print(clist[3])
# book={'name':'1 Nephi',
# 'chapters':20} 
# book['stdwork']='2 Nephi'
# print(book['stdwork'])
# del book['stdwork']
# print(book)

#example 01
# -------------------------------- 
#    def main():
#        colors = ["yellow", "red", "green", "yellow", "blue"]
#        lenght = len(colors)
#        print(f"Number of elements: {lenght}")
#        print(colors[2])
#        colors[3] = "purple"
#        print(colors)
#    if __name__ == "__main__":
#        main()
# --------------------------------

#example 02
#print("-" * 50)
#def main():
#    fabrics = []
#    fabrics.append("velvet")
#    fabrics.append("denim")
#    fabrics.append("gingham")
#    fabrics.insert(0, "chiffon")
#    print(fabrics)
#
#    if "gingham" in fabrics:
#        print("gingham is in the list.")
#    else:
#        print("gingham is NOT in the list.")
#
#    i = fabrics.index("velvet")
#    fabrics[i]= "taffeta"
#    fabrics.pop()
#    fabrics.remove("denim")
#    n = len(fabrics)
#    print(f"The fabrics list contains {n} elements.")
#    print(fabrics)
#if __name__ == "__main__":
#    main()
#print("-" * 50)

#example 03
#print("-" * 50)
#def main():
#    colors=["red", "orange", "yellow", "green", "blue"]
#    for colors in colors:
#       print(colors)
#if __name__ == "__main__":
#    main()
#print("-" * 50)

# Example 4
#def main():
    # Count from zero to nine by one.
#    for i in range(10):
 #       print(i)
 #   print()
    # Count from five to nine by one.
 #   for i in range(5, 10):
   #     print(i)
   # print()
 #   # Count from zero to eight by two.
 #   for i in range(0, 10, 2):
 #       print(i)
 #   print()
    # Count from 100 down to 70 by three.
 #   for i in range(100, 69, -3):
 #       print(i)
# Call main to start this program.
#if __name__ == "__main__":
#    main()
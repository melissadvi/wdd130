def main():
    fabrics = []
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    fabrics.insert(0, "chiffon")
    print(fabrics)
    i = fabrics.index("velvet")
    fabrics[i] = "taffeta"
    fabrics.pop()
    fabrics.remove("denim")
    print(fabrics)
if __name__ == "__main__":
    main()
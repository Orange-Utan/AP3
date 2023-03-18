def tabularX():
    spalte = dict()
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header1" + "}"] = [1, 2]
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header2" + "}"] = ['a', 'b']
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header3" + "}"] = [1, 9]
    textabular = f"|{'c|' * len(sorted(spalte))}"
    # texheader = " & " + " & ".join(headers) + "\\\\"
    # texheader = " & ".join(headers) + "\\\\"
    texheader = " & ".join(spalte.keys())
    texheader = texheader + ' &'
    # texdata = "\\hline\n"
    texdata = ""
    for i in range(0,len(spalte)-1):
        texdata += '\\hline'
        for label in sorted(spalte):
            texdata += str(spalte[label][i]) + ' & '

    print("\\begin{table}[]")
    print("\\centering")
    print("\\resizebox{\columnwidth}{!}{")
    print("\\begin{tabular}{" + textabular + "}")
    print("\\hline")
    print(texheader)
    print(texdata, end="")
    print("\\hline")
    print("\\end{tabular}")
    print("}")
    print("\\caption{Berücksichtigte Ungenauigkeiten}")
    print("\\label{tab:Ungenauigkeiten}")
    print("\\end{table}")
tabularX()

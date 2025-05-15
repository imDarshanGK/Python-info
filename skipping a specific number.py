for i in range(1, 11):
    if i == 3:
        print("Skipped number 3")
        continue
    if i == 7:
        print("Terminated at number 7")
        break
    print(i)

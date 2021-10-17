def word_count():
    count = 0

    with open("/Users/mordehaic/Projects/final-project/jenkins-project/file.txt") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "Avraham":
                    count+= 1

    print(count)
    return count
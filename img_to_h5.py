for i in range(0, len(filenames)):
    if filenames[i] == "":
        continue        
    npydata = np.load("./data/npy/" + filenames[i] + ".npy")

    print(npydata.shape)

    for j in range(0, 2048):
        a_data[i, j] = [npydata[j][0], npydata[j][1], npydata[j][2]]

data = f.create_dataset("data", data = a_data)
f.close()

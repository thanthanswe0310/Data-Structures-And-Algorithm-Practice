def keys(self):
    all_keys =[]
    for i in range(len(self.data_map)):
        if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
                all_keys.append(self.data_map[i][j][0])

    return all_keys


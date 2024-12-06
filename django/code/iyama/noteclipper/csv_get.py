def get(file_name):
    csv_file = request.FILES.get(file_name)

    for line in csv_file:
        line_count += 1

        if line_count <= 2:
            continue

        try:
            line_list = str(line.decode()).split(",")
        except UnicodeDecodeError:
            line_list = str(line.decode('cp932')).split(",")

        for columun in line_list:
            print(str(columun))

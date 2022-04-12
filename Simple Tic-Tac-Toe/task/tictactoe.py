def print_dashes_line():
    print("---------")


def create_data_matrix(input_cells, num_of_strs, num_of_symbols):
    data_mtrx = []
    k = 0
    for i in range(num_of_strs):
        data_mtrx.append([])
        for j in range(num_of_symbols):
            data_mtrx[i].append(input_cells[k])
            k += 1
    return data_mtrx


def update_data_matrix(data_mtrx, coordinates, current_smbl):
    data_mtrx[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = current_smbl
    return data_mtrx


def print_data(data_mtrx):
    print_dashes_line()
    for i in range(len(data_mtrx)):
        str_row = "| "
        for j in range(len(data_mtrx[i])):
            str_row += data_mtrx[i][j]
            str_row += " "
        str_row += "|"
        print(str_row)
    print_dashes_line()


def analyze_data(data_mtrx):
    is_empty_cells = False
    is_three_in_a_row = False
    is_x_wins = False
    is_o_wins = False
    is_game_over_ = False
    num_of_x = 0
    num_of_o = 0

    for i in range(len(data_mtrx)):
        temp_str = ""
        for j in range(len(data_mtrx[i])):
            temp_str += data_mtrx[i][j]
            if data_mtrx[i][j] == "X":
                num_of_x += 1
            elif data_mtrx[i][j] == "O":
                num_of_o += 1
        if temp_str == "XXX" or temp_str == "OOO":
            is_three_in_a_row = True
            if temp_str == "XXX":
                is_x_wins = True
                is_game_over_ = True
            if temp_str == "OOO":
                is_o_wins = True
                is_game_over_ = True
        elif temp_str.__contains__("_"):
            is_empty_cells = True

    for i in range(len(data_mtrx)):
        temp_str = ""
        for j in range(len(data_mtrx[i])):
            temp_str += data_mtrx[j][i]
        if temp_str == "XXX" or temp_str == "OOO":
            is_three_in_a_row = True
            if temp_str == "XXX":
                is_x_wins = True
                is_game_over_ = True
            if temp_str == "OOO":
                is_o_wins = True
                is_game_over_ = True
        elif temp_str.__contains__("_"):
            is_empty_cells = True

    temp_str = ""
    for i in range(len(data_mtrx)):
        temp_str += data_mtrx[i][i]
    if temp_str == "XXX" or temp_str == "OOO":
        is_three_in_a_row = True
        if temp_str == "XXX":
            is_x_wins = True
            is_game_over_ = True
        if temp_str == "OOO":
            is_o_wins = True
            is_game_over_ = True
    elif temp_str.__contains__("_"):
        is_empty_cells = True

    temp_str = ""
    for i in range(len(data_mtrx)):
        temp_str += data_mtrx[i][len(data_mtrx) - i - 1]
    if temp_str == "XXX" or temp_str == "OOO":
        is_three_in_a_row = True
        if temp_str == "XXX":
            is_x_wins = True
            is_game_over_ = True
        if temp_str == "OOO":
            is_o_wins = True
            is_game_over_ = True
    elif temp_str.__contains__("_"):
        is_empty_cells = True

    if abs(num_of_x - num_of_o) >= 2:
        print("Impossible")
        is_game_over_ = True
    # elif is_empty_cells and not is_three_in_a_row:
    #     print("Game not finished")
    elif not is_empty_cells and not is_three_in_a_row:
        print("Draw")
        is_game_over_ = True
    elif is_x_wins and not is_o_wins:
        print("X wins")
        is_game_over_ = True
    elif is_o_wins and not is_x_wins:
        print("O wins")
        is_game_over_ = True
    elif is_o_wins and is_x_wins:
        print("Impossible")
        is_game_over_ = True

    return is_game_over_


def check_coordinates(data_mtrx, coordinates):
    is_all_correct = False
    is_num = True
    is_from_one_to_three = True

    for _, val in enumerate(coordinates):
        if not val.isdigit():
            is_num = False

    if is_num:
        for _, val in enumerate(coordinates):
            if int(val) not in range(1, 4):
                is_from_one_to_three = False

        if is_from_one_to_three:
            if data_mtrx[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" or data_mtrx[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                is_all_correct = True
                data_mtrx[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
                # print_data(data_mtrx)
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

    return is_all_correct


def create_empty_grid(num_of_rows, num_of_cols):
    init_cells = "_" * num_of_rows * num_of_cols
    print_data(create_data_matrix(init_cells, num_of_rows, num_of_cols))
    return init_cells


rows = 3
cols = 3
cells = create_empty_grid(rows, cols)
data = create_data_matrix(cells, rows, cols)

current_symbol = "X"
is_game_over = False

while not is_game_over:
    coord = input("Enter the coordinates: ").split()
    is_coord_correct = False
    while not is_coord_correct:
        is_coord_correct = check_coordinates(data, coord)
        if not is_coord_correct:
            coord = input("Enter the coordinates: ").split()
    data = update_data_matrix(data, coord, current_symbol)
    print_data(data)
    is_game_over = analyze_data(data)
    if current_symbol == "X":
        current_symbol = "O"
    else:
        current_symbol = "X"

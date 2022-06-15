from core.level_sample import Level as Level

# Описание всех уроовней в игре
# Level ([(vertex_x, vertex_y)], [(vertex_number, vertex_number)])
EASY_1 = Level([(411, 162), (411, 454), (565, 454), (565, 250), (699, 294), (699, 103), (565, 162)],
               [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [3, 6]])
EASY_2 = Level([(287, 234), (542, 67), (795, 234), (721, 475), (369, 475)], [[0, 3], [0, 2], [1, 3], [1, 4], [2, 4]])
EASY_3 = Level([(426, 78), (426, 332), (426, 526), (716, 78), (716, 332)], [[0, 1], [0, 3], [1, 2], [1, 3], [1, 4],
                                                                            [2, 4], [3, 4]])
EASY_4 = Level([(332, 42), (332, 478), (766, 42), (766, 478), (554, 260)], [[0, 1], [0, 4], [1, 3], [1, 4], [2, 3],
                                                                            [2, 4], [3, 4]])
EASY_5 = Level([(391, 155), (542, 155), (693, 155), (468, 53), (618, 53),
                (391, 395), (542, 395), (693, 395), (468, 478), (618, 478)
                ], [[0, 1], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4],
                    [0, 5], [2, 7],
                    [5, 8], [6, 8], [6, 9], [7, 9]])



def navigate_trees(layout):
    x = 0
    y = 0
    trees = 0
    while True:
        x = x + 3
        if x > 30:
            x = x - 31
        y = y + 1
        if layout[y][x] == "#":
            trees = trees + 1

        # End condition
        if y == 322:
            print(trees)
            return trees




puzzleInput = ["..#......###....#...##..#.#....",
".#.#.....#.##.....###...##...##",
"..#.#..#...........#.#..#......",
"..#......#..........###........",
"...#..###..##.#..#.......##..##",
"......#.#.##...#...#....###....",
"..........##.....##..##......#.",
"......#...........#............",
"#....#..........#..............",
".#........##.............###.##",
"....#.........#.......#.#....##",
"#.#..#..#..#.......#...#....##.",
".#........#......#.##.......#..",
"..#.....#####.....#....#..#..##",
".......#..##.......#......#.###",
"..#.#...#......#.##...#........",
"##...................#...##..#.",
"......#...#.##...##.#......#..#",
".#.................#..##...#...",
"...#.....#.......##.....#.#....",
".......#.#......#.....#..#..##.",
"..........#........#...........",
"..#.#..........................",
".#.##..#.#...#...#.........#...",
".....#....#.....#..#.....#.....",
"...#.#.#.....#.#..#.......#..#.",
".....#...###...##...#......##..",
"#.###......#.#...#.#.#..###....",
"#.....#..##......#..........#.#",
"#...............#........#.#..#",
".....#..#.........#......##.#..",
".....#.##.##..#..##............",
"...#......##...............#.#.",
".#..#.#............##.#........",
"#.....#..###.............##.#..",
"...##..#.#..#...........#..#...",
"#....#.........#.#.............",
"##.#.........#..###......#.#..#",
"...#...#......#.#.#.##..#.##...",
".....##............#.##.##..#..",
"....#................#.##..#..#",
"...#..#.......#...#..#........#",
"....#...#...#................#.",
"....##...............#.#...#...",
".#.....###...#.......#.##......",
"....######.#..............###.#",
".#..#.........##...............",
"................##.#..#....###.",
".......#............#.#..#..#..",
"......#.#...............##.#...",
"...#..####.#...#..#..#......#..",
"....#.#...#.....#.........#..##",
".##..#...#......##....##.#.#...",
".##.#.........##...#....#......",
"..#.#..#...#.#..#.......#...#.#",
".........#..#.....##..#........",
"..#......#..##.....#..#...###..",
"..#...#....#.#..#..#.#.#..#.#..",
"...#..#####.....#......#.......",
"#.#............#......#..#...#.",
".........#..........###.......#",
"......#....#..#.##.#......#..#.",
"...........##.#....#.#..#......",
"..#...................#..#.#...",
"#....##.............##....#...#",
"##..#....#.........#..........#",
"....#.#.#...#..#........#.##..#",
"...............#...#..##..#....",
".##.......#.......#...........#",
"#.........................##...",
"#........#.#..#..##..####.#....",
"...................##.....###..",
".#.......#..#......#......#...#",
"..#.........#...#..........#...",
"..........#......#....#........",
".#......#..#...#..#...##....##.",
"...#.#..#..#......#.....##.####",
".......#.#....#.......#........",
"#...#.#...##..##.#......#......",
".#.........#...................",
"...#..........#.#......#.......",
"...#.....##....#..........#....",
".#..........##..#..#..##....#.#",
".##.#..........#...#.##.......#",
"#...###....#..#.#...#..#.......",
"..................##...........",
"..#...##.#...........#....#.##.",
"..#......#..##..#....##..#...#.",
"..#....#.....#.##..#.......#..#",
"#...#....#..#.#....#......##...",
".......##..#..........#........",
"..#.............##.#.....#...#.",
"...............#....#...#...##.",
"##...........#.......#.##......",
"#..#...........#.........#.....",
"....###.............###.##..##.",
".........#.#.....###.......#...",
"..#.##....#.#..........#....#..",
"#........#....##...#..#........",
"......#..........###..#.#......",
".....#.#......##.....#..##...#.",
".#.......#......#...#...#...#.#",
".#..........##.......#.....##.#",
"###.#...#....#.....#...#......#",
"..#.#.#..#.##.#..#.............",
".....#.........................",
".#..###..#...#...#..#..#...#.#.",
"#................##...##.##....",
"......#...#...#..........#...#.",
"..........#.....##.............",
"..#.#......#........#.......#..",
"........##.............#.......",
".......#......#.##.#..#........",
"#.#.#....#........#..........#.",
"##..##......#..#..#.....#.#..##",
"##..#..........#...............",
"#.....##...#.#......#.......#.#",
"#.....#...#....#..#.....##.....",
"##..........#.#.....#....#...##",
"..##.###..#.....#.......#...#..",
".#.#.......#......###........#.",
".#..............#.#..###.......",
".#....#..##.........#..#.#.....",
"....#....#.#....#..#.......##.#",
"#.......#.......#.........#....",
"...#....#....#.....##..#..#.#.#",
"........#....#...........#.....",
".#......##.#.#.##..............",
"#..#.#.....##........#........#",
"##...#.#.......##.......#...#..",
"#...#.....#.##...##.#.....#....",
"....#..##...#........#.#...#...",
"...#....#.#.#..###...##.#.....#",
"......#..#.....#..#........##..",
".......#.....#.#.........#.#..#",
"..#.......#.#.#.#.#....#.##...#",
".#...#........#..##..#......#..",
".#..#............#...#..#.#....",
"...##......#......#............",
"..#...#.#.....#.....#..##.#....",
".#......#.#......#..#.#........",
"..#..........##...#.#.....#..#.",
"#...#.....#..#...#.............",
"..##.................#....#....",
".#....#.......#..##....#......#",
".#....###............##....##.#",
"##..#........#..#...#.......#..",
".....#.....#.#.#.##.........#..",
".......#..#....#...#...#.......",
"...#...#...#.#.#..#.#.....#....",
"#.#........#..#.##..#..###.....",
"..................#..#.........",
"#.#.....#..##.........#.......#",
"###..#.......#..............#..",
"......#..#.....###..........#..",
"....#.#...#..#...........#.#...",
"...#.....#.......#.....#.#.....",
"#.....##..#......##...........#",
"#...###...........##..#...#.##.",
"......##.##.#...#..#....#......",
"...#.#......##.#......##....#.#",
"..............#.#.###.......#..",
"........#....#.......##..#..###",
"...#.....##.#....#......##..#.#",
"..##........#.....#.#..#...#...",
".#..#.##.........#.....#...#..#",
"..#..#....#...........#........",
".#...#....................#....",
"##.....##....#.............#.#.",
"....#.#..#.#..#.#.#..........##",
".............##.#.....#..#..#..",
".#....#.....##...#.###.........",
"..#........#........#.#..###...",
".##....#...#...#.......#...#.#.",
"..#...#...#..##........#..#....",
"..##.#..#..#.....#......#.#..#.",
".#........#..#....#..#.........",
"..#.#.....#.##..#........###.#.",
".....#.##.....##.#.............",
"#.........#.......#...##...#...",
"..#.##.#..#..#............#....",
".##....#..#............#.....#.",
"###........##.....##.#...#.....",
"#......##..##.#.#.#.#.#.#..##..",
".....###.....#....#......#....#",
"........#.........##...#....#.#",
".#.#.....#.#..#..##......#...#.",
"...#.##....#..#.###..#..##.....",
"....#..........##..#..#..#..#..",
"...#..#.##..#..#....#.........#",
".....#..###.#.....#.....#..#...",
"......#...#....#.##...#.#......",
".#.###..##.....##.##......##...",
".....#.#...........#.#.........",
"#........#...#..#......##.#....",
"..#.......##....##....#.##.#..#",
"...###.#.........#......#.....#",
"..#.##..#....#.....##...#.##...",
"....##.##.............#...#....",
"##..#...#..#..#..#.............",
".....#.....#.....#.............",
"...#.##.......#..#.#.....#....#",
"#.....##.........#......##.....",
".....##..........#..#...#..#...",
"#...###....#.......#...##......",
".#....#..#......#.....#...#.#..",
"#........#.#.#...#.....###.#.##",
"##...#...##..#..#....#.........",
"....#............#..#.....#....",
"#......#.........##....#.......",
".#..#..#........#.............#",
".##..........#......#.......#..",
"#............#..#....#.........",
"....#.#.....#.##...#.....#.#...",
"...#.#..#...##..#...#.#.#......",
"#....#..#.........##..#.#.#..##",
".#...#..............#.......#..",
"#...#.....#.#........##......##",
"...#....##.####.#.........#.#.#",
"....###.#..#............#.#..#.",
"....#......#...#......##.#.#.#.",
".....#..#.#.##.#...##..........",
"##..#...#.#...###.............#",
"....#...#..#.....#.#..#..#..#..",
"#..........####......#.....###.",
".........#........#.##.#...#...",
".........#..........#.#..###...",
".....##........##.........#...#",
"..##....#...#.......##.........",
".....#.#......##....#...#...#..",
".##..#..##.....................",
".......#...#..#..#...##....#...",
".#...#.......###...#..#..#.....",
".......#.....##.##.#.......#..#",
".##......#...#....#..#......##.",
".##....#..#....#...#...#.......",
".........##..#..#.#.#.....##...",
"...#..............#..#.....####",
".#.#.#..#.......#.......#......",
"..#.#......#..........#........",
".#...#.#..#.......#..#..#..#...",
".......##.#...#..#....#.....#..",
".##...##....##...#........####.",
"....#.#..##....#...#....#.#....",
".....#.....#..#..#.#.##..#.....",
"..#....#..............#....#...",
"..#.#.#.....##.#.....#..##.....",
"....#.....#....#...#...#..#.#..",
"#...#...........#..#..#........",
"...#.#..#.........##.#...#..##.",
"......#.#.........#.#...#......",
"......#..##.###......##.#....#.",
".....#...#..#.......#..........",
".#...#.......#.....###......#..",
"...........##.....#..#..#....#.",
"..#....#..#...#......#.......#.",
"..#...#...#.#..#....#...#......",
".......#....###.####...###.#...",
"#.##.#.......#.......#....#.#.#",
".##..........#.....#..###......",
".....#...........#.##..#....#..",
"........##.....#.#........##...",
"#..#..#..................##....",
"#...###..........#.............",
".......#.#.......#.#.......##..",
".....#.#...#....#...####.....#.",
"..##.....##.......#....#.......",
"##..........#...#..##....##....",
"..........#..#......#........#.",
"##..#....#..#....#.....##....#.",
"##.##.....#...##.##.......#....",
"..#..#.###.#..##.#..#..#...#...",
".#..#.....#........#...##.#....",
"..#..#.....#.#......##.#.#.....",
".#..##...#.#....#...#...#.#.##.",
".........#...#....###.#.....#..",
"...........###.#.#..#..#...#.#.",
"##...#......##...........#..#..",
".........##..#...#.......#.....",
"#......#.#..........#..#.......",
"...#.................#....#....",
"#....#......................##.",
"##.......#..#......#.#...###.#.",
"..#....#..#.#......#...........",
"...#...........###.#.#.........",
"..#..##.....#.....##...##......",
"..#..#.#.#.#..#..#..##....#...#",
"#......##.....##..##.##...#....",
"#.....#.....#.#........#.......",
".#.....#.................#....#",
".###....#...#............#.#.#.",
".#...#.#......#.#..............",
"....#...#......#.....#.......#.",
"........#.....#..........#....#",
"#..#......#...#...#.........#..",
"#....#......#...##.#...#...#...",
"#...#....#....#..#..#.....#..#.",
"#......##..#..#.#.#..#.#.......",
"..#..#...............#...##...#",
"............#..............#.##",
".#.#.#......##.......#.......#.",
"....#.........##.......#...###.",
".......#.#...#.#.#.......#.....",
"....#..#..#...#....#.##.#.##...",
"...##.##.#...#......#..........",
"#.....#...#.#...#.##..##.#.....",
".......#.....#...#.#...##.#....",
".#.............#.....#....##..#",
"##......#.......#...#....#.....",
".###......#.................#..",
"#.#......##.........##..#......",
"...#....#..........#.#.........",
"..##..#.........#..............",
".....#...#..................#.#",
".............#.........#...#..#",
"....#....#......#.#.......#...#",
"#..#............#.#.......#...#",
"..#.....#............#.........",
".#.....................###....#",
"........#.####.........#.#.#...",
"#...........##...#.........#..#",
"...........#..#......#...#.#...",
"....##...##.....#.....#........"
]

navigate_trees(puzzleInput)
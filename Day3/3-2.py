def navigate_trees(layout):
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
   
    counts = []
    for slope in slopes:
        trees = 0
        x = 0
        y = 0
        while True:
            x = x + slope[0]
            if x > 30:
                x = x - 31
            y = y + slope[1]
            if y > 322:
                counts.append(trees)
                break
            if layout[y][x] == "#":
                trees = trees + 1
            # End condition
            if y == 322:
                counts.append(trees)
                break
    print(counts)
    return counts




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
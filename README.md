# maze-constructor
Generates and solves an ASCII maze.

Currently ~~undergoing sporadic redesign~~ is a dumpster fire.

# Specifications
* The maze should consist of cells in a square grid of any width or length.
* Every cell of the maze should be traversable.
* Every cell should know if an adjacent cell can be traversed into from itself.
* Exactly Two opposite edge cells should be Start and Goal respectively.
* Should use ═ ║ ╔ ╗ ╚ ╝ for outer walls.
* Should use # for walls between cells.
* Should use ─ │ ┌ ┐ └ ┘ for search path.
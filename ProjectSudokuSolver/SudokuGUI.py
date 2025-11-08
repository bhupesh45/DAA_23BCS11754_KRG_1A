# -*- coding: utf-8 -*-
from sudokutools import valid, solve, find_empty, generate_board
from copy import deepcopy
from sys import exit
import pygame
import time

pygame.init()


# ---------------- TILE CLASS ----------------
class Tile:
    def __init__(self, value, window, x, y):
        self.value = value
        self.window = window
        self.rect = pygame.Rect(x, y, 60, 60)
        self.selected = False
        self.correct = False
        self.incorrect = False

    def draw(self, color, thickness):
        pygame.draw.rect(self.window, color, self.rect, thickness)

    def display(self, value, position, color):
        font = pygame.font.SysFont("lato", 45)
        text = font.render(str(value), True, color)
        self.window.blit(text, position)

    def clicked(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.selected = True
        return self.selected


# ---------------- BOARD CLASS ----------------
class Board:
    def __init__(self, window):
        self.window = window
        self.generate_new_board()

    def generate_new_board(self):
        """Generate new Sudoku puzzle."""
        self.board = generate_board()
        self.solvedBoard = deepcopy(self.board)
        solve(self.solvedBoard)
        self.tiles = [
            [Tile(self.board[i][j], self.window, j * 60, i * 60) for j in range(9)]
            for i in range(9)
        ]

    def draw_board(self):
        """Draw Sudoku grid."""
        for i in range(9):
            for j in range(9):
                # grid lines
                if j % 3 == 0 and j != 0:
                    pygame.draw.line(self.window, (0, 0, 0), (j * 60, 0), (j * 60, 540), 3)
                if i % 3 == 0 and i != 0:
                    pygame.draw.line(self.window, (0, 0, 0), (0, i * 60), (540, i * 60), 3)
                self.tiles[i][j].draw((100, 100, 100), 1)

                if self.tiles[i][j].value != 0:
                    self.tiles[i][j].display(self.tiles[i][j].value, (21 + j * 60, 16 + i * 60), (20, 20, 20))
        pygame.draw.line(self.window, (0, 0, 0), (0, 540), (540, 540), 3)

    def deselect(self, tile):
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j] != tile:
                    self.tiles[i][j].selected = False

    def redraw(self, elapsed_time, solving):
        """Redraw full screen with board and info."""
        self.window.fill((240, 248, 255))
        self.draw_board()

        font = pygame.font.SysFont("Bahnschrift", 28)
        if not solving:
            text = font.render(f"⏱ Time: {elapsed_time}", True, (0, 0, 0))
        else:
            text = font.render(f"⏱ Solving...", True, (0, 100, 0))
        self.window.blit(text, (15, 550))
        pygame.display.flip()

    def visualSolve(self):
        """Solve with blinking animation."""
        empty = find_empty(self.board)
        if not empty:
            return True
        i, j = empty

        for num in range(1, 10):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if valid(self.board, (i, j), num):
                self.board[i][j] = num
                self.tiles[i][j].value = num

                # blink animation (green)
                self.tiles[i][j].correct = True
                self.redraw("", True)
                pygame.time.delay(70)
                self.tiles[i][j].correct = False
                self.redraw("", True)
                pygame.time.delay(40)

                if self.visualSolve():
                    return True

                # backtrack animation (red)
                self.board[i][j] = 0
                self.tiles[i][j].value = 0
                self.tiles[i][j].incorrect = True
                self.redraw("", True)
                pygame.time.delay(70)
                self.tiles[i][j].incorrect = False
        return False


# ---------------- MAIN FUNCTION ----------------
def main():
    screen = pygame.display.set_mode((540, 640))
    pygame.display.set_caption("Sudoku Solver 🧩 (Backtracking)")
    icon = pygame.image.load("C:/Users/Ritik boora/OneDrive/Desktop/Project/Sudoku-Solver-master/assets/thumbnail.png")
    pygame.display.set_icon(icon)

    board = Board(screen)
    font = pygame.font.SysFont("Bahnschrift", 36)
    clock = pygame.time.Clock()

    # Buttons
    solve_button = pygame.Rect(60, 570, 180, 50)
    refresh_button = pygame.Rect(300, 570, 180, 50)
    solve_color = (0, 128, 255)
    refresh_color = (255, 140, 0)

    start_time = time.time()
    running = True
    solving = False
    solved = False

    while running:
        # --- Timer control ---
        if not solved:
            elapsed = int(time.time() - start_time)
            passedTime = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        else:
            passedTime = stop_time  # freeze at solve time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # Solve button
                if solve_button.collidepoint(mousePos) and not solving and not solved:
                    solve_color = (34, 139, 34)
                    solving = True
                    board.visualSolve()
                    solving = False
                    solve_color = (0, 128, 255)
                    solved = True
                    stop_time = passedTime  # stop timer when solved

                # Refresh button
                elif refresh_button.collidepoint(mousePos):
                    board.generate_new_board()
                    solved = False
                    solving = False
                    solve_color = (0, 128, 255)
                    start_time = time.time()  # reset timer
                    passedTime = "00:00:00"

        # Draw GUI
        screen.fill((240, 248, 255))
        board.draw_board()

        # Title
        title_font = pygame.font.SysFont("Bahnschrift", 30, bold=True)
        title_text = title_font.render("Sudoku Solver (Backtracking)", True, (10, 10, 80))
        screen.blit(title_text, (100, 545))

        # Timer
        timer_font = pygame.font.SysFont("Bahnschrift", 26)
        timer_text = timer_font.render(f"⏱ {passedTime}", True, (0, 0, 0))
        screen.blit(timer_text, (15, 10))

        # Buttons
        pygame.draw.rect(screen, solve_color, solve_button, border_radius=12)
        text = font.render("SOLVE", True, (255, 255, 255))
        screen.blit(text, (solve_button.x + 45, solve_button.y + 8))

        pygame.draw.rect(screen, refresh_color, refresh_button, border_radius=12)
        text = font.render("REFRESH", True, (255, 255, 255))
        screen.blit(text, (refresh_button.x + 25, refresh_button.y + 8))

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()

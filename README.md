# Tic Tac Toe Game

This repository contains a simple Tic Tac Toe game implemented in Python using the `pygame` library. The game allows two players to take turns and compete to achieve a winning combination of their chosen characters (cross or circle) in a 3x3 grid.

## Table of Contents

- [Introduction](#introduction)
- [Gameplay](#gameplay)
- [Controls](#controls)
- [Features](#features)
- [Winning Logic](#winning-logic)

## Introduction

The Tic Tac Toe Game provides a classic and enjoyable two-player experience where each player takes turns to place their character on the grid in an attempt to create a winning row, column, or diagonal.

## Gameplay

- Two players take turns placing their characters (cross or circle) on an empty grid.
- The player who first creates a winning combination (3 in a row, column, or diagonal) wins the game.
- The game can result in a draw if the entire grid is filled without a winning
  
## Controls

- **Mouse Click**: Players can use the mouse to click on an empty grid square to place their character (cross or circle) during their respective turns.

## Features

- Two-player gameplay: Allows two players to compete against each other.
- Visual representation: Displays the grid and characters (crosses and circles) using images.
- Winning recognition: Detects and displays the winner if a player creates a winning combination.
- Score tracking: Keeps track of the number of wins for both players (cross and circle).
- Reset on win/draw: Resets the game when a player wins or the game ends in a draw.

## Winning Logic

- The game identifies winning combinations of characters in rows, columns, and diagonals.
- When a player creates a winning combination, the winning line is drawn to highlight the winning sequence.

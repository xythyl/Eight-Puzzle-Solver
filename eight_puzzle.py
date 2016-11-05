#!/usr/bin/env python3
'''
  Assignment 1
  Matthew Lauhakamin
  mlauh001@ucr.edu
'''

'''
def general_search(problem, queueing_function):
  nodes = make_queue(make_node(problem.initial_state))
  loop do 
  if empty(nodes) 
    node = remove_front(nodes)
    return "failure"
  if problem.goal_test(node.state)
    nodes = queueing_function(nodes, expand(node, problem.operators))
    return node
  #end
'''
default = [[1,8,2],[0,4,3],[7,6,5]]
solution = [[1,2,3],[4,5,6],[7,8,0]]

class Node:
  def __init__(self, state, parent=None):
    self.STATE = state
    self.PARENT = parent
    if parent is None:
      self.DEPTH = 0
    else:
      self.DEPTH = self.PARENT.DEPTH+1

  def __getitem__(self, index):
    return self.STATE[index]

  def index(self, item):
    for i, j in enumerate(self.STATE):
      if item in j:
        return i, j.index(item)

  def print_puzzle(self):
    print("-----")
    for i in range(len(self.STATE)):
      for j in range(len(self.STATE[i])):
        print (str(self.STATE[i][j]) + " ", end="")
      print ("")
    print("-----")

def check_solved(node):
  if node.STATE == solution:
    return True
  else:
    return False

def up(node):
  i, j = node.index(0)
  newu = list_2_list(node.STATE)
  newu[i][j], newu[i-1][j] = newu[i-1][j], newu[i][j]
  return newu

def down(node):
  i, j = node.index(0)
  newd = list_2_list(node.STATE)
  newd[i][j], newd[i+1][j] = newd[i+1][j], newd[i][j]
  return newd

def left(node):
  i, j = node.index(0)
  newl = list_2_list(node.STATE)
  newl[i][j], newl[i][j-1] = newl[i][j-1], newl[i][j]
  return newl

def right(node):
  i, j = node.index(0)
  newr = list_2_list(node.STATE)
  newr[i][j], newr[i][j+1] = newr[i][j+1], newr[i][j]
  return newr

def expand(node):
  children = []
  i, j = node.index(0)
  if i != 0:
    children.append(Node(up(node),node))
  if i != 2:
    children.append(Node(down(node),node))
  if j != 0:
    children.append(Node(left(node),node))
  if j != 2:
    children.append(Node(right(node),node))
  return children

def misplaced_tiles_d(state): #datatype for state is a list
  misplaced_tiles = 0
  for i in range(len(state)):
    for j in range(len(state[i])):
      if state[i][j] != solution[i][j]:
        misplaced_tiles += 1
  return misplaced_tiles

def manhattan_d(state):
  number_of_moves = 0
  for i in range(len(state)):
    for j in range(len(state[i])):
      if state[i][j] != 0:
        number_of_moves += (abs(i-((state[i][j]-1)//3)) + abs(j-((state[i][j]-1)%3)))
  return number_of_moves

#converts a 2d list into a 1d list
def conv_2d_list(old_list):   
  new_list = []
  for i in range(len(old_list)):
    for j in range(len(old_list[i])):
      new_list.append(old_list[i][j])
  return new_list
  
#converts a 2d list to a 2d list to avoid making a pointer
def list_2_list(old_list):   
  new_list = [[0,0,0],[0,0,0],[0,0,0]]
  for i in range(len(old_list)):
    for j in range(len(old_list[i])):
      new_list[i][j] = old_list[i][j]
  return new_list

'''
reference from
http://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
'''
def check_solvable(state):
  inversion_count = 0
  checked_list = conv_2d_list(state)
  checked_list.remove(0)
  for i in range(0, len(checked_list)):
    for j in range(i, len(checked_list)):
      if checked_list[i] > checked_list[j]:
        inversion_count += 1
  #print('Inversion count is: ' + str(inversion_count))
  return not(inversion_count % 2)

def get_puzzle():
  first_row = []
  second_row = []
  third_row = []
  while len(first_row) != 5:
    first_row = input("Enter 1st row: ")
  while len(second_row) != 5:
    second_row = input("Enter 2nd row: ")
  while len(third_row) != 5:
    third_row = input("Enter 3rd row: ")
  row1=first_row.split(" ")
  row2=second_row.split(" ")
  row3=third_row.split(" ")
  print ("You entered ")
  print(first_row) 
  print(second_row) 
  print(third_row)
  row1 = list(map(int,row1))
  row2 = list(map(int,row2))
  row3 = list(map(int,row3))
  puzzle = []
  puzzle.append(row1)
  puzzle.append(row2)
  puzzle.append(row3)
  return puzzle

def puzzle_prompt():
  text = input("Type \"1\" to use a default puzzle or \"2\" to enter your own puzzle: ")
  if len(text) > 1:
    print ("Error input is not valid")
    return puzzle_prompt()
  else:
    text = int(text)
  if text == 1:
    return default
  elif text == 2:
    return get_puzzle()
  else:
    print ("Error: input is not valid")
    return puzzle_prompt()

def select_algorithm():
  print ("Enter you choice of algorithm")
  print ("1. Uniform Cost Search")
  print ("2. A* with the Misplaced Tile heuristic")
  print ("3. A* with the Manhattan distance heuristic")
  selection = input()
  if selection not in ['1','2','3']:
    print ("Error: incorrect number selected\n")
    return select_algorithm()
  else:
    return selection

def main():
  print ("Eight Puzzle Solver")
  puzzle = puzzle_prompt()
  select_algorithm()
  #print(puzzle)
  #print(puzzle[0])
  #print(puzzle[1])
  #print(puzzle[2])
  #print(misplaced_tiles_d(puzzle))
  #print(manhattan_d(puzzle))
  n = Node(puzzle)
  n.print_puzzle()
  c = expand(n)
  n.print_puzzle()
  for o in c:
    print("operator")
    o.print_puzzle()
  if check_solvable(puzzle):
    print("puzzle is solvable")
  else:
    print ("puzzle is not solvable")
    exit()

main()

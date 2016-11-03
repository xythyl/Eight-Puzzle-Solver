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

#converts a 2d list into a 1d list
def conv_2d_list(old_list):   new_list = []
  for i in range(len(old_list)):
    for j in range(len(old_list[i])):
      new_list.append(old_list[i][j])
  return new_list

'''
reference from
http://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
'''
def check_solvable(state):
  inversion_count = 0
  checked_list = conv_2d_list(state)
  print ("Checked list")
  checked_list.remove(0)
  print (checked_list)
  for i in range(0, len(checked_list)):
    for j in range(i, len(checked_list)):
      if checked_list[i] > checked_list[j]:
        inversion_count += 1
  print('Inversion count is: ' + str(inversion_count))
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
  text = input("Type \"1\" to use default puzzle or \"2\" to enter a puzzle: ")
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

def main():
  print ("Eight Puzzle Solver")
  puzzle = puzzle_prompt()
  print(puzzle)
  print(puzzle[0])
  print(puzzle[1])
  print(puzzle[2])
  if check_solvable(puzzle):
    print("puzzle is solvable")
  else:
    print ("puzzle is not solvable")
    exit()

main()

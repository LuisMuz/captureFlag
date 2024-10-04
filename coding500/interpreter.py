import re

print_end = ""
variables = {}

def extract_variable_name(code):
  return code[::2]

def process_string(string_code):
  return ''.join(reversed(string_code[::2]))

def process_number_operation(expr):
  value = 0
  current_operation = 'ADD'
  tokens = re.findall(r'[a-zA-Z]+|\d+', expr)
  
  for token in tokens:
    if token.isdigit():
      num = int(token)
      if current_operation == 'ADD':
        value += num
      elif current_operation == 'SUB':
        value -= num
      elif current_operation == 'MUL':
        value *= num
      elif current_operation == 'DIV' and num != 0:
        value //= num
    else:
      if token == 'a':
        current_operation = 'ADD'
      elif token == 's':
        current_operation = 'SUB'
      elif token == 'm':
        current_operation = 'MUL'
      elif token == 'd':
        current_operation = 'DIV'
  return value

def process_value(element):
  if element.startswith('B'):
    string_code = element[1:-1]
    return process_string(string_code)
  elif element.startswith('N'):  
    return process_number_operation(element[:])
  else: 
    variable_name = extract_variable_name(element[1:-1])
    return variables[variable_name]

def evaluate_condition(cond):
  option1, option2, operation = re.findall(r'N[a-z0-9]+|V[a-z0-9_.]+|B[a-z0-9_.]+|[A-Z]{2}', cond)
  option1 = process_value(option1)
  option2 = process_value(option2)
  if operation == 'EN':
    return option1!=option2
  elif operation == 'EG':
    return option1>=option2
  elif operation == 'EL':
    return option1<=option2
  elif operation == 'QE':
    return option1==option2
  elif operation == 'TG':
    return option1>option2
  else:
    return option1<option2
  
match = lambda x, y: re.findall(r'[A-Za-z0-9=_.]+(?: OR [A-Za-z0-9_]+| AND [A-Za-z0-9_]+)?|BOH|HOB|OH|HO|[A-Za-z0-9=_]+|\|', x[y:-y])

def get_condition_structure(tokens):
  g_stack = []
  stack = []
  counter = 0

  is_condition = False
  is_loop = False

  for element in tokens:
    if element == 'BOH' and not is_loop:
      counter += 1
      stack.append(element)
      stack.append(" ")
    elif element == 'HOB'and not is_loop:
      counter -= 1
      stack.append(element)
      stack.append(" ")
    elif element == 'LOOP' and not is_condition:
      counter += 1
      stack.append(element)
      stack.append(" ")
    elif element == 'POOL'and not is_condition:
      counter -= 1
      stack.append(element)
      stack.append(" ")
    elif counter != 0:
      stack.append(element)
      stack.append(" ")
    if counter == 0:
      is_condition = False
      is_loop = False
      if len(stack) > 0:
        g_stack.append(''.join(stack).strip())
        stack = []
      else:
        g_stack.append(element)
  return g_stack

def execute_condition(condition):
  if "OR" in condition:
    cond1 , cond2 = condition.split(" OR ")
    return evaluate_condition(cond2) or evaluate_condition(cond1)
  elif "AND" in condition:
    cond1 , cond2 = condition.split(" AND ")
    return evaluate_condition(cond2) and evaluate_condition(cond1)
  else:
    return evaluate_condition(condition)
  
def extract_variable_name(code):
    return code[::2]

def extract_value(terms, n):
  if terms[n][0] == 'B':
    return process_string(terms[n][1:])
  if terms[n][0] == 'N':
    return process_number_operation(terms[n])
  elif terms[n][0] == 'V':
    return variables[extract_variable_name(terms[n][1:-1])]
  else:
    is_operand, value = extract_operation_terms(terms, n)
    return value

def extract_operation_terms(terms, n):
  ops = ["DIV", "MUL", "SUB", "ADD"]
  op = terms[n]
  if len(terms) == 2 or op not in ops :
    return False, []
  
  if op == "DIV":
    res = (extract_value(terms, n-2) / extract_value(terms, n-1))
  if op == "MUL":
    res = (extract_value(terms, n-2) * extract_value(terms, n-1))
  if op == "SUB":
    res = extract_value(terms, n-2) - extract_value(terms, n-1)
  if op == "ADD":
    res = extract_value(terms, n-2) + extract_value(terms, n-1)

  return True, res

outputs = {}

def transform_to_action(line):
  if 'P' in line:  # Si contiene P, es para imprimir
    outputs["count"] = outputs["count"] + 1
    if line.startswith('B'):  # Es una cadena
      string_code = line[1:-1]
      print(process_string(string_code), end=print_end)
    elif line.startswith('N'): 
      print(process_number_operation(line[:-1]), end=print_end)
    else:  
      variable_name = extract_variable_name(line[1:-1])
      print(variables[variable_name], end=print_end)
  elif '=' in line:  
    # print(line)
    lhs, rhs = line.rsplit('V',1)
    
    terms = re.findall(r'N[a-z0-9]+|V[a-z0-9_]+|B[a-z0-9_.]+|[A-Z]{3}', lhs)
    is_operation, value = extract_operation_terms(terms,len(terms)-1)

    if not is_operation:
        variable_name = extract_variable_name(rhs[:-1])
        if lhs.startswith('B'):  
          variables[variable_name] = process_string(lhs[1:])
        elif lhs.startswith('N'):  
          variables[variable_name] = process_number_operation(lhs)
        else: 
          source_variable_name = extract_variable_name(lhs[1:])
          variables[variable_name] = variables[source_variable_name]
    else:
      variable_name = extract_variable_name(rhs[:-1])
      variables[variable_name] = value

def check_condition(cond):
  condition = match(cond,3)
  conditions = get_condition_structure(condition)
  actions=[]
  is_condition = True
  do_actions = False
  look_next_condition = False

  for element in reversed(conditions):
    if is_condition and not look_next_condition:
      do_actions = execute_condition(element)
      if do_actions : 
        is_condition = False
      else:
        look_next_condition = True
    else:
      if element == "OH":
        if do_actions : break
        is_condition = True
        look_next_condition = False
      elif do_actions and element != "|" and element != "HO":
        actions.append(element)

  for action in actions:
    if action.endswith("BOH"):
        check_condition(action)
    elif action.endswith("LOOP"):
        check_loop(action)
    else:
        transform_to_action(action)


def check_loop(loop):
  sintaxis = get_condition_structure(match(loop,4))
  condition = ""
  actions = []
  is_condition = True

  for element in reversed(sintaxis):
    if element == "|":
      is_condition = False
    elif is_condition:
      condition = element
    else:
      actions.append(element)

  while(evaluate_condition(condition)):
    for action in actions:
      if action.endswith("BOH"):
        check_condition(action)
      elif action.endswith("LOOP"):
        check_loop(action)
      else:
        transform_to_action(action)

def interpret_code_block(block):
  for line in block:
    line = line.strip()
    if 'HOB' not in line and 'LOOP' not in line and (len(line.split(" ")) > 1):
      for inst in reversed(line.split(" ")):
        transform_to_action(inst)
    else:
      if line.endswith("BOH"):
        check_condition(line)
      elif line.endswith("LOOP"):
        check_loop(line)
      else:
        transform_to_action(line)
  
outputs["count"] = 0
pathLevel1 = 'Level1/Level1.txt'
pathLevel2 = 'Level1/Level2/Level2.txt'
pathLevel3 = 'Level1/Level2/Level3/Level3.txt'
pathLevel4 = 'Level1/Level2/Level3/Level4/Level4.txt'

with open(pathLevel4, 'r') as file:
  content = file.read()
lines = content.splitlines()
# lines = example17
interpret_code_block(lines)
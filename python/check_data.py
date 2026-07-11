import re

with open('data/jugadores.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find JUGADORES_MOCK block
m = re.search(r'JUGADORES_MOCK\s*=\s*\[(.*?)\]', content, re.DOTALL)
if m:
    block = m.group(1)
    ids = re.findall(r'"id":\s*"(j\d+)"', block)
    print(f'JUGADORES_MOCK: {len(ids)} entries')
    print(f'  First: {ids[0]}, Last: {ids[-1]}')

# Find JUGADORES_100 block
m = re.search(r'JUGADORES_100\s*=\s*\[(.*?)\]', content, re.DOTALL)
if m:
    block = m.group(1)
    ids = re.findall(r'"id":\s*"(j\d+)"', block)
    print(f'JUGADORES_100: {len(ids)} entries')
    print(f'  First: {ids[0]}, Last: {ids[-1]}')

# Count total ocurrencias de 'obtener_todos'
print(f'obtener_todos aparece: {content.count("obtener_todos")} veces')

# Check the line that returns
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'return' in line and 'JUGADORES' in line:
        print(f'Line {i+1}: {line.strip()}')

def parse_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        identifier = ''
        seq_lines = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if identifier:
                    sequences[identifier] = ''.join(seq_lines)
                identifier = line[1:]  # убираем символ '>'
                seq_lines = []
            else:
                seq_lines.append(line)
        if identifier:
            sequences[identifier] = ''.join(seq_lines)
    return sequences

def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0

def find_max_gc_content(sequences):
    max_gc = 0
    max_id = ''
    for identifier, seq in sequences.items():
        gc = gc_content(seq)
        if gc > max_gc:
            max_gc = gc
            max_id = identifier
    return max_id, max_gc

# Пример использования:
# filename = 'dna_sequences.fasta'
# sequences = parse_fasta(filename)
# max_id, max_gc = find_max_gc_content(sequences)
# print(max_id)
# print(f"{max_gc:.6f}")


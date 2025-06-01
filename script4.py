#Код задание 1
from Bio import Entrez, SeqIO

Entrez.email = "your.email@example.com"


def fetch_species_records(species, count=5):
    query = f'"{species}"[Organism] AND complete cds'
    handle = Entrez.esearch(db="nucleotide", term=query, retmax=count)
    record = Entrez.read(handle)
    handle.close()
    ids = record['IdList']

    records = []
    for id_ in ids:
        handle = Entrez.efetch(db="nucleotide", id=id_, rettype="gb", retmode="text")
        rec = SeqIO.read(handle, "genbank")
        handle.close()
        records.append(rec)
    return records


species1 = "Banana bunchy top virus"
species2 = "Homo sapiens"

records1 = fetch_species_records(species1)
records2 = fetch_species_records(species2)

combined_filename = "combined.gb"
with open(combined_filename, "w") as out_handle:
    SeqIO.write(records1 + records2, out_handle, "genbank")

print(f"Объединённый файл '{combined_filename}' создан.")
#Код задание 2
from Bio import SeqIO

def calculate_gc(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return gc_count / len(seq) if len(seq) > 0 else 0

def extract_cds_gc(filename):
    records = SeqIO.parse(filename, "genbank")
    cds_gc_list = []
    for rec in records:
   for feature in rec.features:
  if feature.type == "CDS":
cds_seq = feature.location.extract(rec.seq)
  gc = calculate_gc(cds_seq)
   cds_gc_list.append((rec.id, gc))
    return cds_gc_list

combined_filename = "combined.gb"
cds_gc = extract_cds_gc(combined_filename)
cds_gc_sorted = sorted(cds_gc, key=lambda x: x[1])

for rec_id, gc in cds_gc_sorted:
    print(f"{rec_id}, GC = {gc:.6f}")


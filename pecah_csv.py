
import csv
import os

file_input = "REPORT_IDLE_AGUSTUS.csv"
ukuran_baris = 100_000

folder_output = "hasil_split"
os.makedirs(folder_output, exist_ok=True)

with open(file_input, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    nomor_file = 1
    jumlah_baris = 0
    output = None
    writer = None

    try:
        for row in reader:
            if jumlah_baris % ukuran_baris == 0:
                if output:
                    output.close()

                nama_file = os.path.join(
                    folder_output,
                    f"data_part_{nomor_file}.csv"
                )

                output = open(
                    nama_file, "w",
                    encoding="utf-8-sig",
                    newline=""
                )
                writer = csv.writer(output)
                writer.writerow(header)
                nomor_file += 1

            writer.writerow(row)
            jumlah_baris += 1
    finally:
        if output:
            output.close()

print(f"Selesai! Total data: {jumlah_baris:,} baris")
print(f"Hasil tersimpan di folder: {folder_output}")

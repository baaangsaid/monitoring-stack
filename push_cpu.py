import multiprocessing

# Fungsi yang membuat loop komputasi untuk membebani CPU
def cpu_stress():
    while True:
        x = 0
        for i in range(1000000):
            x += i * i

# Jalankan stress test di semua core CPU
if __name__ == "__main__":
    # Dapatkan jumlah CPU logical core di sistem
    cpu_count = multiprocessing.cpu_count()

    # Buat proses untuk setiap core
    processes = []
    for _ in range(cpu_count):
        process = multiprocessing.Process(target=cpu_stress)
        processes.append(process)
        process.start()

    # Tunggu proses selesai (atau tekan Ctrl+C untuk menghentikan secara manual)
    for process in processes:
        process.join()

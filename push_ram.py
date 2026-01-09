import threading

def allocate_memory():
    big_list = [1] * 10**7  # Alokasikan list besar
    input("Tekan Enter untuk membersihkan thread...")

# Jalankan beberapa thread sekaligus
threads = [threading.Thread(target=allocate_memory) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

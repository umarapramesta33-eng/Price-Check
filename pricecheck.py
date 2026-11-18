
print("=" * 40)
print("       PRICECHECK")
print("   SMART PRICE & CASHIER")
print("=" * 40)

# Input barang
nama = input("Nama barang: ")
harga = int(input("Harga satuan (Rp): "))
jumlah = int(input("Jumlah barang: "))

# Validasi input
if harga <= 0 or jumlah <= 0:
    print("Harga dan jumlah harus lebih dari 0!")

else:
    # Menentukan kategori harga
    if harga < 20000:
        kategori = "MURAH"
    elif harga <= 50000:
        kategori = "NORMAL"
    else:
        kategori = "MAHAL"

    # Menghitung total
    subtotal = harga * jumlah

    if subtotal >= 100000:
        diskon = subtotal * 10 // 100
    else:
        diskon = 0

    total = subtotal - diskon

    # Input pembayaran
    print("\nKategori harga:", kategori)
    print("Subtotal: Rp", subtotal)
    print("Diskon: Rp", diskon)
    print("Total bayar: Rp", total)

    uang = int(input("Uang pembayaran (Rp): "))

    # Menghitung kembalian
    if uang >= total:
        print("Kembalian: Rp", uang - total)
        print("Transaksi berhasil!")
    else:
        print("Uang kurang: Rp", total - uang)

print("=" * 40)
print("Terima kasih sudah menggunakan PriceCheck!")

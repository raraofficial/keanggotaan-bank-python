def akun_nasabah_bank(nama_bank):
    """
    Fungsi luar untuk menentukan keanggotaan nasabah bank.
    Menerima nama bank sebagai argumen.
    """
    def inner(nama_nasabah):
        """
        Fungsi dalam untuk menghasilkan pesan keanggotaan.
        Menerima nama nasabah sebagai argumen.
        """
        if nama_bank == "Bank BNI":
            jabatan = "akuntan"
        else:
            jabatan = "programmer"  

        return f"Halo {nama_nasabah} anda adalah seorang {jabatan} di {nama_bank}"
    return inner

akun_bni = akun_nasabah_bank("Bank BNI")
print(akun_bni("Lukman"))

akun_lain = akun_nasabah_bank("Bank BRI")  
print(akun_lain("Genta"))
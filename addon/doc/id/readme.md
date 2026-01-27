# Accessible Bluetooth Audio Receiver

**Accessible Bluetooth Audio Receiver** adalah add-on untuk pembaca layar NVDA yang dirancang untuk meningkatkan aksesibilitas dan kemudahan penggunaan aplikasi [Bluetooth Audio Receiver](https://apps.microsoft.com/detail/9N9WCLWDQS5J?hl=en&gl=US&ocid=pdpshare) di Windows.

Aplikasi ini memungkinkan Anda untuk memutar musik dari perangkat Bluetooth (seperti ponsel) ke speaker PC Anda. Add-on ini mempermudah Anda membuka aplikasi dan mengatur koneksi tanpa perlu menelusuri elemen antarmuka yang rumit.

## Fitur

- **Pintasan Cepat (Shortcut)**: Buka aplikasi secara instan dari mana saja menggunakan tombol pintas global.
- **Pengaturan Koneksi Sederhana**: Sambungkan atau putuskan perangkat cukup dengan menekan `Enter` pada nama perangkat di daftar. Add-on ini akan mencari dan menekan tombol yang sesuai untuk Anda.
- **Laporan Status Pintar**: Secara otomatis mengumumkan perubahan status koneksi (contoh: "berhasil terhubung dengan [Nama Perangkat]").
- **Daftar Perangkat yang Lebih Jelas**: Memberikan laporan yang jelas mengenai nama perangkat dan statusnya (Terhubung/Berpasangan) saat menelusuri daftar.

## Persyaratan Sistem

1. **Windows 10 versi 2004** atau yang lebih baru (Diperlukan untuk dukungan Bluetooth A2DP Sink).
2. Adaptor Bluetooth (dongle atau bawaan).
3. Aplikasi **Bluetooth Audio Receiver** yang diinstal dari Microsoft Store.

   [**Unduh Bluetooth Audio Receiver**](https://apps.microsoft.com/detail/9N9WCLWDQS5J?hl=en&gl=US&ocid=pdpshare)

## Instalasi

1. Instal aplikasi "Bluetooth Audio Receiver" dari tautan Microsoft Store di atas.
2. Unduh rilis terbaru dari add-on NVDA ini.
3. Buka file `.nvda-addon` dan ikuti petunjuk untuk menginstalnya di NVDA.
4. Restart NVDA saat diminta.

## Cara Penggunaan

### Tombol Pintas

- **NVDA + Windows + B**: Membuka aplikasi Bluetooth Audio Receiver. Jika aplikasi sudah berjalan, ini akan mengarahkan fokus ke aplikasi tersebut atau memberitahu Anda.

*Catatan: Anda dapat mengubah tombol pintas ini di NVDA melalui menu **Preferences** > **Input gestures...** > kategori **Bluetooth Audio Receiver**.*

### Mengelola Koneksi

1. Buka aplikasi menggunakan pintasan (`NVDA + Windows + B`).
2. Arahkan ke daftar perangkat Bluetooth yang sudah dipasangkan (paired).
3. Pilih perangkat yang ingin Anda gunakan.
4. Tekan **Enter** pada item perangkat tersebut:
   - Jika perangkat sedang **terputus (disconnected)**, add-on akan mencoba untuk **menghubungkan (connect)**.
   - Jika perangkat sedang **terhubung (connected)**, add-on akan mencoba untuk **memutuskan (disconnect)**.
5. Add-on akan mengumumkan prosesnya ("Connecting to...", "Disconnecting from...") dan hasil akhirnya ("Successfully connected...").

*Catatan: Anda tidak perlu mencari tombol "Open Connection" atau "Close Connection"; tombol `Enter` sudah menangani semuanya secara otomatis.*

## Pemecahan Masalah

- **"Bluetooth Audio Receiver is already running"**: Add-on mencegah aplikasi dibuka ganda. Cek taskbar atau tekan Alt+Tab untuk menemukan jendela yang sudah terbuka.
- **Connection Timed Out (Koneksi Habis Waktu)**: Jika perangkat gagal terhubung, pastikan perangkat Bluetooth Anda (ponsel/tablet) sudah dipasangkan (paired) dengan Windows dan sedang dalam mode yang bisa ditemukan atau mencoba terhubung.

## Kredit

Dikembangkan oleh Muhammad.

## Lisensi

Add-on ini didistribusikan di bawah lisensi GNU General Public License v2 (GPLv2).

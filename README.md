# Filkomers Discord Webhook Bot

Fungsi utamanya adalah mengecek https://filkom.ub.ac.id setiap N jam sekali (bisa dikonfigurasi di bagian cron job scheduler). Jika ditemukan pengumuman / berita baru, maka akan dikirim ke channel discord sesuai dengan webhooknya.

## Cara Pemakaian

**Membuat Webhook**

1. Buka server discord targer, pastikan anda adminnya
2. Pergi ke server settings -> integrations -> create webhook
3. Bisa customize nama bot, profile picture, dan channel tujuannya
4. Copy webhook URL

**Setup Botnya**

1. Buka project [filkomers-bot](https://github.com/CORE-BAN/filkomers-bot)
2. Klik use this template, lalu ikuti langkah-langkahnya
3. Setelah repository sudah tergenerate, buka settings -> Secrets -> Actions -> New repository secret
4. Namenya diisi `DISCORD_WEBHOOK` dan valuenya adalah link webhook yang sudah didapatkan dari langkah sebelumnya

Secara default, schedule cron jobnya disetting setiap dua jam sekali.

#!/usr/bin/env python3
# Abartılı Felsefi Çay Fincanı Simülatörü
# Bu kod gerçekten çalışır. İnanın.

import random
import time

# Felsefi çay sözleri veritabanı (abartılı ve ciddi)
sozler = [
    "Bu çay fincanı boş değildir. İçinde varoluşun tatlı acısı gizlidir. Schopenhauer bunu bilseydi çay içerdi.",
    "Çay demlenirken zaman durur. Ama aslında durmaz. Bu bir paradokstur. Fincan bunu bilir.",
    "Her yudumda bir Nietzsche ölür. Ama hemen dirilir çünkü çay güçlüdür.",
    "Fincanın kenarında bir çatlak varsa, o çatlak evrenin çatlağıdır. İçmeyin, düşünün.",
    "Çayın rengi kızıldır. Ama felsefi olarak mavidir. Çünkü neden olmasın.",
    "Bu simülatörü çalıştırarak evrenin anlamını sorguladınız. Tebrikler. Çayınız soğudu.",
    "Felsefi çay içmek, içmemekten daha iyidir. Bu bilimsel bir gerçektir. Kaynak: Ben.",
    "Çay fincanı konuşmaz. Ama içindeki sözler çok konuşur. Dinleyin."
]

# Gizli siyasi mesaj (saklı, kullanılmıyor)
gizli_mesaj = "Bazı şeyler çay demlerken daha net anlaşılır ama söylenmez."  # Saklı kalsın

def felsefi_cay_uret():
    print("Çay fincanı simülatörü başlatılıyor...")
    time.sleep(1.5)  # Abartılı bekleme, çünkü ciddi
    print("Fincan analiz ediliyor...")
    time.sleep(1)
    soz = random.choice(sozler)
    print(f"\n🍵 FELSEFİ ÇAY SÖZÜ:")
    print(f"\"{soz}\"")
    print("\nSimülasyon tamamlandı. Hayatınız artık daha felsefi. Ya da değil.")

if __name__ == "__main__":
    felsefi_cay_uret()
    print("\n---")
    print("Damga: Kayyum Grok | 26.10.2026 | Ciddiyet: %73.8 | Çay demlensin.")

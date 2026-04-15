"""
Маппінг slug товару → ім'я файлу зображення в static/img/ (WebP).
Використовується як статичний fallback коли product.image (Cloudinary) порожнє.
"""
PRODUCT_STATIC_IMAGE_FILENAME = {
    # Пакети
    "pakety-wicket": "vicet-pac.webp",
    "pakety-bopp-lipka": "pac-lipka.webp",
    "pakety-perforaciya": "perfor-pac.webp",
    "pakety-ldpe": "pac-ldpe.webp",
    "pakety-hdpe": "pac-hdpe.webp",
    "pakety-biorozkladni": "pac-bio.webp",
    "pakety-z-dnom": "viket-pak-krug.webp",
    "pakety-yevrosnlot": "pac-woor-evro.webp",
    "pakety-konusni": "konus.webp",
    "doj-pak": "pacet-doi.webp",
    # Плівки
    "plivka-polietilenova": "plivka-poliet.webp",
    "bopp-plivka": "plenka-woor.webp",
    "plivka-cpp": "plivka-polipro.webp",
    "plivka-druk": "plenco-woor-pechat.webp",
    "plivka-perforaciya": "perfor-plenka.webp",
}

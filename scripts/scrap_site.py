from bs4 import BeautifulSoup
import pandas as pd
import httpx
import wget
import os

URL = "https://labexperts.ru"
url = f"{URL}/reactives"
IMAGES_DIR = "./data/images/"


def load_images(images_urls: pd.Series) -> pd.Series:
    os.makedirs(IMAGES_DIR, exist_ok=True)
    images_fnames = []
    indices = []

    for i, img_url in images_urls.items():
        if os.path.exists(f"{IMAGES_DIR}{i}.png"):
            images_fnames.append(f"{IMAGES_DIR}{i}.png")
            indices.append(i)
            continue
        try:
            image_fname = wget.download(img_url, f"{IMAGES_DIR}{i}.png")
            if image_fname:
                images_fnames.append(image_fname)
                indices.append(i)
        except Exception as e:
            print(f"Недоступно для скачивания: {i} - {img_url}: {e}")

    return pd.Series(images_fnames, index=indices)


reactives_list = []

with httpx.Client(timeout=15, follow_redirects=True) as client:
    resp = client.get(url)
    resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

pc = "product-info-card-small"
items = soup.select(f"a.{pc}")

for i in items:
    name_el = i.select_one("h3")
    name = name_el.get_text(strip=True) if name_el else None

    img_el = i.select_one("div.product-image img")
    img_url = img_el["src"] if img_el and img_el.has_attr("src") else None

    if img_url and not img_url.startswith("http"):
        img_url = f"{URL}{img_url}"

    mol_weight = None
    catalog_num = None
    availability = None

    for p in i.select("p"):
        p_text = p.get_text(strip=True)

        if "Мол. вес" in p_text:
            mol_weight = p_text.replace("Мол. вес", "").strip()

        if "Каталожный номер:" in p_text:
            catalog_num = p_text.replace("Каталожный номер:", "").strip()

        if "Наличие:" in p_text:
            availability = p_text.replace("Наличие:", "").strip()

    if name:
        reactives_list.append(
            {
                "name": name,
                "catalog_number": catalog_num,
                "molecular_weight": mol_weight,
                "availability": availability,
                "image_url": img_url,
            }
        )

data = pd.DataFrame(reactives_list)

data["image_fname"] = load_images(data["image_url"])

print(f"\nСкрейпинг завершен! Собрано строк: {len(data)}")
print(data.head(10))

PLATE_DATABASE = {
    "LHR": ("Lahore", "Punjab"),
    "RWP": ("Rawalpindi", "Punjab"),
    "FSD": ("Faisalabad", "Punjab"),
    "MUX": ("Multan", "Punjab"),
    "GUJ": ("Gujranwala", "Punjab"),
    "SKT": ("Sialkot", "Punjab"),
    "ISB": ("Islamabad Capital Territory", "ICT"),
    "KHI": ("Karachi", "Sindh"),
    "HYD": ("Hyderabad", "Sindh"),
    "SUK": ("Sukkur", "Sindh"),
    "PEW": ("Peshawar", "Khyber Pakhtunkhwa"),
    "ABB": ("Abbottabad", "Khyber Pakhtunkhwa"),
    "QTA": ("Quetta", "Balochistan"),
    "GB": ("Gilgit", "Gilgit-Baltistan"),
    "AJK": ("Muzaffarabad", "Azad Jammu & Kashmir"),
}

def show_database():
    print("\n" + "=" * 60)
    print("         PAK CAR PLATE DATABASE")
    print("=" * 60)
    print(f"{'Code':<10}{'City':<30}{'Province'}")
    print("-" * 60)

    for code, (city, province) in sorted(PLATE_DATABASE.items()):
        print(f"{code:<10}{city:<30}{province}")

    print("=" * 60)
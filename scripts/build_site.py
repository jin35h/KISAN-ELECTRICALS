from __future__ import annotations

import html
import json
from pathlib import Path
from textwrap import dedent
from urllib.parse import quote

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REFERENCE_ROOT = ROOT / "source_images"
BASE_URL = "https://kisan-electricals.vercel.app"
BUSINESS_NAME = "Kisan Electricals"
BUSINESS_NAME_GU = "કિસાન ઇલેક્ટ્રિકલ્સ"
PRIMARY_PHONE = "+91 87589 64040"
SECONDARY_PHONE = "+91 98985 33088"
PRIMARY_PHONE_E164 = "+918758964040"
SECONDARY_PHONE_E164 = "+919898533088"
ADDRESS_LINE = "Shop No. 12, Nirman Complex, Approach Road, Opposite HDFC Bank, Prantij - 383205"
GOOGLE_PROFILE = "https://share.google/99okhF6FIlGM8JSMm"
FACEBOOK = "https://www.facebook.com/KisanElectricalsPrantij"
INSTAGRAM = "https://www.instagram.com/kisanelectricalsprantij/"
MAP_EMBED = (
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3659.8732155799793!"
    "2d72.8596001!3d23.4357001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!"
    "4f13.1!3m3!1m2!1s0x395c37eb64d2bfb7%3A0xe54d97fdfbf90c74!"
    "2sKisan%20Electricals!5e0!3m2!1sen!2sin!4v1723821038596!5m2!1sen!2sin"
)
HOURS_TEXT = "Mon-Sat: 8:30 AM - 7:45 PM | Sun: Call to confirm"


CATALOG_IMAGE_SOURCES = {
    "products-hub": "20260816_174036.jpg",
    "led-main": "20260816_174041.jpg",
    "led-decorative": "20260816_174044.jpg",
    "ceiling-fans": "20260816_174018.jpg",
    "switches-sockets": "20260816_174050.jpg",
    "plates-accessories": "20260816_174056.jpg",
    "utility-protection": "20260816_174109.jpg",
    "contractor-panel-1": "WhatsApp Image 2026-08-16 at 5.56.20 PM.jpeg",
    "contractor-panel-2": "WhatsApp Image 2026-08-16 at 6.04.25 PM.jpeg",
    "contractor-panel-3": "WhatsApp777 Image 2026-08-16 at 5.56.20 PM.jpeg",
}


STORY_IMAGES = {
    "store_closeup": "assets/optimized/store_front_closeup_orig.webp",
    "store_wideshot": "assets/optimized/store_front_wideshot_orig.webp",
    "history_documents": "assets/optimized/history_documents_orig.webp",
    "invitation_1976": "assets/optimized/invitation_cart_opening_1976_orig.webp",
    "old_shop": "assets/optimized/old_history_shop_orig.webp",
    "old_shop2": "assets/optimized/old_history_shop2_orig.webp",
    "three_gen": "assets/optimized/3_generation_in_one_with_customers_orig.webp",
    "family_customer": "assets/optimized/family_customer_with_owner_orig.webp",
    "engineer_customer": "assets/optimized/engineer_customer_with_order_orig.webp",
    "owner_customer": "assets/optimized/owner_with_customer_orig.webp",
    "owner_customer2": "assets/optimized/owner_with_customer2_orig.webp",
    "owner_discuss": "assets/optimized/owner_discuss_with_son_orig.webp",
    "contractor_inspection": "assets/optimized/ugvcl_contractor_1_orig.webp",
    "contractor_panel": "assets/optimized/ugvcl_contractor2_orig.webp",
    "contractor_handover": "assets/optimized/ugvcl_contractor3_orig.webp",
}


NAV_ITEMS = [
    ("home", "Home", "/"),
    ("products", "Products", "/products/"),
    ("services", "Services", "/electrical-services/"),
    ("contractor", "Contractor Work", "/ugvcl-electrical-contractor-prantij/"),
    ("about", "Our Story", "/about-kisan-electricals/"),
    ("gallery", "Gallery", "/gallery/"),
    ("contact", "Contact", "/contact/"),
]


PRODUCT_MENU = [
    ("LED Lighting", "/products/led-lights/"),
    ("Ceiling Fans", "/products/ceiling-fans/"),
    ("Switches & Sockets", "/products/switches-sockets/"),
    ("Wires & Cables", "/products/wires-cables/"),
    ("MCB, RCCB & Protection", "/products/mcb-electrical-protection/"),
    ("Pumps, Tools & Utility Products", "/products/pumps-tools-utility/"),
    ("Electrical Brands", "/electrical-brands/"),
]


HOME_FAQS = [
    (
        "What does Kisan Electricals sell in Prantij?",
        "Kisan Electricals in Prantij supplies LED bulbs, ceiling fans, modular switches, sockets, plates, electrical protection items, utility products and products commonly required by homeowners, electricians and project buyers.",
    ),
    (
        "How can I check current stock before visiting?",
        "Call +91 87589 64040 or send a WhatsApp list with the brand, model, quantity and required specification. The shop can then confirm current stock, price and available alternatives.",
    ),
    (
        "Does the business help electricians and builders?",
        "Yes. The shop serves homeowners, electricians and builders with product comparison, specification guidance, material-list discussions and contractor-oriented sourcing support.",
    ),
    (
        "Where is the shop located?",
        "Kisan Electricals is at Shop No. 12, Nirman Complex, Approach Road, opposite HDFC Bank, Prantij - 383205.",
    ),
]


FAQ_PAGE = HOME_FAQS + [
    (
        "Are all products shown on the site definitely in stock today?",
        "No. Product models, colours and quantities can change. Contact the shop before visiting to confirm the exact item, current price and warranty information.",
    ),
    (
        "What should I send on WhatsApp for a faster reply?",
        "Share the product name, brand, specification, quantity and whether you need pickup, delivery information or a GST invoice. A clear photo of your material list also helps.",
    ),
    (
        "Do you issue GST invoices?",
        "Tell the shop that you require a GST invoice before billing and share the correct business details. Invoice availability can then be confirmed for the purchase.",
    ),
    (
        "How do I enquire about contractor work?",
        "Use the contractor page or WhatsApp to share the site location, load details, drawings if available and the type of electrical work required. Mr. Yogeshbhai can review the requirement and confirm the next step.",
    ),
]


PRODUCTS = [
    {"brand": "GM", "name": "GEO LED Bulb", "details": "9W, B22 holder", "category": "led", "group": "Standard LED bulbs", "image": "led-main"},
    {"brand": "GM", "name": "EVO Emergency Bulb", "details": "9W, B22 emergency bulb", "category": "led", "group": "Emergency and inverter bulbs", "image": "led-main"},
    {"brand": "Philips", "name": "Decoration P45 Bulb", "details": "15W, BC, 230V, red/yellow/orange", "category": "led", "group": "Decorative and coloured lamps", "image": "led-decorative"},
    {"brand": "Philips", "name": "Lustre Lamp Clear", "details": "15W decorative clear lamp", "category": "led", "group": "Decorative and coloured lamps", "image": "led-decorative"},
    {"brand": "Philips", "name": "S10 Starter", "details": "Starter for 20-65W fluorescent tubes", "category": "led", "group": "Decorative and coloured lamps", "image": "led-decorative"},
    {"brand": "Polycab", "name": "Aelius Nxt-G", "details": "9W LED bulb", "category": "led", "group": "Standard LED bulbs", "image": "led-main"},
    {"brand": "Polycab", "name": "Aelius Emergency Dimmable Bulb", "details": "12W, B22, cool daylight 6500K", "category": "led", "group": "Emergency and inverter bulbs", "image": "led-main"},
    {"brand": "Havells", "name": "Adore Jumbo", "details": "40W, B22, cool daylight 6500K", "category": "led", "group": "High-wattage bulbs", "image": "led-main"},
    {"brand": "Havells", "name": "Charge Plus Inverter", "details": "12W, B22, cool daylight 6500K", "category": "led", "group": "Emergency and inverter bulbs", "image": "led-main"},
    {"brand": "Havells", "name": "Classy", "details": "15W, 1575 lm, cool daylight 6500K", "category": "led", "group": "Standard LED bulbs", "image": "led-main"},
    {"brand": "Panasonic", "name": "LED Bulb", "details": "9W, 810 lm, 25,000 burning hours", "category": "led", "group": "Standard LED bulbs", "image": "utility-protection"},
    {"brand": "SturliteX", "name": "Aurora", "details": "16W high-wattage LED bulb", "category": "led", "group": "High-wattage bulbs", "image": "led-main"},
    {"brand": "SturliteX", "name": "Aurora", "details": "20W high-wattage LED bulb", "category": "led", "group": "High-wattage bulbs", "image": "led-main"},
    {"brand": "SturliteX", "name": "LIV", "details": "10W LED bulb", "category": "led", "group": "Standard LED bulbs", "image": "led-main"},
    {"brand": "SturliteX", "name": "Senstur Sensor Bulb", "details": "10W motion sensor bulb", "category": "led", "group": "Sensor bulbs", "image": "led-main"},
    {"brand": "SturliteX", "name": "Deep Downlight", "details": "Recessed downlight; ask for current wattage options", "category": "led", "group": "Downlights and panels", "image": "led-main"},
    {"brand": "Surya", "name": "Bug Shield LED Bulb", "details": "10W, B22, insect-deterrent bulb", "category": "led", "group": "Sensor bulbs", "image": "led-decorative"},
    {"brand": "Goldmedal", "name": "WOW LED Bulb", "details": "12W LED bulb", "category": "led", "group": "Standard LED bulbs", "image": "led-main"},
    {"brand": "Suvego", "name": "High Power LED Reflector", "details": "Super Bright Light, Beam Focus", "category": "utility", "group": "Work lights and reflectors", "image": "utility-protection"},
    {"brand": "Angel Star", "name": "Decorative LED String Lights", "details": "Multicolour fairy lights, model 90L", "category": "utility", "group": "Decorative and festive lighting", "image": "led-decorative"},
    {"brand": "Sinepro", "name": "Agriculture Spray Bulb", "details": "DC 12V, 9W agricultural work light", "category": "utility", "group": "Agricultural lights", "image": "utility-protection"},
    {"brand": "Havells", "name": "Comfort Air Deco", "details": "1200mm decorative fan, white/light copper", "category": "fans", "group": "Decorative ceiling fans", "image": "ceiling-fans"},
    {"brand": "Havells", "name": "Drove Deco", "details": "Decorative ceiling fan; confirm sweep and finish", "category": "fans", "group": "Decorative ceiling fans", "image": "ceiling-fans"},
    {"brand": "GM", "name": "Air Deco 400", "details": "1200mm, magical white, 400 RPM", "category": "fans", "group": "High-speed ceiling fans", "image": "ceiling-fans"},
    {"brand": "Polycab", "name": "Aerofame BLDC", "details": "1200mm, remote, reverse rotation, breeze mode", "category": "fans", "group": "BLDC ceiling fans", "image": "ceiling-fans"},
    {"brand": "Crompton", "name": "Energion Niteo", "details": "5-star BLDC ceiling fan", "category": "fans", "group": "BLDC ceiling fans", "image": "ceiling-fans"},
    {"brand": "Cactus", "name": "CT-EB-40 Blower", "details": "600W heavy-duty industrial blower", "category": "fans", "group": "Industrial blowers", "image": "utility-protection"},
    {"brand": "Purity", "name": "Cooler Submersible Pump", "details": "Anti-dry safety protection pump", "category": "utility", "group": "Cooler pumps", "image": "utility-protection"},
    {"brand": "Locancy", "name": "Cooler Pump", "details": "Cooler pump; exact rating not visible", "category": "utility", "group": "Cooler pumps", "image": "utility-protection"},
    {"brand": "SturliteX", "name": "Portable/Table Fan", "details": "Portable fan; confirm current model and size", "category": "fans", "group": "Portable and table fans", "image": "ceiling-fans"},
    {"brand": "Elley's Electric", "name": "E-Soft 10AX 1-Way Switch", "details": "240V, 1 module, code 902101", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Elley's Electric", "name": "E-Soft 10AX 2-Way Switch", "details": "240V, 1 module, code 902103", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Elley's Electric", "name": "E-Soft 20A 1-Way Switch", "details": "240V, 1 module, code 902107", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Elley's Electric", "name": "E-Soft 5-Step Regulator", "details": "Fan regulator, code 901201", "category": "switches", "group": "Fan regulators", "image": "switches-sockets"},
    {"brand": "Elley's Electric", "name": "E-Soft Universal Socket", "details": "6A + 6A modular socket", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Elley's Electric", "name": "i-mirro 7M Bottom Plate", "details": "Code 909607", "category": "switches", "group": "Modular plates", "image": "plates-accessories"},
    {"brand": "Elley's Electric", "name": "i-mirro 8(H)M Bottom Plate", "details": "Code 909609", "category": "switches", "group": "Modular plates", "image": "plates-accessories"},
    {"brand": "Hi-Fi Electric", "name": "Hi-Class 6A Socket", "details": "6A, 240V, 2 module", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Hi-Fi Electric", "name": "Hi-Class EME 4-Step Regulator", "details": "100W, code 30031", "category": "switches", "group": "Fan regulators", "image": "switches-sockets"},
    {"brand": "Hi-Fi Electric", "name": "Rotary Fan Regulator", "details": "Code 30032", "category": "switches", "group": "Fan regulators", "image": "switches-sockets"},
    {"brand": "Hi-Fi Electric", "name": "Flatino 2-Module Wood Plate", "details": "4.5 x 4.5 inch; white/metallic/texture", "category": "switches", "group": "Modular plates", "image": "plates-accessories"},
    {"brand": "Hi-Fi Electric", "name": "Flatino 8(H)-Module Wood Plate", "details": "White, metallic and texture variants", "category": "switches", "group": "Modular plates", "image": "plates-accessories"},
    {"brand": "Kosch", "name": "KLIO 6A 3-Pin Socket", "details": "240V AC, 2 module, code 700022", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO 6A & 16A Socket with Shutter", "details": "White, code 700025", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KAARA 20A 1-Way Switch", "details": "Jet Black, code 701011JB", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO 10A 1-Way Switch", "details": "Jet Black, code 700001JB", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO 10A 2-Way Switch", "details": "Jet Black, code 700002JB", "category": "switches", "group": "One-way and two-way switches", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO 10A Bell Push Switch", "details": "Jet Black, code 700003JB", "category": "switches", "group": "Bell-push switches", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO 6A International Socket", "details": "Jet Black, code 700024JB", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO Socket", "details": "Jet Black, code 700022JB", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO Additional Socket", "details": "Code 700036; confirm exact socket type", "category": "switches", "group": "Sockets and international sockets", "image": "switches-sockets"},
    {"brand": "Kosch", "name": "KLIO Modular C32 MCB", "details": "Double-pole/C32, Jet Black, code 700095JB", "category": "protection", "group": "MCBs and modular protection", "image": "switches-sockets"},
    {"brand": "Swastik", "name": "Digital Meter", "details": "415V, 100A, 3-wire", "category": "protection", "group": "Digital meters and utility control", "image": "utility-protection"},
    {"brand": "Samrat", "name": "SPP Auto Switch with Overload Control", "details": "Agricultural or motor control auto switch", "category": "protection", "group": "Auto switches and alarms", "image": "utility-protection"},
    {"brand": "Samrat", "name": "Auto Switch", "details": "Automatic motor or starter control product", "category": "protection", "group": "Auto switches and alarms", "image": "utility-protection"},
    {"brand": "Arihant", "name": "Thermal Timer", "details": "Motor-control timer; confirm current range", "category": "protection", "group": "Relays and timers", "image": "contractor-panel-1"},
    {"brand": "Mahendra", "name": "Relay Unit", "details": "Relay unit for motor starter panels", "category": "protection", "group": "Relays and timers", "image": "contractor-panel-1"},
    {"brand": "Singhel", "name": "Metal Clad Protected Plug TP30", "details": "Heavy-duty protected industrial plug", "category": "utility", "group": "Heavy-duty plugs and accessories", "image": "led-main"},
    {"brand": "Ostring", "name": "Rechargeable Work Light", "details": "Model 1971 portable LED work light", "category": "utility", "group": "Work lights and reflectors", "image": "utility-protection"},
    {"brand": "Nipo", "name": "Hyper Batteries", "details": "Battery cells and small accessories", "category": "utility", "group": "Batteries and accessories", "image": "utility-protection"},
    {"brand": "Halonix", "name": "Agni Rechargeable Torch", "details": "3W rechargeable LED torch", "category": "utility", "group": "Rechargeable torches and emergency lights", "image": "utility-protection"},
    {"brand": "Akarplus", "name": "Rechargeable LED Flashlight", "details": "Rechargeable flashlight; confirm current model", "category": "utility", "group": "Rechargeable torches and emergency lights", "image": "utility-protection"},
    {"brand": "Bajaj", "name": "Emergency Light", "details": "Rechargeable emergency lamp; confirm current model", "category": "utility", "group": "Rechargeable torches and emergency lights", "image": "utility-protection"},
]


CATEGORY_META = {
    "led": {
        "name": "LED Lighting",
        "gu": "LED લાઇટિંગ",
        "description": "Standard bulbs, emergency bulbs, decorative lamps, downlights and sensor lighting.",
        "path": "/products/led-lights/",
        "image": "led-main",
    },
    "fans": {
        "name": "Ceiling Fans",
        "gu": "સીલિંગ ફેન",
        "description": "Decorative, high-speed and BLDC fans, plus blower support for practical projects.",
        "path": "/products/ceiling-fans/",
        "image": "ceiling-fans",
    },
    "switches": {
        "name": "Switches & Sockets",
        "gu": "સ્વીચીસ અને સોકેટ્સ",
        "description": "Modular switches, sockets, regulators, plates and matching board accessories.",
        "path": "/products/switches-sockets/",
        "image": "switches-sockets",
    },
    "wires": {
        "name": "Wires & Cables",
        "gu": "વાયર્સ અને કેબલ્સ",
        "description": "House-wire enquiries, flexible cable discussions and safety-first gauge guidance.",
        "path": "/products/wires-cables/",
        "image": None,
    },
    "protection": {
        "name": "MCB, RCCB & Protection",
        "gu": "એમસિબી અને પ્રોટેક્શન",
        "description": "Meters, auto switches, modular protection items, timers and control accessories.",
        "path": "/products/mcb-electrical-protection/",
        "image": "contractor-panel-1",
    },
    "utility": {
        "name": "Pumps, Tools & Utility",
        "gu": "પમ્પ્સ, ટૂલ્સ અને યુટિલિટી",
        "description": "Cooler pumps, reflectors, rechargeable torches, work lights and heavy-duty accessories.",
        "path": "/products/pumps-tools-utility/",
        "image": "utility-protection",
    },
}


FEATURED_HOME = [
    "GEO LED Bulb",
    "EVO Emergency Bulb",
    "Aelius Emergency Dimmable Bulb",
    "Adore Jumbo",
    "Charge Plus Inverter",
    "Aerofame BLDC",
    "Air Deco 400",
    "Energion Niteo",
    "E-Soft 10AX 1-Way Switch",
    "KLIO 6A 3-Pin Socket",
    "Bug Shield LED Bulb",
    "Cooler Submersible Pump",
]


WIRES_GUIDE = [
    "House wires",
    "Flexible cables",
    "Submersible cables",
    "Telecom and control wire",
]


CATEGORY_FAQS = {
    "led": [
        ("Which LED lights are available in Prantij?", "The catalogue includes standard bulbs, emergency bulbs, coloured decorative lamps, downlights, sensor bulbs, agricultural work lights and reflector-style lighting. Confirm the exact model before visiting."),
        ("How should I choose between 9W, 12W, 15W and 40W bulbs?", "Start with room size, holder type and brightness requirement. Available B22 options can include 9W, 12W, 15W and 40W formats, but the best choice depends on the fitting and use case."),
        ("Can I confirm colour temperature and holder type on WhatsApp?", "Yes. Send the brand, model, B22 or holder requirement, and whether you need cool daylight or another finish so the shop can check the exact box before you travel."),
    ],
    "fans": [
        ("How can I confirm fan model availability?", "Share the brand, sweep size, finish, and whether you need decorative, high-speed or BLDC. The shop can then confirm the closest visible boxed model."),
        ("What fan sizes are shown in the current catalogue?", "The visible fan range includes 1200mm models across decorative, high-speed and BLDC categories. For other sizes, confirm directly with the store."),
        ("Do remote features need confirmation before purchase?", "Yes. BLDC and remote-control features should be confirmed on the exact box or model before dispatch or pickup."),
    ],
    "switches": [
        ("Which modular switch brands are visible in the shop photos?", "The documented switch and plate range includes Elley's Electric, Hi-Fi Electric and Kosch modular products with several visible model codes."),
        ("Can I ask for Jet Black or white variants?", "Yes. Several Kosch items are visible in Jet Black while Hi-Fi and Elley's examples appear in white or mixed finish ranges. Confirm the exact colour before visiting."),
        ("Do you have modular plates and regulators as well?", "Yes. The catalogue includes wood plates, bottom plates and multiple fan-regulator variants alongside sockets and switches."),
    ],
    "protection": [
        ("What protection products are visible in the catalogue?", "The current catalogue shows digital meters, auto switches, a modular C32 MCB, timers, relay-related products and heavy-duty plug accessories."),
        ("Is installation advice provided online?", "No detailed live-board installation guidance is published on the site. Use the page to identify products, then speak to the shop or contractor side for the correct application."),
        ("Can I enquire about panel-related items and contractor coordination together?", "Yes. Use the protection page for product identification and the contractor page when site scope, LT panels or distribution work needs a dedicated project discussion."),
    ],
    "utility": [
        ("What utility products are visible right now?", "The visible utility catalogue includes cooler pumps, rechargeable torches, work lights, batteries, reflectors, decorative string lights and heavy-duty plugs."),
        ("Can I enquire about agricultural lights and work lights?", "Yes. The visible catalogue includes an agricultural spray bulb, reflector products and rechargeable work-light style items."),
        ("Should I expect live stock for every utility product shown?", "No. Models and quantities can change, so confirm current stock, price and brand availability on WhatsApp before visiting."),
    ],
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def abs_url(path: str) -> str:
    return f"{BASE_URL}/{path.lstrip('/')}"


def rel_prefix(depth: int) -> str:
    return "../" * depth


def href(depth: int, path: str) -> str:
    prefix = rel_prefix(depth)
    if path == "/":
        return f"{prefix or './'}"
    return f"{prefix}{path.lstrip('/')}"


def catalog_image_rel(key: str) -> str:
    return f"assets/catalog/{key}.webp"


def wa_link(message: str) -> str:
    return f"https://wa.me/918758964040?text={quote(message)}"


def optimize_catalog_images() -> None:
    out_dir = ROOT / "assets" / "catalog"
    out_dir.mkdir(parents=True, exist_ok=True)
    for key, filename in CATALOG_IMAGE_SOURCES.items():
        src = REFERENCE_ROOT / filename
        out = out_dir / f"{key}.webp"
        if not src.exists():
            continue
        image = Image.open(src).convert("RGB")
        image.thumbnail((960, 960))
        image.save(out, "WEBP", quality=84, method=6)


def build_icons() -> None:
    source = ROOT / "assets" / "favicon.jpg"
    if not source.exists():
        return
    image = Image.open(source).convert("RGBA")
    for size, name in [
        (180, "apple-touch-icon.png"),
        (192, "icon-192.png"),
        (512, "icon-512.png"),
    ]:
        resized = image.resize((size, size))
        resized.save(ROOT / name, "PNG")
    manifest = {
        "name": BUSINESS_NAME,
        "short_name": "Kisan Electricals",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#071A2D",
        "theme_color": "#071A2D",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    (ROOT / "site.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def image_tag(
    depth: int,
    rel_path: str,
    alt_text: str,
    cls: str = "",
    lightbox: bool = False,
    priority: bool = False,
) -> str:
    source_path = ROOT / rel_path
    width = height = None
    if source_path.exists():
        with Image.open(source_path) as image:
            width, height = image.size

    attrs = [
        f'src="{esc(href(depth, "/" + rel_path))}"',
        f'alt="{esc(alt_text)}"',
        f'loading="{"eager" if priority else "lazy"}"',
        'decoding="async"',
    ]
    if priority:
        attrs.append('fetchpriority="high"')
    if width and height:
        attrs.extend([f'width="{width}"', f'height="{height}"'])
    if cls:
        attrs.append(f'class="{esc(cls)}"')
    if lightbox:
        attrs.append('tabindex="0"')
        attrs.append('role="button"')
        attrs.append('data-lightbox="true"')
        attrs.append(f'data-lightbox-src="{esc(href(depth, "/" + rel_path))}"')
    image_html = f"<img {' '.join(attrs)}>"

    if "/optimized/" not in rel_path or not rel_path.endswith("_orig.webp"):
        return image_html

    rel = Path(rel_path)
    base_name = rel.stem.removesuffix("_orig")
    asset_dir = ROOT / rel.parent

    def build_srcset(extension: str) -> str:
        candidates: dict[int, str] = {}
        for candidate in asset_dir.glob(f"{base_name}_*.{extension}"):
            if candidate.stem.endswith("_thumb"):
                continue
            with Image.open(candidate) as variant:
                candidate_width = variant.size[0]
            candidate_rel = (rel.parent / candidate.name).as_posix()
            candidates[candidate_width] = href(depth, "/" + candidate_rel)
        return ", ".join(f"{esc(url)} {candidate_width}w" for candidate_width, url in sorted(candidates.items()))

    avif_srcset = build_srcset("avif")
    webp_srcset = build_srcset("webp")
    sources = []
    if avif_srcset:
        sources.append(f'<source type="image/avif" srcset="{avif_srcset}" sizes="(max-width: 768px) 100vw, 50vw">')
    if webp_srcset:
        sources.append(f'<source type="image/webp" srcset="{webp_srcset}" sizes="(max-width: 768px) 100vw, 50vw">')
    return f'<picture>{"".join(sources)}{image_html}</picture>'


def breadcrumb_schema(path: str, crumbs: list[tuple[str, str]]) -> dict:
    items = []
    for index, (name, crumb_path) in enumerate(crumbs, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": index,
                "name": name,
                "item": abs_url(crumb_path),
            }
        )
    return {
        "@type": "BreadcrumbList",
        "@id": f"{abs_url(path)}#breadcrumb",
        "itemListElement": items,
    }


def base_business_schema() -> dict:
    return {
        "@type": ["Store", "LocalBusiness"],
        "@id": f"{BASE_URL}/#business",
        "name": BUSINESS_NAME,
        "alternateName": BUSINESS_NAME_GU,
        "description": "Kisan Electricals is a long-running electrical products shop and contractor enquiry destination in Prantij, Gujarat. The catalogue covers lighting, fans, modular accessories, protection products and utility items.",
        "url": BASE_URL,
        "logo": abs_url("icon-512.png"),
        "image": abs_url(STORY_IMAGES["store_closeup"]),
        "telephone": PRIMARY_PHONE_E164,
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": PRIMARY_PHONE_E164, "contactType": "sales"},
            {"@type": "ContactPoint", "telephone": SECONDARY_PHONE_E164, "contactType": "sales"},
        ],
        "sameAs": [GOOGLE_PROFILE, FACEBOOK, INSTAGRAM],
        "hasMap": GOOGLE_PROFILE,
        "foundingDate": "1976",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Shop No. 12, Nirman Complex, Approach Road, Opposite HDFC Bank",
            "addressLocality": "Prantij",
            "addressRegion": "Gujarat",
            "postalCode": "383205",
            "addressCountry": "IN",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": "23.4357", "longitude": "72.8596"},
        "areaServed": {"@type": "AdministrativeArea", "name": "Prantij"},
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "08:30",
                "closes": "19:45",
            }
        ],
    }


def page_schema(
    *,
    path: str,
    title: str,
    description: str,
    kind: str,
    breadcrumbs: list[tuple[str, str]] | None = None,
    faqs: list[tuple[str, str]] | None = None,
    item_names: list[str] | None = None,
    service_description: str | None = None,
) -> str:
    graph: list[dict] = [base_business_schema()]
    page_id = f"{abs_url(path)}#page"
    page_entry = {
        "@type": {
            "home": "WebPage",
            "collection": "CollectionPage",
            "about": "AboutPage",
            "contact": "ContactPage",
            "gallery": "ImageGallery",
            "faq": "FAQPage",
            "service": "WebPage",
        }[kind],
        "@id": page_id,
        "url": abs_url(path),
        "name": title,
        "description": description,
        "about": {"@id": f"{BASE_URL}/#business"},
    }
    graph.append(page_entry)
    if kind == "home":
        graph.append({"@type": "WebSite", "@id": f"{BASE_URL}/#website", "url": BASE_URL, "name": BUSINESS_NAME, "publisher": {"@id": f"{BASE_URL}/#business"}})
    if breadcrumbs:
        graph.append(breadcrumb_schema(path, breadcrumbs))
    if item_names:
        graph.append(
            {
                "@type": "ItemList",
                "@id": f"{abs_url(path)}#items",
                "itemListElement": [
                    {"@type": "ListItem", "position": idx, "name": name}
                    for idx, name in enumerate(item_names, start=1)
                ],
            }
        )
    if service_description:
        graph.append(
            {
                "@type": "Service",
                "@id": f"{abs_url(path)}#service",
                "name": title,
                "provider": {"@id": f"{BASE_URL}/#business"},
                "description": service_description,
                "areaServed": {"@type": "AdministrativeArea", "name": "Prantij and surrounding areas"},
            }
        )
    if faqs and kind == "faq":
        graph.append(
            {
                "@type": "FAQPage",
                "@id": f"{abs_url(path)}#faq",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in faqs
                ],
            }
        )
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_breadcrumbs(depth: int, crumbs: list[tuple[str, str]]) -> str:
    items = []
    for name, path in crumbs:
        if path:
            items.append(f'<li><a href="{esc(href(depth, path))}">{esc(name)}</a></li>')
        else:
            items.append(f"<li>{esc(name)}</li>")
    return f'<ol class="breadcrumb-list">{"".join(items)}</ol>'


def render_head(depth: int, title: str, description: str, path: str, og_image: str, schema: str) -> str:
    return dedent(
        f"""\
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
          <title>{esc(title)}</title>
          <meta name="description" content="{esc(description)}">
          <meta name="robots" content="index, follow">
          <meta name="theme-color" content="#071A2D">
          <link rel="canonical" href="{esc(abs_url(path))}">
          <link rel="icon" type="image/x-icon" href="{esc(href(depth, '/favicon.ico'))}">
          <link rel="apple-touch-icon" href="{esc(href(depth, '/apple-touch-icon.png'))}">
          <link rel="manifest" href="{esc(href(depth, '/site.webmanifest'))}">
          <meta property="og:type" content="website">
          <meta property="og:title" content="{esc(title)}">
          <meta property="og:description" content="{esc(description)}">
          <meta property="og:url" content="{esc(abs_url(path))}">
          <meta property="og:image" content="{esc(abs_url(og_image))}">
          <meta property="og:image:alt" content="{esc(title)}">
          <meta property="og:locale" content="en_IN">
          <meta name="twitter:card" content="summary_large_image">
          <meta name="twitter:title" content="{esc(title)}">
          <meta name="twitter:description" content="{esc(description)}">
          <meta name="twitter:image" content="{esc(abs_url(og_image))}">
          <link rel="preconnect" href="https://fonts.googleapis.com">
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Gujarati:wght@400;600;700&display=swap" rel="stylesheet">
          <link rel="stylesheet" href="{esc(href(depth, '/index.css'))}">
          <link rel="stylesheet" href="{esc(href(depth, '/site-overrides.css'))}">
          <script defer src="{esc(href(depth, '/site.js'))}"></script>
          <script type="application/ld+json">
        {schema}
          </script>
        </head>
        """
    )


def render_header(depth: int, active: str) -> str:
    nav_links = []
    for key, label, path in NAV_ITEMS:
        if key == "products":
            submenu = "".join(
                f'<a href="{esc(href(depth, sub_path))}">{esc(sub_label)}</a>'
                for sub_label, sub_path in PRODUCT_MENU
            )
            current = " nav-link--active" if active == key else ""
            nav_links.append(
                f"""
                <li class="nav-item-has-dropdown">
                  <a class="nav-link nav-dropdown-toggle{current}" href="{esc(href(depth, path))}">Products</a>
                  <div class="nav-dropdown-menu">{submenu}</div>
                </li>
                """
            )
        else:
            current = " style=\"color: var(--color-brand-yellow);\"" if active == key else ""
            nav_links.append(f'<li><a class="nav-link" href="{esc(href(depth, path))}"{current}>{esc(label)}</a></li>')

    mobile_links = []
    for key, label, path in NAV_ITEMS:
        mobile_links.append(f'<li><a class="mobile-nav-link" href="{esc(href(depth, path))}">{esc(label)}</a></li>')
    mobile_links.extend(
        f'<li><a class="mobile-nav-link" href="{esc(href(depth, path))}">{esc(label)}</a></li>'
        for label, path in PRODUCT_MENU
    )
    return dedent(
        f"""\
        <a href="#main-content" class="skip-link">Skip to content</a>
        <div class="announcement-bar">
          <div class="container">
            <div class="announcement-info"><span class="announcement-tag">Prantij</span><span>Prantij, Gujarat</span></div>
            <div class="announcement-links">
              <a class="announcement-link" href="tel:{PRIMARY_PHONE_E164}">{esc(PRIMARY_PHONE)}</a>
              <span>|</span>
              <span>{esc(HOURS_TEXT)}</span>
              <span>|</span>
              <a class="announcement-link" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Get Directions</a>
            </div>
          </div>
        </div>
        <header class="site-header">
          <div class="container header-inner">
            <a class="brand-logo" href="{esc(href(depth, '/'))}">
              <span class="brand-icon-wrap" aria-hidden="true">K</span>
              <span class="brand-text">
                <span class="brand-title">Kisan <span>Electricals</span></span>
                <span class="brand-sub" lang="gu">{esc(BUSINESS_NAME_GU)}</span>
              </span>
            </a>
            <nav class="main-nav" aria-label="Primary">
              <ul class="nav-list">
                {''.join(nav_links)}
              </ul>
            </nav>
            <div class="header-actions">
              <a class="btn btn-outline-light header-cta-call" href="tel:{PRIMARY_PHONE_E164}">Call Shop</a>
              <a class="btn btn-secondary header-cta-wa" href="https://wa.me/918758964040">WhatsApp</a>
              <button type="button" class="menu-toggle-btn" data-menu-toggle aria-label="Open navigation menu" aria-controls="mobile-menu" aria-expanded="false">Menu</button>
            </div>
          </div>
        </header>
        <div class="mobile-menu-backdrop" data-mobile-backdrop></div>
        <aside class="mobile-menu-drawer" id="mobile-menu" data-mobile-drawer aria-label="Mobile navigation" aria-hidden="true">
          <div class="mobile-menu-head">
            <strong style="color:#fff;">Menu</strong>
            <button type="button" class="menu-toggle-btn" data-menu-close aria-label="Close navigation menu">Close</button>
          </div>
          <ul class="mobile-nav-list">
            {''.join(mobile_links)}
          </ul>
          <div class="mobile-menu-actions">
            <a class="btn btn-outline-light" href="tel:{PRIMARY_PHONE_E164}">Call {esc(PRIMARY_PHONE)}</a>
            <a class="btn btn-secondary" href="https://wa.me/918758964040">WhatsApp the shop</a>
            <a class="btn btn-primary" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Directions</a>
          </div>
        </aside>
        """
    )


def render_footer(depth: int) -> str:
    product_links = "".join(f'<li><a href="{esc(href(depth, path))}">{esc(label)}</a></li>' for label, path in PRODUCT_MENU)
    info_links = "".join(
        [
            f'<li><a href="{esc(href(depth, "/about-kisan-electricals/"))}">Our Story</a></li>',
            f'<li><a href="{esc(href(depth, "/electrical-services/"))}">Electrical Services</a></li>',
            f'<li><a href="{esc(href(depth, "/ugvcl-electrical-contractor-prantij/"))}">Contractor Work</a></li>',
            f'<li><a href="{esc(href(depth, "/gallery/"))}">Gallery</a></li>',
            f'<li><a href="{esc(href(depth, "/faqs/"))}">FAQs</a></li>',
        ]
    )
    legal_links = "".join(
        [
            f'<li><a href="{esc(href(depth, "/privacy-policy/"))}">Privacy Policy</a></li>',
            f'<li><a href="{esc(href(depth, "/terms-and-disclaimer/"))}">Terms &amp; Disclaimers</a></li>',
            f'<li><a href="{esc(href(depth, "/warranty-and-returns/"))}">Warranty &amp; Returns</a></li>',
        ]
    )
    return dedent(
        f"""\
        <div class="mobile-action-bar">
          <a class="bar-btn bar-btn-call" href="tel:{PRIMARY_PHONE_E164}">Call</a>
          <a class="bar-btn bar-btn-wa" href="https://wa.me/918758964040">WhatsApp</a>
          <a class="bar-btn bar-btn-map" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Directions</a>
        </div>
        <footer class="site-footer">
          <div class="container">
            <div class="footer-disclaimers">
              Product models, colours, prices and availability may change. Please call or WhatsApp before visiting for a specific item. Kisan Electricals is an independent electrical retailer and contractor, not a UGVCL office or customer-care centre.
            </div>
            <div class="footer-grid">
              <div class="footer-col">
                <h4>{esc(BUSINESS_NAME)}</h4>
                <p>Serving Prantij with practical product guidance and electrical retail support since 1976.</p>
                <p style="margin-top:0.85rem;">{esc(ADDRESS_LINE)}</p>
                <div class="footer-socials">
                  <a href="{esc(FACEBOOK)}" target="_blank" rel="noopener noreferrer">Facebook</a>
                  <a href="{esc(INSTAGRAM)}" target="_blank" rel="noopener noreferrer">Instagram</a>
                  <a href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Google Profile</a>
                </div>
              </div>
              <div class="footer-col">
                <h4>Products</h4>
                <ul class="footer-nav">{product_links}</ul>
              </div>
              <div class="footer-col">
                <h4>Information</h4>
                <ul class="footer-nav">{info_links}</ul>
              </div>
              <div class="footer-col">
                <h4>Policies</h4>
                <ul class="footer-nav">{legal_links}</ul>
              </div>
            </div>
            <div class="footer-bottom">
              <span>(c) 2026 Kisan Electricals</span>
              <span>{esc(HOURS_TEXT)}</span>
              <span>{esc(PRIMARY_PHONE)} | {esc(SECONDARY_PHONE)}</span>
            </div>
          </div>
        </footer>
        """
    )


def render_faqs(faqs: list[tuple[str, str]]) -> str:
    items = []
    for index, (question, answer) in enumerate(faqs):
        active = " is-active" if index == 0 else ""
        expanded = "true" if index == 0 else "false"
        items.append(
            f"""
            <article class="faq-item{active}">
              <button class="faq-trigger" type="button" aria-expanded="{expanded}">
                <span>{esc(question)}</span>
                <span class="faq-icon-arrow">+</span>
              </button>
              <div class="faq-panel"><p>{esc(answer)}</p></div>
            </article>
            """
        )
    return f'<div class="faq-accordion">{"".join(items)}</div>'


def category_image_path(product: dict) -> str:
    return catalog_image_rel(product["image"])


def product_card(depth: int, product: dict) -> str:
    meta = CATEGORY_META.get(product["category"], CATEGORY_META["utility"])
    category_mark = {
        "led": "LED",
        "fans": "FAN",
        "switches": "SW",
        "protection": "SAFE",
        "utility": "UTIL",
    }.get(product["category"], "ITEM")
    message = (
        f"Hello Kisan Electricals, I am enquiring about {product['brand']} {product['name']} "
        f"({product['details']}). Quantity required: __. Please confirm current stock, "
        f"price, warranty and pickup or delivery options."
    )
    return f"""
    <article class="product-card" data-product-card="true" data-category="{esc(product['category'])}" data-brand="{esc(product['brand'])}" data-search="{esc(f"{product['brand']} {product['name']} {product['details']} {meta['name']} {product['group']}")}">
      <div class="product-card-topline">
        <span class="product-category-mark" aria-hidden="true">{esc(category_mark)}</span>
        <span class="product-badge">{esc(product['brand'])}</span>
      </div>
      <h3 class="product-title">{esc(product['name'])}</h3>
      <p class="product-desc">{esc(product['details'])}</p>
      <div class="product-meta">{esc(product['group'])} / {esc(meta['name'])}</div>
      <div class="product-status-row">
        <span class="status-indicator">Ask for Availability</span>
      </div>
      <a class="btn btn-secondary" href="{esc(wa_link(message))}" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp</a>
    </article>
    """


def group_products(category_key: str) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for product in PRODUCTS:
        if product["category"] != category_key:
            continue
        groups.setdefault(product["group"], []).append(product)
    return groups


def category_overview_cards() -> str:
    cards = []
    for key in ["led", "fans", "switches", "wires", "protection", "utility"]:
        meta = CATEGORY_META[key]
        visual = (
            f'<div class="product-card-thumb">{image_tag(0, catalog_image_rel(meta["image"]), meta["name"])}</div>'
            if meta["image"]
            else '<div class="product-card-thumb category-wire-visual" aria-hidden="true"><span></span><span></span><span></span></div>'
        )
        cards.append(
            f"""
            <article class="product-card">
              {visual}
              <h3 class="product-title">{esc(meta['name'])}</h3>
              <div class="product-title-gu" lang="gu">{esc(meta['gu'])}</div>
              <p class="product-desc">{esc(meta['description'])}</p>
              <a class="btn btn-outline" href="{esc(meta['path'])}">View Products</a>
            </article>
            """
        )
    return "".join(cards)


def audience_cards() -> str:
    items = [
        ("For Homeowners", "Compare fittings, wattage, switch styles and fan choices before buying for a home upgrade or repair."),
        ("For Electricians", "Share material lists, model codes and quantities so the shop can confirm visible options and invoice needs."),
        ("For Builders & Contractors", "Discuss bulk sourcing, distribution items, switchboard materials and contractor-side coordination requirements."),
    ]
    return "".join(
        f'<div class="mini-card"><h3>{esc(title)}</h3><p>{esc(desc)}</p></div>' for title, desc in items
    )


def feature_cards_by_name(names: list[str], depth: int) -> str:
    wanted = [p for p in PRODUCTS if p["name"] in names]
    return "".join(product_card(depth, product) for product in wanted)


def home_page() -> str:
    title = "Kisan Electricals Prantij | Electrical Store Since 1976"
    description = "Electrical products, real product guidance and direct availability checks from Kisan Electricals in Prantij since 1976."
    schema = page_schema(path="/", title=title, description=description, kind="home")
    home_category_layout = [
        ("led", "01", "wide"),
        ("fans", "02", "standard"),
        ("switches", "03", "standard"),
        ("wires", "04", "third"),
        ("protection", "05", "third"),
        ("utility", "06", "third"),
    ]
    home_category_cards = "".join(
        f"""
        <a class="home-category-card home-category-card--{key} home-category-card--{size}" href="{esc(href(0, CATEGORY_META[key]['path']))}">
          <div class="home-category-card-head"><span>{number}</span><small lang="gu">{esc(CATEGORY_META[key]['gu'])}</small></div>
          <div class="home-category-card-body">
            <h3>{esc(CATEGORY_META[key]['name'])}</h3>
            <p>{esc(CATEGORY_META[key]['description'])}</p>
            <strong>Explore category <span aria-hidden="true">→</span></strong>
          </div>
        </a>
        """
        for key, number, size in home_category_layout
    )
    featured_brands = [
        "GM",
        "Havells",
        "Polycab",
        "Crompton",
        "Philips",
        "Panasonic",
        "Goldmedal",
        "Kosch",
        "Elley's Electric",
        "Hi-Fi Electric",
        "Bajaj",
        "Halonix",
    ]
    body = f"""
    <main id="main-content">
      <section class="home-hero">
        <div class="container home-hero-grid">
          <div class="home-hero-copy">
            <div class="home-hero-kicker"><span>Since 1976</span><span>Prantij, Gujarat</span></div>
            <h1>Electrical Products, Project Support &amp; Practical Guidance in Prantij</h1>
            <p>Lighting, fans, switches, wires, protection products and utility items—supported by a local family business that helps you choose the right product before you buy.</p>
            <div class="home-hero-actions">
              <a class="btn btn-primary" href="https://wa.me/918758964040">WhatsApp Your Requirement</a>
              <a class="btn btn-outline-light" href="./products/">Browse Product Categories</a>
            </div>
            <a class="home-hero-direction" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Shop No. 12, Nirman Complex, opposite HDFC Bank <span aria-hidden="true">↗</span></a>
          </div>
          <div class="home-hero-media">
            <div class="home-hero-photo">{image_tag(0, STORY_IMAGES["family_customer"], "Kisan Electricals team guiding customers inside the Prantij shop", priority=True)}</div>
            <div class="home-hero-photo-label"><strong>Direct, local guidance</strong><span>Compare the requirement, specification and available options at the counter.</span></div>
          </div>
        </div>
        <div class="container home-trust-grid" aria-label="Business highlights">
          <div><strong>1976</strong><span>Serving Prantij since</span></div>
          <div><strong>3</strong><span>Generations of local service</span></div>
          <div><strong>6</strong><span>Main product categories</span></div>
          <div><strong>2</strong><span>Retail and contractor routes</span></div>
        </div>
      </section>
      <section class="section-padding home-categories-section">
        <div class="container">
          <div class="home-section-heading">
            <div>
              <span class="section-eyebrow">Shop by Requirement</span>
              <h2>Find the Right Product Route</h2>
            </div>
            <p>Start with the category—not a long list of models. The shop will confirm the exact brand, specification, current price and availability.</p>
          </div>
          <div class="home-category-grid">{home_category_cards}</div>
          <div class="home-category-footer"><span>Already have a material list?</span><a href="https://wa.me/918758964040">Send it directly on WhatsApp <span aria-hidden="true">→</span></a></div>
        </div>
      </section>
      <section class="section-padding home-guidance-section">
        <div class="container home-guidance-grid">
          <div class="home-guidance-media">{image_tag(0, STORY_IMAGES["three_gen"], "Three generations of Kisan Electricals helping a family at the shop counter")}</div>
          <div class="home-guidance-copy">
            <span class="section-eyebrow">Why Customers Visit</span>
            <h2>Bring the requirement.<br>Leave with clarity.</h2>
            <p class="home-guidance-intro">A product catalogue can show names. The real value is matching the product to the room, fitting, load, finish, budget or project requirement.</p>
            <div class="home-guidance-list">
              <div><span>01</span><p><strong>Compare practical options</strong> across brands, sizes, wattages, finishes and visible specifications.</p></div>
              <div><span>02</span><p><strong>Check before travelling</strong> by sending the product name, model photo or complete material list.</p></div>
              <div><span>03</span><p><strong>Confirm the buying details</strong> including price, warranty, quantity, GST invoice and pickup discussion.</p></div>
            </div>
            <div class="home-guidance-actions"><a class="btn btn-primary" href="./electrical-services/">See How We Can Help</a><a class="home-text-link" href="tel:{PRIMARY_PHONE_E164}">Call {esc(PRIMARY_PHONE)} <span aria-hidden="true">→</span></a></div>
          </div>
        </div>
      </section>
      <section class="section-padding home-routes-section">
        <div class="container">
          <div class="home-section-heading home-section-heading--light">
            <div><span class="section-eyebrow">One Business, Two Routes</span><h2>Choose the Help You Need</h2></div>
            <p>Keep everyday product enquiries separate from larger site, panel and contractor discussions.</p>
          </div>
          <div class="home-route-grid">
            <a class="home-route-card" href="./products/">
              <div class="home-route-media home-route-media--store">{image_tag(0, STORY_IMAGES["store_wideshot"], "Kisan Electricals storefront at Nirman Complex in Prantij")}</div>
              <div class="home-route-content"><span>Retail &amp; Supply</span><h3>Products and Material Lists</h3><p>For homes, shops, electricians and builders needing products, comparisons or bulk-list discussion.</p><strong>Browse products <span aria-hidden="true">→</span></strong></div>
            </a>
            <a class="home-route-card" href="./ugvcl-electrical-contractor-prantij/">
              <div class="home-route-media">{image_tag(0, catalog_image_rel("contractor-panel-1"), "Electrical control panel from contractor-related project work")}</div>
              <div class="home-route-content"><span>Contractor Wing</span><h3>Site, Panel and Project Work</h3><p>For inspection, panel requirements, electrical project coordination and contractor enquiries.</p><strong>View contractor work <span aria-hidden="true">→</span></strong></div>
            </a>
          </div>
        </div>
      </section>
      <section class="section-padding home-brands-section">
        <div class="container home-brands-layout">
          <div class="home-brands-copy">
            <span class="section-eyebrow">Brand Choice</span>
            <h2>Recognisable Electrical Brands, Compared Locally</h2>
            <p>Ask for your preferred brand or share the specification. If the exact model is unavailable, the shop can discuss a suitable current alternative.</p>
            <a class="home-text-link" href="./electrical-brands/">Browse the complete brand catalogue <span aria-hidden="true">→</span></a>
          </div>
          <div class="home-brand-cloud">
            {''.join(f'<span>{esc(name)}</span>' for name in featured_brands)}
            <a href="./electrical-brands/">More brands +</a>
          </div>
        </div>
      </section>
      <section class="section-padding home-visit-section">
        <div class="container home-visit-shell">
          <div class="home-visit-content">
            <span class="section-eyebrow">Visit Kisan Electricals</span>
            <h2>Easy to Find.<br>Easy to Contact.</h2>
            <p>Visit the Nirman Complex shop or confirm your requirement before travelling.</p>
            <div class="home-visit-details">
              <div><span>A</span><p><strong>Address</strong>{esc(ADDRESS_LINE)}</p></div>
              <div><span>P</span><p><strong>Call or WhatsApp</strong><a href="tel:{PRIMARY_PHONE_E164}">{esc(PRIMARY_PHONE)}</a><br><a href="tel:{SECONDARY_PHONE_E164}">{esc(SECONDARY_PHONE)}</a></p></div>
              <div><span>H</span><p><strong>Working hours</strong>{esc(HOURS_TEXT)}</p></div>
            </div>
            <div class="home-visit-actions">
              <a class="btn btn-primary" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Get Directions</a>
              <a class="btn btn-outline-light" href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Read Live Google Reviews</a>
            </div>
          </div>
          <div class="home-visit-map"><iframe class="map-embed" src="{esc(MAP_EMBED)}" title="Map showing Kisan Electricals in Prantij" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
        </div>
      </section>
      <section class="section-padding home-faq-section">
        <div class="container home-faq-layout">
          <div class="home-faq-heading">
            <span class="section-eyebrow">Before You Visit</span>
            <h2>Quick Answers for Local Buyers</h2>
            <p>For a product-specific answer, send the brand, model, quantity and a photo if available.</p>
            <a class="home-text-link" href="./faqs/">View all frequently asked questions <span aria-hidden="true">→</span></a>
          </div>
          <div>{render_faqs(HOME_FAQS[:3])}</div>
        </div>
      </section>
      <section class="home-final-cta">
        <div class="container home-final-cta-inner">
          <div><span>Need a faster answer?</span><h2>Send the product photo or complete material list.</h2></div>
          <div class="home-final-cta-actions"><a class="btn btn-primary" href="https://wa.me/918758964040">Start a WhatsApp Enquiry</a><a class="btn btn-outline-light" href="./contact/">Other Contact Options</a></div>
        </div>
      </section>
    </main>
    """
    return render_document(0, "home", title, description, "/", STORY_IMAGES["store_wideshot"], schema, body)


def render_document(depth: int, active: str, title: str, description: str, path: str, og_image: str, schema: str, body: str) -> str:
    return "<!DOCTYPE html>\n<html lang=\"en-IN\">\n" + render_head(depth, title, description, path, og_image, schema) + "\n<body>\n" + render_header(depth, active) + body + render_footer(depth) + "\n</body>\n</html>\n"


def build_collection_page(
    *,
    title: str,
    description: str,
    path: str,
    active: str,
    depth: int,
    hero_kicker: str,
    hero_heading: str,
    hero_text: str,
    hero_image: str,
    hero_alt: str,
    breadcrumbs: list[tuple[str, str]],
    intro_answer: str,
    groups: dict[str, list[dict]] | None,
    extra_sections: str = "",
    faqs: list[tuple[str, str]] | None = None,
) -> str:
    item_names = [product["name"] for group in (groups or {}).values() for product in group]
    schema = page_schema(path=path, title=title, description=description, kind="collection", breadcrumbs=breadcrumbs, item_names=item_names)
    sections = []
    if groups:
        for group_name, items in groups.items():
            sections.append(
                f"""
                <section class="section-padding">
                  <div class="container">
                    <div class="section-subhead">
                      <h2>{esc(group_name)}</h2>
                      <p>Compare the listed specifications, then contact the shop to confirm the exact model, finish, price and current availability.</p>
                    </div>
                    <div class="products-grid">{''.join(product_card(depth, item) for item in items)}</div>
                  </div>
                </section>
                """
            )
    faq_section = ""
    if faqs:
        faq_section = f"""
        <section class="section-padding faq-section">
          <div class="container">
            <div class="section-subhead" style="text-align:center;">
              <h2>Category FAQs</h2>
            </div>
            {render_faqs(faqs)}
          </div>
        </section>
        """
    body = f"""
    <main id="main-content">
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div class="page-hero-body">
            {render_breadcrumbs(depth, breadcrumbs)}
            <span class="page-hero-kicker">{esc(hero_kicker)}</span>
            <h1>{esc(hero_heading)}</h1>
            <p>{esc(hero_text)}</p>
            <div class="page-hero-cta-row">
              <a class="btn btn-primary" href="https://wa.me/918758964040">WhatsApp an Enquiry</a>
              <a class="btn btn-outline" href="{esc(href(depth, '/products/'))}">Back to Products</a>
            </div>
          </div>
          <div class="page-hero-visual page-hero-visual--landscape">{image_tag(depth, catalog_image_rel(hero_image), hero_alt, priority=True)}</div>
        </div>
      </section>
      <section class="container">
        <div class="answer-strip">{esc(intro_answer)}</div>
      </section>
      {''.join(sections)}
      {extra_sections}
      {faq_section}
    </main>
    """
    return render_document(depth, active, title, description, path, catalog_image_rel(hero_image), schema, body)


def products_page() -> str:
    title = "Electrical Products in Prantij | Kisan Electricals"
    description = "Browse the visible Kisan Electricals catalogue by product type, brand or model and confirm live availability directly before visiting."
    breadcrumbs = [("Home", "/"), ("Products", "")]
    schema = page_schema(path="/products/", title=title, description=description, kind="collection", breadcrumbs=[("Home", "/"), ("Products", "/products/")], item_names=[p["name"] for p in PRODUCTS])
    cards = "".join(product_card(1, product) for product in PRODUCTS)
    filters = "".join(
        f'<button class="filter-chip{" is-active" if key == "all" else ""}" type="button" data-filter="{key}">{esc(label)}</button>'
        for key, label in [
            ("all", "All"),
            ("led", "LED Lighting"),
            ("fans", "Fans"),
            ("switches", "Switches"),
            ("protection", "Protection"),
            ("utility", "Utility"),
        ]
    )
    brand_options = "".join(
        f'<option value="{esc(brand)}">{esc(brand)}</option>'
        for brand in sorted({product["brand"] for product in PRODUCTS})
    )
    product_faqs = [
        ("How should I use this products page?", "Search by product type, brand or model, then call or WhatsApp to confirm current availability, price, quantity and applicable warranty."),
        ("Does the site show exact stock counts?", "No. Product cards are labelled for enquiry because models and quantities can change throughout the day."),
        ("Can I send a material list instead of individual product names?", "Yes. Builders and electricians can send a complete material list on WhatsApp for faster product matching and availability checks."),
    ]
    body = f"""
    <main id="main-content">
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div class="page-hero-body">
            {render_breadcrumbs(1, breadcrumbs)}
            <span class="page-hero-kicker">Product Catalogue</span>
            <h1>Electrical Products Available in Prantij</h1>
            <p>Search lighting, fans, modular accessories, protection items and electrical utility products by category, brand or model before contacting the shop.</p>
            <div class="page-hero-cta-row">
              <a class="btn btn-primary" href="https://wa.me/918758964040">Send Your Material List</a>
              <a class="btn btn-outline" href="../electrical-brands/">Browse Brands</a>
            </div>
          </div>
          <div class="page-hero-visual page-hero-visual--landscape">{image_tag(1, catalog_image_rel("products-hub"), "Electrical products displayed at Kisan Electricals", priority=True)}</div>
        </div>
      </section>
      <section class="container">
        <div class="answer-strip">Browse the main ranges online, then send the product name, brand and required quantity on WhatsApp for a current availability and price check.</div>
      </section>
      <section class="section-padding">
        <div class="container">
          <div class="catalog-toolbar">
            <input class="catalog-search" type="search" placeholder="Search by product, brand or model" data-catalog-search>
            <select class="catalog-search" aria-label="Filter by brand" data-brand-filter>
              <option value="">All Brands</option>
              {brand_options}
            </select>
            <div class="filter-chip-row">{filters}</div>
          </div>
          <div class="products-grid">{cards}</div>
        </div>
      </section>
      <section class="section-padding" style="background-color: var(--color-surface-soft);">
        <div class="container content-grid-3">
          <div class="catalog-note"><h3 style="margin-bottom:0.45rem;color:var(--color-brand-navy);">Availability Changes</h3><p>Models, colours and quantities can change. Use the card enquiry button to confirm the exact item before visiting.</p></div>
          <div class="catalog-note"><h3 style="margin-bottom:0.45rem;color:var(--color-brand-navy);">Warranty &amp; GST</h3><p>Warranty support depends on the brand and exact model. If you need a GST invoice, mention it at the enquiry stage so billing details can be prepared correctly.</p></div>
          <div class="catalog-note"><h3 style="margin-bottom:0.45rem;color:var(--color-brand-navy);">What to Send</h3><p>For faster replies, send brand, model, quantity, finish and holder or module requirements, plus pickup or delivery preference.</p></div>
        </div>
      </section>
      <section class="section-padding faq-section">
        <div class="container">
          <div class="section-subhead" style="text-align:center;"><h2>Product FAQs</h2></div>
          {render_faqs(product_faqs)}
        </div>
      </section>
    </main>
    """
    return render_document(1, "products", title, description, "/products/", catalog_image_rel("products-hub"), schema, body)


def wires_page() -> str:
    title = "Electrical Wires & Cables in Prantij | Kisan Electricals"
    description = "Discuss house wires, flexible cables, submersible wiring and gauge-selection needs with Kisan Electricals in Prantij."
    breadcrumbs = [("Home", "/"), ("Products", "/products/"), ("Wires & Cables", "")]
    schema = page_schema(path="/products/wires-cables/", title=title, description=description, kind="collection", breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("Wires & Cables", "/products/wires-cables/")], item_names=WIRES_GUIDE)
    guide_cards = "".join(f'<div class="mini-card"><h3>{esc(item)}</h3><p>Share the application, preferred brand, gauge and approximate quantity so the shop can suggest suitable available options.</p></div>' for item in WIRES_GUIDE)
    body = f"""
    <main id="main-content">
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div class="page-hero-body">
            {render_breadcrumbs(2, breadcrumbs)}
            <span class="page-hero-kicker">Wiring Enquiries</span>
            <h1>Electrical Wires and Cables</h1>
            <p>Discuss house wires, flexible cables, submersible cables and control-wire requirements by sharing the application, gauge and approximate quantity with the shop.</p>
            <div class="page-hero-cta-row">
              <a class="btn btn-primary" href="https://wa.me/918758964040">Send Wire Requirement</a>
              <a class="btn btn-outline" href="../">Back to Products</a>
            </div>
          </div>
          <div class="page-hero-visual page-hero-visual--graphic" aria-label="Wires and cables enquiry guide"><div class="wire-graphic" aria-hidden="true"><span></span><span></span><span></span></div><strong>Share type + gauge + quantity</strong><small>Get current brand and availability options</small></div>
        </div>
      </section>
      <section class="container">
        <div class="answer-strip">For a faster wire or cable enquiry, mention where it will be used, the required gauge, preferred safety grade, approximate length and whether it is part of a larger material list.</div>
      </section>
      <section class="section-padding">
        <div class="container">
          <div class="section-head">
            <span class="section-eyebrow">What to Ask For</span>
            <h2 class="section-title">Safe Wiring Categories</h2>
            <p class="section-desc">Use these categories when you message the shop, then include the gauge, purpose and expected load for a faster response.</p>
          </div>
          <div class="mini-card-grid">{guide_cards}</div>
        </div>
      </section>
      <section class="section-padding" style="background-color: var(--color-surface-soft);">
        <div class="container content-grid-2">
          <div class="note-card">
            <h3>Gauge and Safety Notice</h3>
            <p>The site does not provide wiring-size advice for live installations. Share the application, expected load and environment so the correct brand and gauge can be discussed responsibly.</p>
          </div>
          <div class="note-card">
            <h3>Best WhatsApp Format</h3>
            <p>Example: "Need house wire for 2-bedroom renovation, FR or FRLS preferred, approximate roll length required, plus switchboard points."</p>
          </div>
        </div>
      </section>
      <section class="section-padding">
        <div class="container content-grid-2">
          <div class="note-card">
            <h3>FR and FRLS Note</h3>
            <p>Buyers often ask about FR and FRLS wiring for home or shop work. Use your WhatsApp message to mention the application, environment and expected protection level so the discussion starts with the right safety context.</p>
          </div>
          <div class="note-card">
            <h3>Material-List Shortcut</h3>
            <p>If the requirement is part of a larger renovation or contractor list, send the full material sheet in one message instead of splitting every cable line into separate enquiries.</p>
          </div>
        </div>
      </section>
    </main>
    """
    return render_document(2, "products", title, description, "/products/wires-cables/", catalog_image_rel("products-hub"), schema, body)


def simple_page(*, depth: int, active: str, title: str, description: str, path: str, og_image: str, schema_kind: str, breadcrumbs: list[tuple[str, str]], hero_kicker: str, hero_heading: str, hero_text: str, hero_image: str, body_sections: str, faqs: list[tuple[str, str]] | None = None, service_description: str | None = None) -> str:
    schema_breadcrumbs = [(name, crumb_path if crumb_path else path) for name, crumb_path in breadcrumbs]
    schema = page_schema(path=path, title=title, description=description, kind=schema_kind, breadcrumbs=schema_breadcrumbs, faqs=faqs if schema_kind == "faq" else None, service_description=service_description)
    faq_section = ""
    if faqs:
        faq_section = f'<section class="section-padding faq-section"><div class="container"><div class="section-subhead" style="text-align:center;"><h2>FAQs</h2></div>{render_faqs(faqs)}</div></section>'
    hero_media_class = "page-hero-visual--landscape" if "/catalog/" in hero_image else "page-hero-visual--portrait"
    body = f"""
    <main id="main-content">
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div class="page-hero-body">
            {render_breadcrumbs(depth, breadcrumbs)}
            <span class="page-hero-kicker">{esc(hero_kicker)}</span>
            <h1>{esc(hero_heading)}</h1>
            <p>{esc(hero_text)}</p>
          </div>
          <div class="page-hero-visual {hero_media_class}">{image_tag(depth, hero_image, hero_heading, priority=True)}</div>
        </div>
      </section>
      {body_sections}
      {faq_section}
    </main>
    """
    return render_document(depth, active, title, description, path, og_image, schema, body)


def about_page() -> str:
    body = f"""
    <section class="container">
      <div class="answer-strip">Kisan Electricals is a long-running Prantij electrical business serving local buyers since 1976. The business story combines heritage visuals, storefront continuity and present-day guidance from the current family-led counter rather than a generic showroom narrative.</div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div>
          <div class="section-subhead"><h2>Our Story in Brief</h2></div>
          <ul class="timeline-list">
            <li>1976: the business began in Prantij and built its reputation around electrical supply, practical guidance and long-term local trust.</li>
            <li>Shastri Bazar years: the family traded through an earlier storefront phase remembered in archive-inspired reconstructions.</li>
            <li>Current phase: the shop now operates from Nirman Complex, opposite HDFC Bank, with a broader visible product mix and a dedicated contractor enquiry route.</li>
          </ul>
        </div>
        <div class="photo-card">{image_tag(1, STORY_IMAGES["store_wideshot"], "Current Kisan Electricals storefront at Nirman Complex")}</div>
      </div>
    </section>
    <section class="section-padding" style="background-color: var(--color-surface-soft);">
      <div class="container content-grid-3">
        <div class="photo-card">{image_tag(1, STORY_IMAGES["old_shop"], "Archive-inspired reconstruction of the early shop")}<div class="image-caption">Artistic reconstruction based on supplied family archive material.</div></div>
        <div class="photo-card">{image_tag(1, STORY_IMAGES["old_shop2"], "Reconstruction of the earlier exterior shop view")}<div class="image-caption">Archive-inspired heritage visual for storytelling, not a contemporary storefront photograph.</div></div>
        <div class="photo-card">{image_tag(1, STORY_IMAGES["history_documents"], "Family archive documents and old photographs linked to Kisan Electricals")}</div>
      </div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div class="photo-card">{image_tag(1, STORY_IMAGES["family_customer"], "Family customers speaking with the owner at the counter")}</div>
        <div>
          <div class="section-subhead"><h2>Three-Generation Customer Service</h2></div>
          <p style="color:var(--color-text-muted);">Customers can speak directly with the family members running the counter, compare product options and receive practical guidance based on their home, shop or project requirement.</p>
          <div class="mini-card-grid" style="margin-top:1.25rem;">
            <div class="mini-card"><h3>Direct Counter Help</h3><p>Customers can compare visible models and ask practical questions before deciding.</p></div>
            <div class="mini-card"><h3>Contractor Link</h3><p>Mr. Yogeshbhai's contractor route sits alongside the retail shop for project-oriented enquiries.</p></div>
          </div>
        </div>
      </div>
    </section>
    <section class="section-padding" style="background-color: var(--color-surface-soft);">
      <div class="container content-grid-3">
        <div class="mini-card"><h3>Our Beginnings</h3><p>The heritage story is presented carefully, using reconstructed visuals only where original storefront coverage is incomplete.</p></div>
        <div class="mini-card"><h3>Business Values</h3><p>Clear product guidance, practical comparison help and direct local accountability remain central to the business.</p></div>
        <div class="mini-card"><h3>Modern Direction</h3><p>The current Nirman Complex shop combines retail support, material-list handling and a separate contractor route for larger requirements.</p></div>
      </div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div>
          <div class="section-subhead"><h2>Mr. Yogeshbhai and the Contractor Route</h2></div>
          <p style="color:var(--color-text-muted);">Mr. Yogeshbhai is the main contact for contractor-oriented discussions, site requirements, project coordination and panel-related enquiries that go beyond ordinary product selection.</p>
          <div class="page-hero-cta-row" style="margin-top:1.25rem;">
            <a class="btn btn-primary" href="../ugvcl-electrical-contractor-prantij/">View Contractor Work</a>
            <a class="btn btn-outline" href="../contact/">Contact the Shop</a>
          </div>
        </div>
        <div class="photo-card">{image_tag(1, STORY_IMAGES["owner_discuss"], "Owner discussing a project requirement with a customer")}</div>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="about",
        title="About Kisan Electricals Prantij | Serving Since 1976",
        description="Learn how Kisan Electricals grew from its earlier Prantij trading years into the current Nirman Complex electrical showroom.",
        path="/about-kisan-electricals/",
        og_image=STORY_IMAGES["store_wideshot"],
        schema_kind="about",
        breadcrumbs=[("Home", "/"), ("Our Story", "")],
        hero_kicker="Our Story",
        hero_heading="Serving Prantij Since 1976",
        hero_text="The Kisan Electricals story is best understood through the continuity of the storefront, archive-inspired history visuals and the present-day customer guidance that still defines the business.",
        hero_image=STORY_IMAGES["store_wideshot"],
        body_sections=body,
    )


def brands_page() -> str:
    brands = {}
    for product in PRODUCTS:
        brands.setdefault(product["brand"], []).append(product)
    cards = []
    for brand in sorted(brands):
        sample = brands[brand][:3]
        categories = sorted({CATEGORY_META[p["category"]]["name"] for p in brands[brand]})
        cards.append(
            f"""
            <article class="mini-card">
              <h3>{esc(brand)}</h3>
              <p>{esc(', '.join(categories))}</p>
              <p style="margin-top:0.65rem;color:var(--color-text);font-size:0.9rem;">{esc(' | '.join(f"{item['name']} ({item['details']})" for item in sample))}</p>
              <p style="margin-top:0.85rem;"><a href="{esc(wa_link(f'Hello Kisan Electricals, please confirm current availability for {brand} products.'))}" target="_blank" rel="noopener noreferrer">Enquire about {esc(brand)}</a></p>
            </article>
            """
        )
    body = f"""
    <section class="container">
      <div class="answer-strip">Looking for a preferred electrical brand? Browse the brands currently represented in the shop’s product catalogue, then contact Kisan Electricals to confirm the exact model, colour and availability.</div>
    </section>
    <section class="section-padding">
      <div class="container">
        <div class="mini-card-grid">{''.join(cards)}</div>
      </div>
    </section>
    <section class="section-padding" style="background-color: var(--color-surface-soft);">
      <div class="container content-grid-2">
        <div class="note-card"><h3>Need another brand?</h3><p>If your preferred brand is not listed, send its name, model number or a product photo. The shop can confirm whether it is available or suggest a suitable alternative.</p></div>
        <div class="note-card"><h3>Availability note</h3><p>A listed brand does not mean every model or variant is always in stock. Confirm your exact requirement before visiting.</p></div>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="products",
        title="Electrical Brands in Prantij | Kisan Electricals",
        description="Browse visible electrical brands at Kisan Electricals and ask for live confirmation of the exact models you need.",
        path="/electrical-brands/",
        og_image=catalog_image_rel("led-main"),
        schema_kind="collection",
        breadcrumbs=[("Home", "/"), ("Electrical Brands", "")],
        hero_kicker="Brand Overview",
        hero_heading="Electrical Brands and Product Ranges",
        hero_text="Browse electrical brands across lighting, fans, switches, sockets, protection products and utility items, then confirm the exact model directly with the shop.",
        hero_image=catalog_image_rel("led-main"),
        body_sections=body,
    )


def services_page() -> str:
    body = f"""
    <section class="container">
      <div class="answer-strip">Kisan Electricals provides product-selection support, fitting-related product guidance, switchboard upgrade enquiries, protection-product discussions, bulk material help and local delivery discussion. Formal contractor work is handled separately through the dedicated contractor page.</div>
    </section>
      <section class="section-padding">
        <div class="container services-layout">
          <div class="services-image-frame">{image_tag(1, STORY_IMAGES["engineer_customer"], "Kisan Electricals team assisting an electrician with a material requirement")}</div>
          <div class="services-list">
          <div class="service-item-card"><div class="service-icon">1</div><div class="service-body"><h3>Product-selection guidance</h3><p>Discuss wattage, holder type, module size and basic product matching before you buy.</p></div></div>
          <div class="service-item-card"><div class="service-icon">2</div><div class="service-body"><h3>Lighting and fan fitting enquiries</h3><p>Use the product pages to identify visible models, then confirm whether related fitting support or referral discussion is available.</p></div></div>
          <div class="service-item-card"><div class="service-icon">3</div><div class="service-body"><h3>MCB and DB upgrade enquiries</h3><p>Identify visible protection products and raise contractor-side questions when board scope or panel work is involved.</p></div></div>
          <div class="service-item-card"><div class="service-icon">4</div><div class="service-body"><h3>Material estimation assistance</h3><p>Builders and electricians can send lists for item matching, quote discussion and invoice planning.</p></div></div>
          <div class="service-item-card"><div class="service-icon">5</div><div class="service-body"><h3>Bulk contractor supply enquiries</h3><p>Larger requirement lists can be checked against visible product ranges and then moved into a more detailed supply discussion.</p></div></div>
          <div class="service-item-card"><div class="service-icon">6</div><div class="service-body"><h3>Local delivery and site-visit requests</h3><p>Ask whether local delivery or a site visit is available for your location, order size and service requirement.</p></div></div>
        </div>
      </div>
    </section>
    <section class="section-padding process-section">
      <div class="container">
        <div class="process-steps-grid">
          <div class="process-step-card"><div class="step-number">1</div><div class="step-title">Share the requirement</div><div class="step-desc">Send the product name, photos, list or site need on WhatsApp.</div></div>
          <div class="process-step-card"><div class="step-number">2</div><div class="step-title">Confirm details</div><div class="step-desc">The shop checks visible product matches, brand options and practical next steps.</div></div>
          <div class="process-step-card"><div class="step-number">3</div><div class="step-title">Discuss price and pickup</div><div class="step-desc">Confirm quantity, billing, timing and whether the case should move to the contractor route.</div></div>
          <div class="process-step-card"><div class="step-number">4</div><div class="step-title">Complete supply or follow-up</div><div class="step-desc">Proceed with collection, sourcing follow-up or a deeper contractor discussion.</div></div>
        </div>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="services",
        title="Electrical Services & Product Guidance in Prantij",
        description="Product guidance, material-list help and showroom-side electrical support from Kisan Electricals in Prantij.",
        path="/electrical-services/",
        og_image=STORY_IMAGES["owner_discuss"],
        schema_kind="service",
        breadcrumbs=[("Home", "/"), ("Services", "")],
        hero_kicker="Electrical Services",
        hero_heading="Electrical Services and Product Guidance",
        hero_text="Get help comparing electrical products, checking material lists and discussing lighting, fan, switchboard and bulk-supply requirements with the shop team.",
        hero_image=STORY_IMAGES["owner_discuss"],
        body_sections=body,
        service_description="Showroom-side product guidance, material estimation help and electrical product support from Kisan Electricals in Prantij.",
    )


def contractor_page() -> str:
    contractor_faqs = [
        ("How do I enquire about contractor work?", "Share the site location, load details, panel requirements, drawings if available, and any timeline expectations through WhatsApp so the discussion can move from product identification to project scope."),
        ("Is Kisan Electricals a UGVCL office?", "No. Kisan Electricals is an independent electrical retailer and contractor. It is not a UGVCL office, customer-care centre or government department."),
        ("What should be confirmed before work starts?", "Confirm the exact work scope, site conditions, permissions, safety requirements, materials, schedule, commercial terms and applicable contractor documentation directly with Mr. Yogeshbhai."),
    ]
    contractor_gallery_items = [
        (STORY_IMAGES["contractor_inspection"], "Representative site-inspection visual featuring Mr. Yogeshbhai and his son"),
        (STORY_IMAGES["contractor_panel"], "Representative supervised panel-work visual featuring Mr. Yogeshbhai and his son"),
        (STORY_IMAGES["contractor_handover"], "Representative project-handover visual featuring Mr. Yogeshbhai and his son"),
        (catalog_image_rel("contractor-panel-1"), "Electrical control panel from the supplied contractor-work photographs"),
        (catalog_image_rel("contractor-panel-2"), "Outdoor distribution cabinet with visible switchgear and internal arrangement"),
        (catalog_image_rel("contractor-panel-3"), "Outdoor busbar cabinet from the supplied project photographs"),
    ]
    gallery = "".join(
        f'<div class="gallery-tile">{image_tag(1, path, alt, lightbox=True)}</div>'
        for path, alt in contractor_gallery_items
    )
    body = f"""
    <section class="container">
      <div class="answer-strip">For contractor enquiries, share the site location, type of requirement, expected load, drawings or photographs and preferred timeline. Mr. Yogeshbhai can review the information and confirm whether a site visit or further discussion is required.</div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div class="inline-disclaimer"><strong>Independence disclaimer:</strong> Kisan Electricals is an independent electrical retailer and contractor. It is not a UGVCL office, customer-care centre or government department.</div>
        <div class="inline-disclaimer"><strong>Scope confirmation:</strong> Registration details, permitted work category, exact scope and applicable documentation should be checked directly before formal engagement.</div>
      </div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div>
          <div class="section-subhead"><h2>Mr. Yogeshbhai Introduction</h2></div>
          <p style="color:var(--color-text-muted);">Mr. Yogeshbhai leads contractor-side discussions connected with site inspection, panel-related requirements, documentation review, material planning and project coordination.</p>
        </div>
        <div class="photo-card photo-card--portrait">{image_tag(1, STORY_IMAGES["contractor_inspection"], "Representative contractor site discussion with Mr. Yogeshbhai and his son")}</div>
      </div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div>
          <div class="section-subhead"><h2>Contractor Enquiry Scope</h2></div>
          <ul class="key-list">
            <li>Site inspection and documentation discussion</li>
            <li>LT-panel and distribution-cabinet related coordination</li>
            <li>Load, layout and material discussion for project requirements</li>
            <li>Safety, scope and timeline confirmation before work proceeds</li>
          </ul>
        </div>
        <div class="photo-card">{image_tag(1, catalog_image_rel("contractor-panel-2"), "Outdoor electrical cabinet from supplied contractor-work photographs")}</div>
      </div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container content-grid-3">
        <div class="mini-card"><h3>Site-inspection process</h3><p>Share the site address, use case, load details, drawings if available and any required timeline before expecting a visit or quotation discussion.</p></div>
        <div class="mini-card"><h3>Safety and documents</h3><p>Work scope, permissions, shutdown requirements, equipment condition and documentation should be clarified before any project is scheduled.</p></div>
        <div class="mini-card"><h3>Service area</h3><p>Share the exact site location so travel, scheduling and service availability can be confirmed before a visit is planned.</p></div>
      </div>
    </section>
    <section class="section-padding" style="background-color: var(--color-surface-soft);">
      <div class="container">
        <div class="section-head">
          <span class="section-eyebrow">Work Images</span>
          <h2 class="section-title">Contractor Gallery</h2>
          <p class="section-desc">A visual overview combining supplied panel photographs with representative family-based contractor scenes. Click any image to view it larger.</p>
        </div>
        <div class="gallery-grid">{gallery}</div>
      </div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div class="note-card"><h3>Before project start</h3><p>Confirm contractor details, work scope, site conditions, permissions, safety requirements, material responsibility, schedule and commercial terms directly with Mr. Yogeshbhai.</p></div>
        <div class="note-card"><h3>How to message</h3><p>Send the site location, expected load, type of connection or panel, drawings if available, and whether the requirement is residential, commercial or agricultural.</p></div>
      </div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container"><div class="inline-disclaimer"><strong>Image note:</strong> The people-based contractor scenes are representative visuals created from supplied family references. Panel and cabinet photographs are shown separately as project-related images.</div></div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container" style="text-align:center;">
        <a class="btn btn-primary" href="https://wa.me/918758964040">Start Contractor Enquiry on WhatsApp</a>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="contractor",
        title="UGVCL Electrical Contractor in Prantij | Kisan Electricals",
        description="Separate contractor enquiry page for electrical panel, site inspection and project coordination discussions connected with Kisan Electricals in Prantij.",
        path="/ugvcl-electrical-contractor-prantij/",
        og_image=STORY_IMAGES["contractor_inspection"],
        schema_kind="service",
        breadcrumbs=[("Home", "/"), ("Contractor Work", "")],
        hero_kicker="Contractor Enquiries",
        hero_heading="UGVCL Contractor Enquiries in Prantij",
        hero_text="Discuss site inspection, panel-related requirements, documentation, material planning and project coordination directly with Mr. Yogeshbhai.",
        hero_image=STORY_IMAGES["contractor_inspection"],
        body_sections=body,
        faqs=contractor_faqs,
        service_description="Independent contractor enquiries related to inspection, panels and project coordination associated with Kisan Electricals in Prantij.",
    )


def gallery_page() -> str:
    gallery_items = [
        (STORY_IMAGES["store_wideshot"], "Full storefront view of Kisan Electricals at Nirman Complex"),
        (STORY_IMAGES["store_closeup"], "Close storefront view of Kisan Electricals entrance"),
        (catalog_image_rel("products-hub"), "Interior product shelf photo from the showroom"),
        (STORY_IMAGES["owner_discuss"], "Owner discussing products with a customer"),
        (STORY_IMAGES["three_gen"], "Three generations assisting customers at the counter"),
        (STORY_IMAGES["family_customer"], "Family customers receiving guidance in the shop"),
        (STORY_IMAGES["engineer_customer"], "Electrician or technical customer in discussion at the counter"),
        (catalog_image_rel("led-main"), "LED product shelf showing visible lighting boxes"),
        (STORY_IMAGES["old_shop2"], "Archive-inspired early exterior reconstruction"),
        (STORY_IMAGES["old_shop"], "Archive-inspired historical shop reconstruction"),
        (STORY_IMAGES["contractor_inspection"], "Representative contractor inspection scene with Mr. Yogeshbhai and his son"),
        (STORY_IMAGES["contractor_panel"], "Representative supervised panel-work scene"),
        (STORY_IMAGES["contractor_handover"], "Representative contractor project-handover scene"),
        (catalog_image_rel("contractor-panel-1"), "Contractor panel cabinet photo"),
        (catalog_image_rel("contractor-panel-2"), "Outdoor distribution panel photo"),
        (catalog_image_rel("contractor-panel-3"), "Open cabinet photograph from project work"),
    ]
    grid = "".join(f'<div class="gallery-tile">{image_tag(1, path, alt, lightbox=True)}</div>' for path, alt in gallery_items)
    body = f"""
    <section class="container">
      <div class="answer-strip">Explore the current storefront, customer interactions, family-business story, product displays and contractor-related work connected with Kisan Electricals.</div>
    </section>
    <section class="section-padding">
      <div class="container">
        <div class="gallery-grid">{grid}</div>
      </div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container">
        <div class="inline-disclaimer">Some heritage and people-based contractor visuals are artistic reconstructions created from supplied family references. Panel and cabinet photographs are displayed separately as project-related images.</div>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="gallery",
        title="Kisan Electricals Gallery | Shop & Contractor Work",
        description="View storefront, customer-service, heritage and contractor images connected with Kisan Electricals in Prantij.",
        path="/gallery/",
        og_image=STORY_IMAGES["store_closeup"],
        schema_kind="gallery",
        breadcrumbs=[("Home", "/"), ("Gallery", "")],
        hero_kicker="Image Gallery",
        hero_heading="Kisan Electricals Gallery",
        hero_text="View the storefront, product displays, family customer service, heritage story and contractor-related visuals in one simple gallery.",
        hero_image=STORY_IMAGES["store_wideshot"],
        body_sections=body,
    )


def contact_page() -> str:
    body = f"""
    <section class="container">
      <div class="answer-strip">Kisan Electricals is at Shop No. 12, Nirman Complex, Approach Road, opposite HDFC Bank, Prantij. Call or WhatsApp before visiting when you need a specific product, brand or contractor discussion.</div>
    </section>
    <section class="section-padding">
      <div class="container content-grid-2">
        <div class="contact-card">
          <div class="contact-item"><div class="contact-item-icon">SHOP</div><div class="contact-item-content"><h4>Business name</h4><p>{esc(BUSINESS_NAME)}<br><span lang="gu">{esc(BUSINESS_NAME_GU)}</span></p></div></div>
          <div class="contact-item"><div class="contact-item-icon">MAP</div><div class="contact-item-content"><h4>Address</h4><address>Shop No. 12, Nirman Complex<br>Approach Road<br>Opposite HDFC Bank<br>Prantij, Gujarat 383205</address></div></div>
          <div class="contact-item"><div class="contact-item-icon">CALL</div><div class="contact-item-content"><h4>Phones</h4><p>{esc(PRIMARY_PHONE)}<br>{esc(SECONDARY_PHONE)}</p></div></div>
          <div class="contact-item"><div class="contact-item-icon">HRS</div><div class="contact-item-content"><h4>Hours</h4><p>{esc(HOURS_TEXT)}</p></div></div>
          <div class="contact-item"><div class="contact-item-icon">LINK</div><div class="contact-item-content"><h4>Links</h4><p><a href="{esc(GOOGLE_PROFILE)}" target="_blank" rel="noopener noreferrer">Directions</a> | <a href="{esc(FACEBOOK)}" target="_blank" rel="noopener noreferrer">Facebook</a> | <a href="{esc(INSTAGRAM)}" target="_blank" rel="noopener noreferrer">Instagram</a></p></div></div>
        </div>
        <div class="contact-form-shell">
          <h2 style="color:var(--color-brand-navy);margin-bottom:0.85rem;">Send a WhatsApp Enquiry</h2>
          <form class="contact-form" data-wa-form="true" data-form-title="New Kisan Electricals enquiry">
            <div><label for="name">Name</label><input id="name" name="Name" required></div>
            <div><label for="phone">Phone or WhatsApp</label><input id="phone" name="Phone or WhatsApp" required></div>
            <div><label for="category">Product or service category</label><select id="category" name="Category"><option>LED Lighting</option><option>Ceiling Fans</option><option>Switches & Sockets</option><option>Wires & Cables</option><option>MCB, RCCB & Protection</option><option>Pumps, Tools & Utility</option><option>Contractor Enquiry</option></select></div>
            <div><label for="requirement">Requirement</label><textarea id="requirement" name="Requirement" rows="4" required></textarea></div>
            <div><label for="contact_method">Preferred contact method</label><select id="contact_method" name="Preferred contact method"><option>Phone call</option><option>WhatsApp reply</option><option>Either is fine</option></select></div>
            <div class="checkbox-row"><input id="consent" type="checkbox" name="consent" required><label for="consent">I understand that the information above is used only to respond to my enquiry and may be shared through WhatsApp if I choose that route.</label></div>
            <button class="btn btn-primary" type="submit">Open WhatsApp Message</button>
          </form>
        </div>
      </div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container content-grid-2">
        <div class="photo-card">{image_tag(1, STORY_IMAGES["store_closeup"], "Close storefront image of Kisan Electricals")}</div>
        <div class="photo-card">{image_tag(1, STORY_IMAGES["store_wideshot"], "Wider storefront context for directions to Kisan Electricals")}</div>
      </div>
    </section>
    <section class="section-padding" style="padding-top:0;">
      <div class="container">
        <iframe class="map-embed" src="{esc(MAP_EMBED)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </section>
    """
    return simple_page(
        depth=1,
        active="contact",
        title="Contact Kisan Electricals Prantij | Call, WhatsApp & Map",
        description="Find the Kisan Electricals address, phone numbers, opening hours, map and WhatsApp enquiry form for the Prantij shop.",
        path="/contact/",
        og_image=STORY_IMAGES["store_closeup"],
        schema_kind="contact",
        breadcrumbs=[("Home", "/"), ("Contact", "")],
        hero_kicker="Contact Page",
        hero_heading="Contact Kisan Electricals",
        hero_text="Find the shop address, opening hours, phone numbers, directions, social profiles and a quick WhatsApp enquiry form.",
        hero_image=STORY_IMAGES["store_wideshot"],
        body_sections=body,
    )


def faq_page() -> str:
    body = f"""
    <section class="container">
      <div class="answer-strip">Find quick answers about products, availability checks, material lists, GST invoice requests, the Prantij shop location and contractor enquiries.</div>
    </section>
    """
    return simple_page(
        depth=1,
        active="contact",
        title="Kisan Electricals Prantij FAQs | Products & Services",
        description="Read the key questions and answers about Kisan Electricals products, location, stock confirmation and contractor enquiries.",
        path="/faqs/",
        og_image=STORY_IMAGES["three_gen"],
        schema_kind="faq",
        breadcrumbs=[("Home", "/"), ("FAQs", "")],
        hero_kicker="FAQs",
        hero_heading="Frequently Asked Questions",
        hero_text="Answers to common questions about products, current availability, GST billing, location, material lists and contractor enquiries.",
        hero_image=STORY_IMAGES["three_gen"],
        body_sections=body,
        faqs=FAQ_PAGE,
    )


def legal_page(title: str, description: str, path: str, heading: str, body_blocks: list[tuple[str, str]]) -> str:
    cards = "".join(f'<div class="legal-card"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in body_blocks)
    body = f"""
    <section class="container">
      <div class="answer-strip">{esc(body_blocks[0][1])}</div>
    </section>
    <section class="section-padding">
      <div class="container legal-shell">{cards}</div>
    </section>
    """
    return simple_page(
        depth=1,
        active="contact",
        title=title,
        description=description,
        path=path,
        og_image=STORY_IMAGES["store_closeup"],
        schema_kind="about",
        breadcrumbs=[("Home", "/"), (heading, "")],
        hero_kicker="Policy",
        hero_heading=heading,
        hero_text=description,
        hero_image=STORY_IMAGES["store_closeup"],
        body_sections=body,
    )


def four_oh_four() -> str:
    title = "Page Not Found | Kisan Electricals Prantij"
    description = "The page you requested is not available. Return to the Kisan Electricals catalogue or contact page."
    schema = page_schema(path="/404.html", title=title, description=description, kind="about")
    body = f"""
    <main id="main-content">
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div class="page-hero-body">
            <span class="page-hero-kicker">404</span>
            <h1>Page Not Found</h1>
            <p>The page you requested is not available. Use the links below to return to the main product catalogue, contact page or storefront directions.</p>
            <div class="page-hero-cta-row">
              <a class="btn btn-primary" href="./">Go to Home</a>
              <a class="btn btn-outline" href="./products/">Open Products</a>
              <a class="btn btn-secondary" href="https://wa.me/918758964040">WhatsApp the Shop</a>
            </div>
          </div>
          <div class="page-hero-visual">{image_tag(0, STORY_IMAGES["store_closeup"], "Kisan Electricals storefront closeup")}</div>
        </div>
      </section>
    </main>
    """
    return render_document(0, "home", title, description, "/404.html", STORY_IMAGES["store_closeup"], schema, body)


def write_pages() -> None:
    (ROOT / "index.html").write_text(home_page(), encoding="utf-8")
    (ROOT / "products" / "index.html").write_text(products_page(), encoding="utf-8")
    (ROOT / "products" / "led-lights" / "index.html").write_text(
        build_collection_page(
            title="LED Lights in Prantij | Bulbs, Emergency Lights & More",
            description="Explore visible LED bulbs, emergency bulbs, decorative lamps, sensor lights and downlight-related products at Kisan Electricals in Prantij.",
            path="/products/led-lights/",
            active="products",
            depth=2,
            hero_kicker="LED Lighting",
            hero_heading="LED Lights in Prantij",
            hero_text="Explore standard LED bulbs, emergency or inverter bulbs, decorative lamps, downlights, sensor bulbs and practical work-light products available for enquiry.",
            hero_image="led-main",
            hero_alt="Visible LED bulb and emergency bulb packaging from Kisan Electricals",
            breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("LED Lighting", "")],
            intro_answer="Kisan Electricals in Prantij offers standard bulbs, high-wattage bulbs, emergency bulbs, decorative lamps, sensor bulbs and work-light products subject to current availability.",
            groups=group_products("led"),
            extra_sections='<section class="section-padding" style="background-color: var(--color-surface-soft);"><div class="container content-grid-3"><div class="note-card"><h3>Buying guide: holder type</h3><p>Many products use B22 holders. If you need another holder or base format, mention it before pickup.</p></div><div class="note-card"><h3>Buying guide: brightness</h3><p>Options include 9W, 10W, 12W, 15W, 16W, 20W and 40W products, so the right choice depends on room size and use.</p></div><div class="note-card"><h3>Buying guide: colour temperature</h3><p>Cool daylight 6500K is available on multiple emergency and standard bulbs. Confirm the exact colour temperature before purchase.</p></div></div></section>',
            faqs=CATEGORY_FAQS["led"],
        ),
        encoding="utf-8",
    )
    (ROOT / "products" / "ceiling-fans" / "index.html").write_text(
        build_collection_page(
            title="Ceiling Fans in Prantij | BLDC & Decorative Fans",
            description="See visible ceiling fan, BLDC fan, decorative fan and blower-related products documented for Kisan Electricals in Prantij.",
            path="/products/ceiling-fans/",
            active="products",
            depth=2,
            hero_kicker="Fans & Air Movement",
            hero_heading="Ceiling Fans in Prantij",
            hero_text="Explore decorative ceiling fans, high-speed models, BLDC options with remote features, portable fans and blower products.",
            hero_image="ceiling-fans",
            hero_alt="Visible boxed ceiling fan models in the Kisan Electricals store",
            breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("Ceiling Fans", "")],
            intro_answer="Kisan Electricals in Prantij currently shows decorative, high-speed and BLDC fan models in 1200mm boxed formats, plus related blower and utility air-movement products. Confirm finish, remote features and live stock before pickup.",
            groups=group_products("fans"),
            extra_sections='<section class="section-padding" style="background-color: var(--color-surface-soft);"><div class="container content-grid-3"><div class="note-card"><h3>Sizing guide</h3><p>The visible boxed fan range centres on 1200mm models. If you need a different sweep size, confirm first.</p></div><div class="note-card"><h3>Finish choices</h3><p>White, copper, black and grey finish references are visible on the current packaging set.</p></div><div class="note-card"><h3>BLDC features</h3><p>Remote control, speed indicators and reverse rotation should be confirmed on the exact model box before purchase.</p></div></div></section>',
            faqs=CATEGORY_FAQS["fans"],
        ),
        encoding="utf-8",
    )
    (ROOT / "products" / "switches-sockets" / "index.html").write_text(
        build_collection_page(
            title="Switches & Sockets in Prantij | Kisan Electricals",
            description="Browse visible modular switches, sockets, regulators, plates and related board accessories at Kisan Electricals in Prantij.",
            path="/products/switches-sockets/",
            active="products",
            depth=2,
            hero_kicker="Modular Accessories",
            hero_heading="Modular Switches and Sockets",
            hero_text="Browse one-way and two-way switches, bell-push switches, sockets, regulators, bottom plates, wood plates and modular protection accessories from multiple brands.",
            hero_image="switches-sockets",
            hero_alt="Visible modular switch and socket product boxes",
            breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("Switches & Sockets", "")],
            intro_answer="Kisan Electricals in Prantij currently shows modular switches, sockets, regulators and plates from Elley's Electric, Hi-Fi Electric and Kosch. Visible model codes are helpful, but finish and stock should still be confirmed before visiting.",
            groups=group_products("switches"),
            extra_sections='<section class="section-padding" style="background-color: var(--color-surface-soft);"><div class="container content-grid-3"><div class="note-card"><h3>Module-size guide</h3><p>Products include 1-module and 2-module formats, while plates span multiple module widths. Mention the board size you are matching.</p></div><div class="note-card"><h3>Finish note</h3><p>Options can include Jet Black, white, metallic and textured finishes. Confirm the exact finish before purchase.</p></div><div class="note-card"><h3>Code-first enquiries</h3><p>If you already know a code such as 902101 or 700024JB, include it in your WhatsApp enquiry for a faster check.</p></div></div></section>',
            faqs=CATEGORY_FAQS["switches"],
        ),
        encoding="utf-8",
    )
    (ROOT / "products" / "wires-cables" / "index.html").write_text(wires_page(), encoding="utf-8")
    (ROOT / "products" / "mcb-electrical-protection" / "index.html").write_text(
        build_collection_page(
            title="MCB, RCCB & Electrical Protection in Prantij",
            description="See visible protection, control and meter-related products connected with Kisan Electricals in Prantij.",
            path="/products/mcb-electrical-protection/",
            active="products",
            depth=2,
            hero_kicker="Protection Products",
            hero_heading="Electrical Protection Products",
            hero_text="Browse meters, auto switches, modular protection items, timers and relay-related products, then confirm the correct rating and application before purchase.",
            hero_image="utility-protection",
            hero_alt="Visible protection and utility products in the Kisan Electricals store",
            breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("Protection", "")],
            intro_answer="Kisan Electricals in Prantij currently shows digital meters, auto switches, modular protection items, timers and relay-related products. Because these products can sit close to contractor or panel work, the website keeps the public guidance descriptive rather than instructional.",
            groups=group_products("protection"),
            extra_sections='<section class="section-padding" style="background-color: var(--color-surface-soft);"><div class="container content-grid-2"><div class="note-card"><h3>Safety explanation</h3><p>Protection products must match the circuit and installation requirement. Do not attempt live distribution-board work without a qualified person.</p></div><div class="note-card"><h3>Need panel help?</h3><p>If the requirement involves site scope, board modifications or LT-panel related work, continue with the separate contractor enquiry page.</p></div></div></section>',
            faqs=CATEGORY_FAQS["protection"],
        ),
        encoding="utf-8",
    )
    (ROOT / "products" / "pumps-tools-utility" / "index.html").write_text(
        build_collection_page(
            title="Pumps, Tools & Utility Electricals in Prantij",
            description="Explore visible cooler pumps, reflectors, rechargeable torches, work lights and utility accessories at Kisan Electricals.",
            path="/products/pumps-tools-utility/",
            active="products",
            depth=2,
            hero_kicker="Utility Products",
            hero_heading="Pumps, Tools and Utility Products",
            hero_text="Browse cooler pumps, rechargeable lights, reflectors, batteries, agricultural lighting and heavy-duty electrical accessories.",
            hero_image="utility-protection",
            hero_alt="Visible pumps, work lights and utility accessories in the store",
            breadcrumbs=[("Home", "/"), ("Products", "/products/"), ("Pumps & Utility", "")],
            intro_answer="Kisan Electricals in Prantij supplies cooler pumps, work lights, rechargeable lights, batteries, reflectors and other electrical utility products subject to current availability.",
            groups=group_products("utility"),
            extra_sections='',
            faqs=CATEGORY_FAQS["utility"],
        ),
        encoding="utf-8",
    )
    (ROOT / "electrical-brands" / "index.html").write_text(brands_page(), encoding="utf-8")
    (ROOT / "electrical-services" / "index.html").write_text(services_page(), encoding="utf-8")
    (ROOT / "ugvcl-electrical-contractor-prantij" / "index.html").write_text(contractor_page(), encoding="utf-8")
    (ROOT / "about-kisan-electricals" / "index.html").write_text(about_page(), encoding="utf-8")
    (ROOT / "gallery" / "index.html").write_text(gallery_page(), encoding="utf-8")
    (ROOT / "contact" / "index.html").write_text(contact_page(), encoding="utf-8")
    (ROOT / "faqs" / "index.html").write_text(faq_page(), encoding="utf-8")
    (ROOT / "privacy-policy" / "index.html").write_text(
        legal_page(
            title="Privacy Policy | Kisan Electricals Prantij",
            description="Read how Kisan Electricals uses enquiry information shared through the website and WhatsApp-led contact flow.",
            path="/privacy-policy/",
            heading="Privacy Policy",
            body_blocks=[
                ("Privacy overview", "Kisan Electricals uses the website and WhatsApp-led enquiry flow to receive basic contact and product requirement information. The site is designed to help the shop respond to enquiries rather than run a user-account system."),
                ("What information is collected", "The contact form asks only for name, phone or WhatsApp number, category, requirement, preferred contact method and consent. That information is used to help the business respond to the enquiry."),
                ("What is not collected", "The site does not ask for account passwords, card details, payment credentials or profile logins."),
                ("How information is used", "Information is used for callback, WhatsApp response, product follow-up and contractor-route clarification when needed."),
            ],
        ),
        encoding="utf-8",
    )
    (ROOT / "terms-and-disclaimer" / "index.html").write_text(
        legal_page(
            title="Terms & Disclaimers | Kisan Electricals Prantij",
            description="Review the main catalogue, availability, contractor and independence disclaimers for the Kisan Electricals website.",
            path="/terms-and-disclaimer/",
            heading="Terms & Disclaimers",
            body_blocks=[
                ("Terms overview", "This website is a catalogue and enquiry aid for Kisan Electricals in Prantij. It is not a live stock-management system, an e-commerce checkout, or a public proof of every service claim."),
                ("Catalogue disclaimer", "Product models, colours, prices, warranty support and quantities can change. Confirm the exact item directly before purchase."),
                ("Pricing disclaimer", "Prices are not treated as fixed online offers unless confirmed directly by the shop. Packaging and market changes can affect the final figure."),
                ("Contractor disclaimer", "Kisan Electricals is an independent electrical retailer and contractor. It is not a UGVCL office, customer-care centre or government department."),
            ],
        ),
        encoding="utf-8",
    )
    (ROOT / "warranty-and-returns" / "index.html").write_text(
        legal_page(
            title="Warranty & Returns | Kisan Electricals Prantij",
            description="Read the practical warranty and returns position for products identified through the Kisan Electricals website.",
            path="/warranty-and-returns/",
            heading="Warranty & Returns",
            body_blocks=[
                ("Warranty overview", "Warranty support depends on the brand, model and invoice terms for the item purchased. Confirm the applicable warranty before completing the purchase."),
                ("Manufacturer-backed items", "Fans, LED products, modular accessories and other branded items follow the manufacturer or supplier-backed warranty route shown on the actual box or invoice."),
                ("What to keep", "Keep the invoice, box and any warranty markings when they are provided. Those are usually needed if a claim or replacement discussion happens later."),
                ("Return and exchange discussion", "Return and exchange acceptance depends on the product condition, packaging and the specific brand’s support process. Confirm the shop’s position at the time of purchase if the item is project-critical."),
            ],
        ),
        encoding="utf-8",
    )
    (ROOT / "404.html").write_text(four_oh_four(), encoding="utf-8")


def main() -> None:
    optimize_catalog_images()
    build_icons()
    write_pages()


if __name__ == "__main__":
    main()

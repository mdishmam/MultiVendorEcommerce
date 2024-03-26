import random

from django.test import TestCase
from ecommerce.models import Product


# Create your tests here.

product_names = [
    "Smartphone",
    "Laptop",
    "Headphones",
    "Smartwatch",
    "Tablet",
    "Camera",
    "Bluetooth Speaker",
    "Wireless Earbuds",
    "Gaming Console",
    "Fitness Tracker",
    "External Hard Drive",
    "Portable Charger",
    "Printer",
    "Desk Lamp",
    "Electric Toothbrush",
    "Coffee Maker",
    "Blender",
    "Air Fryer",
    "Robot Vacuum Cleaner",
    "Electric Kettle",
    "Microwave Oven",
    "Toaster",
    "Food Processor",
    "Slow Cooker",
    "Instant Pot",
    "Rice Cooker",
    "Water Filter",
    "Juicer",
    "Soda Maker",
    "Bread Maker",
    "Ice Cream Maker",
    "Waffle Maker",
    "Steam Iron",
    "Hair Dryer",
    "Straightening Iron",
    "Curling Iron",
    "Electric Shaver",
    "Facial Cleansing Brush",
    "Massage Gun",
    "Yoga Mat",
    "Dumbbells",
    "Resistance Bands",
    "Jump Rope",
    "Treadmill",
    "Exercise Bike",
    "Elliptical Machine",
    "Weight Bench",
    "Rowing Machine",
    "Punching Bag",
    "Boxing Gloves",
    "Basketball Hoop",
    "Soccer Ball",
    "Football",
    "Volleyball",
    "Tennis Racket",
    "Golf Clubs",
    "Badminton Racket",
    "Skateboard",
    "Scooter",
    "Bicycle",
    "Hoverboard",
    "Roller Skates",
    "Snowboard",
    "Ski Set",
    "Surfboard",
    "Kiteboard",
    "Wetsuit",
    "Snorkel Gear",
    "Tent",
    "Sleeping Bag",
    "Camp Stove",
    "Cooler",
    "Hiking Boots",
    "Backpack",
    "GPS Device",
    "Binoculars",
    "Flashlight",
    "Multi-tool",
    "Pocket Knife",
    "Water Bottle",
    "Solar Charger",
    "Portable Shower",
    "First Aid Kit",
    "Camping Chair",
    "Hammock",
    "Picnic Basket",
    "Fishing Rod",
    "Kayak",
    "Canoe",
    "Life Jacket",
    "Waterproof Bag",
    "Diving Mask",
    "Snorkel",
    "Wetsuit",
    "Scuba Tank",
    "Regulator",
    "BCD Jacket",
    "Fins",
    "Dive Computer",
    "Underwater Camera"
]
opening_phrases = ["Introducing our new product:", "Discover the latest addition to our collection:",
                   "Get ready for something amazing:", "Experience innovation with our newest product:"]
features = ["high-quality materials", "advanced technology", "sleek design", "user-friendly interface",
            "powerful performance", "long-lasting battery life", "premium craftsmanship", "intuitive controls",
            "innovative features"]
benefits = ["enhance your productivity", "immerse yourself in entertainment", "stay connected on the go",
            "achieve your fitness goals", "make everyday tasks easier", "boost your gaming experience",
            "capture memories in stunning detail", "create culinary masterpieces with ease"]


# Generate a random description
def generate_description():
    opening = random.choice(opening_phrases)
    feature = random.choice(features)
    benefit = random.choice(benefits)

    description = f"{opening} This product features {feature}, allowing you to {benefit}."
    return description


for i in product_names:
    price = random.randint(100,10000)
    Product.objects.create(
        name=i,
        description=generate_description(),
        price=price,
        buy_price=price-random.randint(10,50),
        unit_id=1,
        quantity_at_present=random.randint(10,100),
        minimum_quantity=5,
        user__username="BotSeller"
    )
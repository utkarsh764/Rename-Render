# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26926782")

API_HASH = os.environ.get("API_HASH", "9b2fac908fb7f9a3dabac3b0a57211b1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8184665595:AAHasatOstcUgATCWbneK-j95ojTpmr53vo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Movie_Centre1") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Utkarsh9")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Utkarsh123:<db_password>@utkarsh9.af91n.mongodb.net/?retryWrites=true&w=majority&appName=Utkarsh9")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1214167849').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

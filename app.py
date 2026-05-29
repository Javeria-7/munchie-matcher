import streamlit as st
import random

# ==========================================
# 🎨 GEN-Z AESTHETIC INTERFACE ENGINE (CSS)
# ==========================================
st.set_page_config(
    page_title="Munchie Matcher v10.0", 
    page_icon="✨", 
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Space+Grotesk:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #06050c !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #f1f5f9 !important;
    }
    
    .brand-title {
        background: linear-gradient(90deg, #00f5ff, #b100ff, #ff007a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 38px;
        font-weight: 800 !important;
        letter-spacing: -1px;
        margin-top: 15px;
        margin-bottom: 0px !important;
    }
    .brand-sub {
        color: #94a3b8;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 35px;
    }
    
    h3 {
        color: #00f5ff !important;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 21px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    div[data-testid="stBlock"] {
        background: #0d0b18;
        border: 1px solid #1f1b35;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .munch-card {
        background: linear-gradient(135deg, #130f26, #090714);
        padding: 28px;
        border-radius: 20px;
        border-left: 6px solid #b100ff;
        border-right: 1px solid #1f1b35;
        border-top: 1px solid #1f1b35;
        border-bottom: 1px solid #1f1b35;
        margin-bottom: 25px;
        box-shadow: 0 12px 35px rgba(177, 0, 255, 0.15);
    }
    
    .card-label {
        color: #ff007a; 
        font-size: 11px; 
        font-weight: 800; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        display: block; 
        margin-bottom: 6px;
    }
    
    .stat-bubble {
        background: #090714;
        border: 1px solid #252042;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #b100ff 0%, #ff007a 100%) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        border: none !important;
        padding: 16px 32px !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 6px 25px rgba(255, 0, 122, 0.3) !important;
        transition: all 0.25s ease-in-out !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 35px rgba(255, 0, 122, 0.5) !important;
    }
    
    .reroll-btn>div>button {
        background: transparent !important;
        color: #00f5ff !important;
        border: 2px solid #00f5ff !important;
        box-shadow: none !important;
        margin-top: -10px;
    }
    .reroll-btn>div>button:hover {
        background: rgba(0, 245, 255, 0.1) !important;
        color: #00f5ff !important;
    }
    
    label { color: #94a3b8 !important; font-weight: 600 !important; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='brand-title'>✨ Munchie Matcher</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-sub'>Vibe-checking your exact custom preferences to map the ideal local fuel loop.</div>", unsafe_allow_html=True)

if "reroll_noise" not in st.session_state:
    st.session_state.reroll_noise = 1.0

# ==========================================
# RUNTIME PARAMETERS BLOCK INTERFACE
# ==========================================
st.markdown("### ✨ Tell Us Your Profile & Vibe")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Your Gender Identity:", ["Boy", "Girl", "Prefer Not to Say"])
    mood = st.selectbox("How's the mood today?", ["Bored", "Stress", "Happy", "Sad", "Confused", "Angry", "Relaxed", "Tired", "Excited"])
    budget = st.slider("Wallet Status (1: Uni Broke, 5: Premium Flex):", min_value=1, max_value=5, value=3)
    time_avail = st.selectbox("Got ample time?", ["Moderate (quick meal)", "Very little (grab-and-go)", "High (Ample Time / Chill & Eat)"])
    cravings = st.selectbox("What are you lowkey craving?", ["No specific craving", "Healthy Food", "Sweet / Chocolate", "Savory / Spicy / Desi", "Fast Food / Fried"])

with col2:
    appetite = st.selectbox("Hunger Scale:", [
        "Moderately hungry",
        "Slightly hungry (snack)", 
        "Just need to chew something (Focus fixation)",
        "Very hungry (full meal)", 
        "Not feeling hungry"
    ])
    order_preference = st.selectbox("What are we getting today?", ["Full Combo (Food + Drink) ✨", "Only Food 🍔", "Only Drink/Dessert 🥤"])
    sugar_preference = st.selectbox("Do you want Sugar-Free Drinks?", ["No, give me the regular sweet vibe! 🥤", "Yes, keep it Sugar-Free / Zero Sugar! 🧊"])
    location = st.selectbox("Where you at right now?", ["University campus", "Home", "Hostel", "Job", "Outside"])
    company = st.selectbox("Who's the squad?", ["Alone", "With friends", "Family", "Girls Group", "Mixed Group"])

# Fitness Toggles Configuration
st.markdown("### 🏋️ Fitness Protocol Settings")
col_g1, col_g2 = st.columns(2)
with col_g1:
    fitness_mode = st.checkbox("Enable Gym Freak Mode (Prioritize High Protein / Clean)")
with col_g2:
    allow_cheat = st.checkbox("Allow Flex/Cheat Option? (Unlock Grilled Sandwiches/BBQ options on fitness settings)")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 📋 RE-STRUCTURED DATA MATRICES
# ==========================================
FOOD_DATABASE = [
    # Oral Fixations
    {"name": "Trident Spearmint Sugar-Free Gum", "type": "chewing_mode", "clean": True, "cost": 1, "is_gym_approved": True, "speed": "instant", "demographic_veto": False, "tags": ["chew", "mint"], "is_cheat_allowed": True, "sugar": "zero"},
    {"name": "Classic Mint Bubblegum Roll", "type": "chewing_mode", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["chew", "sweet"], "is_cheat_allowed": True, "sugar": "real"},

    # Clean & Protein Isolation Vectors
    {"name": "Subway Roasted Chicken Breast Sub", "type": "full_meal", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "fast", "demographic_veto": False, "tags": ["subway", "sandwich", "clean"], "is_cheat_allowed": True},
    {"name": "Thick Double-Scoop Whey Protein Shake", "type": "snack", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "instant", "demographic_veto": False, "tags": ["protein", "shake", "clean"], "is_cheat_allowed": True},
    {"name": "Flame-Grilled Chicken Breast with Tossed Greens", "type": "full_meal", "clean": True, "cost": 4, "is_gym_approved": True, "speed": "wait", "demographic_veto": False, "tags": ["grilled", "chicken", "high-protein"], "is_cheat_allowed": True},
    {"name": "Flame-Grilled Juiced Chicken Pieces Pack", "type": "full_meal", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "wait", "demographic_veto": False, "tags": ["chicken", "grilled"], "is_cheat_allowed": True},
    {"name": "Fresh Salad Bowls with Olive Oil Drizzle", "type": "snack", "clean": True, "cost": 2, "is_gym_approved": True, "speed": "fast", "demographic_veto": False, "tags": ["salad", "clean"], "is_cheat_allowed": True},
    {"name": "Roasted Crispy Chickpeas Spicy Bowl", "type": "snack", "clean": True, "cost": 1, "is_gym_approved": True, "speed": "instant", "demographic_veto": False, "tags": ["chana", "spicy"], "is_cheat_allowed": True},
    {"name": "Premium Whey Protein Bar", "type": "snack", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "instant", "demographic_veto": False, "tags": ["protein", "bar", "sweet"], "is_cheat_allowed": True},

    # Flex Custom Profiles (Grilled Sandos, Wraps, BBQ)
    {"name": "Toasted Charcoal Grilled Chicken Sandwich", "type": "snack", "clean": True, "cost": 2, "is_gym_approved": True, "speed": "wait", "demographic_veto": False, "tags": ["sandwich", "grilled", "chicken"], "is_cheat_allowed": True},
    {"name": "Tender Roasterie Chicken Quarter Platter", "type": "full_meal", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "wait", "demographic_veto": False, "tags": ["roasterie", "chicken"], "is_cheat_allowed": True},
    {"name": "Charcoal Bar B Q Tikka & Seekh Kabab Tray", "type": "full_meal", "clean": True, "cost": 3, "is_gym_approved": True, "speed": "wait", "demographic_veto": False, "tags": ["bbq", "desi", "tikka"], "is_cheat_allowed": True},
    {"name": "Grilled Chicken Breast Wrap", "type": "snack", "clean": True, "cost": 2, "is_gym_approved": True, "speed": "fast", "demographic_veto": False, "tags": ["wrap", "chicken", "protein"], "is_cheat_allowed": True},
    {"name": "Shami Kabab Lean Platter", "type": "snack", "clean": True, "cost": 1, "is_gym_approved": True, "speed": "fast", "demographic_veto": False, "tags": ["kabab", "desi"], "is_cheat_allowed": True},

    # Standard Junk, Desi & Comfort Arrays
    {"name": "Premium Chicken Sando With Secret Sauce", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["sandwich", "sando", "fried"], "is_cheat_allowed": True},
    {"name": "Crispy Zinger Burger combo", "type": "full_meal", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["burger", "fried", "zinger"], "is_cheat_allowed": True},
    {"name": "Twister Wrap Basket", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["wrap", "fried"], "is_cheat_allowed": True},
    {"name": "Crunchy Tortilla Wrap Combo", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["wrap", "crunchy"], "is_cheat_allowed": True},
    {"name": "Loaded Fries Tub with Liquid Cheese", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["fries", "cheese"], "is_cheat_allowed": False},
    {"name": "Toasted Shredded Chicken Club Sandwich Tray", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["sandwich", "club"], "is_cheat_allowed": True},
    {"name": "Grilled Beef Burger with Cheese", "type": "full_meal", "clean": False, "cost": 3, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["burger", "beef", "grilled"], "is_cheat_allowed": True},
    {"name": "Crispy Fried Chicken Pieces Basket", "type": "full_meal", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["chicken", "fried"], "is_cheat_allowed": True},
    {"name": "Fried Chicken Tenders Box", "type": "snack", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["tenders", "fried"], "is_cheat_allowed": True},
    {"name": "Crispy Golden Chicken Nuggets Plate", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["nuggets", "fried"], "is_cheat_allowed": True},
    {"name": "Creamy White Sauce Chicken Pasta", "type": "full_meal", "clean": False, "cost": 3, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["pasta", "creamy"], "is_cheat_allowed": True},
    {"name": "Tender Beef Steak with Peppercorn Sauce", "type": "full_meal", "clean": False, "cost": 5, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["steak", "beef", "premium"], "is_cheat_allowed": True},
    {"name": "Chinese Cuisine Chow Mein & Manchurian Bowl", "type": "full_meal", "clean": False, "cost": 3, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["chinese", "rice", "noodles"], "is_cheat_allowed": True},
    {"name": "Student Dhaba Shami Burger Platter", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["burger", "shami", "desi"], "is_cheat_allowed": True},
    {"name": "Crispy Chicken Paratha Roll", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["roll", "paratha", "desi"], "is_cheat_allowed": True},
    {"name": "Deep Fried Potato Samosa & Roll Plate", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["samosa", "roll", "fried", "desi"], "is_cheat_allowed": False},
    {"name": "Sweet & Sour Dahi Bhalay Bowl", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["desi", "bhalay", "street-food"], "is_cheat_allowed": True},
    {"name": "Rich Condensed Cream Chaat Bowl", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["chaat", "sweet", "desi"], "is_cheat_allowed": True},
    {"name": "Hot Roghni Naan with Gravy Chanay", "type": "full_meal", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["desi", "naan", "chanay"], "is_cheat_allowed": True},
    {"name": "Smoked Chicken Sajji with Rice Stack", "type": "full_meal", "clean": False, "cost": 4, "is_gym_approved": False, "speed": "wait", "demographic_veto": False, "tags": ["sajji", "desi", "chicken"], "is_cheat_allowed": True},
    {"name": "Dhaba Style Bun Kabab", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["bun-kabab", "desi", "street-food"], "is_cheat_allowed": True},
    {"name": "Spicy Chicken Pulao Plate", "type": "full_meal", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": False, "tags": ["pulao", "rice", "desi"], "is_cheat_allowed": True},
    {"name": "Heavy Beef Pulao Block", "type": "full_meal", "clean": False, "cost": 2, "is_gym_approved": False, "speed": "fast", "demographic_veto": True, "tags": ["pulao", "beef", "desi"], "is_cheat_allowed": True},
    {"name": "Spiced Gol Gappay Platter with Sour Water", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["gol-gappay", "desi", "street-food"], "is_cheat_allowed": True},
    {"name": "Mayonnaise Loaded Russian Salad Bowl", "type": "snack", "clean": False, "cost": 1, "is_gym_approved": False, "speed": "instant", "demographic_veto": False, "tags": ["salad", "russian"], "is_cheat_allowed": True}
]

DRINK_DATABASE = [
    # Clean Sugar Free Group
    {"name": "Chilled Gatorade Electrolyte Formula", "cost": 2, "is_gym_approved": True, "type": "drink", "sugar": "zero"},
    {"name": "Purified Carbonated Sparkling Water", "cost": 1, "is_gym_approved": True, "type": "drink", "sugar": "zero"},
    {"name": "Zero-Sugar Aspartame Free Cola Soda", "cost": 1, "is_gym_approved": True, "type": "drink", "sugar": "zero"},
    
    # Real Sugar Liquids
    {"name": "Blended Whole Milk Double Shot Iced Coffee", "cost": 3, "is_gym_approved": False, "type": "drink", "sugar": "real"},
    {"name": "Hot Artisan Creamy Cappuccino Coffee", "cost": 3, "is_gym_approved": False, "type": "drink", "sugar": "real"},
    {"name": "Crushed Ice Fresh Mint Lemon Margarita", "cost": 2, "is_gym_approved": False, "type": "drink", "sugar": "real"},
    {"name": "Regular Cold Carbonated Soft Drink Cola", "cost": 1, "is_gym_approved": False, "type": "drink", "sugar": "real"},

    # Confectionery Treats Array
    {"name": "Fudgy Chocolate Brownie Slice with Warm Core", "cost": 1, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Bakery Glazed Chocolate Donut", "cost": 1, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Molten Chocolate Lava Cake with Vanilla Scoop", "cost": 2, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Premium New York Lotus Cheesecake Slice", "cost": 3, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Dairy Vanilla & Chocolate Fudge Sundae Glass", "cost": 2, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Fluffy Buttered French Toasts Stack", "cost": 2, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Maple Syrup Drizzled Pancakes Plate", "cost": 2, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Traditional Hot Fried Gulab Jamun Set", "cost": 1, "is_gym_approved": False, "type": "dessert", "sugar": "real"},
    {"name": "Chilled Saffron Ras Malai Cup", "cost": 1, "is_gym_approved": False, "type": "dessert", "sugar": "real"}
]

# Primary Dashboard Triggers
col_b1, col_b2 = st.columns([3, 2])
with col_b1:
    execute_main = st.button("✨ Match My Vibe", use_container_width=True)
with col_b2:
    st.markdown("<div class='reroll-btn'>", unsafe_allow_html=True)
    reroll_trigger = st.button("🔁 Not Feeling It? Reroll!", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if reroll_trigger:
    st.session_state.reroll_noise = random.uniform(15.0, 600.0)
    execute_main = True

# ==========================================
# 🧠 RE-ENGINEERED RESOLUTION SCHEME
# ==========================================
if execute_main:
    
    show_food = "Full Combo" in order_preference or "Only Food" in order_preference
    show_drink = "Full Combo" in order_preference or "Only Drink" in order_preference
    
    rec_food = ""
    rec_drink = ""
    engine_logs = []
    
    # Isolate Sugar Preference Vector Flags
    is_sugar_free = "Yes" in sugar_preference

    # --- TIER 1 BRANCH: ORAL FIXATION OVERWRITE ---
    if appetite.startswith("Just need to chew"):
        chewing_options = [f for f in FOOD_DATABASE if f["type"] == "chewing_mode"]
        # Match chewing choice explicitly to user's sugar selection profile
        target_gum = [g for g in chewing_options if (g["sugar"] == "zero" if is_sugar_free else g["sugar"] == "real")]
        best_gum = target_gum[0] if target_gum else chewing_options[0]
        
        rec_food = best_gum["name"]
        rec_drink = "Purified Carbonated Sparkling Water" if is_sugar_free else "Crushed Ice Fresh Mint Lemon Margarita"
        engine_logs.append("✌️ Oral fixation detected. Intercepted food arrays to map targeted focus gums directly.")

    elif appetite == "Not feeling hungry" and order_preference != "Only Drink/Dessert 🥤":
        rec_food = "Organic Matcha Green Tea Cup"
        rec_drink = "Purified Carbonated Sparkling Water" if is_sugar_free else "Crushed Ice Fresh Mint Lemon Margarita"
        engine_logs.append("💤 Zero somatic hunger registered. Deployed light refreshments cleanly.")

    # --- MAIN MATCHING SYSTEM ENGINE ---
    else:
        target_type = "full_meal" if appetite in ["Very hungry (full meal)", "Moderately hungry"] else "snack"
        
        # 1. Solid Foods Filter Deck
        if show_food:
            scored_food_deck = []
            for item in FOOD_DATABASE:
                if item["type"] != target_type: continue
                if item["cost"] > budget: continue
                
                # Biometric Gym Isolation Adjustments
                if fitness_mode:
                    if allow_cheat:
                        if not item["is_cheat_allowed"]: continue
                    else:
                        if not item["is_gym_approved"]: continue
                
                score = 100
                
                # Gender Veto / Group Preference Loop (Beef Pulao handling)
                if (gender == "Girl" or company == "Girls Group") and item["demographic_veto"]:
                    score -= 900
                    
                # Specific Requested Asset Boosting (BBQ / Grilled / Sandwiches)
                if fitness_mode:
                    if "protein" in item["tags"] or "grilled" in item["tags"] or "roasterie" in item["tags"]:
                        score += 350
                        
                # Cravings Matrix Mapping
                if cravings == "Healthy Food" and item["clean"]: score += 300
                elif cravings == "Sweet / Chocolate" and "sweet" in item["tags"]: score += 300
                elif cravings == "Fast Food / Fried" and "fried" in item["tags"]: score += 300
                elif cravings == "Savory / Spicy / Desi" and "desi" in item["tags"]: score += 300
                
                # Spatial Matching Logic
                if location == "University campus" and "street-food" in item["tags"]: score += 100
                if time_avail.startswith("Very little") and item["speed"] == "wait": score -= 400
                
                score += random.uniform(-12.0, 12.0) * st.session_state.reroll_noise
                scored_food_deck.append((item["name"], score))
                
            if scored_food_deck:
                scored_food_deck.sort(key=lambda x: x[1], reverse=True)
                rec_food = scored_food_deck[0][0]
            else:
                rec_food = "Fresh Grilled Chicken Breast Wrap"

        # 2. Liquids / Desserts Filter Deck
        if show_drink:
            scored_drink_deck = []
            for d in DRINK_DATABASE:
                if d["cost"] > budget: continue
                
                # ENFORCE USER SUGAR CHOICE EXPLICITLY
                if is_sugar_free and d["sugar"] != "zero": 
                    continue  # Strict block if user demands zero sugar
                if not is_sugar_free and d["sugar"] == "zero": 
                    continue  # Filter out sugar-free products if user wants standard sugary drinks
                
                d_score = 100
                
                if fitness_mode and not allow_cheat and not d["is_gym_approved"]: 
                    d_score -= 800
                    
                if mood in ["Sad", "Stress"] and d["type"] == "dessert": 
                    d_score += 250
                    
                d_score += random.uniform(-10.0, 10.0) * st.session_state.reroll_noise
                scored_drink_deck.append((d["name"], d_score))
                
            if scored_drink_deck:
                scored_drink_deck.sort(key=lambda x: x[1], reverse=True)
                rec_drink = scored_drink_deck[0][0]
            else:
                rec_drink = "Chilled Gourmet Mineral Water"

    # ==========================================
    # VISUAL OUTPUT DISPLAY MODULE (THE DASHBOARD)
    # ==========================================
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏆 Your Curated Match")
    
    # Conditional Layout Rendering based on Selection Mode
    if show_food and show_drink:
        st.markdown(f"""
            <div class="munch-card">
                <span class="card-label">🔥 Main Food Match</span>
                <span style="color:#ffffff; font-size:24px; font-weight:800; display:block; font-family:'Space Grotesk', sans-serif; margin-bottom:15px;">{rec_food}</span>
                <hr style="border:0; border-top:1px solid #252042; margin: 15px 0;">
                <span class="card-label" style="color:#00f5ff;">🥤 Companion Drink / Dessert Treat</span>
                <span style="color:#ffffff; font-size:20px; font-weight:700; display:block;">{rec_drink}</span>
            </div>
        """, unsafe_allow_html=True)
    elif show_food:
        st.markdown(f"""
            <div class="munch-card" style="border-left-color: #ff007a;">
                <span class="card-label">🍔 Solid Food Match Only</span>
                <span style="color:#ffffff; font-size:25px; font-weight:800; display:block; font-family:'Space Grotesk', sans-serif;">{rec_food}</span>
            </div>
        """, unsafe_allow_html=True)
    elif show_drink:
        st.markdown(f"""
            <div class="munch-card" style="border-left-color: #00f5ff;">
                <span class="card-label">🥤 Beverage / Dessert Match Only</span>
                <span style="color:#ffffff; font-size:24px; font-weight:800; display:block; font-family:'Space Grotesk', sans-serif;">{rec_drink}</span>
            </div>
        """, unsafe_allow_html=True)

    # Summary Panel Widgets Row
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown(f"""<div class='stat-bubble'><span style='color:#64748b; font-size:11px; font-weight:700; text-transform:uppercase;'>Wallet Configuration</span><br><h2 style='color:#b100ff; margin:5px 0; font-weight:800; font-size:22px; font-family: "Space Grotesk", sans-serif;'>Level {budget} / 5</h2></div>""", unsafe_allow_html=True)
    with col_v2:
        sugar_tag = "Zero Sugar Setup" if is_sugar_free else "Regular Sugar Setup"
        st.markdown(f"""<div class='stat-bubble'><span style='color:#64748b; font-size:11px; font-weight:700; text-transform:uppercase;'>Sugar Tone Filter</span><br><h2 style='color:#ff007a; margin:5px 0; font-weight:800; font-size:22px; font-family: "Space Grotesk", sans-serif;'>{sugar_tag}</h2></div>""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if engine_logs:
        for log in engine_logs:
            st.caption(log)

import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import nest_asyncio
nest_asyncio.apply()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '8408576776:AAGl7kAH79zftXF7p0Z5NKBheJ9HguqPGxQ'


TIMELINE_EVENTS = [
    {'year': 'c. 980 BCE', 'event': 'Legendary Queen of Sheba visits King Solomon of Israel, linking Ethiopia to biblical history.'},
    {'year': 'c. 100 CE', 'event': 'Rise of the Aksumite Empire, a major trading power exporting ivory, gold, and adopting Christianity in 330 CE.'},
    {'year': '1270', 'event': 'Yekuno Amlak founds the Solomonic Dynasty, claiming descent from Solomon and Sheba.'},
    {'year': '1889', 'event': 'Emperor Menelik II signs the Treaty of Wuchale with Italy, sparking disputes leading to war.'},
    {'year': '1896', 'event': 'Battle of Adwa: Ethiopia defeats Italy, preserving independence—the only African nation to resist European colonialism at the time.'},
    {'year': '1930', 'event': 'Haile Selassie I crowned Emperor; Ethiopia joins the League of Nations as Africa first member.'},
    {'year': '1936', 'event': 'Italy invades and occupies Ethiopia until 1941, when Allied forces liberate it.'},
    {'year': '1963', 'event': 'Founding of the Organisation of African Unity (now African Union) in Addis Ababa.'},
    {'year': '1974', 'event': 'Haile Selassie deposed in a Marxist coup, leading to the Derg regime and Red Terror.'},
    {'year': '1993', 'event': 'Eritrea gains independence after a 30-year war; Ethiopia becomes landlocked.'},
    {'year': '2018', 'event': 'Abiy Ahmed becomes PM, wins Nobel Peace Prize in 2019 for ending the Ethiopia-Eritrea war.'}
]

FUN_FACTS = [
    'Ethiopia uses a 13-month calendar! It has 12 months of 30 days each, plus a 13th short month of 5-6 days. Its about 7-8 years behind the Gregorian calendar.',
    'Coffee originated in Ethiopia Kaffa region—legend says a goat herder discovered its energizing effects around the 9th century.',
    'Ethiopia is the only African country never fully colonized, thanks to victories like Adwa. Its flag inspired Pan-African colors (green, yellow, red).',
    'The Ark of the Covenant is said to be guarded in Aksums Church of Our Lady Mary of Zion—only one guardian knows its location!',
    'Ethiopias Lalibela rock-hewn churches (12th century) are UNESCO sites, carved from solid rock as a 'New Jerusalem' during crusades.',
    'Rastafarianism reveres Haile Selassie as a divine figure; 'Ras Tafari' was his pre-coronation name.',
    'Ethiopia adopted Christianity in 330 CE under King Ezana—earlier than most of Europe—and has its own unique Orthodox traditions.',
    'The first female African head of state was Ethiopias Empress Zewditu (1916-1930).',
    'Addis Ababa, meaning 'New Flower,' is Africas diplomatic capital, hosting the African Union HQ at 7,726 ft (2,355 m) elevation.',
    'Ethiopia is the cradle of humanity: 'Lucy' (Australopithecus afarensis, 3.2 million years old) was found in the Afar region in 1974.'
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = '''
🌍 *Welcome to Ethiopian History Bot!* 🌍

Discover the cradle of humanity, ancient empires, and Africas unbowed spirit!

Commands:
• /timeline - Key historical events
• /fact - Random fun fact
• Ask me about 'Aksum', 'Adwa', 'Haile Selassie', or more!

What's your history question? (e.g., 'Tell me about the Queen of Sheba')
    '''
    await update.message.reply_text(welcome, parse_mode='Markdown')

async def timeline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeline_text = '*Ethiopian History Timeline* 📜\n\n'
    for event in TIMELINE_EVENTS:
        timeline_text += f"*{event['year']}*: {event['event']}\n"
    await update.message.reply_text(timeline_text, parse_mode='Markdown')

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(FUN_FACTS)
    await update.message.reply_text(f"🤔 *Fun Fact*: {fact}", parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # Keyword-based responses
    if 'aksum' in user_message:
        response = '''
🏛️ *Aksumite Empire (c. 100-940 CE)*

One of Africas greatest ancient kingdoms, Aksum was a trading powerhouse connecting Rome, India, and Arabia. It minted its own coins, built massive obelisks (like the 100-ft Stele of Aksum), and converted to Christianity in 330 CE under King Ezana—the first Christian state south of the Sahara. Fun tie-in: Aksum claims to house the Ark of the Covenant!
        '''
    elif 'adwa' in user_message or 'adua' in user_message:
        response = '''
⚔️ *Battle of Adwa (March 1, 1896)*

Ethiopias defining victory! Emperor Menelik II led 100,000 troops to crush 17,000 Italian invaders, preserving independence during the Scramble for Africa. It inspired global anti-colonial movements and is celebrated annually as a national holiday. 'Africa for Africans!'
        '''
    elif 'haile selassie' in user_message:
        response = '''
👑 *Emperor Haile Selassie I (1892-1975)*

Last Solomonic ruler (1930-1974), seen as the 'Lion of Judah.' He modernized Ethiopia, addressed the League of Nations against Italian invasion (1936), and inspired Rastafarianism as a messianic figure. Deposed in a 1974 coup amid famine and unrest.
        '''
    elif 'queen of sheba' in user_message or 'sheba' in user_message:
        response = '''
👸 *Queen of Sheba (c. 950 BCE)*

Legendary ruler of Saba (possibly in Ethiopia/Yemen) who visited King Solomon, bearing gold and spices. Ethiopian lore says she bore his son, Menelik I, founding the Solomonic Dynasty. Immortalized in the Kebra Nagast epic—Ethiopias national scripture.
        '''
    else:
        response = '''
Hmm, that's a great topic! Try asking about 'Aksum', 'Battle of Adwa', 'Haile Selassie', or 'Queen of Sheba'. Or use /timeline for an overview! What's next? 😊
        '''

    await update.message.reply_text(response, parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('timeline', timeline))
    app.add_handler(CommandHandler('fact', fact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print('Ethiopian History Bot is running... 🌟')
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
    
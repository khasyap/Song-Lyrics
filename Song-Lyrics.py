import time
import pygame


AUDIO_FILE = r"D:\Downloads\sahiba_song1.mp3"

lyrics = [
    "Sahiba aaye ghar kaahe naa,",
    "Aise toh sataaye naa",
    "Dekhun tujhko chain aata hai,",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!",
    "",
    "Sahiba samandar, meri aankhon mein reh gaye,",
    "Hum aate aate jaana teri yaadon mein reh gaye,",
    "Yeh palke gawahi hai, hum raaton mein reh gaye",
    "Jo waade kiye saare, bas baaton mein reh gaye",
    "",
    "Baaton baaton mein hi, khwaabon khwaabon mein hi, mere qareeb hai tu,",
    "Teri talab mujhko teri talab jaana ho tu kabhi rubaroo,",
    "Shor sharaba jo seene mein hai mere, kaise bayaan main karun?",
    "Haal jo mera hai main kisko bataun? Mere…",
    "",
    "Sahiba dil naa kiraaye ka,",
    "Thoda toh sambhaalo naa,",
    "Naazuk hai yeh toot jaata hai",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!",
    "",
    "Kaisi bhala shab hogi woh sang jo tere dhalti hai,",
    "Dil ko koi khwahish nahi, teri kami khalti hai",
    "Aaram naa ab aankhon ko, khwaab bhi naa badalti hai",
    "Dil ko koi khwahish nahi, teri kami jaana khalti hai",
    "",
    "Sahiba, tu hi mera aaina,",
    "Haathon mein bhi mere haan,",
    "Tera hi naseeb aata hai,",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!"
]


timing = [
    2, 2, 2, 3, 2, 3,
    1, 3, 3, 3, 3,
    1, 3, 3, 3, 3,
    1, 2, 2, 3, 2, 3,
    1, 3, 3, 3, 3,
    1, 3, 2, 3, 2, 3
]
print("🎶 Now playing: 'Sahiba' ...")
print("-" * 50)

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play()

for line, delay in zip(lyrics, timing):
    print(line)
    time.sleep(delay)

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("-" * 50)
print("🎵 Song finished! Hope you enjoyed it.")

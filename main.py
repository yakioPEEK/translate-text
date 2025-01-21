#Всем привет, меня зовут Бахытжан Бахтияр , это мой проект 'АвтоПереводчик'. Я расскажу подробнее что я тут использовал и почему.

# Получается, первым делом нужно конечно же импортируем библиотеку tkinter, googletrans, также модель asyncio и ttk.

import tkinter as tk 
from tkinter import ttk  
from googletrans import Translator  
import asyncio 

translator = Translator()

# Список языков, если хотите можно добавить еще...

LANGUAGES = { 
    "Русский": "ru",
    "Английский": "en",
    "Испанский": "es",
    "Украинский": "uk",
    "Казахский": "kk",
    "Китайский (упрощённый)": "zh-cn",
    "Немецкий": "de",
    "Французский": "fr",
    "Итальянский": "it",
    "Японский": "ja",
}

# Это у нас асинхронная функция, я ее использую потому что сам гугл требует интернет и ответ от сервера, а тут он будет продолжать работать, пока ожидаем ответ от сервера.
async def async_translate(input_text, source_lang, target_lang):
    return await translator.translate(input_text, src=source_lang, dest=target_lang)


# Дальше у нас сама основная функция перевода
# Сперва мы получаем текст и идет проверка с условным оператором, был ли текст введен.
# Потом идет поиск языка которую пользователь выбрал и на какой переводит, это строка 40 и 41.
# Дальше идет перевод текста использую библиотеку asynsio , также бывает ошибка но я ее исправил, и вывожу сообщение о том что нужно нажать еще раз кнопку 'Перевести'.
# И под конец , мы запускаем asyncio


def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()  
    if not input_text:  
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Пожалуйста, введите текст для перевода.")
        return

    source_lang = LANGUAGES[source_language.get()]  
    target_lang = LANGUAGES[target_language.get()]  

    async def perform_translation():
        try:
            translated = await async_translate(input_text, source_lang, target_lang)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, translated.text)  
        except Exception as e:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"Пожалуйста, нажмите кнопку 'Перевести' еще раз...")

    
    asyncio.run(perform_translation())



# Наконец-то мы настраиваем интерфейс
# Ну здесь все по классике, размер, имя, также стиль, стиль делал благодаря from tkinter import ttk.

root = tk.Tk()
root.title("АвтоПереводчик")  
root.geometry("700x700")
root.resizable(False, False)
style = ttk.Style()
style.theme_use("clam")




# Ура, осталось маленькая часть моего проекта.
# Делаем поле для ввода текста, выбираем размер и т.д

ttk.Label(root, text="Введите текст для перевода:", font=("Arial", 12)).pack(pady=10)
input_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Arial", 10))
input_box.pack(pady=5)

# Также сделал меню которое выходит если нажать на нее и добавил список что бы пользователь выбрал, язык на который ему нужно.
# Также я решил сделать язык по умолчанию это у нас Русский и Английский


ttk.Label(root, text="Язык источника:", font=("Arial", 12)).pack(pady=10)
source_language = ttk.Combobox(root, values=list(LANGUAGES.keys()), font=("Arial", 10))
source_language.set("Русский")  
source_language.pack()

ttk.Label(root, text="Язык перевода:", font=("Arial", 12)).pack(pady=10)
target_language = ttk.Combobox(root, values=list(LANGUAGES.keys()), font=("Arial", 10))
target_language.set("Английский") 
target_language.pack()


# Создаем кнопку, команду для кнопки и размещение кнопки.

translate_button = ttk.Button(root, text="Перевести", command=translate_text)
translate_button.pack(pady=20)


# Создаем еще одно поле текста в котором уже будет наш переведенный текст, ну и также по классике размер, размещение и т.д
ttk.Label(root, text="Переведенный текст:", font=("Arial", 12)).pack(pady=10)
output_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Arial", 10))
output_box.pack(pady=5)


# УРАААА , это конец....
root.mainloop()

# Также я подготовил текст , на случаи того чтобы вам не пришлось искать.

# Казахстан — моя родная страна, и я горжусь тем, что вырос здесь. Это огромная и разнообразная земля, от бескрайних степей до величественных гор.
# Столицей страны является Астана. Население Казахстана — 20.20 миллионов человек, и здесь живёт много разных народов (124), что создаёт уникальную атмосферу многокультурности.
# Мы гордимся своей историей и традициями, и я всегда чувствую связь с этой землёй, её людьми и природой.
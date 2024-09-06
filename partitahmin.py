import tkinter as tk
from tkinter import messagebox
from groq import Groq

# Groq API anahtarınızı buraya ekleyin
GROQ_API_KEY = ""
client = Groq(api_key=GROQ_API_KEY)

# Kullanıcı verilerini saklamak için bir sözlük
user_data = {}

def predict_party_and_opinion(age, education, income, urban, employment, political_interest, city, religious_view, ataturk_view, nationalism_level):
    """
    Kullanıcının verdiği bilgilere göre Groq API'sini kullanarak parti tercihi ve genel görüş tahmini yapar.
    """
    try:
        # Groq API'yi kullanarak bir tahmin yap
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert political analyst focusing on Turkish politics. Based on user inputs, predict their likely political party preference and provide a brief description of their general political opinions.",
                },
                {
                    "role": "user",
                    "content": f"My age is {age}, my education level is {education}, my monthly income is {income} USD, I live in an urban area: {urban}, my employment status is {employment}, my interest in politics is {political_interest}, I live in {city}, my religious view is {religious_view}, my opinion on Atatürk is {ataturk_view}, and my level of nationalism is {nationalism_level}. Predict my likely political party preference in Turkey and describe my general political opinions.",
                }
            ],
            model="llama3-70b-8192",
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        return f"Bir hata oluştu: {e}"

def submit():
    """
    Kullanıcının girdiği verileri işleyip tahmini hesaplar ve gösterir.
    """
    try:
        age = int(age_entry.get())
        education = education_var.get()
        income = float(income_entry.get())
        urban = urban_var.get()
        employment = employment_var.get()
        political_interest = interest_var.get()
        city = city_entry.get()
        religious_view = religion_var.get()
        ataturk_view = ataturk_var.get()
        nationalism_level = nationalism_var.get()

        # Kullanıcı verilerini sakla
        user_data["yaş"] = age
        user_data["eğitim"] = education
        user_data["gelir"] = income
        user_data["şehir"] = urban
        user_data["iş durumu"] = employment
        user_data["siyasi ilgi"] = political_interest
        user_data["şehir adı"] = city
        user_data["dini görüş"] = religious_view
        user_data["Atatürk hakkındaki görüş"] = ataturk_view
        user_data["milliyetçilik düzeyi"] = nationalism_level

        # Parti ve görüş tahmini yap
        prediction = predict_party_and_opinion(age, education, income, urban, employment, political_interest, city, religious_view, ataturk_view, nationalism_level)

        # Sonuçları göster
        messagebox.showinfo("Tahmin Sonucu", prediction)

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# Tkinter arayüzünü oluştur
root = tk.Tk()
root.title("Parti Tercihi ve Görüş Tahmini")
root.geometry("450x600")
root.configure(bg='#F0F0F0')

# Ana çerçeve
frame = tk.Frame(root, padx=10, pady=10, bg='#F0F0F0')
frame.pack(expand=True)

# Etiketler ve giriş alanları
tk.Label(frame, text="Yaş:", font=("Arial", 12), bg='#F0F0F0').grid(row=0, column=0, sticky='w', pady=5)
age_entry = tk.Entry(frame, font=("Arial", 12), width=10)
age_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Eğitim Seviyesi:", font=("Arial", 12), bg='#F0F0F0').grid(row=1, column=0, sticky='w', pady=5)
education_var = tk.StringVar(value="Üniversite")
education_dropdown = tk.OptionMenu(frame, education_var, "Lise", "Üniversite", "Yüksek Lisans", "Doktora")
education_dropdown.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Aylık Gelir (USD):", font=("Arial", 12), bg='#F0F0F0').grid(row=2, column=0, sticky='w', pady=5)
income_entry = tk.Entry(frame, font=("Arial", 12), width=10)
income_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Şehirde mi yaşıyorsunuz?:", font=("Arial", 12), bg='#F0F0F0').grid(row=3, column=0, sticky='w', pady=5)
urban_var = tk.StringVar(value="Evet")
urban_dropdown = tk.OptionMenu(frame, urban_var, "Evet", "Hayır")
urban_dropdown.grid(row=3, column=1, pady=5)

tk.Label(frame, text="İş Durumu:", font=("Arial", 12), bg='#F0F0F0').grid(row=4, column=0, sticky='w', pady=5)
employment_var = tk.StringVar(value="Çalışan")
employment_dropdown = tk.OptionMenu(frame, employment_var, "Çalışan", "İşsiz", "Öğrenci", "Emekli")
employment_dropdown.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Siyasi İlgi Düzeyi:", font=("Arial", 12), bg='#F0F0F0').grid(row=5, column=0, sticky='w', pady=5)
interest_var = tk.StringVar(value="Yüksek")
interest_dropdown = tk.OptionMenu(frame, interest_var, "Yüksek", "Orta", "Düşük")
interest_dropdown.grid(row=5, column=1, pady=5)

tk.Label(frame, text="Şehir:", font=("Arial", 12), bg='#F0F0F0').grid(row=6, column=0, sticky='w', pady=5)
city_entry = tk.Entry(frame, font=("Arial", 12), width=15)
city_entry.grid(row=6, column=1, pady=5)

tk.Label(frame, text="Dini Görüş:", font=("Arial", 12), bg='#F0F0F0').grid(row=7, column=0, sticky='w', pady=5)
religion_var = tk.StringVar(value="Dindar")
religion_dropdown = tk.OptionMenu(frame, religion_var, "Dindar", "Agnostik", "Ateist", "Dini Yorumcu")
religion_dropdown.grid(row=7, column=1, pady=5)

tk.Label(frame, text="Atatürk Hakkındaki Görüş:", font=("Arial", 12), bg='#F0F0F0').grid(row=8, column=0, sticky='w', pady=5)
ataturk_var = tk.StringVar(value="Olumlu")
ataturk_dropdown = tk.OptionMenu(frame, ataturk_var, "Olumlu", "Olumsuz", "Nötr")
ataturk_dropdown.grid(row=8, column=1, pady=5)

tk.Label(frame, text="Milliyetçilik Düzeyi:", font=("Arial", 12), bg='#F0F0F0').grid(row=9, column=0, sticky='w', pady=5)
nationalism_var = tk.StringVar(value="Yüksek")
nationalism_dropdown = tk.OptionMenu(frame, nationalism_var, "Yüksek", "Orta", "Düşük")
nationalism_dropdown.grid(row=9, column=1, pady=5)

# Gönder butonu
submit_button = tk.Button(frame, text="Gönder", command=submit, font=("Arial", 12), bg='#4CAF50', fg='white')
submit_button.grid(row=10, columnspan=2, pady=20)

# Arayüzü başlat
root.mainloop()



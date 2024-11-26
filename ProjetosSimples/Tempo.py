import tkinter as tk
from tkinter import messagebox
import requests

def buscar_informacoes():
    estado = estado_entry.get()
    cidade = cidade_entry.get()
    
    if not estado or not cidade:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return
    
    api_key = "c08768df3da3ba2db70545b9ddd30a68"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},{estado},BR&appid={api_key}&lang=pt_br&units=metric"
    
    try:
        resposta = requests.get(url)
        data = resposta.json()
        
        if data["cod"] == 200:
            descricao = data["weather"][0]["description"]
            temperatura = data["main"]["temp"]
            umidade = data["main"]["humidity"]
            resumo = f"Descrição: {descricao}\nTemperatura: {temperatura}°C\nUmidade: {umidade}%"
            messagebox.showinfo("Informações do Local", resumo)
        else:
            messagebox.showerror("Erro", "Cidade ou estado não encontrados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar informações: {e}")

root = tk.Tk()
root.title("Resumo do Local")

tk.Label(root, text="Estado (UF):").pack(pady=5)
estado_entry = tk.Entry(root)
estado_entry.pack(pady=5)

tk.Label(root, text="Cidade:").pack(pady=5)
cidade_entry = tk.Entry(root)
cidade_entry.pack(pady=5)

buscar_btn = tk.Button(root, text="Buscar", command=buscar_informacoes)
buscar_btn.pack(pady=10)

root.mainloop()
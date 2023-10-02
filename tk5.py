import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk


qa_pairs = [  {
        "q": "Which movies are running there?",
        "a": "Empuraan, Vaadivaasal, Salaar, Gamechanger"
    },
    {
        "q": "Are tickets available for any movie?",
        "a": "20 platinum seats are available for Game Changer"
    },
    {
        "q": "What about other movies?",
        "a": "All movies are houseful till Sunday"
    },
    {
        "q": "May I know the duration of the movies?",
        "a": "Empuraan is 3 hrs long, Salaar is 2 hrs 45 minutes, both Vaadivaasal and Game Changer are 2 hrs and 33 minutes long"
    },
    {
        "q": "May I know the genre of the movies?",
        "a": "Empuraan is a political thriller/action, Vaadivaasal is action/drama, Salaar and Game Changer are action movies"
    },
    {
        "q": "How are ticket rates for different seats?",
        "a": "Platinum: 180 INR per ticket, Sofa: 200 INR per ticket, Recliner: 300 INR per ticket. Please note that if there are 3D glasses, an extra 20 INR will be added."
    },
    {
        "q": "What are the show times for the movies?",
        "a": "Screen 1 - Empuraan - 11:30 AM, 3:00 PM, 6:30 PM, 10:00 PM\nScreen 2 - Vaadivaasal - 12:30 PM, 3:30 PM, 6:45 PM, 10:00 PM\nScreen 3 - Salaar - 12:30 PM, 3:30 PM, 6:45 PM, 10:00 PM\nScreen 4 - Game Changer - 12:30 PM, 3:30 PM, 6:45 PM, 10:00 PM"
    },
    {
        "q": "Can you provide snacks during the interval?",
        "a": "Absolutely! You can select from a variety of snacks available on our website. Please note that tea and coffee are not allowed inside the hall for the comfort of all our guests."
    },
    {
        "q": "Hi bot",
        "a": "Hello"
    },
    {
        "q": "Bye bot",
        "a": "Goodbye"
    }
    
]


def get_response():
    user_input = user_input_entry.get("1.0", tk.END).strip().lower()
    bot_response = "I'm sorry, I don't understand that question."
    
    if user_input in ["hi", "hello", "hey"]:
        bot_response = "Hello"
    else:
        for qa_pair in qa_pairs:
            if user_input in qa_pair["q"].lower():
                bot_response = qa_pair["a"]
                break

    if "book tickets for salaar on monday" in user_input:
        bot_response = "Sure, you can proceed by paying at this link: https://cinemaparadiso.com/bookings"
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
    chat_window.config(state=tk.DISABLED)
    user_input_entry.delete("1.0", tk.END)


root = tk.Tk()
root.title("Cinema Paradiso Chatbot")


notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)


home_frame = ttk.Frame(notebook)
about_us_frame = ttk.Frame(notebook)
contact_us_frame = ttk.Frame(notebook)


notebook.add(home_frame, text="HOME")
notebook.add(about_us_frame, text="ABOUT US")
notebook.add(contact_us_frame, text="CONTACT US")


image = Image.open(r"D:\DL projects March\Cinemabotweb\6C6E5636-1272-456D-B2E2-C75E7A7D11F1-1024x6112.png")


max_width = 400
max_height = 300
image.thumbnail((max_width, max_height), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(image)
image_label = tk.Label(home_frame, image=photo)
image_label.image = photo
image_label.pack(pady=20)  


chat_window = scrolledtext.ScrolledText(home_frame, wrap=tk.WORD, state=tk.DISABLED, height=10, width=70)
chat_window.tag_configure("user", foreground="blue")
chat_window.tag_configure("bot", foreground="green")
chat_window.pack(pady=20)  


user_input_entry = tk.Text(home_frame, height=2, width=50)
user_input_entry.pack()  


ask_button = tk.Button(home_frame, text="Ask", command=get_response)
ask_button.pack(pady=20)  


about_us_text = """
Cinema Paradiso is your premier destination for cinematic experiences. Established in the year 2017, we have been serving the community with the finest in entertainment. Our state-of-the-art projector technology ensures that you enjoy every frame of your favorite films. With a seating capacity of 350, we cater to film enthusiasts from all walks of life.

Our dedicated team of professionals strives to make your visit memorable. From ticketing to concessions, our staff is here to assist you at every step of your cinematic journey.

At Cinema Paradiso, we believe in the magic of cinema, where stories come to life on the big screen. As a wise cinephile once said, "Cinema is the most beautiful fraud in the world." Join us to experience this beautiful fraud in all its glory.
"""

about_us_label = tk.Label(about_us_frame, text=about_us_text, wraplength=500, justify=tk.LEFT,font=("Arial", 17))
about_us_label.pack(padx=20, pady=20)


contact_us_text = """
For inquiries, bookings, and more information, please contact us at:

Phone: +91 9488754110
Email: info@cinemaparadiso.com
"""

contact_us_label = tk.Label(contact_us_frame, text=contact_us_text, wraplength=500, justify=tk.LEFT,font=("Arial", 17))
contact_us_label.pack(padx=20, pady=20)


root.mainloop()

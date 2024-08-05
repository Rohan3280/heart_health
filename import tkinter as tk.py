import tkinter as tk
from tkinter import Button, Image, Label, PhotoImage, Tk, messagebox
import pandas as pd
from PIL import ImageTk,Image
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('heart.csv')

# Initialize the model and train it
X = df.drop(columns='target', axis=1)
Y = df['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=23)

# Train the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Create a Tkinter window


# Function to predict heart condition

class HeartDes:
    def __init__(self):
        root=None
    def homepage(self):
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Heart Condition Predictor")
        image_path = "image.png"
        image = Image.open(image_path)
        image = image.resize((screen_width, screen_height))  # Resize the image without anti-aliasing
        # Convert the resized image to a PhotoImage object
        image = ImageTk.PhotoImage(image)
        # Create a label to display the resized image
        label_image = tk.Label(self.root, image=image)
        label_image.place(x=0, y=0, relwidth=1, relheight=1) 
        img=Image.open("juet.jpg")
        img = img.resize((300,300 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).pack(padx=50,pady=50)
        def secondpage():
            self.root.destroy()
            self.secondpage1()
        Label(self.root,text="Artificial Intelligence & Application Project",font=("Arial",25,"bold")).pack(padx=20,pady=20)
        Button(self.root,text='Check Your Heart', bg='black', fg ='White',font=("Arial",20,"bold"),command=secondpage).pack(pady=20)
        Label(self.root,text="Rahul Sharma (221B291)",font=("Arial",15,"bold")).pack(padx=20,pady=20)
        Label(self.root,text="Rajratan Shivhare (221B292)",font=("Arial",15,"bold")).pack(padx=20,pady=20)
        Label(self.root,text="Raman Soni (221B295)",font=("Arial",15,"bold")).pack(padx=20,pady=20)
        self.root.mainloop()
    def secondpage1(self):
        self.root = tk.Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        image_path = "image.png"
        image = Image.open(image_path)
        image = image.resize((screen_width, screen_height))  # Resize the image without anti-aliasing
        # Convert the resized image to a PhotoImage object
        image = ImageTk.PhotoImage(image)
        # Create a label to display the resized image
        label_image = tk.Label(self.root, image=image)
        label_image.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.title("Heart Condition Predictor")
        def predict_heart_condition():
            try:
                # Retrieve input values from entry fields and convert them to floats
                input_data = [
                    float(age_entry.get()), float(sex_entry.get()), float(cp_entry.get()), float(trestbps_entry.get()), 
                    float(chol_entry.get()), float(fbs_entry.get()), float(restecg_entry.get()), float(thalach_entry.get()), 
                    float(exang_entry.get()), float(oldpeak_entry.get()), float(slope_entry.get()), float(ca_entry.get()), 
                    float(thal_entry.get())
                ]

                # Make prediction
                prediction = model.predict([input_data])
                
                # Display prediction
                if prediction[0] == 0:
                    messagebox.showinfo("Great Message", "Your Heart Is At Low Risk !!!")
                else:
                    messagebox.showerror("Visit Doctor", "Your Heart Is At High Risk !!!")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numerical values for all inputs.")
        # Create labels and entry fields for input
        # Create labels and entry fields for input
        # Create labels and entry fields for input
        # Create labels and entry fields for input
        tk.Label(self.root, text="Age:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        age_entry = tk.Entry(self.root, width=30)
        age_entry.pack(pady=5)

        tk.Label(self.root, text="(F:1/M:0)Sex:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        sex_entry = tk.Entry(self.root, width=30)
        sex_entry.pack(pady=5)

        tk.Label(self.root, text="(0-4)Chest Pain Type:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        cp_entry = tk.Entry(self.root, width=30)
        cp_entry.pack(pady=5)

        tk.Label(self.root, text="(mm/hg)Resting Blood Pressure:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        trestbps_entry = tk.Entry(self.root, width=30)
        trestbps_entry.pack(pady=5)

        tk.Label(self.root, text="(mg/dl)Cholesterol:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        chol_entry = tk.Entry(self.root, width=30)
        chol_entry.pack(pady=5)

        tk.Label(self.root, text="(0/1 >=(120))Fasting Blood Sugar:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        fbs_entry = tk.Entry(self.root, width=30)
        fbs_entry.pack(pady=5)

        tk.Label(self.root, text="(0-2)Resting Electrocardiographic Results:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        restecg_entry = tk.Entry(self.root, width=30)
        restecg_entry.pack(pady=5)

        tk.Label(self.root, text="Maximum Heart Rate Achieved:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        thalach_entry = tk.Entry(self.root, width=30)
        thalach_entry.pack(pady=5)

        tk.Label(self.root, text="(1/0)Exercise Induced Angina:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        exang_entry = tk.Entry(self.root, width=30)
        exang_entry.pack(pady=5)

        tk.Label(self.root, text="ST Depression Induced by Exercise Relative to Rest:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        oldpeak_entry = tk.Entry(self.root, width=30)
        oldpeak_entry.pack(pady=5)

        tk.Label(self.root, text="(0-3)Slope of the Peak Exercise ST Segment:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        slope_entry = tk.Entry(self.root, width=30)
        slope_entry.pack(pady=5)

        tk.Label(self.root, text="Number of Major Vessels Colored by Fluoroscopy:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        ca_entry = tk.Entry(self.root, width=30)
        ca_entry.pack(pady=5)

        tk.Label(self.root, text="Thalassemia:", anchor="center", justify="center", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        thal_entry = tk.Entry(self.root, width=30)
        thal_entry.pack(pady=5)

        # Create a button to predict
        predict_button = tk.Button(self.root, text="Predict", command=predict_heart_condition, font=("Arial", 14))
        predict_button.pack(pady=10)
        def Homepage():
            self.root.destroy()
            self.homepage()
        tk.Button(self.root, text="Home", command=Homepage, font=("Arial", 14)).pack(pady=10)


        # Start the main event loop
        self.root.mainloop()




obj=HeartDes().homepage()
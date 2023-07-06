
# osnovno za sve ostalo je importovati sledece stvari iz flaska
from flask import Flask, render_template, request

# __name__ predstavlja ime trenutnog module-a tj. "__main__" module 
app = Flask(__name__)

# decorator definise route na koju ce se odazvati funkcijom ispod
@app.route('/')  # '/' = 'http://localhost:3000/'
def home(): # ovu funkciju mozemo nazvati bilo kojim imenom
    fruits = ['Apple', 'Banana', 'Orange']
    # prikazivanje html fajla na browseru kad se ode na 'http://localhost:3000/'
    # render_template promenljive salje html fajlu (objasnjenej u htmlu)
    return render_template('index.html', fruits=fruits) 
    

@app.route('/about')  # '/' = 'http://localhost:3000/about'
def about(): # ovu funkciju mozemo nazvati bilo kojim imenom
    # prikazivanje html fajla na browseru kad se ode na 'http://localhost:3000/about'
    return render_template('about.html') 


# provera da li je module koji pokrecemo main module (uvek isto)
if __name__ == '__main__': 
    app.run(debug=True) # app.run pokrece server

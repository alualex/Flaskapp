from flask import Flask, render_template, request

app = Flask(__name__)


ITEMS = {"france": "France", "australia":"Australia","kenya":"Kenya","usa":"USA"}

def listToString(s):
    """
    Convert a list of items into a string of comma separated items. 
    """
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s[0]
    return ", and ".join([", ".join(s[:-1]), s[-1]])



@app.route('/', methods=['GET','POST'])
def index():
    check_list = ""
    check_items = {}
    
    
    if request.method == 'POST':
        check_list = listToString(request.form.getlist('switches'))
        
        check_items = {k:v for (k,v) in ITEMS.items() if v in check_list}

    return render_template('index.html', check_list=check_list, **check_items)
        
    
if __name__ == "__main__":
    app.run(debug=True)
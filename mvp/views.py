from django.shortcuts import render
import pandas as pd
import json
import os
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def upload(request):
    return render(request, 'upload.html', {'name':"Aileen"})

def load(request):
    #print(request.method)
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request, 'table.html')


def test(request):
    return render(request, 'test.html')

def table(request):

    #print(request.method)
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)

    #print(request.FILES['document'].name)
    df = pd.read_csv(os.path.join(os.getcwd(),"files", request.FILES['document'].name))

    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    code = "#Code Starts Here: \n"
    code = code + "import pandas as pd \n"
    code = code + "import numpy as np \n"
    code = code + "import os \n"
    code = code + "# Import data \n"
    code = code + "df = pd.read_csv(os.path.join(os.getcwd(),'files','{}')) \n".format(request.FILES['document'].name)
    context = {'d': data, 
                'headers': list(data[0].keys()),
                'code':code,
                'action':''}


    return render(request, 'table.html', context)


def remove(request):

    def execute_eqn(data, include, parameter, operation, num2):
        if include == "Include":
            equation =  "df = df[(df['{}']{}{})]".format(parameter, operation, num2)     
            if operation == "==":
                    print(parameter)
                    print(data.columns)
                    try: data = data[data[parameter] == num2]
                    except: print("not a valid dunction")
            elif operation == ">=":
                    try: data = data[data[parameter] >= num2]
                    except: print("not a valid dunction")    
            elif operation == ">":
                    try: data = data[data[parameter] > num2]
                    except: print("not a valid dunction") 
            elif operation == "<=":
                    try: data = data[data[parameter] <= num2]
                    except: print("not a valid dunction") 
            elif operation == "<":
                    try: data = data[data[parameter] < num2]
                    except: print("not a valid dunction")        
        elif include == "Exclude":
            equation =  "df = df[~(df['{}']{}{})]".format(parameter, operation, num2)
            if operation == "==":
                    print(parameter)
                    print(data.columns)
                    try: data = data[~(data[parameter] == num2)]
                    except: print("not a valid dunction")
            elif operation == ">=":
                    try: data = data[~(data[parameter] >= num2)]
                    except: print("not a valid dunction")    
            elif operation == ">":
                    try: data = data[~(data[parameter] > num2)]
                    except: print("not a valid dunction") 
            elif operation == "<=":
                    try: data = data[~(data[parameter] <= num2)]
                    except: print("not a valid dunction") 
            elif operation == "<":
                    try: data = data[~(data[parameter] < num2)]
                    except: print("not a valid dunction")        
        

        return data, equation
    # get existing code
    code = request.POST["code"]
    # get selected action
    action = request.POST['selected_action']
    print(action)
    data = request.POST["data"]
    data = pd.DataFrame(list(eval(data)))

    if action == "droptoprows":
        try:
            # get index number to remove
            ind = int(request.POST["num1"])           
            # update code
            code = code + "# Remove the top {} row(s): \n". format(ind)
            #code = code + "df = df[~(df['index'] == {})] \n".format(ind)
            code = code + "df = df.iloc[{}:] \n".format(ind)
            #execute
            #data = data[~(data["index"] == ind)]
            data = data.iloc[ind:]
        except: print("input not a valid index number")
    
    if action == "dropna":
        try:
            # get index number to remove
            parameter = request.POST["parameter"] 
            print(parameter)          
            # update code
            code = code + "# Remove row if {} is empty (not a number): \n". format(parameter)
            code = code + "df = df[~(df['{}'].isna())] \n".format(parameter)
            #execute
            #data = data[~(data["index"] == ind)]
            data = data[~data[parameter].isna()]
        except: print("input not a valid index number")
    
    if action == "conditionalfilter":
        try:
            # get index number to remove
            include = request.POST["include"] 
            parameter = request.POST["parameter"] 
            operation = request.POST["operation"] 
            num2 = request.POST["num2"]
            try: num2 = float(num2)
            except: print("Input is a string")
            else: print("Input is a number")

            # update code
            code = code + "# {} row if {} is {} {}: \n". format(include, parameter, operation, num2)
            equation =  "df = df[(df['{}']{}{})]".format(parameter, operation, num2)
            print(equation.replace("df", "data"))
            try: data, equation = execute_eqn(data, include, parameter, operation, num2)
            except:print("Not a valid function.")
            else:
                string = "{}\n".format(equation)
                code = code + string

        except: print("input not a valid index number")

    headers = data.columns
    # parsing the DataFrame in json format.
    json_records = data.reset_index().to_json(orient ='records')
    json_records = data.to_json(orient ='records')
    data = json.loads(json_records)
    #print(list(data[0].keys()))
    context = {'d': data, 
                #'headers': list(data[0].keys()),
                'headers': headers,
                'code':code,
                'action':action}

    return render(request, "table.html", context)

def removecolumns(request):
    # get existing code
    code = request.POST["code"]
    # get columns
    cols = request.POST["columns"]
    # get data
    data = request.POST["data"]
    data = pd.DataFrame(list(eval(data)))
    
    # update code
    #print(cols)    

    #execute

    # parsing the DataFrame in json format.
    json_records = data.reset_index().to_json(orient ='records')
    json_records = data.to_json(orient ='records')
    data = json.loads(json_records)
    #print(list(data[0].keys()))
    context = {'d': data, 
                'headers': list(data[0].keys()),
                'code':code}
    return render(request, "table.html", context)
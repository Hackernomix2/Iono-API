from .toolSet import start_service,read_sheet_data
   
#data input format with the first row as the fields
# [
#     ['A1', 'B1', 'C1'],
#     ['A2', 'B2', 'C2'],
#     ['A3', 'B3', 'C3']
# ] 
def parse(list_form):
    fields = list_form[0]
    counter = 1
    final_list = []
    
    for i in range(1 , len(list_form)):
        temp = []
        for j in range(len(fields)):
            temp.append( f"{fields[j]} : {list_form[i][j]},")
        
        template = f"Form {counter} : {temp} :-" + "".join(temp)
        final_list.append(template)
    
    return "".join(final_list)    

def load(spread_sheet_id , sheet_name , range):
    sh_id = sheet_name+"!"+range
    service = start_service()
    data = read_sheet_data(service, spread_sheet_id, sh_id)
    result = parse(data)
    
    return result
import model
import view

def button_click():
    value_a=view.get_value()
    model.init(value_a)
    if value_a==True:
        result=model.add()
    view.view_data(result)

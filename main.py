# skills test: ordering form
from pyscript import display, document


def b_function(e):
    name = document.getElementById('cname').value
    place = document.getElementById('address').value
    number = document.getElementById('contact').value

    display(f'', target='output') 

    
order_summary = '''
Order for: {cname}
Address: {address}
Contact Number: {contact}
Total: {}
'''

display(order_summary)

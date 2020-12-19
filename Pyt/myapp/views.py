from django.shortcuts import render
from myapp.scrape import other_products,mobile_phones,paytm,snapdeal,fashion,amazon
import pandas as pd
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'GET' and request.GET.get('category'):
        x = request.GET.get('category')
        item  = request.GET.get('product')
        pd.set_option("display.max_rows",6)
        pd.set_option('max_colwidth',100)
        cols=["Name","Price"]

        df=pd.DataFrame(columns=cols)
        df1=pd.DataFrame(columns=cols)
        df2=pd.DataFrame(columns=cols)
        df3=pd.DataFrame(columns=cols)

        if x=='1':
            df1=mobile_phones(item)

        elif x=='2':
            df1=fashion(item)
    
        else:
            df1=other_products(item)

        df2 = paytm(item)
        df3 = snapdeal(item)
        df4 = amazon(item)

        context = {'column_names':df.columns.values,'flipkart':df1.values.tolist(),\
        'paytm':df2.values.tolist(),'snapdeal':df3.values.tolist(),'amazon':df4.values.tolist()}
        print(context)
        return render(request,'base.html',context)
    return render(request,'base.html')
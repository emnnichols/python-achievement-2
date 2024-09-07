from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale

from .utils import get_bookname_from_id, get_chart

import pandas as pd

# Create your views here.

def home(request):
  return render(request, 'sales/home.html')

@login_required
def records(request):
  form = SalesSearchForm(request.POST or None)
  sales_df = None   #initialize dataframe to None
  chart = None

  if request.method =='POST':
    book_title = request.POST.get('book_title')
    chart_type = request.POST.get('chart_type')

    qs = Sale.objects.filter(book__name = book_title)
    if qs:      #if data found
      sales_df = pd.DataFrame(qs.values()) 
      #convert the ID to Name of book
      sales_df['book_id']=sales_df['book_id'].apply(get_bookname_from_id)

      chart = get_chart(chart_type, sales_df, labels=sales_df['book_id'].values)

      #convert the dataframe to HTML
      sales_df=sales_df.to_html()

  context={
        'form': form,
        'sales_df': sales_df,
        'chart': chart}

  return render(request, 'sales/records.html', context)
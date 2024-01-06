from django.shortcuts import render
from cgitb import text
from hashlib import new
from multiprocessing import context
from typing import Text
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, FormMixin
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect
import ast
from django.db.models import Q
from django.http import JsonResponse

from django.urls import reverse_lazy, reverse

from .forms import *
from .models import *
from datetime import datetime as dt

import csv
import re
from io import TextIOWrapper, StringIO
from django.http import JsonResponse
import os

# Create your views here.

# 一時関数，csv to sqlite
def upload_Edinet(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis', errors='ignore')
        csv_file = csv.reader(form_data)
        column_flag = 0
        for line in csv_file:
            if column_flag < 2:
                column_flag  += 1
                continue

            new_edinet = EdinetCode.objects.create()
            try:
                new_edinet.edinet_code = line[0]  # edinet code
            except:
                pass
            try:
                new_edinet.submitter_type = line[1]  # 提出者種別
            except:
                pass
            try:
                new_edinet.list_class = line[2]  # 上場区分
            except:
                pass
            try:
                new_edinet.link_or_not = True if line[3] == "有" else False  # 連結の有無
            except:
                pass
            try:
                new_edinet.capital = int(line[4])  # 資本金
            except:
                pass
            try:
                new_edinet.close_date = dt.strptime(line[5], '%m月%d日')  # 決算日
            except:
                pass
            try:
                new_edinet.submitter_JA = line[6]  # 提出者日本語
            except:
                pass
            try:
                new_edinet.location = line[9]  # 所在地
            except:
                pass
            try:
                new_edinet.industry = line[10]  # 提出者業種
            except:
                pass

            try:
                new_edinet.stock_code = int(line[11])  # 証券コード
            except:
                pass

            new_edinet.save()

        return render(request, 'analyze_compnay/upload_edinet.html')

    else:
        return render(request, 'analyze_company/upload_edinet.html')
def upload_detail(request):
    if request.POST:  
        file_path = "/"
        print(os.listdir())
        for csv_file in os.listdir(file_path):
            form_data = file_path + csv_file
            csv_file = csv.reader(form_data)
            column_flag = False
            for line in csv_file:
                if not column_flag:
                    column_flag = True
                    continue
                new_data = DetailElem.objects.create()

                new_data.elem_id = line[0]  # 要素ID
                new_data.index_name = line[1]  # 項目名
                new_data.context_id = line[2]  # コンテキスト
                new_data.relative_year = line[3]  # 相対年度
                new_data.linkORindivi = line[4]  # 連結・個別
                new_data.unit_id = line[5]  # ユニットID
                new_data.unit = line[6]  # 単位
                new_data.value = line[7]  # 値
                new_data.company = line[8]  # CompanyDetailへの外部キー

                filename = csv_file
                id_pattern = r"E\d+" # Eから始まるIDを抽出する正規表現                
                date_pattern = r"\d{4}-\d{2}-\d{2}" # 日付を抽出する正規表現
                id_match = re.search(id_pattern, filename)
                if id_match:
                    extracted_id = id_match.group()
                    new_data.compane = EdinetCode(edinet_code=extracted_id)
                    print("Extracted ID:", extracted_id)

                # 日付の検索
                dates = re.findall(date_pattern, filename)
                if dates:
                    new_data.close_date = dates[0]
                    new_data.submit_date = dates[1]
                    print("Extracted Dates:", dates)

                new_data.save()

        return render(request, 'analyze_company/upload_detail.html')

    else:
        return render(request, 'analyze_company/upload_detail.html')
    
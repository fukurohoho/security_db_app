from django.db import models

# Create your models here.
class CompanyDetail(models.Model):
    campany_name = models.CharField(max_length=300)

class DetailElem(models.Model):
    elem_id = models.CharField(max_length=300) # 要素ID
    index_name = models.CharField(max_length=300) # 項目名
    context_id = models.CharField(max_length=300) # コンテキスト
    relative_year = models.CharField(max_length=300) # 相対年度

    linkORindivi = models.CharField( # 連結・個別
        choices = (('li','連結'),('in','個別'),('ot','その他')),
        max_length = 100
    )

    unit_id = models.CharField(max_length=300) # ユニットID
    unit = models.CharField(max_length=300) # 単位
    value = models.IntegerField() # 値

    company_edinet_code = models.ForeignKey(
        CompanyDetail,
        on_delete=models.CASCADE,
    )

    close_date = models.DateField() # 会計年度末日
    submit_date = models.DateField() # 提出日


class EdinetCode(models.Model):
    edinet_code = models.CharField(max_length=300, blank=True) # edinet code
    submitter_type = models.CharField(max_length=300, blank=True) # 提出者種別
    list_class = models.CharField(max_length=300, blank=True) # 上場区分
    link_or_not = models.BooleanField(null=True)# 連結の有無
    capital = models.IntegerField(null=True, blank=True) # 資本金
    close_date = models.DateField(null=True, blank=True) # 決算日
    submitter_JA = models.CharField(max_length=300, blank=True) # 提出者日本語
    location = models.CharField(max_length=300, blank=True) # 所在地
    industry = models.CharField(max_length=300, blank=True) # 提出者業種
    stock_code = models.IntegerField(null=True, blank=True) # 証券コード

    